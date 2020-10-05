# state machine
import sys
from random import randrange

from clock import Clock
from key import Key
###############################################################################
######################  title  ################################################
###############################################################################
def title_screen_selections():
    option = input(">")  #  > 
    if option.lower().strip() == "play":
        start_game()  # go to the game function
    elif option.lower().strip() == "help":
        help_menu()
    elif option.lower().strip() == "quit":
        sys.exit()
    else:
        print("Please enter a valid command")
        title_screen_selections()  # recursion

def title_screen():
    print("                                   ████████                                  ")
    print("                              ██████        ██████                            ")
    print("                          ▓▓▓▓░░░░░░░░░░░░░░░░░░░░▓▓██                        ")
    print("                        ██  ░░░░░░░░▒▒▒▒▒▒▒▒░░░░░░    ██                      ")
    print("                      ██░░░░░░░░▒▒▒▒████████▒▒▒▒░░░░░░░░██                    ")
    print("                    ██  ░░░░▒▒▒▒████        ████▒▒▒▒░░░░  ██                  ")
    print("                  ▓▓░░░░░░▒▒████                ████▒▒░░░░░░▓▓                ")
    print("                  ██░░░░▒▒██                        ██▒▒░░░░██                ")
    print("                ██░░░░▒▒██                            ██▒▒░░░░██              ")
    print("                ██░░▒▒██                                ██▒▒░░██              ")
    print("              ▒▒░░░░▒▒██                                ██▒▒░░░░▒▒            ")
    print("              ██░░░░▒▒██                                ██▒▒░░░░██            ")
    print("            ██  ░░▒▒██                                    ██▒▒░░  ██          ")
    print("            ██░░░░▒▒██                                    ██▒▒░░░░██          ")
    print("            ██░░░░▒▒██                                    ██▒▒░░░░██          ")
    print("            ██░░░░▒▒██                                    ██▒▒░░░░██          ")
    print("            ██░░░░▒▒██                                    ██▒▒░░░░██          ")
    print("            ██░░░░▒▒██                                    ██▒▒░░░░██          ")
    print("            ██░░░░▒▒██                                    ██▒▒░░░░██          ")
    print("            ██░░░░▒▒██                                    ██▒▒░░░░██          ")
    print("            ██░░░░▒▒██                                    ██▒▒░░░░██          ")
    print("            ██░░░░▒▒██                                    ██▒▒░░░░██          ")
    print("      ▒▒▒▒▒▒██░░░░▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒░░░░██▒▒▒▒▒▒    ")
    print("    ██░░░░░░██▒▒▒▒▒▒██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▒▒▒▒▒▒██░░░░░░██  ")
    print("  ██░░░░░░░░░░██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████░░░░░░░░░░██")
    print("  ██░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░██")
    print("  ██░░░░░░████████████████████████████████████████████████████████████░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
    print("  ██░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░██")
    print("  ██░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░██")
    print("  ██░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░██")
    print("  ██▒▒░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░▒▒██")
    print("  ██▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒██")
    print("  ██▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒██")
    print("  ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██")
    print("    ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██  ")
    print("      ████████████████████████████████████████████████████████████████████ ")
    print(" _             _              _       _                ")
    print("| |           | |            (_)     | |               ")
    print("| | ___   ____| |  _    ____  _  ____| |  _ ____  ____ ")
    print("| |/ _ \ / ___) | / )  |  _ \| |/ ___) | / ) _  )/ ___)")
    print("| | |_| ( (___| |< (   | | | | ( (___| |< ( (/ /| |    ")
    print("|_|\___/ \____)_| \_)  | ||_/|_|\____)_| \_)____)_|    ")
    print("                       |_| ")
    print("----------------------------------------")
    print("------ welcome to the lock picker ------")
    print("----------------------------------------")
    print("                - play -                ")
    print("                - help -                ")
    print("                - quit -                ")

def help_menu():
    print("----------------------------------------")
    print("-------------- help  menu --------------")
    print("----------------------------------------")
    print("input your command after '>'            ")
    print("There will be a random 5 * 5 lock for   ")
    print("us to pick.                             ")
    print("                                        ")
    print("For example:                            ")
    print(" A B C D E                              ")
    print(" # - # # #                              ")
    print(" # - - # #                              ")
    print(" # - - # -                              ")
    print(" - - - # -                              ")
    print(" - - - - -                              ")
    print("                                        ")
    print(" YOU NEED TO INPUT A COMPLEMENT         ")
    print(" SET OF NUMBERS WITHIN 0 AND 5          ")
    print(" TO PICK THE LOCK                       ")
    print("                                        ")
    print(" In this case, the correct key is:      ")
    print(" 2 5 4 1 3                              ")
    print("                                        ")
    print(" These numbers will generate the key:   ")
    print(" - # - - -                              ")
    print(" - # # - -                              ")
    print(" - # # - #                              ")
    print(" # # # - #                              ")
    print(" # # # # #                              ")
    print(" A B C D E                              ")
    print("                                        ")
    print(" IMPORTANT ! ! !                        ")
    print(" THERE ARE SPACES IN BETWEEN NUMBERS !  ")
    print(" SPACES ! LIKE THIS ' ' <--             ")
    print("                                        ")
    print(" BAD THINGS WILL HAPPEN                 ")
    print(" IF YOU DONT FOLLOW                     ")
    print(" DON'T SAY I NEVER WARN YOU ! ! !       ")
    print("                                        ")
    print(" ONLY CORRECT KEY WILL UNLOCK YOU FROM  ")
    print(" THIS ETERNITY ! ! !                    ")
    print("                                        ")
    print(" key 'play' to start playing            ")
    print("                                        ")
    print(" key 'quit' to quit like a loser        ")
    print("                                        ")
    print(" key 'help' to read this again. You know")
    print(" sometimes people do weird stuff.       ")
    title_screen_selections()

###############################################################################
######################  game functions ########## array equals to list ########
###############################################################################
def start_game():
    game_state = "idle"

    temp_lock_array = generate_random_lock_array()
    clock = Clock(temp_lock_array)
    clock.print_lock()
    lock_array = temp_lock_array

    user_input = input(">")
    user_input_array = list(map(int, user_input.replace(" ", "")))

    # print(lock_array)
    # print(user_input_array)

    game_state = check_key(lock_array, user_input_array)

    # while game_state != "finish":

    while game_state == "wrong key":
        clock.print_lock()
        user_input = input(">")
        user_input_array = list(map(int, user_input.replace(" ", "")))  # get user input and save as a list
        game_state = check_key(lock_array, user_input_array)

    while game_state == "idle":
        temp_lock_array = generate_random_lock_array()  # list
        clock = Clock(temp_lock_array)
        lock_array = temp_lock_array
        clock.print_lock()
        user_input = input(">")  # string(str)   --> "    3   3  3 3 3" ####
        ####### list of int, list of str
        user_input_array = list(map(int, user_input.replace(" ", "")))  # convert the string to the, NOTE --> LIST --> [3, 3, 3, 3, 3] (int)
        game_state = check_key(lock_array, user_input_array)  # ANCHOR str?/int?    [ "3" !== 3  ]  [ "3" === "3"  ] [  3 === 3  ]

    # end message
    print("thanks for playing")

# (lock-array, user_input_array)  ==>  function check-key()  ==> return game-state (str)
def check_key(lock_array, user_input_array):
    game_state = "idle"
    if len(user_input_array) == 5:
        key = Key(user_input_array)  # small-case -key- is the actual -Key- object  

        ##    Person class --> -wutong- is the actual -Person- object 

        # class Person
        #     def __init__(self, characteristic, name):
        #         self.characteristic = characteristic
        #         self.name = name
        # 
        # wutong = Person("胖子", "wutong")     attribute
        # xiaoming = Person("瘦子", "xiaoming")     attribute
        # print(wutong.characteristic) 
        # print(wutong.name)


        # key.get_key()
        key.print_key()
        # declare state as checking
        state = "checking"
        for i in range(5):
            if user_input_array[i] + lock_array[i] != 5 and state == "checking" and i != 4:  # not equal 
                # print(user_input_array)
                # print(lock_array)
                print("wrong key! try again")
                game_state = "wrong key"
                break
            elif user_input_array[i] + lock_array[i] == 5 and state == "checking" and i != 4:  # equal ( * * * * X)
                state = "checking"
            elif i == 4 and state == "checking" and user_input_array[i] + lock_array[i] == 5:
                state = "finish"
                break
            else:
                game_state = "crash"
        if state == "finish":
            print("great you picked the lock")
            if input("key 'y' to play again, else quit game >") == "y":
                game_state = "idle"
            else:
                game_state = "finish game"

        else:
            game_state = "wrong key"
    else:
        state == "illegal key"
        print("Illegal key input")
    return game_state

def generate_random_lock_array():
    lock_array = [0, 0, 0, 0, 0]
    for i in range(5):
        lock_array[i] = randrange(5)
    return lock_array

title_screen()
title_screen_selections()
