from game_logic import Game

def title_screen():
    print('''
    ┏━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┓
    ┗━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┛           
    []                 _____                                                     []
    []                 \   /                                                     []
    []                 |   |                                                     []
    []    .__.         |   |_____________________________________________        []
    []    |  |_________|   |        Natural Savagery                      \      []
    []    |  |         |   |________________________________________________\    []
    []    |  |_________|   |            >START<                             /    []
    []    |__|         |   |_____________________________________________ /      []
    []                 |   |                                                     []
    []                 |   |                                                     []
    []                 /___\                                                     []
    ┏━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┓
    ┗━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┛ 
    ''')
    while True:
        answer = input("Type START to begin: ").strip().upper()
        if answer == "START":
            return
        else:
            print("Invalid input. Please type START to begin.")

def play_again():
    while True:
        answer = input("Do you want to play again? (Yes or No): ").strip().lower()
        if answer == "yes":
            main()
            break
        elif answer == "no":
            print("Thank you for playing!")
            break
        else:
            print("Please type 'Yes' or 'No'.")

def main():
    title_screen()
    game = Game()
    game.start()
    play_again()

if __name__ == "__main__":
    main()
