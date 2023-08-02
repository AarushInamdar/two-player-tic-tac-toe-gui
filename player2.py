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

def contPlaying()-> None:
    """Continues playing the game based on user input and resets the gameboard while setting up the new buttons."""
    BoardClass.currGameBoard = BoardClass.resetGameBoard(BoardClass.currGameBoard, buttonsList)
    firstMove = serverSocket.recv(1024)
    firstMove = firstMove.decode()
    buttonSetup(firstMove)

def stopPlaying()-> None:
    """Stops playing the game based on user input, destroys the frames and computes statistics in a new frame."""
    BoardClass.computeStats(BoardClass, board, BoardClass.p2UserName)


def buttonSetup(firstMove: str) -> None:
    """Sets up the buttons and their respective functions for the game board. Waits for the first move from player 1 and then acts according to game rules."""
    def gameOverRoute():
        """Handles the game over scenario and asks if player 1 wants to continue if there is a winner or a tie."""
        BoardClass.updateGamesPlayed(BoardClass)
        
        if BoardClass.boardIsFull(BoardClass.currGameBoard) and not BoardClass.isWinner(BoardClass.currGameBoard):
            BoardClass.numTies += 1
        playDecision = serverSocket.recv(1024)
        playDecision = playDecision.decode()
        if playDecision == 'Play Again':
            contPlaying()
        else:
            stopPlaying()

    def checkWinOrTie()-> None:
        """Check if the game has ended in a win or tie.

        This function checks the current state of the game board to determine if the game has ended
        in a win or tie. If either condition is met, the corresponding player's win/loss count is
        updated, and the game over route is triggered. Otherwise, it waits for the other player's move
        and updates the game board accordingly. If the game ends after the other player's move, the
        current player's loss count is updated, and the game over route is triggered."""
        if BoardClass.isWinner(BoardClass.currGameBoard) or BoardClass.boardIsFull(BoardClass.currGameBoard):
                if BoardClass.isWinner(BoardClass.currGameBoard):
                    BoardClass.numWins += 1
                gameOverRoute()
                
        else:
            otherPlayerMove = serverSocket.recv(1024)
            otherPlayerMove = otherPlayerMove.decode()
            updateGameBoard(otherPlayerMove)
            if BoardClass.isWinner(BoardClass.currGameBoard) or BoardClass.boardIsFull(BoardClass.currGameBoard):
                if BoardClass.isWinner(BoardClass.currGameBoard):
                    BoardClass.numLosses += 1
                gameOverRoute()
    
    def placeOon1()-> None:
        """Places an 'O' on slot 1 and handles game over scenarios along with sending and receiving the other players move and updating the backend board with the respective move"""
        slot1Button.config(text='O', bg='blue')
        BoardClass.currGameBoard[0][0] = 'O'
        slot1Button["state"]= "disabled"
        placedBlock = '1'
        serverSocket.sendall(placedBlock.encode())
        checkWinOrTie()
    
    def placeOon2()-> None:
        """Places an 'O' on slot 2 and handles game over scenarios along with sending and receiving the other players move and updating the backend board with the respective move"""
        slot2Button.config(text='O', bg='blue')
        BoardClass.currGameBoard[0][1] = 'O'
        slot2Button["state"]= "disabled"
        placedBlock = '2'
        serverSocket.sendall(placedBlock.encode())
        checkWinOrTie()
    
    def placeOon3()-> None:
        """Places an 'O' on slot 3 and handles game over scenarios along with sending and receiving the other players move and updating the backend board with the respective move"""
        slot3Button.config(text='O', bg='blue')
        BoardClass.currGameBoard[0][2] = 'O'
        slot3Button["state"]= "disabled"
        placedBlock = '3'
        serverSocket.sendall(placedBlock.encode())
        checkWinOrTie()
    
    def placeOon4()-> None:
        """Places an 'O' on slot 4 and handles game over scenarios along with sending and receiving the other players move and updating the backend board with the respective move"""
        slot4Button.config(text='O', bg='blue')
        BoardClass.currGameBoard[1][0] = 'O'
        slot4Button["state"]= "disabled"
        placedBlock = '4'
        serverSocket.sendall(placedBlock.encode())
        checkWinOrTie()


    def placeOon5()-> None:
        """Places an 'O' on slot 5 and handles game over scenarios along with sending and receiving the other players move and updating the backend board with the respective move"""
        slot5Button.config(text='O', bg='blue')
        BoardClass.currGameBoard[1][1] = 'O'
        slot5Button["state"]= "disabled"
        placedBlock = '5'
        serverSocket.sendall(placedBlock.encode())
        checkWinOrTie()
    
    def placeOon6()-> None:
        """Places an 'O' on slot 6 and handles game over scenarios along with sending and receiving the other players move and updating the backend board with the respective move"""
        slot6Button.config(text='O', bg='blue')
        BoardClass.currGameBoard[1][2] = 'O'
        slot6Button["state"]= "disabled"
        placedBlock = '6'
        serverSocket.sendall(placedBlock.encode())
        checkWinOrTie()
    
    def placeOon7()-> None:
        """Places an 'O' on slot 7 and handles game over scenarios along with sending and receiving the other players move and updating the backend board with the respective move"""
        slot7Button.config(text='O', bg='blue')
        BoardClass.currGameBoard[2][0] = 'O'
        slot7Button["state"]= "disabled"
        placedBlock = '7'
        serverSocket.sendall(placedBlock.encode())
        checkWinOrTie()
    
    def placeOon8()-> None:
        """Places an 'O' on slot 8 and handles game over scenarios along with sending and receiving the other players move and updating the backend board with the respective move"""
        slot8Button.config(text='O', bg='blue')
        BoardClass.currGameBoard[2][1] = 'O'
        slot8Button["state"]= "disabled"
        placedBlock = '8'
        serverSocket.sendall(placedBlock.encode())
        checkWinOrTie()
    
    def placeOon9()-> None:
        """Places an 'O' on slot 9 and handles game over scenarios along with sending and receiving the other players move and updating the backend board with the respective move"""
        slot9Button.config(text='O', bg='blue')
        BoardClass.currGameBoard[2][2] = 'O'
        slot9Button["state"]= "disabled"
        placedBlock = '9'
        serverSocket.sendall(placedBlock.encode())
        checkWinOrTie()
    
    def placeXon1()-> None:
        """Places an 'X' on slot 1 and handles game over scenarios and updating the backend board with the respective move"""
        switchPlayerTurn()
        slot1Button.config(text='X', bg='red')
        BoardClass.currGameBoard[0][0] = 'X'
        slot1Button["state"]= "disabled"
    def placeXon2()-> None:
        """Places an 'X' on slot 2 and handles game over scenarios and updating the backend board with the respective move"""
        switchPlayerTurn()
        slot2Button.config(text='X', bg='red')
        BoardClass.currGameBoard[0][1] = 'X'
        slot2Button["state"]= "disabled"
    def placeXon3()-> None:
        """Places an 'X' on slot 3 and handles game over scenarios and updating the backend board with the respective move"""
        switchPlayerTurn()
        slot3Button.config(text='X', bg='red')
        BoardClass.currGameBoard[0][2] = 'X'
        slot3Button["state"]= "disabled"
    def placeXon4()-> None:
        """Places an 'X' on slot 4 and handles game over scenarios and updating the backend board with the respective move"""
        switchPlayerTurn()
        slot4Button.config(text='X', bg='red')
        BoardClass.currGameBoard[1][0] = 'X'
        slot4Button["state"]= "disabled"
    def placeXon5()-> None:
        """Places an 'X' on slot 5 and handles game over scenarios and updating the backend board with the respective move"""
        switchPlayerTurn()
        slot5Button.config(text='X', bg='red')
        BoardClass.currGameBoard[1][1] = 'X'
        slot5Button["state"]= "disabled"
    def placeXon6()-> None:
        """Places an 'X' on slot 6 and handles game over scenarios and updating the backend board with the respective move"""
        switchPlayerTurn()
        slot6Button.config(text='X', bg='red')
        BoardClass.currGameBoard[1][2] = 'X'
        slot6Button["state"]= "disabled"
    def placeXon7()-> None:
        """Places an 'X' on slot 7 and handles game over scenarios and updating the backend board with the respective move"""
        switchPlayerTurn()
        slot7Button.config(text='X', bg='red')
        BoardClass.currGameBoard[2][0] = 'X'
        slot7Button["state"]= "disabled"
    def placeXon8()-> None:
        """Places an 'X' on slot 8 and handles game over scenarios and updating the backend board with the respective move"""
        switchPlayerTurn()
        slot8Button.config(text='X', bg='red')
        BoardClass.currGameBoard[2][1] = 'X'
        slot8Button["state"]= "disabled"
    def placeXon9()-> None:
        """Places an 'X' on slot 9 and handles game over scenarios and updating the backend board with the respective move"""
        switchPlayerTurn()
        slot9Button.config(text='X', bg='red')
        BoardClass.currGameBoard[2][2] = 'X'
        slot9Button["state"]= "disabled"
    
    def updateGameBoard(oppositionMove: str) -> None:
        """Update the game board based on the opposition's move.

        This function takes the opposition's move as input and uses a dictionary mapping to call the
        corresponding function to update the game board. The dictionary maps each move to a specific
        function that places an 'X' at the corresponding position on the board."""
        functionDictionary = {'1': placeXon1, '2': placeXon2, '3': placeXon3, '4': placeXon4, '5': placeXon5, '6': placeXon6, '7': placeXon7, '8': placeXon8, '9': placeXon9}
        functionDictionary[oppositionMove]()
    
    
    def switchPlayerTurn()-> None:
        """Switch the turn from the current player to the other player.

        This function switches the turn from the current player to the other player. It checks the
        current player displayed on the GUI and updates it to the corresponding opposite player."""
        if currentPlayerTab['text'] == f'{BoardClass.p1UserName}':
            currentPlayerTab.config(text=f'{BoardClass.p2UserName}')
        
        elif currentPlayerTab['text'] == f'{BoardClass.p2UserName}':
            currentPlayerTab.config(text=f'{BoardClass.p1UserName}')

    slot1Button = tk.Button(board,text='Slot 1',command=lambda: [switchPlayerTurn(), placeOon1()], height=10, width=10)
    slot1Button.grid(row=1, column = 1, padx=5,  pady=5)


    slot2Button = tk.Button(board,text='Slot 2',command=lambda: [switchPlayerTurn(), placeOon2()], height=10, width=10)
    slot2Button.grid(row=1, column = 2, padx=0,  pady=5)


    slot3Button = tk.Button(board,text='Slot 3',command=lambda: [switchPlayerTurn(), placeOon3()], height=10, width=10)
    slot3Button.grid(row=1, column = 3, padx=0,  pady=5)


    slot4Button = tk.Button(board,text='Slot 4',command=lambda: [switchPlayerTurn(), placeOon4()], height=10, width=10)
    slot4Button.grid(row=2, column = 1, padx=5,  pady=5)


    slot5Button = tk.Button(board,text='Slot 5',command=lambda: [switchPlayerTurn(), placeOon5()], height=10, width=10)
    slot5Button.grid(row=2, column = 2, padx=5,  pady=5)


    slot6Button = tk.Button(board,text='Slot 6',command=lambda: [switchPlayerTurn(), placeOon6()], height=10, width=10)
    slot6Button.grid(row=2, column = 3, padx=5,  pady=5)

    slot7Button = tk.Button(board,text='Slot 7',command=lambda: [switchPlayerTurn(), placeOon7()], height=10, width=10)
    slot7Button.grid(row=3, column = 1, padx=5,  pady=5)


    slot8Button = tk.Button(board,text='Slot 8',command=lambda: [switchPlayerTurn(), placeOon8()], height=10, width=10)
    slot8Button.grid(row=3, column = 2, padx=5,  pady=5)


    slot9Button = tk.Button(board,text='Slot 9',command=lambda: [switchPlayerTurn(), placeOon9()], height=10, width=10)
    slot9Button.grid(row=3, column = 3, padx=5,  pady=5)
    
    notificationWindow = tk.Tk()
    notificationTab = tk.Button(notificationWindow, text='Last Player Turn:')
    notificationTab.grid()
    currentPlayerTab = tk.Button(notificationWindow, text=f'{BoardClass.p1UserName}')
    currentPlayerTab.grid()

    updateGameBoard(firstMove)

    global buttonsList
    buttonsList = [slot1Button, slot2Button, slot3Button, slot4Button, slot5Button, slot6Button, slot7Button, slot8Button, slot9Button, notificationWindow]




board.title("2-Player Tic Tac Toe")
board.geometry("1000x1000")
BoardClass.p1IP = ''
BoardClass.p1Port = ''

global IP
global Port
IP = tk.StringVar()
Port = tk.StringVar()
global p2UserName
p2UserName = tk.StringVar()
ipSet = False
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def sendUserName()-> None:
    """Send the user name to the server.

    This function retrieves the user name entered in the GUI, sets it as the second player's user
    name, and sends it to the server using the `serverSocket`. It also sets the `ipSet` flag to
    True, indicating a successful connection. Afterward, it displays a "Connected!" label on the
    GUI and sets up the initial game board."""
    global p2UserName
    p2UserName = p2UserName.get()
    BoardClass.p2UserName = p2UserName
    serverSocket.sendall(str(p2UserName).encode())
    global ipSet
    ipSet = True
    BoardClass.currGameBoard = [['1','2','3'],['4','5','6'],['7','8','9']]
    while ipSet:
        tk.Label(board, text=f'Connected!').grid()
        

        label = tk.Label(board, text='Welcome to Tic Tac Toe!', font=('Arial', 21))
        label.grid(padx=20, pady=20)

        firstMove = serverSocket.recv(1024)
        firstMove = firstMove.decode()
        buttonSetup(firstMove)
        board.mainloop()

    

def attemptConnection()-> None:
    """Attempt to establish a connection with the server.

    This function attempts to connect to the server using the IP address and port number provided
    in `BoardClass.p2IP` and `BoardClass.p2Port`. If the connection is successful, it sets the
    `ipSet` flag to True, indicating a successful connection. It receives the first player's user
    name from the server, sets it as the first player's user name in `BoardClass.p1UserName`, and
    displays it on the GUI. It prompts the second player to input their user name in the GUI and
    binds the "Send" button to the `sendUserName` function."""
    serverSocket.connect((BoardClass.p2IP, int(BoardClass.p2Port)))
    global ipSet
    ipSet = True
    p1UserName = serverSocket.recv(1024)
    p1UserName = p1UserName.decode()
    BoardClass.p1UserName = p1UserName
    tk.Label(board, text=f'Player 1s User Name: {p1UserName}').grid()
    tk.Label(board, text='Please input Player 2 user name:').grid()
    global p2UserName
    tk.Entry(board, textvariable=p2UserName).grid()
    sendButton = tk.Button(board,text='Send', command=sendUserName).grid()

def askIP()-> None:
    """Ask the user to input the IP address and port number.

    This function displays labels and input fields on the GUI, prompting the user to enter the IP
    address and port number they want to connect to."""
    tk.Label(board, text='Please put the IP address you want to connect to:').grid()
    tk.Entry(board, textvariable=IP).grid()
    tk.Label(board, text='Please put the Port you want to connect to:').grid()
    tk.Entry(board, textvariable=Port).grid()
    submitButton = tk.Button(board,text='Submit', command=setIP).grid()    


def setIP()-> None:
    """Set the IP address and port number.

    This function retrieves the IP address and port number entered in the GUI, sets them as the
    second player's IP address and port number in `BoardClass.p2IP` and `BoardClass.p2Port`,
    respectively."""
    BoardClass.p2IP = IP.get()
    BoardClass.p2Port = Port.get()
    
    connectButton = tk.Button(board,text='Connect', command=attemptConnection).grid()

BoardClass.p1UserName = tk.StringVar()
BoardClass.p2UserName = tk.StringVar()

if __name__ == '__main__':
     
    askIP()

