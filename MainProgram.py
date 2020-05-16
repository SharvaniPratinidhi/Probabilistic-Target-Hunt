from tkinter import *
from Environment import Environment
from Agent import Agent

# Default values
dimensions = 50


class MainProgram:
    def __init__(self):
        self.dim = dimensions
        self.env = Environment(self.dim)
        self.agent = None
        self.window = Tk()
        self.window.title("Probabilistic Hunting")
        self.window.geometry('1000x800+200+10')

        # Control Frame
        self.controlFrame = Frame(self.window, height=800)
        self.controlFrame.pack(side=LEFT)

        self.rule = IntVar()
        R1 = Radiobutton(self.controlFrame, text="Rule 1", variable=self.rule, value=1, padx=2, pady=2
                         )
        R1.pack()

        R2 = Radiobutton(self.controlFrame, text="Rule 2", variable=self.rule, value=2, padx=2, pady=2
                         )
        R2.pack()

        self.solveButton = Button(self.controlFrame, text="Find Target", height=2, width=10, command=self.solveField)
        self.solveButton.pack()
        # Frame for drawing the field
        self.mazeFrame = Frame(self.window, width=800, height=800)
        self.mazeFrame.pack(side=RIGHT)

        self.mazeCanvas = Canvas(self.mazeFrame, width=800, height=800)
        self.mazeCanvas.pack()
        self.drawMaze()
        self.window.mainloop()

    def solveField(self):
        self.agent = Agent(self.env, self.rule.get(),self.dim)


    def drawMaze(self):
        tileHeight = (780) / self.dim
        tileWidth = (780) / self.dim
        self.mazeCanvas.delete("all")  # Clear the canvas
        self.tiles = [[self.mazeCanvas.create_rectangle(10 + i * tileWidth, 10 + j * tileHeight,
                                                        10 + (i + 1) * tileWidth, 10 + (j + 1) * tileHeight) for i in
                       range(self.dim)] for j in range(self.dim)]

        for i in range(self.dim):
            for j in range(self.dim):
                if self.env.grid[i][j].type == 1:
                    self.mazeCanvas.itemconfig(self.tiles[i][j], fill="#ffff00")
                elif self.env.grid[i][j].type == 2:
                    self.mazeCanvas.itemconfig(self.tiles[i][j], fill="#ff8000")
                elif self.env.grid[i][j].type == 3:
                    self.mazeCanvas.itemconfig(self.tiles[i][j], fill="#40ff00")
                elif self.env.grid[i][j].type == 4:
                    self.mazeCanvas.itemconfig(self.tiles[i][j], fill="#ff0000")

                # if self.env.grid[i][j].target==TRUE:
                #     self.mazeCanvas.itemconfig(self.tiles[i][j], fill="#0000ff")


if __name__ == "__main__":
    ms = MainProgram()
