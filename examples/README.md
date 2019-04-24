# Input description

The input for the net construction currently 
consists of text files reflecting the hierarchy of
the system places and their features.
In the text input files each line corresponds 
to a place description. 
The same line reports the name of the predecessor 
of a particular place, the
the relationship between them and the name of the 
associated transition.
In this way each line corresponds to an edge
connecting a place to its parent place.

Each line should contain the following info:
- place id (**Mark**)
- parent of the place id (**Father_mark**)
- parent-child relationship 
(**Father_cond**: *AND*, *OR*, *SINGLE*, *ORPHAN*)
- name of the transition
(**Level**: **Father_cond** + predecessors Marks)


The hierarchy of the place explains how tokens
flow from one place to another place.


In the graph, the places represent the system place 
while the transitions harbor 
the logic relations existing between the place 
(*ORPHAN*, *SINGLE*, *AND*, and *OR*).
- An **ORPHAN** condition indicates a place without predecessors.
- A **SINGLE** condition connects a place to its only one predecessor.
- An **AND** condition indicates that the place 
has more than one predecessor. All the predecessors are 
necessary for the functioning of that place.
- An **OR** condition indicates that the place has 
more than one predecessor. Just one of the place’s 
predecessors should be active to guarantee the functioning 
of the place.
For this reason, correct input formatting 
is one of the most important steps of the analysis.

# Example 1

In the input file `TOY_graph.csv `are present 8 places
(A, B, C, D, E, F, G, H) connected by input arcs, 
transitions (AND_AB, SINGLE_H, SINGLE_C, OR_DF) and output arcs
reflecting the hierarchy of the system 
in a parent-child fashion.


## Simulate a damage to place 'A' 

1. In file `general_net.py`:

* Uncomment `g.delete_places(['A'])`


2. Run:

 `python general_net.py Input_net.csv `


## Output description


### STDOUT

```bash
All starting places:  {'D', 'B', 'F', 'H', 'C', 'A', 'E', 'G'}
 
Remove place:  A

Deleted places:  {'D', 'H', 'C', 'A', 'E'}
 
List of remaining places:  {'G', 'B', 'F'}
```bash


### Figures

![](../output_files/intact_PN_1.png)

__Figure1__: Intact system representation. Places are represented by
circles, transitions by rectangles and arcs by arrows.
By convention, **ORPHAN** condition places (A, B, F) are assigned
initial making equal to 1.

![](../output_files/damaged_PN_2.png)

__Figure2__: Damaged system representation. Places are represented by
circles, transitions by rectangles and arcs by arrows. Places involved 
in the damage propagation cascade process are removed from the net.


# Example 2

## Simulate a damage to places 'H' and 'G'

1. In file `general_net.py`:

* Uncomment `g.delete(['H','G'])`

2. Run:

 `python general_net.py Input_net.csv `


# Expected output:

### STDOUT

```bash
All starting places:  {'D', 'C', 'B', 'F', 'H', 'E', 'A', 'G'}
 
Remove places:  ['H', 'G']

Deleted places:  {'D', 'C', 'H', 'E', 'A'}

Deleted places:  {'D', 'C', 'H', 'E', 'A', 'G'}
 
Remaining places:  {'F', 'B'}

```bash

### Figures

![](../output_files/intact_PN_3.png)

__Figure3__: Intact system representation. Places are represented by
circles, transitions by rectangles and arcs by arrows.
By convention, **ORPHAN** condition places (A, B, F) are assigned
initial making equal to 1.
(
![](../output_files/damaged_PN_4.png)

__Figure4__: Damaged system representation. Places are represented by
circles, transitions by rectangles and arcs by arrows. Places involved 
in the damage propagation cascade process are removed from the net.






