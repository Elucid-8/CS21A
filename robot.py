# -----------------------------------------------------------------------------
# Name:        robot
# Purpose:     class definition for robots in a square maze
#
# Author:      David Markowitz
# Date:        February 25, 2019
# -----------------------------------------------------------------------------

"""
Module to describe and control Robot objects in a square maze.
"""
import tkinter


class Robot(object):
    """
    Represent a Robot that navigates a maze

    Arguments:
    name (string): name of robot
    color (string): color of robot
    loc_x (int): horizontal location of robot
    loc_y (int): vertical location of robot

    Attributes:
    name (string): name of robot
    color (string): color of robot
    row (int): vertical location of robot, default = 0
    column (int): horizontal location of robot, default = 0
    battery (int): charge level of robot's battery

    ****** Note that the robot's battery is an instance variable with no
    corresponding argument in __init__.   ******
    """

    # class variable used by the show method
    unit_size = 60

    # Class variable describing the maze
    # False represents an obstacle, True represents open space
    maze = [[True, True, False, True, True, True, False, True, True, True],
            [True, True, False, True, True, True, False, True, True, True],
            [True, False, True, True, True, True, False, True, True, True],
            [True, True, True, True, True, True, True, True, False, True],
            [True, True, True, True, True, True, True, True, False, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, False, False, False, False, True, True, True, True, True],
            [True, True, False, True, True, True, True, True, False, True],
            [True, False, True, True, True, True, True, True, False, True],
            [True, True, True, True, True, True, True, True, False, True]]

    maze_size = len(maze)
    # class variable to represent the maximum charge
    # A robot with a fully charged battery can take up to 20 steps

    max_charge = 20

    def __init__(self, name, color, row=0, column=0):
        self.name = name
        self.color = color
        self.row = row
        self.column = column
        self.max_charge = Robot.max_charge
        self.battery = Robot.max_charge

    def __str__(self):
        return f'{self.name} is a {self.color} robot exploring the maze.'

    def __le__(self, other):
        """
        Compare two robot objects based on their battery charge.

        Parameter:
        other (str) = name of second robot to compare
        Return:
        True or False (bool)
        """
        return self.battery <= other.battery


    def recharge(self):
        """
        Recharge the robot's battery to the Robot.max_charge value

        Parameter:
        none
        Return:
        the updated robot object (Robot)
        """
        self.battery = Robot.max_charge
        return self                         # returns the updated robot object


    @property
    def one_step_forward(self):
        """
        Move robot forward one row and decrement the battery, if possible.

        Parameter:
        (row+=1): moves the robot forward by one row.
        Return:
        the updated robot object
        """
        if self.row+1 in range(Robot.maze_size):
            if Robot.maze[(self.row)+1][self.column]:
                if self.battery:
                    self.row += 1
                    self.battery -=1
                else:                          # insufficient charge in battery
                    pass
            else:                              # obstacle blocking robot's path
                pass
        else:                                  # boundary of maze is reached
            pass
        return self


    def one_step_back(self):
        """
        Move robot back one row and decrement the battery, if possible.

        Parameter:
        row(-=1): moves the robot back by one row.
        Return:
        the updated robot object
        """
        if self.row - 1 in range(Robot.maze_size):
            if Robot.maze[(self.row)-1][self.column]:
                if self.battery:
                    self.row -= 1
                    self.battery -= 1
                else:                          # insufficient charge in battery
                    pass
            else:                              # obstacle blocking robot's path
                pass
        else:                                  # boundary of maze is reached
            pass
        return self

    def one_step_right(self):
        """
        Move robot right one column and decrement the battery, if possible.

        Parameter:
        column(+=1): moves the robot to the right one square.
        Return:
        the updated robot object
        """
        if self.column + 1 in range(Robot.maze_size):
            if Robot.maze[self.row][self.column+1]:
                if self.battery:
                    self.column += 1
                    self.battery -= 1
                else:                          # insufficient charge in battery
                    pass
            else:                              # obstacle blocking robot's path
                pass
        else:                                  # boundary of maze is reached
            pass
        return self


    def one_step_left(self):
        """
        Move robot left one column and decrement the battery, if possible.

        Parameter:
        column(-=1): moves the robot to the left one square.
        Return:
        the updated robot object
        """
        if self.column - 1 in range(Robot.maze_size):
            if Robot.maze[self.row][(self.column)-1]:
                if self.battery:
                    self.column -= 1
                    self.battery -= 1
                else:                          # not enough charge in battery
                    pass
            else:                              # obstacle blocking robot's path
                pass
        else:                                  # boundary of maze is reached
            pass
        return self

    def forward(self, steps):
        """
        Move robot forward by 'n' rows and decrement the battery, if possible.

        Parameter:
        row(steps): the number of rows to move the robot.
        Return:
        the updated robot object
        """
        for i in range(0,steps):
            self.one_step_forward
        return self

    def backward(self, steps):
        """
        Move robot backward by 'n' rows and decrement the battery, if possible.

        Parameter:
        (steps): the number of rows to move the robot.
        Return:
        the updated robot object
        """
        for i in range(0,steps):
            self.one_step_back()
        return self


    def right(self, steps):
        """
        Move robot right by 'n' columns and decrement the battery, if possible.

        Parameter:
        (steps): the number of columns to move the robot.
        Return:
        the updated robot object
        """
        for i in range(0,steps):
            self.one_step_right()
        return self

    def left(self, steps):
        """
        Move robot left by 'n' columns and decrement the battery, if possible.

        Parameter:
        (steps): the number of columns to move the robot.
        Return:
        the updated robot object (Robot)
        """
        for i in range(0,steps):
            self.one_step_left()
        return self


    # The method below has been written for you
    # You can use it when testing your class

    def show(self):
        """
        Draw a graphical representation of the robot in the maze.

        The robot's position and color are shown.
        The color is assumed to be one of the colors recognized by tkinter
        (https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm)
        If the robot's battery is empty, the robot is shown in a
        horizontal position. Otherwise the robot is shown in an upright
        position.
        The obstacles in the maze are shown in red.

        Parameter: None
        Return: None
        """
        root = tkinter.Tk()
        root.title(self.name + ' in the Maze')
        canvas = tkinter.Canvas(root, background='light green',
                                width=self.unit_size * self.maze_size,
                                height=self.unit_size * self.maze_size)
        canvas.grid()

        # draw a representation of the robot in the maze
        if self.battery:
            upper_x = self.column * self.unit_size + self.unit_size / 4
            upper_y = self.row * self.unit_size
            lower_x = upper_x + self.unit_size / 2
            lower_y = upper_y + self.unit_size
            eye_x = lower_x - 3 * self.unit_size / 20
            eye_y = upper_y + self.unit_size / 10

        else: # the robot ran out of battery
            upper_x = self.column * self.unit_size
            upper_y = self.row * self.unit_size + self.unit_size / 2
            lower_x = upper_x + self.unit_size
            lower_y = upper_y + self.unit_size / 2
            eye_x = lower_x - 9 * self.unit_size / 10
            eye_y = lower_y - 3 * self.unit_size / 20

        rectangle = canvas.create_rectangle(upper_x,
                                            upper_y,
                                            lower_x,
                                            lower_y,
                                            fill=self.color)
        # draw the robot's eyes
        canvas.create_oval(upper_x + self.unit_size / 10,
                           upper_y + self.unit_size / 10,
                           upper_x + 3 * self.unit_size / 20,
                           upper_y + 3 * self.unit_size / 20,
                           fill='black')
        canvas.create_oval(eye_x,
                           eye_y,
                           eye_x + self.unit_size / 20,
                           eye_y + self.unit_size / 20,
                           fill='black')
        # draw the obstacles in the maze
        for row in range(self.maze_size):
            for col in range(self.maze_size):
                if not self.maze[row][col]:
                    canvas.create_rectangle(col * self.unit_size,
                                            row * self.unit_size,
                                            (col + 1) * self.unit_size,
                                            (row + 1) * self.unit_size,
                                            fill='red')
        for row in range(self.maze_size):
            canvas.create_line(0,
                               row * self.unit_size,
                               self.maze_size * self.unit_size,
                               row * self.unit_size)
        for col in range(self.maze_size):
            canvas.create_line(col * self.unit_size,
                               0,
                               col * self.unit_size,
                               self.maze_size * self.unit_size)
        root.mainloop()


# Enter your UnderwaterRobot Class definition below

class UnderwaterRobot(Robot):
    """
    Represent an UnderWaterRobot.

    Argument:
        name (str): robot's name
    Attributes:
        name (str): underwaterRobot's name
        depth (int): robot's depth position
    """

    # UnderwaterRobot class variable
    max_charge = 30

    def __init__(self,  name, color, depth, row=0, column=0):
        self.depth = depth
        Robot.__init__(self, name, color, row, column)
        self.battery = UnderwaterRobot.max_charge

    def __str__(self):
        return f'{self.name} is a {self.color} robot diving under water.'

    def dive(self, distance):
        """
        Move robot some specified distance in depth.

        Parameter:
        distance (int): moves the robot some specified depth.
        Return:
        self: the updated robot object(UnderwaterRobot)
        """
        self.depth += distance
        return self

    def recharge(self):
        """
        this method will recharge the robot's battery to the Robot.max_charge
        class variable.  It will return the updated robot object.
        """
        self.battery = UnderwaterRobot.max_charge
        return self                         # returns the updated robot object
