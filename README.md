# Visualize-Approximate-Salesman


![](/Template.gif)

### This project is a seemingly basic and elegent  *GUI*  implementation of Christofides_algorithm

#### 1 [Christofides algorithm](#christofides-algorithm)
#### 2 [Using This Project](#using-this-project)
#### 3 [Run it on Your Computer](#run-it-on-your-computer)

- [main code](main.py)
## Christofides algorithm::

Implimentation is of Christofides Algorithm


	1- Create minimum Spanning Tree 'T' of graph 'G'

	2- O is set of odd vertices, |O| is even

	3- Find a minimum weight 'perfect matching' 'M' in the 'induced subgraph'
			given by the vertices from 'O'

	4- Combine 'M' and 'T' to form a connected multigraph 'H'

	5- Form an Eulerian Circuit in 'H'

	6- Make the circuit found in previous step into Hamiltonian circuit by shortcutting


## Using This Project::

1 Select Few Points on top left Block. ( This will be your *graph*.)

3 Press Done.

## Run it on Your Computer::

1 Download this repository by directly clicking **download** button under **clone or download**
  copy url and download using command **git clone url**
  
2 Open cmd in Windows or Terminal in Linux then **cd** your way into the directory where you have
  downloaded this project.
  
3 run using command

>**pip3 install kivy**

>**python3 gui.py**
