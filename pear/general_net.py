import csv
import sys
import snakes
import snakes.plugins
snakes.plugins.load('gv', 'snakes.nets', 'nets')
from nets import *

class GeneralNet():
    """Class GeneralNet for Petri nets.

    Constructs a new Petri nets given an input file.
    A Petri net is a bipartite graph that consists of two types of nodes,
    places, and transitions connected by arcs.

    Parameters
    ----------
    incoming_data : input data
        Data to initialize the net.
    """

    def load(self, filename):
        """Load input file.

        Parameters
        ----------
        filename : input file in csv format
            The input for the Petri net construction currently
            consists of text files reflecting the hierarchy of
            the places.
            In the text input files each line corresponds
            to a place description.
            The same line reports the name of the predecessor
            of a particular place, and the relationship between them.
            Each line should contain the following info:
            - place id ("Mark")
            - parent of the place id ("Father_mark")
            - parent-child relationship ("Father_cond": AND, OR, SINGLE, ORPHAN)
            - name of the transition ("Level")

            • An ORPHAN "Father_cond" is assigned to a place without predecessors.
            • A SINGLE "Father_cond" connects a place to its only one predecessor.
            • An AND "Father_cond" indicates that the place has more than
              one predecessor. All the predecessors are necessary.
            • An OR "Father_cond" indicates that the place has
              more than one predecessor. Just one of the place
              predecessors should be active to guarantee the functioning
              of the place.
        """

        with open(filename, 'r') as csvfile:
            self.input = []
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.input.append(dict(row))

    def add_places(self):
        """ Add the places.
        """

        self.n = PetriNet('net')

        self.list_places = []
        self.list_input_places = []
        self.list_level = []

        for dic in self.input:
            if dic["Father_Mark"] == "NULL":
                self.list_input_places.append(dic["Mark"])
                self.n.add_place(Place(dic["Mark"], [1]))

            i = dic["Mark"]
            if i not in self.list_input_places and i not in self.list_places:
                self.list_places.append(i)
                self.n.add_place(Place(i, []))

        self.all_places = set(self.list_places+self.list_input_places)

    def add_transitions(self):
        """ Add the transitions.
        """

        self.list_transitions = []
        for dic in self.input:
            cond = dic["Father_cond"]
            lev = dic["Level"]
            if cond != "ORPHAN" and lev not in self.list_transitions:
                self.list_transitions.append(lev)
                self.t = Transition(lev)
                self.n.add_transition(self.t)

    def add_input(self):
        """ Add input arcs.
        """

        combinations = []

        for dic in self.input:
            fmark = dic["Father_Mark"]
            cond = dic["Father_cond"]
            lev = dic["Level"]
            var = Variable('x')
            if cond != "ORPHAN":
                if (fmark+lev+str(var)) not in combinations:
                    combinations.append(fmark+lev+str(var))
                    self.n.add_input(fmark, lev, var)

    def add_output(self):
        """ Add output arcs.
        """

        combinations = []

        for dic in self.input:
            mark = dic["Mark"]
            cond = dic["Father_cond"]
            lev = dic["Level"]
            var = Variable('x')
            if cond != "ORPHAN":
                if (mark+lev+str(var)) not in combinations:
                    combinations.append(mark+lev+str(var))
                    self.n.add_output(mark, lev, var)

        self.n.draw('intact_PN.png')

    def rm_places(self, place, visited=None):
        """ Remove places from the net in a depth first search way to
        propagate the damage.

        Parameters
        ----------
        place : place
            The first place from which the damage propagation cascade begins.
        visited : None or string, optional
        """

        if visited is None:
            visited = set()
        visited.add(place)

        cond = list(self.n.post(place))

        if cond:
            if "OR" not in cond[0]:
                predecessors = set(self.n.pre(cond))
                if "AND" in cond[0]:
                    if len(predecessors.intersection(self.places_to_delete)) <= 1:
                        for i in predecessors:
                            if Marking({i: MultiSet([0])}):
                                self.n.add_marking(Marking({i:MultiSet([1])}))
                        modes_l = self.n.transition(cond[0]).modes()
                        self.n.transition(cond[0]).fire(modes_l[0])
                        successors = list(self.n.post(cond[0]))
                        for next in set(successors) - visited:
                            self.places_to_delete.add(next)
                            self.rm_places(next, visited)
                else:
                    for i in predecessors:
                        if Marking({i: MultiSet([0])}):
                            self.n.add_marking(Marking({i:MultiSet([1])}))
                    modes_l = self.n.transition(cond[0]).modes()
                    self.n.transition(cond[0]).fire(modes_l[0])
                    successors = list(self.n.post(cond[0]))
                    for next in set(successors) - visited:
                        self.places_to_delete.add(next)
                        self.rm_places(next, visited)

            return visited

    def delete_places(self, places):
        """ Delete a place and propagate the cascade damage.
        """

        #all_places = list(sorted(self.n.place(), key=str))
        print(" \nAll starting places: ", self.all_places)

        print(" \nRemove places: ", places)

        self.places_to_delete = set()


        for place in places:
            if place in self.n:
                successors_c = list(sorted(self.n.post(place), key=str))
                if successors_c:
                    for successor in successors_c:
                        if "OR" in successor:
                            self.places_to_delete.add(place)
                        elif "OR" not in successor:
                            self.places_to_delete.add(place)
                            self.rm_places(place)
                else:
                    self.places_to_delete.add(place)

                print("\nDeleted places: ", self.places_to_delete)

                for i in self.places_to_delete:
                    if i in self.n:
                        self.n.remove_place(i)


        #remaining_places = list(sorted(self.n.place(), key=str))
        remaining_places = self.all_places - self.places_to_delete

        if len(remaining_places) > 0:
            print(" \nRemaining places: ", remaining_places)
        else:
            print(" \nRemaining places: ALL PLACES WERE DELETED")

        self.n.draw('damaged_PN.png')


if __name__ == '__main__':

    g = GeneralNet()
    g.load(sys.argv[1])
    g.add_places()
    g.add_transitions()
    g.add_input()
    g.add_output()
    #g.delete_places(['A'])
    g.delete_places(['H','G'])
