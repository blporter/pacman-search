Name: Brooke Porter
Email: bporter3@mail.sfsu.edu
ID: 920000624



search.py
I eventually got an implementation working on DFS, but then noticed that BFS was almost identical. I converted my implementation into a generic method that takes in the problem, a data structure, a path structure, and optionally a heuristic. From there, each search method can create its required structures and pass them to the generic method, reducing repeat code.

The generic method checks whether the current node has been visited already, gets the node's successors, and adds them to the data structure as needed as long as the node is not a goal state.

searchAgents.py
I changed the state to take a second parameter as a list, and used that to keep track of which corners had already been visited. From there, I check if the size of that list == 4 or not to determine goal state, and update that list within the getSuccessors function while appending the successors.

I noticed that there were provided functions manhattanHeuristic and euclideanHeuristic, but also found mazeDistance. Manhattan and euclidean both got me fast results, but expanded too many nodes. I found that mazeDistance uses the BFS implementation from search.py, which is complete and optimal according to my lecture notes. It takes significantly longer for the autograder to calculate, but still within reason (in my opinion) and reduces the number of expanded nodes dramatically.



I spent around 30 hours on this assignment, I think. Maybe more? I didn't keep track...
