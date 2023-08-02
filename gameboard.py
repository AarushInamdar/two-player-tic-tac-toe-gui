import tkinter as tk
class BoardClass():
    def __init__(self) -> None:
        self.p1UserName = ''
        self.p2UserName = ''
        self.lastTurnUserName = ''
        self.numWins = 0
        self.numLosses = 0
        self.numTies = 0
        self.gamesPlayed = 0
        self.playerValue = ''
        self.p1IP = ''
        self.p1Port = ''
        self.p2IP = ''
        self.p2Port = ''
        pass

    def updateGamesPlayed(self) -> None:
        """Increment the count of games played by one.

        This method updates the 'gamesPlayed' attribute of the object by incrementing it by one."""
        self.gamesPlayed += 1
        
    def resetGameBoard(currGameBoard: list, buttonsList: list) -> list:
        """Reset the game board and destroy the buttons.

        This function resets the 'currGameBoard' to its initial state, which is a 3x3 grid with numbers from 1 to 9.
        It also destroys the buttons in the 'buttonsList' to clear the game board visually.
        The updated 'currGameBoard' is returned."""
        currGameBoard = [['1','2','3'],['4','5','6'],['7','8','9']]
        for button in buttonsList:
            button.destroy()
        return currGameBoard
        

    def updateGameBoard(self):
        '''This function has beend defined locally in each player file due to the structure of my code. Please refer to updateGameBoard() in player1.py and player2.py'''

        '''Updates the game board with the player's move'''
        pass

    def isWinner(gameBoard:list) -> bool:
        ''' Checks if the latest move resulted in a win. Updates the wins and losses count. Goes over every possible combination of win criteria for the game board and checks if the players have won or not.'''
        Flag = False
        for lists in gameBoard:
            if lists[0] == lists[1] == lists[2]:
                return True
        if (gameBoard[0][0].lower() == 'x' and gameBoard[1][0].lower() == 'x' and gameBoard[2][0].lower() == 'x') or (gameBoard[0][0].lower() == 'o' and gameBoard[1][0].lower() == 'o' and gameBoard[2][0].lower() == 'o'):
            Flag = True
        elif (gameBoard[0][1].lower() == 'x' and gameBoard[1][1].lower() == 'x' and gameBoard[2][1].lower() == 'x') or (gameBoard[0][1].lower() == 'o' and gameBoard[1][1].lower() == 'o' and gameBoard[2][1].lower() == 'o'):
            Flag = True
        elif (gameBoard[0][2].lower() == 'x' and gameBoard[1][2].lower() == 'x' and gameBoard[2][2].lower() == 'x') or (gameBoard[0][2].lower() == 'o' and gameBoard[1][2].lower() == 'o' and gameBoard[2][2].lower() == 'o'):
            Flag = True
        elif (gameBoard[0][0].lower() == 'x' and gameBoard[1][1].lower() == 'x' and gameBoard[2][2].lower() == 'x') or (gameBoard[0][0].lower() == 'o' and gameBoard[1][1].lower() == 'o' and gameBoard[2][2].lower() == 'o'):
            Flag = True
        elif (gameBoard[0][2].lower() == 'x' and gameBoard[1][1].lower() == 'x' and gameBoard[2][0].lower() == 'x') or (gameBoard[0][2].lower() == 'o' and gameBoard[1][1].lower() == 'o' and gameBoard[2][0].lower() == 'o'):
            Flag = True
        return Flag
        
    def boardIsFull(gameBoard:list) -> bool:
        '''Goes over every piece on the board to see if a valid move has been played, if so the board is full and it returns true otherwise it will return False'''
        movesPlayable = ['x', 'X', 'o', 'O']
        Flag = True
        for list in gameBoard:
            for variable in list:
                if variable not in movesPlayable:
                    Flag = False
        return Flag

    def computeStats(self, board: tk, currentPlayer: str) -> None:
        """Compute and display player statistics in a separate window.

        This method creates a new window to display player statistics based on the current game state.
        The statistics shown include the usernames of Player 1 and Player 2, the number of games played,
        the current player's wins, losses, and total ties. The 'board' window is destroyed after the stats
        window is created."""
        statsSheet = tk.Tk()
        statsSheet.geometry("400x400")
        statsSheet.title(f'{currentPlayer}\'s Statistics')
        tk.Label(statsSheet, text=f'Username of Player 1: {self.p1UserName}').grid()
        tk.Label(statsSheet, text=f'Username of Player 2: {self.p2UserName}').grid()
        tk.Label(statsSheet, text=f'Number of Games: {self.gamesPlayed}').grid()
        tk.Label(statsSheet, text=f'{currentPlayer}\'s Wins: {self.numWins}').grid()
        tk.Label(statsSheet, text=f'{currentPlayer}\'s Losses: {self.numLosses}').grid()
        tk.Label(statsSheet, text=f'Total Ties: {self.numTies}').grid()
        board.destroy()

