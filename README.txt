Name: Brooke Porter
Email: bporter3@mail.sfsu.edu
ID: 920000624



search.py
I eventually got an implementation working on DFS, but then noticed that BFS was almost identical. I converted my implementation into a generic method that takes in the problem, a data structure, a path structure, and optionally a heuristic. From there, each search method can create its required structures and pass them to the generic method, reducing repeat code.
The generic method checks whether the current node has been visited already, gets the node's successors, and adds them to the data structure as needed as long as the node is not a goal state.

searchAgents.py
I changed the starting state to take a second parameter as a list, and used that to keep track of which corners had already been visited. From there, I check if the size of that list == 4 or not to determine goal state, and update that list within the getSuccessors function while appending the successors.
For the heuristics, I used the provided manhattanHeuristic function to get the distance to the next "goal" spot.
I reused these principles for the remaining functions.



I spent around 30 hours on this assignment, I think. Maybe more? I didn't think to keep track.
