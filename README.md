<h1 align='center'> A Heuristic for the Tree Poset Cover Problem </h1>
The Tree Poset Cover Problem is an optimization problem where the goal is to determine a
minimum set of Tree Posets that covers a given set of input linear orders. This problem finds
application in various real-world scenarios including data mining where constructing directed
networks from sequential data is the primary objective. The decision version of the problem is
already known to be NP-hard while constrained versions such as Hammock(2)-Poset is in P.
The main objective of this research is to create a heuristic algorithm to solve the Tree Poset
Cover Problem. To achieve this goal, the research will utilize the properties of tree posets and
their connections to adjacent transposition graphs and linear extensions.

<p align = "center"> 
    <img src="Utils\images\TreePosetCoverProblem.png" alt="image">
</p>

## Run the following commands in order:
1. Generate an input file and optimal solution file (choose either exhaustive or random generation)  
    **Exhaustive**
    ```python
    python optimalsolutions.py <vertex count*> <max posets*>
    ```
    **Random**
    ```python
    python optimalsolutions2.py <vertex count*> <max posets*>
    ```
2. Generate heuristic solutions on the input file (choose either heuristic-one or heuristic-two)
    ```python
    python heuristic-<one/two>.py <vertex count*>
    ```
3. Generate analysis of optimal and heuristic solutions
    ```python
    python analysis.py <vertex count*>
    ```

*`vertex count` should be valued 3 or greater  
*`max posets` should be valued 1 or greater

> **Note**  
> When using a standard or typical machine, it is advisable to limit the `<vertex count*>` to a maximum of 6 and the `<max posets*>` to a maximum of 4. Once you exceed these values, generating the desired file will require a significant amount of time.
