'''NOTE: When you click buttons on player 1 or player 2s side, they may appear pressed down even after unclicking them. This is just that side awaiting a response from the other side and is a feature on the tic tac toe game board to show the last player their latest move before the 
board updates from the other sides response'''


from gameboard import BoardClass
import tkinter as tk
import socket

board = tk.Tk()
BoardClass.gamesPlayed = 0
BoardClass.numTies = 0
BoardClass.numWins = 0
BoardClass.numLosses = 0
BoardClass.currGameBoard = [['1','2','3'],['4','5','6'],['7','8','9']]

def buttonSetup() -> None:
    """Sets up the buttons and their respective functions for the game board."""
    def updateGameBoard(oppositionMove: str) -> list:
        """Updates the game board based on the opposition's move.

        Args:
            oppositionMove (str): The opposition's move.

        Returns:
            list: The updated game board.
        """
        functionDictionary = {'1': placeOon1, '2': placeOon2, '3': placeOon3, '4': placeOon4, '5': placeOon5, '6': placeOon6, '7': placeOon7, '8': placeOon8, '9': placeOon9}
        functionDictionary[oppositionMove]()
        oppositionMove = int(oppositionMove)
        if 1 <= oppositionMove <= 3:
            BoardClass.currGameBoard[0][oppositionMove-1] = 'O'
        elif 4 <= oppositionMove <= 6:
            BoardClass.currGameBoard[1][oppositionMove-4] = 'O'
        elif 7 <= oppositionMove <= 9:
            BoardClass.currGameBoard[2][oppositionMove-7] = 'O'
        return BoardClass.currGameBoard
    
    def askQuestion() -> None:
        """Displays a question and buttons for continuing or stopping the game."""
        global question
        global yesButton
        global noButton
        global questionFrame
        questionFrame = tk.Tk()
        question = tk.Label(questionFrame, text='Do you want to continue playing?').grid()
        yesButton = tk.Button(questionFrame, text='YES', command=contPlaying).grid()
        noButton = tk.Button(questionFrame, text='NO', command=stopPlaying).grid()
        
        
    def gameOverRoute() -> None:
        """Handles the game over scenario and asks if player 1 wants to continue if there is a winner or a tie."""
        BoardClass.updateGamesPlayed(BoardClass)
        if BoardClass.isWinner(BoardClass.currGameBoard):
            askQuestion()
        elif BoardClass.boardIsFull(BoardClass.currGameBoard):
            BoardClass.numTies += 1
            askQuestion()
    
    def contPlaying() -> None:
        """Continues playing the game based on user input and resets the gameboard while setting up the new buttons."""
        questionFrame.destroy()
        BoardClass.conn.sendall('Play Again'.encode())
        BoardClass.currGameBoard = BoardClass.resetGameBoard(BoardClass.currGameBoard, buttonsList)
        buttonSetup()

    def stopPlaying() -> None:
        """Stops playing the game based on user input, destroys the frames and computes statistics in a new frame."""

        questionFrame.destroy()
        BoardClass.conn.sendall('Game Over'.encode())
        BoardClass.computeStats(BoardClass, board, BoardClass.p1UserName)

    def placeXon1() -> None:
        """Places an 'X' on slot 1 and handles game over scenarios along with sending and receiving the other players move."""
        slot1Button.config(text='X', bg='red')
        BoardClass.currGameBoard[0][0] = 'X'
        slot1Button["state"]= "disabled"
        placedBlock = '1'
        BoardClass.conn.sendall(placedBlock.encode())
        if BoardClass.isWinner(BoardClass.currGameBoard) or BoardClass.boardIsFull(BoardClass.currGameBoard):
            if BoardClass.isWinner(BoardClass.currGameBoard):
                BoardClass.numWins += 1
            gameOverRoute()
            
        else:
            otherPlayerMove = BoardClass.conn.recv(1024)
            otherPlayerMove = otherPlayerMove.decode()
            BoardClass.currGameBoard = updateGameBoard(otherPlayerMove)
            if BoardClass.isWinner(BoardClass.currGameBoard) or BoardClass.boardIsFull(BoardClass.currGameBoard):
                if BoardClass.isWinner(BoardClass.currGameBoard):
                    BoardClass.numLosses += 1
                gameOverRoute()
    
    def placeXon2() -> None:
        """Places an 'X' on slot 2 and handles game over scenarios along with sending and receiving the other players move."""
        slot2Button.config(text='X', bg='red')
        BoardClass.currGameBoard[0][1] = 'X'
        slot2Button["state"]= "disabled"
        placedBlock = '2'
        BoardClass.conn.sendall(placedBlock.encode())
        if BoardClass.isWinner(BoardClass.currGameBoard) or BoardClass.boardIsFull(BoardClass.currGameBoard):
            if BoardClass.isWinner(BoardClass.currGameBoard):
                BoardClass.numWins += 1
            gameOverRoute()
            
        else:
            otherPlayerMove = BoardClass.conn.recv(1024)
            otherPlayerMove = otherPlayerMove.decode()
            BoardClass.currGameBoard = updateGameBoard(otherPlayerMove)
            if BoardClass.isWinner(BoardClass.currGameBoard) or BoardClass.boardIsFull(BoardClass.currGameBoard):
                if BoardClass.isWinner(BoardClass.currGameBoard):
                    BoardClass.numLosses += 1
                gameOverRoute()

    def placeXon3() -> None:
        """Places an 'X' on slot 3 and handles game over scenarios along with sending and receiving the other players move."""

        slot3Button.config(text='X', bg='red')
        BoardClass.currGameBoard[0][2] = 'X'
        slot3Button["state"]= "disabled"
        placedBlock = '3'
        BoardClass.conn.sendall(placedBlock.encode())
        if BoardClass.isWinner(BoardClass.currGameBoard) or BoardClass.boardIsFull(BoardClass.currGameBoard):
            if BoardClass.isWinner(BoardClass.currGameBoard):
                BoardClass.numWins += 1
            gameOverRoute()
            
        else:
            otherPlayerMove = BoardClass.conn.recv(1024)
            otherPlayerMove = otherPlayerMove.decode()
            BoardClass.currGameBoard = updateGameBoard(otherPlayerMove)
            if BoardClass.isWinner(BoardClass.currGameBoard) or BoardClass.boardIsFull(BoardClass.currGameBoard):
                if BoardClass.isWinner(BoardClass.currGameBoard):
                    BoardClass.numLosses += 1
                gameOverRoute()
        
    def placeXon4() -> None:
        """Places an 'X' on slot 4 and handles game over scenarios along with sending and receiving the other players move."""
        slot4Button.config(text='X', bg='red')
        BoardClass.currGameBoard[1][0] = 'X'
        slot4Button["state"]= "disabled"
        placedBlock = '4'
        BoardClass.conn.sendall(placedBlock.encode())
        if BoardClass.isWinner(BoardClass.currGameBoard) or BoardClass.boardIsFull(BoardClass.currGameBoard):
            if BoardClass.isWinner(BoardClass.currGameBoard):
                BoardClass.numWins += 1
            gameOverRoute()
            
        else:
            otherPlayerMove = BoardClass.conn.recv(1024)
            otherPlayerMove = otherPlayerMove.decode()
            BoardClass.currGameBoard = updateGameBoard(otherPlayerMove)
            if BoardClass.isWinner(BoardClass.currGameBoard) or BoardClass.boardIsFull(BoardClass.currGameBoard):
                if BoardClass.isWinner(BoardClass.currGameBoard):
                    BoardClass.numLosses += 1
                gameOverRoute()
        
    def placeXon5() -> None:
        """Places an 'X' on slot 5 and handles game over scenarios along with sending and receiving the other players move."""
        slot5Button.config(text='X', bg='red')
        BoardClass.currGameBoard[1][1] = 'X'
        slot5Button["state"]= "disabled"
        placedBlock = '5'
        BoardClass.conn.sendall(placedBlock.encode())
        if BoardClass.isWinner(BoardClass.currGameBoard) or BoardClass.boardIsFull(BoardClass.currGameBoard):
            if BoardClass.isWinner(BoardClass.currGameBoard):
                BoardClass.numWins += 1
            gameOverRoute()
            
        else:
            otherPlayerMove = BoardClass.conn.recv(1024)
            otherPlayerMove = otherPlayerMove.decode()
            BoardClass.currGameBoard = updateGameBoard(otherPlayerMove)
            if BoardClass.isWinner(BoardClass.currGameBoard) or BoardClass.boardIsFull(BoardClass.currGameBoard):
                if BoardClass.isWinner(BoardClass.currGameBoard):
                    BoardClass.numLosses += 1
                gameOverRoute()
        
    def placeXon6() -> None:
        """Places an 'X' on slot 6 and handles game over scenarios along with sending and receiving the other players move."""
        slot6Button.config(text='X', bg='red')
        BoardClass.currGameBoard[1][2] = 'X'
        slot6Button["state"]= "disabled"
        placedBlock = '6'
        BoardClass.conn.sendall(placedBlock.encode())
        if BoardClass.isWinner(BoardClass.currGameBoard) or BoardClass.boardIsFull(BoardClass.currGameBoard):
            if BoardClass.isWinner(BoardClass.currGameBoard):
                BoardClass.numWins += 1
            gameOverRoute()
            
        else:
            otherPlayerMove = BoardClass.conn.recv(1024)
            otherPlayerMove = otherPlayerMove.decode()
            BoardClass.currGameBoard = updateGameBoard(otherPlayerMove)
            if BoardClass.isWinner(BoardClass.currGameBoard) or BoardClass.boardIsFull(BoardClass.currGameBoard):
                if BoardClass.isWinner(BoardClass.currGameBoard):
                    BoardClass.numLosses += 1
                gameOverRoute()
        
    def placeXon7() -> None:
        """Places an 'X' on slot 7 and handles game over scenarios along with sending and receiving the other players move."""
        slot7Button.config(text='X', bg='red')
        BoardClass.currGameBoard[2][0] = 'X'
        slot7Button["state"]= "disabled"
        placedBlock = '7'
        BoardClass.conn.sendall(placedBlock.encode())
        if BoardClass.isWinner(BoardClass.currGameBoard) or BoardClass.boardIsFull(BoardClass.currGameBoard):
            if BoardClass.isWinner(BoardClass.currGameBoard):
                BoardClass.numWins += 1
            gameOverRoute()
            
        else:
            otherPlayerMove = BoardClass.conn.recv(1024)
            otherPlayerMove = otherPlayerMove.decode()
            BoardClass.currGameBoard = updateGameBoard(otherPlayerMove)
            if BoardClass.isWinner(BoardClass.currGameBoard) or BoardClass.boardIsFull(BoardClass.currGameBoard):
                if BoardClass.isWinner(BoardClass.currGameBoard):
                    BoardClass.numLosses += 1
                gameOverRoute()
        
    def placeXon8() -> None:
        """Places an 'X' on slot 8 and handles game over scenarios along with sending and receiving the other players move."""
        slot8Button.config(text='X', bg='red')
        BoardClass.currGameBoard[2][1] = 'X'
        slot8Button["state"]= "disabled"
        placedBlock = '8'
        BoardClass.conn.sendall(placedBlock.encode())
        if BoardClass.isWinner(BoardClass.currGameBoard) or BoardClass.boardIsFull(BoardClass.currGameBoard):
            if BoardClass.isWinner(BoardClass.currGameBoard):
                BoardClass.numWins += 1
            gameOverRoute()
            
        else:
            otherPlayerMove = BoardClass.conn.recv(1024)
            otherPlayerMove = otherPlayerMove.decode()
            BoardClass.currGameBoard = updateGameBoard(otherPlayerMove)
            if BoardClass.isWinner(BoardClass.currGameBoard) or BoardClass.boardIsFull(BoardClass.currGameBoard):
                if BoardClass.isWinner(BoardClass.currGameBoard):
                    BoardClass.numLosses += 1
                gameOverRoute()
        
    def placeXon9() -> None:
        """Places an 'X' on slot 9 and handles game over scenarios along with sending and receiving the other players move."""
        slot9Button.config(text='X', bg='red')
        BoardClass.currGameBoard[2][2] = 'X'
        slot9Button["state"]= "disabled"
        placedBlock = '9'
        BoardClass.conn.sendall(placedBlock.encode())
        if BoardClass.isWinner(BoardClass.currGameBoard) or BoardClass.boardIsFull(BoardClass.currGameBoard):
            if BoardClass.isWinner(BoardClass.currGameBoard):
                BoardClass.numWins += 1
            gameOverRoute()
        else:
            otherPlayerMove = BoardClass.conn.recv(1024)
            otherPlayerMove = otherPlayerMove.decode()
            BoardClass.currGameBoard = updateGameBoard(otherPlayerMove)
            if BoardClass.isWinner(BoardClass.currGameBoard) or BoardClass.boardIsFull(BoardClass.currGameBoard):
                if BoardClass.isWinner(BoardClass.currGameBoard):
                    BoardClass.numLosses += 1
                gameOverRoute()
        
    def placeOon1()-> None:
        """Places an 'O' on slot 1 and handles game over scenarios while updating the backend board with the respective move."""
        switchPlayerTurn()
        slot1Button.config(text='O', bg='blue')
        BoardClass.currGameBoard[0][0] = 'O'
        slot1Button["state"]= "disabled"
    def placeOon2()-> None:
        """Places an 'O' on slot 2 and handles game over scenarios while updating the backend board with the respective move."""
        switchPlayerTurn()
        slot2Button.config(text='O', bg='blue')
        BoardClass.currGameBoard[0][1] = 'O'
        slot2Button["state"]= "disabled"
    def placeOon3()-> None:
        """Places an 'O' on slot 3 and handles game over scenarios while updating the backend board with the respective move."""
        switchPlayerTurn()
        slot3Button.config(text='O', bg='blue')
        BoardClass.currGameBoard[0][2] = 'O'
        slot3Button["state"]= "disabled"
    def placeOon4()-> None:
        """Places an 'O' on slot 4 and handles game over scenarios while updating the backend board with the respective move."""
        switchPlayerTurn()
        slot4Button.config(text='O', bg='blue')
        BoardClass.currGameBoard[1][0] = 'O'
        slot4Button["state"]= "disabled"
    def placeOon5()-> None:
        """Places an 'O' on slot 5 and handles game over scenarios while updating the backend board with the respective move."""
        switchPlayerTurn()
        slot5Button.config(text='O', bg='blue')
        BoardClass.currGameBoard[1][1] = 'O'
        slot5Button["state"]= "disabled"
    def placeOon6()-> None:
        """Places an 'O' on slot 6 and handles game over scenarios while updating the backend board with the respective move."""
        switchPlayerTurn()
        slot6Button.config(text='O', bg='blue')
        BoardClass.currGameBoard[1][2] = 'O'
        slot6Button["state"]= "disabled"
    def placeOon7()-> None:
        """Places an 'O' on slot 7 and handles game over scenarios while updating the backend board with the respective move."""
        switchPlayerTurn()
        slot7Button.config(text='O', bg='blue')
        BoardClass.currGameBoard[2][0] = 'O'
        slot7Button["state"]= "disabled"
    def placeOon8()-> None:
        """Places an 'O' on slot 8 and handles game over scenarios while updating the backend board with the respective move."""
        switchPlayerTurn()
        slot8Button.config(text='O', bg='blue')
        BoardClass.currGameBoard[2][1] = 'O'
        slot8Button["state"]= "disabled"
    def placeOon9()-> None:
        """Places an 'O' on slot 9 and handles game over scenarios while updating the backend board with the respective move."""
        switchPlayerTurn()
        slot9Button.config(text='O', bg='blue')
        BoardClass.currGameBoard[2][2] = 'O'
        slot9Button["state"]= "disabled"


    def switchPlayerTurn()-> None:
        """Switches the current player's turn in the game. This function is responsible for changing the current player's turn in the game."""
        if currentPlayerTab['text'] == f'{BoardClass.p1UserName}':
            currentPlayerTab.config(text=f'{BoardClass.p2UserName}')
        
        elif currentPlayerTab['text'] == f'{BoardClass.p2UserName}':
            currentPlayerTab.config(text=f'{BoardClass.p1UserName}')

    slot1Button = tk.Button(board,text='Slot 1',command=lambda: [switchPlayerTurn(), placeXon1()], height=10, width=10)
    slot1Button.grid(row=1, column = 1, padx=5,  pady=5)


    slot2Button = tk.Button(board,text='Slot 2',command=lambda: [switchPlayerTurn(), placeXon2()], height=10, width=10)
    slot2Button.grid(row=1, column = 2, padx=0,  pady=5)


    slot3Button = tk.Button(board,text='Slot 3',command=lambda: [switchPlayerTurn(), placeXon3()], height=10, width=10)
    slot3Button.grid(row=1, column = 3, padx=0,  pady=5)


    slot4Button = tk.Button(board,text='Slot 4',command=lambda: [switchPlayerTurn(), placeXon4()], height=10, width=10)
    slot4Button.grid(row=2, column = 1, padx=5,  pady=5)


    slot5Button = tk.Button(board,text='Slot 5',command=lambda: [switchPlayerTurn(), placeXon5()], height=10, width=10)
    slot5Button.grid(row=2, column = 2, padx=5,  pady=5)


    slot6Button = tk.Button(board,text='Slot 6',command=lambda: [switchPlayerTurn(), placeXon6()], height=10, width=10)
    slot6Button.grid(row=2, column = 3, padx=5,  pady=5)

    slot7Button = tk.Button(board,text='Slot 7',command=lambda: [switchPlayerTurn(), placeXon7()], height=10, width=10)
    slot7Button.grid(row=3, column = 1, padx=5,  pady=5)


    slot8Button = tk.Button(board,text='Slot 8',command=lambda: [switchPlayerTurn(), placeXon8()], height=10, width=10)
    slot8Button.grid(row=3, column = 2, padx=5,  pady=5)


    slot9Button = tk.Button(board,text='Slot 9',command=lambda: [switchPlayerTurn(), placeXon9()], height=10, width=10)
    slot9Button.grid(row=3, column = 3, padx=5,  pady=5)
    
    notificationWindow = tk.Tk()
    notificationTab = tk.Button(notificationWindow, text='Last Player Turn:')
    notificationTab.grid()
    currentPlayerTab = tk.Button(notificationWindow, text=f'{BoardClass.p1UserName}')
    currentPlayerTab.grid()
    
    global buttonsList
    buttonsList = [slot1Button, slot2Button, slot3Button, slot4Button, slot5Button, slot6Button, slot7Button, slot8Button, slot9Button, currentPlayerTab, notificationWindow]


def sendUserName() -> None:
    """Send the user name to the other player and update the game board.

    This function sends the player's user name to the other player through the established connection,
    updates 'BoardClass.p1UserName' and 'BoardClass.p2UserName' accordingly, and displays Player 2's user name on the board.
    It initializes the game board, sets the 'ipSet' flag, and starts the main event loop."""
    global p1UserName
    
    p1UserName = p1UserName.get()
    BoardClass.p1UserName = p1UserName
    BoardClass.conn.sendall(str(p1UserName).encode())
    p2UserName = BoardClass.conn.recv(1024)
    p2UserName = p2UserName.decode()
    BoardClass.p2UserName = p2UserName
    tk.Label(board, text=f'Player 2s User Name: {p2UserName}').grid()
    global ipSet
    ipSet = True
    BoardClass.currGameBoard = [['1','2','3'],['4','5','6'],['7','8','9']]
    tk.Label(board, text=f'Connected!').grid()
        
    label = tk.Label(board, text='Welcome to Tic Tac Toe!', font=('Arial', 21))
    label.grid(padx=20, pady=20)

    while ipSet:
        buttonSetup()
        board.mainloop()

def attemptConnection() -> None:
    """Attempt to establish a connection with another player and set up the game board.

    This function binds the specified IP address and port to the server socket, accepts a connection from the other player, prompts the player to input their user name, and sets up the necessary components for this on the game board."""
    serverSocket.bind((BoardClass.p1IP, int(BoardClass.p1Port)))
    serverSocket.listen(2)
    BoardClass.conn, BoardClass.address = serverSocket.accept()
    tk.Label(board, text='Please input Player 1 user name:').grid()
    tk.Entry(board, textvariable=p1UserName).grid()
    sendButton = tk.Button(board,text='Send', command=sendUserName).grid()

    
    

def askIP() -> None:
    """Prompt the user to enter the IP address and port to connect to.

    This function displays input fields for the IP address and port on the game board,allowing the player to enter the desired connection details."""
    tk.Label(board, text='Please put the IP address you want to connect to:').grid()
    tk.Entry(board, textvariable=IP).grid()
    tk.Label(board, text='Please put the Port you want to connect to:').grid()
    tk.Entry(board, textvariable=Port).grid()
    submitButton = tk.Button(board,text='Submit', command=setIP).grid()    


def setIP() -> None:
    """Set the IP address and port for the connection.

    This function retrieves the IP address and port entered by the player, assigns them to 'BoardClass.p1IP' and 'BoardClass.p1Port', and creates a 'Connect' button on the game board to initiate the connection."""
    BoardClass.p1IP = IP.get()
    BoardClass.p1Port = Port.get()
    connectButton = tk.Button(board,text='Connect', command=attemptConnection).grid()

BoardClass.p1UserName = tk.StringVar()

if __name__ == '__main__':
    board.title("2-Player Tic Tac Toe")
    board.geometry("1000x1000")

    BoardClass.p1IP = ''
    BoardClass.p1Port = ''

    global IP
    global Port
    IP = tk.StringVar()
    Port = tk.StringVar()
    global p1UserName
    p1UserName = tk.StringVar()
    ipSet = False
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    askIP()
    
