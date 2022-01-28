# -----------------------------------------------------------------------------
# Name:        game
# Purpose:     Implement a general board game
#
# Author:      Rula Khayrallah
# -----------------------------------------------------------------------------
'''
Module to implement a generic board GUI game app
'''
import tkinter
import math             # to perform division floor calculation
import random

class Game(object):
    '''
    GUI Game class to support a general purpose 8 x 8 board game

    Argument:
    parent: (tkinter.Tk) the root window object

    Attributes:
    parent: (tkinter.Tk) the root window object
    canvas: (tkinter.Canvas) canvas representing the game board
    '''


    # specify a class variable for the tile_size
    tile_size = 100

    def __init__(self, parent):
        parent.title('CS 21A Board Game')

        # save the parent as an instance variable
        # so that it can be accessed by the draw_board method
        self.parent = parent

        # create a RESTART button and associate it with the restart method
        # note: specify self.restart and not self.restart() as the command
        restart_button = tkinter.Button(self.parent, text='RESTART',
                                      width=20,
                                      command=self.restart)
        # register it with a geometry manager
        restart_button.grid()

        # since we need to access the canvas widget from other methods,
        # save it in the object as an instance variable: self.paintcanvas
        self.draw_board()  # draws tictac grid
        self.paintcanvas = tkinter.Canvas(parent, width=300, height=300)
        # register it with a geometry manager
        self.paintcanvas.create_rectangle(0, 0, 300, 300)
        # bind the leftmost button click to the fill_tile method
        self.gameboard.bind("<Button-1>", self.fill_tile)
        # instantiate a Label widget with root as the parent widget
        self.table_label = tkinter.Label(parent, text="")
        # register it with a geometry manager
        self.table_label.grid()
        # create an array to track game board tiles
        self.arr = [[None, None, None],
                    [None, None, None],
                    [None, None, None]]
        self.game_over = False                                # game status

    def draw_board(self):
        """
        Draw a 3 x 3 game board
        :return: None
        """
        # create a canvas to draw our board
        self.gameboard = tkinter.Canvas(self.parent,
                                     width=self.tile_size * 3,
                                     height=self.tile_size * 3)
        # register it with a geometry manager
        self.gameboard.grid()
        color = 'white'
        # draw the tiles on the game board
        for row in range(3):
            for column in range(3):
                self.gameboard.create_rectangle(self.tile_size * column,
                                             self.tile_size * row,
                                             self.tile_size * (column + 1),
                                             self.tile_size * (row + 1),
                                             fill=color)


    def restart(self):
        """
        Restart the game: clear the board and table label
        :return: None
        """
        new_arr =  [[None, None, None],   # 3x3 array to track tile selections
                    [None, None, None],
                    [None, None, None]]
        self.arr = new_arr
        self.gameboard.destroy()
        self.table_label.destroy()
        self.draw_board()  # draws tictac grid
        self.paintcanvas = tkinter.Canvas(self.parent, width=300, height=300)
        self.paintcanvas.create_rectangle(0, 0, 300, 300)
        # bind the leftmost button click to the draw_circle method
        self.gameboard.bind("<Button-1>", self.fill_tile)
        self.table_label = tkinter.Label(self.parent, text="")
        # register it with a geometry manager
        self.table_label.grid()

        print('restarting the game')
        self.game_over = False


    def win_status(self, array):
        """
        Checks current game status to determine if there is a winner.
        :parameters: array
        :return: status
        """
        if    (self.arr[0][0] == self.arr[0][1] == self.arr[0][2] == 'human'
            or self.arr[1][0] == self.arr[1][1] == self.arr[1][2] == 'human'
            or self.arr[2][0] == self.arr[2][1] == self.arr[2][2] == 'human'
            or self.arr[0][0] == self.arr[1][0] == self.arr[2][0] == 'human'
            or self.arr[0][1] == self.arr[1][1] == self.arr[2][1] == 'human'
            or self.arr[0][2] == self.arr[1][2] == self.arr[2][2] == 'human'
            or self.arr[0][0] == self.arr[1][1] == self.arr[2][2] == 'human'
            or self.arr[0][2] == self.arr[1][1] == self.arr[2][0] == 'human'):
            status = 'You win!'
        elif  (self.arr[0][0] == self.arr[0][1] == self.arr[0][2] == 'comp'
            or self.arr[1][0] == self.arr[1][1] == self.arr[1][2] == 'comp'
            or self.arr[2][0] == self.arr[2][1] == self.arr[2][2] == 'comp'
            or self.arr[0][0] == self.arr[1][0] == self.arr[2][0] == 'comp'
            or self.arr[0][1] == self.arr[1][1] == self.arr[2][1] == 'comp'
            or self.arr[0][2] == self.arr[1][2] == self.arr[2][2] == 'comp'
            or self.arr[0][0] == self.arr[1][1] == self.arr[2][2] == 'comp'
            or self.arr[0][2] == self.arr[1][1] == self.arr[2][0] == 'comp'):
            status = 'You lost!'
        else:
            return

        return (status)



    def fill_tile(self, event):
        """
        Draw a square to fill selected tic-tac-toe board tile
        """
        if self.game_over:
            return
        # assign player's mouse click to correct row and column (0, 1, or 2)
        invalid_entry = True
        while invalid_entry:      # run random generator until empty tile found
            col_id = (math.floor(event.x / self.tile_size))
            row_id = (math.floor(event.y / self.tile_size))
            print('line 151: self.arr[col_id][row_id] = ',self.arr[col_id][row_id])
            # generate computer random row and column selection (0, 1, or 2)
            if not self.arr[col_id][row_id]: # confirm tile is empty
                invalid_entry = False                                           #LATE INDENT CAUSES FREEZE
            else:
                event.x = event.y = None
                print('line 155: self.arr[col_id][row_id] = ',self.arr[col_id][row_id])
                # draw rectangle to fill in appropriate tile selected by human
        self.gameboard.create_rectangle(col_id * 100,
                                            row_id * 100,
                                            col_id * 100 + 100,
                                            row_id * 100 + 100,
                                            fill="magenta")
            # update array with human tile selection
            # if not self.arr[col_id][row_id]:       # confirm tile is empty
        self.arr[col_id][row_id] = 'human' # record human's entry

        # check if human wins
        status = self.win_status(self.arr)
        if status:
            self.table_label.destroy()
            self.table_label = tkinter.Label(self.parent, text= status)
        # register it with a geometry manager
            self.table_label.grid()
            self.game_over = True
            return

        # check if all board tiles filled
        if (None not in self.arr[0]
               and None not in self.arr[1]
               and None not in self.arr[2]):
            status = self.win_status(self.arr)
            if status:
                self.table_label.destroy()
                self.table_label = tkinter.Label(self.parent,text=status)
                # register it with a geometry manager
                self.table_label.grid()
            else:
                self.table_label.destroy()
                self.table_label = tkinter.Label(self.parent,
                                                 text= "it's a tie!")
                # register it with a geometry manager
                self.table_label.grid()
                self.game_over = True
            return

           # generate a random tile selection for the computer
        invalid_entry = True
        while invalid_entry:      # run random generator until empty tile found
            # generate computer random row and column selection (0, 1, or 2)
            col_id2 = random.randint(0, 2)
            row_id2 = random.randint(0, 2)
            if not self.arr[col_id2][row_id2]: # confirm tile is empty
                self.arr[col_id2][row_id2] = 'comp' # write random choice
                self.gameboard.create_rectangle(col_id2 * 100,
                                                row_id2 * 100,
                                                col_id2 * 100 + 100,
                                                row_id2 * 100 + 100,
                                                fill="blue")
                invalid_entry = False

        # check if computer wins
        status = self.win_status(self.arr)
        if status:
            self.table_label.destroy()
            self.table_label = tkinter.Label(self.parent,
                                             # text= 'you win!')
                                             text=status)
            # register it with a geometry manager
            self.table_label.grid()
            self.game_over = True



def main():
    # create the GUI application main window
    root = tkinter.Tk()

    # instantiate our Game object
    gen_game = Game(root)

    #if not game_over:
    root.mainloop()

if __name__ == '__main__':
    main()