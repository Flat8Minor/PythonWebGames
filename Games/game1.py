winning_guess = 0
no_guess = 0
winning_1 =  False

def start():
        import random
        global winning_guess
        winning_guess = random.randint(1,10)
        return

def game():
        global no_guess
        correct_input = False
        if no_guess == 3:
                game_over()
        else:
                while correct_input == False:
                        guess = int(input('What is your guess?'))
                        spacing()
                        if (guess >= 1) and (guess <= 10):
                                check_no(guess)
                        else:
                                print('Please between 1 and 10')
                                spacing()

def check_no(user_guess):
        global winning_no
        if user_guess == winning_no:
                win()
        elif user_guess < winning_no:
                return 'higher'
        else:
                return 'lower'
        return

def comment(feedback):
        global no_guess
        if feedback == [True, False]:
                print("Go higher")
        else:
                print("Go Lower")
        spacing()
        no_guess = no_guess + 1
        print("You have "+str(3-no_guess)+" guesses left.")
        spacing()
        return

def win():
        global winning_no
        print("You have won the number was "+str(winning_no))
        spacing()
        exit()

def game_over():
        print("You have lost better luck next time.")
        spacing()
        exit()

def main():
        start()
        intro()
        game()
