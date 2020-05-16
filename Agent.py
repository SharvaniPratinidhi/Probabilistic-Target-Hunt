from random import randint

DEFAULT_DIMENSIONS = 50
IS_UNDECIDED = 0
IS_FLAT = 1
IS_HILLY = 2
IS_FOREST = 3
IS_CAVE = 4
# Probability that target NOT FOUND in cell given that target is IN cell
PROB_FLAT = 0.1
PROB_HILLY = 0.3
PROB_FOREST = 0.7
PROB_CAVE = 0.9

NOT_FOUND = False
FOUND = True


class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.type = IS_UNDECIDED


class Agent:
    def __init__(self, env, rule, dimensions=DEFAULT_DIMENSIONS):
        self.grid = [[Cell(i, j) for j in range(dimensions)] for i in range(dimensions)]
        initialprob = float(1) / (dimensions * dimensions)
        self.belief = [[initialprob for j in range(dimensions)] for i in range(dimensions)]
        self.env = env
        self.setvalues(env)
        self.numberOfSteps = 0
        self.rule = rule
        self.dimension = dimensions
        self.target = NOT_FOUND
        self.finalSteps = self.solve()

    def setvalues(self, env):
        for row in range(len(env.grid)):
            for col in range(len(env.grid)):
                self.grid[row][col].type = env.grid[row][col].type

    def solve(self):
        while self.target == NOT_FOUND:
            self.numberOfSteps += 1
            result, row, col = self.searchTarget()
            if result == True:
                # print("success at ", row, col);
                self.target = FOUND

                print("The true target is at", self.env.targetcell)
                print(self.numberOfSteps)
                return self.numberOfSteps
            else:
                # print("update belief")
                self.update_belief(row, col)

    def searchTarget(self):
        maxprob = 0
        maxprobcells = []
        if self.rule == 1:
            # Highest probability for containing the target in cell
            for i in range(self.dimension):
                for j in range(self.dimension):
                    p = self.belief[i][j]
                    if (p > maxprob):
                        maxprob = p
                        maxprobcells = [(i, j)]
                    elif (p == maxprob):
                        maxprobcells.append((i, j))
        else:
            # Highest probability for finding the target in cell
            for i in range(self.dimension):
                for j in range(self.dimension):
                    p = self.belief[i][j] * (1 - self.get_false_negative_score(i, j))

                    if (p > maxprob):
                        maxprob = p
                        maxprobcells = [(i, j)]

                    elif (p == maxprob):
                        maxprobcells.append((i, j))

        celltosearch = randint(0, len(maxprobcells) - 1)
        (xi, yi) = maxprobcells[celltosearch]
        return self.env.returnTarget(self.env.grid[xi][yi]), xi, yi

    def get_false_negative_score(self, row, col):
        if self.grid[row][col].type == IS_FLAT:
            return PROB_FLAT
        elif self.grid[row][col].type == IS_HILLY:
            return PROB_HILLY
        elif self.grid[row][col].type == IS_FOREST:
            return PROB_FOREST
        else:
            return PROB_CAVE

    def update_belief(self, row, col):
        delta = (1 - self.get_false_negative_score(row, col)) * self.belief[row][col]
        for i in range(self.dimension):
            for j in range(self.dimension):
                if (i != row or j != col):
                    self.belief[i][j] = self.belief[i][j] / (1 - delta)

        self.belief[row][col] = (self.belief[row][col] - delta) / (1 - delta)
