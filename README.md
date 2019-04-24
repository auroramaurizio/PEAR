**PEAR**: Petri-net Evolution Analysis Report

## Table of contents

* [Description](#description)
* [Dependencies and installation](#dependencies-and-installation)
* [Documentation](#documentation)
* [Authors](#authors-and-contributors)
* [License](#License)
## Description


**PEAR** is a Python program that takes advantage of **Petri nets** and
logical conditions to develop a screening tool aimed at studying the effect of 
perturbations in interconnected systems.

### Petri nets

A Petri net is a mathematical model that allows the
representation and description of a process, but also
the modeling of the process evolution in terms of its new state
after the occurrence of a perturbation event.
Edges in the graph, called arcs (graphycally represented 
as arrows), are directed and connect places 
(graphycally represented as circles) to transitions (graphycally 
represented as rectangles) or transitions to places.
To simulate a dynamic process, a number of tokens is
assigned to each place in order to indicate the presence of some
quantitative property. This assignment of tokens to places encodes
the state of the system and is called a marking. The tokens move 
among the places when some event happens (transition firing). 
A transition can only fire when it is enabled, meaning that each of
its input places has at least one token in the current marking.
The firing of a transition is triggered by a specific event that occurs in
the environment. 
The order in which events are generated depends upon the event which
generates them and the hyerarchy of the system. 
When a transition fires, it removes one token from each place connected 
by input arcs and gives one token to each place connected by
output arcs until a stop condition is met.


## Dependencies and installation

**PEAR** requires `snakes`. 

### Installing from source

You can clone the repository using

```bash
> git clone https://github.com/auroramaurizio/PEAR
```

To install the package just type:

```bash
> python setup.py install
```

To uninstall the package you have to rerun the installation and record the installed files in order to remove them:

```bash
> python setup.py install --record installed_files.txt
> cat installed_files.txt | xargs rm -rf
```

## Authors 

- [Aurora Maurizio](mailto:auroramaurizio1@gmail.com)


## License

See the [LICENSE](LICENSE.rst) file for license rights and limitations (MIT).

