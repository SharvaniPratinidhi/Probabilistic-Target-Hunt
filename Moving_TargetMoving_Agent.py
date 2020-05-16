from random import randint
import random

# from Environment import Environment

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
IS_TARGET = True
NOT_TARGET = False
NOT_FOUND = False
FOUND = True


class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.type = IS_UNDECIDED


class Moving_Target_Moving_Agent:
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
        curr_xi = 0
        curr_yi = 0
        while self.target == NOT_FOUND:
            # while self.numberOfSteps < 10000:
            self.numberOfSteps += 1
            result, row, col = self.pick_next(curr_xi,curr_yi)
            curr_xi = row
            curr_yi = col
            #print(row,col,'and',self.env.targetcell)
            if result == True:
                #print("success at ", row, col);
                self.target = FOUND

                print("The true target is at", self.env.targetcell)
                print(self.numberOfSteps)
                return self.numberOfSteps


    def get_false_negative_score(self, row, col):
        if self.grid[row][col].type == IS_FLAT:
            return PROB_FLAT
        elif self.grid[row][col].type == IS_HILLY:
            return PROB_HILLY
        elif self.grid[row][col].type == IS_FOREST:
            return PROB_FOREST
        else:
            return PROB_CAVE

        
    def move_target(self):
        r = random.random()
        (curr_target_row,curr_target_col) = self.env.targetcell
        new_target_row = curr_target_row
        new_target_col = curr_target_col
        if(curr_target_row > 0 and curr_target_row < self.dimension-1 and 
         curr_target_col > 0 and curr_target_col < self.dimension -1):
           if(r <= 0.25):
               new_target_row = curr_target_row - 1
           elif (r > 0.25 and r <= 0.50):
               new_target_col = curr_target_col - 1
           elif (r > 0.50 and r <= 0.75):
               new_target_col = curr_target_col + 1
           else:
               new_target_row = curr_target_row + 1
        elif (curr_target_row > 0 and curr_target_row < self.dimension-1):
           if(r <= 0.33 and curr_target_col == 0):
               new_target_col = curr_target_col + 1
           elif (r <= 0.33 and curr_target_col == self.dimension - 1):
               new_target_col = curr_target_col - 1
           elif (r > 0.33 and r <= 0.66):
               new_target_row = curr_target_row - 1
           else:
               new_target_row = curr_target_row + 1        
        elif (curr_target_col > 0 and curr_target_col < self.dimension-1):
           if(r <= 0.33 and curr_target_row == 0):
               new_target_row = curr_target_row + 1
           elif (r <= 0.33 and curr_target_row == self.dimension - 1):
               new_target_row = curr_target_row - 1
           elif (r > 0.33 and r <= 0.66):
               new_target_col = curr_target_col - 1
           else:
               new_target_col = curr_target_col + 1        
        else:
            if(curr_target_row == 0 and curr_target_col == 0):
                if (r <= 0.5):
                    new_target_row = curr_target_row + 1
                else:
                    new_target_col = curr_target_col + 1
            elif(curr_target_row == 0 and curr_target_col == self.dimension-1):
                if (r <= 0.5):
                    new_target_row = curr_target_row + 1
                else:
                    new_target_col = curr_target_col - 1
            elif(curr_target_row == self.dimension - 1 and curr_target_col == 0):
                if (r <= 0.5):
                    new_target_row = curr_target_row - 1
                else:
                    new_target_col = curr_target_col + 1
            else:
                if(r <= 0.5):
                    new_target_row = curr_target_row - 1
                else:
                    new_target_col = curr_target_col - 1
        type1 = self.env.grid[curr_target_row][curr_target_col].type
        self.env.grid[curr_target_row][curr_target_col].target = NOT_TARGET
        self.env.grid[new_target_row][new_target_col].target = IS_TARGET
        type2 = self.env.grid[new_target_row][new_target_col].type
        self.env.targetcell = (new_target_row,new_target_col) 
    
        return type1, type2    

    def pick_next(self,current_xi,current_yi):
        type1, type2 = self.move_target()
        extra = 0.0       
        for i in range(self.dimension):
            for j in range (self.dimension):
                distance = abs(i - current_xi) + abs(j - current_yi)
                surrounding_cell = 0.0
                if self.belief[i][j] != 0:
                    if (i > 0 and (self.grid[i-1][j].type == type1 or self.grid[i-1][j].type == type2)):
                        surrounding_cell += 1
                    if (i < self.dimension-1  and (self.grid[i+1][j].type == type1 or self.grid[i+1][j].type == type2)):
                        surrounding_cell += 1
                    if (j > 0 and (self.grid[i][j-1].type == type1 or self.grid[i][j-1].type == type2)):
                        surrounding_cell += 1
                    if (j < self.dimension-1 and (self.grid[i][j+1].type == type1 or self.grid[i][j+1].type == type2)):
                        surrounding_cell += 1                        
                if surrounding_cell > 0:
                    if (i > 0 and (self.grid[i-1][j].type == type1 or self.grid[i-1][j].type == type2)):
                        self.belief[i-1][j] += self.belief[i][j]/(surrounding_cell*distance+1) 
                    if (i < self.dimension-1  and (self.grid[i+1][j].type == type1 or self.grid[i+1][j].type == type2)):
                        self.belief[i+1][j] += self.belief[i][j]/(surrounding_cell*distance+1)
                    if (j > 0 and (self.grid[i][j-1].type == type1 or self.grid[i][j-1].type == type2)):
                        self.belief[i][j-1] += self.belief[i][j]/(surrounding_cell*distance+1)
                    if (j < self.dimension-1 and (self.grid[i][j+1].type == type1 or self.grid[i][j+1].type == type2)):
                        self.belief[i][j+1] += self.belief[i][j]/(surrounding_cell*distance+1)  
                    
                    self.belief[i][j] = 0.0
                else:
                    extra += self.belief[i][j]
                    self.belief[i][j] = 0.0
        
        
        if extra != 0.0:
            nonEmptyCount = 0.0
            for i in range(self.dimension):
                for j in range(self.dimension):
                    if(self.belief[i][j] != 0):
                        nonEmptyCount += 1
            for i in range(self.dimension):
                for j in range(self.dimension):
                    if self.belief[i][j] != 0.0:
                        self.belief[i][j] = self.belief[i][j] *(1.0 + (extra/nonEmptyCount))
        
        maxprob = 0
        maxprobcells = []            
        
        if(self.rule == 1):

            # Highest probability for containing the target in cell
            for i in range(self.dimension):
                for j in range(self.dimension):
                    p = self.belief[i][j]
                    if (p > maxprob):
                        maxprob = p
                        maxprobcells = [(i, j)]
                    elif (p == maxprob):
                        maxprobcells.append((i, j))
            celltosearch = randint(0, len(maxprobcells) - 1)
            (xi, yi) = maxprobcells[celltosearch]
            return self.env.returnTarget(self.env.grid[xi][yi]), xi, yi
        
        else:

                # Highest probability for containing the target in cell
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

        