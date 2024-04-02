import numpy as np


class State:
    """
    Class representing the state of a Tic Tac Toe game.

    Attributes:
    state (list): A 3x3 array representing the current state of the Tic Tac Toe board.
    dict (dict): A dictionary mapping numeric positions (1-9) to corresponding indices in the state array.
    """

    def __init__(self, array):
        """
        Initializes a State object with the given array representing the current state of the game.

        Args:
        array (list): A 3x3 array representing the initial state of the Tic Tac Toe board.
        """
        self.state = array
        self.dict = {
            1: [0, 0], 2: [0, 1], 3: [0, 2],
            4: [1, 0], 5: [1, 1], 6: [1, 2],
            7: [2, 0], 8: [2, 1], 9: [2, 2]
        }

    def printState(self):
        """
        Prints the current state of the Tic Tac Toe board.
        """
        print("------ACTUAL-STATE------")
        print(self.state[0])
        print(self.state[1])
        print(self.state[2], "\n\n")

    def insertchoice(self, player):
        """
        Inserts the choice made by the player into the Tic Tac Toe board.

        Args:
        player (str): A string representing the player's choice ('X' or 'O').

        Returns:
        None
        """
        n = input("MAKE A CHOICE (1-9): ")

        while True:
            if n.isnumeric:
                n = int(n)
                if self.state[self.dict[n][0]][self.dict[n][1]] == "-":
                    break

            print("ACTION NOT ALLOWED \n ")
            n = input("SELECT AN ACTION :")

        self.addChoice([self.dict[n][0], self.dict[n][1]], player)

    def addChoice(self, pos, player):
        """
        Adds the player's choice to the specified position on the Tic Tac Toe board.

        Args:
        pos (list): A list containing the row and column indices where the player's choice is to be added.
        player (str): A string representing the player's choice ('X' or 'O').

        Returns:
        None
        """
        self.state[pos[0]][pos[1]] = player




class MinMax:
    """
    Class implementing the Minimax algorithm for Tic Tac Toe game.

    Attributes:
    value (int): Current evaluation value of the game state.
    dafare (list): Coordinates of the best move to be made by the AI.
    """

    def __init__(self):
        """
        Initializes the MinMax object with default values.

        Attributes:
        value (int): Current evaluation value of the game state (default 0).
        dafare (list): Coordinates of the best move to be made by the AI (default [0, 0]).
        """
        self.value = 0
        self.dafare = [0, 0]

    def check(self, state):
        """
        Checks if the game has been won by either player or if it's a draw.

        Args:
        state (list): 3x3 array representing the current state of the Tic Tac Toe board.

        Returns:
        list: A list containing two elements:
              - Boolean value indicating if the game is over.
              - Integer value representing the outcome of the game (1 for X win, -1 for O win, 0 for draw).
        """
        for n in range(3):
            if self.checkrow(state[n]):
                return [True, self.value]
            if self.checkrow([state[0][n], state[1][n], state[2][n]]):
                return [True, self.value]

        if self.checkrow([state[0][0], state[1][1], state[2][2]]):
            return [True, self.value]

        if self.checkrow([state[0][2], state[1][1], state[2][0]]):
            return [True, self.value]

        finished = True
        for i in range(3):
            for j in range(3):
                if state[i][j] == "-":
                    finished = False
        if finished:
            self.value = 0
            return [True, 0]

        return [False, None]

    def checkrow(self, row):
        """
        Checks if a row on the Tic Tac Toe board represents a winning configuration.

        Args:
        row (list): A list representing a row on the Tic Tac Toe board.

        Returns:
        bool: True if the row represents a winning configuration, False otherwise.
        """
        if row[0] == row[1] == row[2] and row[0] != "-":
            if row[0] == "X":
                self.value = 1
            else:
                self.value = -1
            return True
        return False

    def action(self, state):
        """
        Generates all possible actions (empty cells) available in the current state.

        Args:
        state (list): 3x3 array representing the current state of the Tic Tac Toe board.

        Returns:
        list: A list containing coordinates of all empty cells in the current state.
        """
        actions = []
        for x in range(3):
            for y in range(3):
                if state[x][y] == "-":
                    actions.append([x, y])
        return actions

    def makeaction(self, state, action, player):
        """
        Updates the game state by making a move.

        Args:
        state (list): 3x3 array representing the current state of the Tic Tac Toe board.
        action (list): Coordinates of the cell where the move is to be made.
        player (str): The player making the move ('X' or 'O').

        Returns:
        list: Updated game state after making the move.
        """
        state[action[0]][action[1]] = player
        return state

    def Min(self, state):
        """
        Minimax function for the minimizing player.

        Args:
        state (list): 3x3 array representing the current state of the Tic Tac Toe board.

        Returns:
        int: The evaluation value of the current state for the minimizing player.
        """
        v = 2
        dafare = []
        res = self.check(state)
        if res[0]:
            v = res[1]
            return v

        actions = self.action(state)
        for a in actions:
            vn = self.Max(self.makeaction(state.copy(), a, "O"))
            if v > vn:
                v = vn
                dafare = a

        self.dafare = dafare
        return v

    def Max(self, state):
        """
        Minimax function for the maximizing player.

        Args:
        state (list): 3x3 array representing the current state of the Tic Tac Toe board.

        Returns:
        int: The evaluation value of the current state for the maximizing player.
        """
        v = -2
        dafare = []
        res = self.check(state)
        if res[0]:
            v = res[1]
            return v

        actions = self.action(state)
        for a in actions:
            vn = self.Min(self.makeaction(state.copy(), a, "X"))
            if v < vn:
                v = vn
                dafare = a

        self.dafare = dafare
        return v




print("WELCOME TO TIC TAC TOE")
turno=0

#initialize algorithm
Ai=MinMax()
#create the initial state
tab=State([["-","-","-"],["-","-","-"],["-","-","-"]])
#game loop
while(True):
    print("\n\nTURN ",turno)

    #check if player turn or AI turn
    if(turno%2==0):
        print("YOUR TURN")
        tab.printState()
        tab.insertchoice("X")
    else:
        print("AI TURN")
        tab.printState()
        Ai.Min(np.copy(tab.state))
        tab.addChoice(Ai.dafare,"O")

    turno=turno+1
    
    #check if game is over
    if(Ai.check(np.copy(tab.state))[0]):
        break
    
#check final result and print related prompt
if(Ai.value==1):
    print("YOU WON, CONGRATULATIONS")
elif Ai.value==0:
    print("TIE; U WILL NEVER BEAT ME")
else:
    print("I WON, EZ GAME")

tab.printState()