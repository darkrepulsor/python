import os
import time
from Game.GameHelper import helper


class TicTacToe:
    def Main():
        print("Let's play Tic Tac Toe!!!\n")
        Player1 = input("Player 1 name: ")
        Player2 = input("Player 2 name: ")
        time.sleep(2)
        spots = {1: '1', 2: '2', 3: '3', 4: '4',
                 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
        Playing = True
        Complete = False
        Turn = 0
        Prev_turn = -1
        # Game Loop
        while Playing:
            # reset the screen
            os.system('cls') or None
            # Draw the board
            helper.draw_board(spots)
            # If invalid turn ocurred, let the player know
            if Prev_turn == Turn:
                print("Invalid spot selected, please pick another.")
            Prev_turn = Turn
            if ((Turn % 2) + 1) == 1:
                print("\n"+Player1 + "'s turn: Pick your spot or press q to quit")
            else:
                print("\n"+Player2 + "'s turn: Pick your spot or press q to quit")
            # Get input from player
            choice = input()
            if choice == 'q':
                Playing = False
            # Check if the player gave a number from 1-9
            elif str.isdigit(choice) and int(choice) in spots:
                # Check if the spot has already been taken
                if not spots[int(choice)] in {"X", "O"}:
                    # Valid input, update the board
                    Turn += 1
                    spots[int(choice)] = helper.check_turn(Turn)
            # Check if the game has ended (and if someone won)
            if helper.check_for_win(spots):
                Playing, Complete = False, True
            if Turn > 8:
                Playing = False
        # Out of the loop, print the results
        # Draw the board one last time.
        os.system('cls') or None
        helper.draw_board(spots)
        # If there's a winner, say who won
        if Complete:
            if helper.check_turn(Turn) == 'X':
                print(Player1+" Wins!")
            else:
                print(Player2 + " Wins!")
        else:
            # Tie game
            print("No Winner!")

        again = int(
            input("\n\nWant to play again? \n\t 1 - Yes \n\t 2 - No\n\n"))
        if again == 1:
            TicTacToe.Main()
        else:
            os.system('cls') or None
            print("\nThanks for playing\n")
