#!/usr/bin/env python

# def start():
#     print(get_number())
#
# def get_number():
#     number = 12
#     return number

''' -- using raw input -- '''
# def start():
#     print(get_name())
#
# def get_name():
#     name = raw_input("What is your name? ") # Python3: input()
#     return name

''' -- formatting using wildcards >> {} -- '''

# def start():
#     print("Hello {}!".format(get_name()))
#
# def get_name():
#     name = raw_input("What is your name? ") # Python3: input()
#     return name

# ''' -- using wildcards -- '''
# def start():
#     f_name = "Sarah"
#     l_name = "Connor"
#     age = 28
#     gender = "Female"
#     get_info(f_name, l_name, age, gender)
#
# def get_info(f_name, l_name, age, gender):
#     print("My name is {} {}. I am a {} year old {}.".format(f_name, l_name, age, gender))


def start(nice=0,mean=0,name=""):
    # get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
    '''
    check if new game or not, if new game get user's name
    if not new game, thank player and continue with game
    '''
    if name != "": # if we do not have user's name, then they are a new player and need to submit name
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = raw_input("\nWhat is your name? ").capitalize()
                if name !="":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted by several different people. \nYou can be nice or mean.")
                    print("At the end of the game your fate will be influenced from your actions.")
                    stop = False
    return name

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = raw_input("\nA stranger approaches you for a conversation.\nWill you be nice or mean? n/m: ").lower()
        if pick == "n":
            print("They smile, wave, and walk away...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you menacingly and aburptly storms off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) # pass the 3 variables to the score()

def show_score(nice,mean,name):
    print("\n{}, you currently have ({}, Nice and {}, Mean) points.".format(name,nice,mean))

def score(nice,mean,name):
    # score function is being passed the values stored within the 3 variables
    if nice > 5:
        # if condition is valid, call win function passing in the variables so it can use them
        win(nice,mean,name)
    if mean > 5:
        # if condition is valid, call lose function passing in the variables so it can use them
        lose(nice,mean,name)
    else:
        # if condition is valid, call win function passing in the variables so it can use them
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    print("\nNice job {}, you win!\nEveryone loves you and you now live in a palace!".format(name)) # substitute the {} wildcards with our variables
    again(nice,mean,name) # call again function and pass in our variables

def lose(nice,mean,name):
    print("\nToo bad, game over! \n{}, you live in a van by the river, wretched and alone!".format(name)) # substitute the {} wildcards with our variables
    again(nice,mean,name) # call again function and pass in our variables

def again(nice,mean,name):
    stop = True
    while stop:
        choice = raw_input("\nDo you want to play again? y/n: ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nSee you later, alligator!")
            stop = False
            exit()
        else:
            print("\nPlease enter 'y for 'Yes, 'n' for 'No'")

def reset(nice,mean,name):
    nice = 0
    mean = 0
    #  No reset for 'name' variable because the same user is deciding to play again
    start(nice,mean,name)

if __name__ == "__main__":
    start()
