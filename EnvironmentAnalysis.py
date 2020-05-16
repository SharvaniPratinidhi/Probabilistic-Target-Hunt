import random

DEFAULT_DIMENSIONS = 50
IS_UNDECIDED = 0
IS_FLAT = 1
IS_HILLY = 2
IS_FOREST = 3
IS_CAVE = 4
IS_TARGET = True
NOT_TARGET = False

# Probability that target NOT FOUND in cell given that target is IN cell
PROB_FLAT = 0.1
PROB_HILLY = 0.3
PROB_FOREST = 0.7
PROB_CAVE = 0.9


class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.type = IS_UNDECIDED
        self.target = NOT_TARGET
        # self.targetcell = None

class Environment:
    def __init__(self, dimensions,celltype):
        self.grid = [[Cell(i, j) for j in range(dimensions)] for i in range(dimensions)]
        self.targetcell = None
        print(celltype)
        self.setValues(celltype)


    def setValues(self,celltype):
        total_cells = len(self.grid) ** 2
        flatCells = 0.2 * total_cells
        hillyCells = 0.3 * total_cells
        forestCells = 0.2 * total_cells
        # caveCells = 0.3 * total_cells
        for i in range(total_cells):
            row = random.randrange(len(self.grid))
            col = random.randrange(len(self.grid))
            while (self.grid[row][col].type != IS_UNDECIDED):
                row = random.randrange(len(self.grid))
                col = random.randrange(len(self.grid))

            if i < flatCells:
                self.grid[row][col].type = IS_FLAT
            elif i < flatCells + hillyCells:
                self.grid[row][col].type = IS_HILLY
            elif i < flatCells + hillyCells + forestCells:
                self.grid[row][col].type = IS_FOREST
            else:
                self.grid[row][col].type = IS_CAVE


        row = random.randrange(len(self.grid))
        col = random.randrange(len(self.grid))
        while celltype!=self.grid[row][col].type:
            row = random.randrange(len(self.grid))
            col = random.randrange(len(self.grid))

        self.grid[row][col].target = IS_TARGET
        print("Target at:", row, col, celltype)
        self.targetcell = (row, col)

    @staticmethod
    def returnTarget(cell):
        if (cell.target == NOT_TARGET):
            return False
        else:
            r = random.random()
            if (cell.type == IS_FLAT and r > PROB_FLAT):
                return True
            elif (cell.type == IS_HILLY and r > PROB_HILLY):
                return True
            elif (cell.type == IS_FOREST and r > PROB_FOREST):
                return True
            elif (cell.type == IS_CAVE and r > PROB_CAVE):
                return True
            else:
                return False
