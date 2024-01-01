import random
from subprocess import call

class Game:
    def __init__(self, name):
        self.name = name

    def play(self):
        pass

        #Tic Tac Toe Game

def Tic_Tac_Toe():
    def sum(a, b, c ):
     return a + b + c

    def printBoard(xState, zState):
        zero = 'X' if xState[0] else ('O' if zState[0] else 0)
        one = 'X' if xState[1] else ('O' if zState[1] else 1)
        two = 'X' if xState[2] else ('O' if zState[2] else 2)
        three = 'X' if xState[3] else ('O' if zState[3] else 3)
        four = 'X' if xState[4] else ('O' if zState[4] else 4)
        five = 'X' if xState[5] else ('O' if zState[5] else 5)
        six = 'X' if xState[6] else ('O' if zState[6] else 6)
        seven = 'X' if xState[7] else ('O' if zState[7] else 7)
        eight = 'X' if xState[8] else ('O' if zState[8] else 8)
        print(f"{zero} | {one} | {two} ")
        print(f"--|---|---")
        print(f"{three} | {four} | {five} ")
        print(f"--|---|---")
        print(f"{six} | {seven} | {eight} ") 

    def checkWin(xState, zState):
        wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for win in wins:
            if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
                print("X Won the match")
                return 1
            if(sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
                print("O Won the match")
                return 0
        return -1
    
    if __name__ == "__main__":
        xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        turn = 1 # 1 for X and 0 for O
        print("Welcome to Tic Tac Toe")
        while(True):
            printBoard(xState, zState)
            if(turn == 1):
                print("X's Chance")
                value = int(input("Please enter a value: "))
                xState[value] = 1
            else:
                print("O's Chance")
                value = int(input("Please enter a value: "))
                zState[value] = 1
            cwin = checkWin(xState, zState)
            if(cwin != -1):
                print("Match over")
                break
        
            turn = 1 - turn

class TicTacToe(Game):
    def __init__(self):
        super().__init__("Tic Tac Toe")

    def play(self):
        print("Playing Tic Tac Toe...")
        Tic_Tac_Toe()

        #Word Guessing Game


    

def Word_Guessing():
    import random
    words = ['python', 'programming', 'code', 'computer', 'algorithm']
    word = random.choice(words)
    guessed_letters = []
    tries = 3

    print("Words are :")
    print("python")
    print("programming")
    print("code")
    print("computer")
    print("algorithm")

    while tries > 0:
        guessed_word = ""
        for letter in word:
            if letter in guessed_letters:
                guessed_word += letter
            else:
                guessed_word += "_"

        print(guessed_word)

        if guessed_word == word:
            print("Congratulations! You guessed the word correctly!")
            break

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif guess in word:
            guessed_letters.append(guess)
        else:
            tries -= 1
            print(f"Wrong guess! You have {tries} tries left.")

        if tries == 0:
            print(f"Game over! The word was {word}.")
            break

class Hangman(Game):
    def __init__(self):
        super().__init__("Word Guessing")

    def play(self):
        print("Playing Word Guessing...")
        Word_Guessing()
        
        

        #Rock Paper Scissor Game

def Rock_Parer_Scissor():
    import random

    def play_game():
        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            return

        print(f"Computer chose: {computer_choice}")
        print(f"You chose: {user_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'paper' and computer_choice == 'rock') or \
            (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
        else:
            print("Computer wins!")

    play_game()

class RockPaperScissors(Game):
    def __init__(self):
        super().__init__("Rock Paper Scissors")

    def play(self):
        print("Playing Rock Paper Scissors...")
        Rock_Parer_Scissor()


class App:
    def __init__(self):
        self.games = [TicTacToe(), Hangman(), RockPaperScissors()]

    def start(self):
        print("Welcome to the Game App!")
        while True:
            print("Choose a game to play:")
            for i, game in enumerate(self.games):
                print(f"{i+1}. {game.name}")
            choice = input("Enter the number of the game: ")
            if choice.isdigit() and int(choice) in range(1, len(self.games)+1):
                game = self.games[int(choice)-1]
                game.play()
                break
            else:
                print("Invalid choice. Please try again.")

app = App()
app.start()
