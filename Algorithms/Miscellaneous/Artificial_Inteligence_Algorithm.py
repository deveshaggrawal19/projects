from queue import PriorityQueue
class State(object):
    def __init__(self, value, parent, start=0, goal=0):
        self.children = []
        self.parent = parent
        self.value = value
        self.dist = 0
        if parent:
            self.path = parent.path[:]
            self.path.append(value)
            self.start = parent.start
            self.goal = parent.goal
        else:
            self.path = [value]
            self.start = start
            self.goal = goal

    def get_dist(self):
        pass

    def create_child(self):
        pass


class StateString(State):
    def __init__(self, value, parent, start=0, goal=0):
        super(StateString, self).__init__(value, parent, start, goal)
        self.dist = self.get_dist()

    def get_dist(self):
        if self.value == self.goal:
            return 0
        dist = 0
        for i in range(len(self.goal)):
            letter = self.goal[i]
            dist += abs(i-self.value.index(letter))
        return dist

    def create_child(self):
        if not self.children:
            for i in range(len(self.goal)-1):
                val = self.value
                val = val[:i] + val[i+1] + val[i] + val[i+2:]
                child = StateString(val, self)
                self.children.append(child)


class AStar_Solver:
    def __init__(self, start, goal):
        self.path = []
        self.visited_queue = []
        self.priority_queue = PriorityQueue()
        self.start = start
        self.goal = goal

    def solve(self):
        pass
