# Tree Poset Cover Problem
The Tree Poset Cover Problem is an optimization problem where the goal is to determine a
minimum set of Tree Posets that covers a given set of input linear orders. This problem finds
application in various real-world scenarios including data mining where constructing directed
networks from sequential data is the primary objective. The decision version of the problem is
already known to be NP-hard while constrained versions such as Hammock(2)-Poset is in P.
The main objective of this research is to create a heuristic algorithm to solve the Tree Poset
Cover Problem. To achieve this goal, the research will utilize the properties of tree posets and
their connections to adjacent transposition graphs and linear extensions.

<p align = "center"> 
    <img src="Utils\images\1.png" alt="image">
</p>

Step-by-step in running the heuristic and generating the results and analysis.
1. python optimalsolutions.py <vertex count*> <max posets>
Generates all the optimal solutions and the input files
2. python TreePoset.py <vertex count*>
Generates all the heuristic solutions
3. python analysis.py <vertex count*>
Generates the analysis of optimal and heuritsic solutions
