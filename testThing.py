def this_is_a_func(problem):
    from util import Stack

    fringe = Stack()  # Fringe to manage which states to expand
    fringe.push(problem.getStartState())
    visited = []  # List to check whether state has already been visited
    path = []  # Final direction list

    pathToCurrent = Stack()  # Stack to maintaing path from start to a state

    currState = fringe.pop()
    while not problem.isGoalState(currState):
        if currState not in visited:
            visited.append(currState)

            successors = problem.getSuccessors(currState)
            for child, direction, cost in successors:
                fringe.push(child)
                tempPath = path + [direction]
                pathToCurrent.push(tempPath)

        currState = fringe.pop()
        path = pathToCurrent.pop()

    return path
