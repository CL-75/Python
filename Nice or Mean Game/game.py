#
#  Python: 3.8.5
#
#  Author: Casey Levy
#
#  Purpose: Nice or Mean Game
#
#
#
#
#
#

def start(nice=0,mean=0,name=""):
    # get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)




def describe_game(name):
    """
        Check if this is a new game or not.
        If it is new, get the user's name.
        If not, thank the player for playing
        again and continue with the game.
    """

    if name != "":
        print("\nThank you for playing again {}!".format(name))
    else:
        stop= True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome {}!".format(name))
                    print("\nIn this game, you will be greeted by \nseveral different people. \nYou can choose to be nice or mean.")
                    print("But at the end of the game, your fate \nwill be sealed by your acions.")
                    stop = False
    return name




def nice_mean(nice, mean, name):
    stop = True
    while stop:
        show_score(nice, mean, name)
        pick = input("\nA stranger approaches you for a conversation. \nWill you be nice or mean? \n(N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you menacingly and storms off...")
            mean = (mean + 1)
            stop = False
    score(nice, mean, name)




def show_score(nice, mean, name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name, nice, mean))




def score(nice, mean, name):
    #score function is being passed the values stored within the 3 variables
    if nice > 2:
        win(nice, mean, name)
    if mean > 2:
        lose(nice, mean, name)
    else:
        nice_mean(nice, mean, name)





def win(nice, mean, name):
    print("\nNice job {}! You win! \nEveryone loves you and you've made \nlots of friends along the way.".format(name))
    again(nice, mean, name)






def lose(nice, mean, name):
    print("\nAhh too bad, game over! \n{}, you live in a dirty beat-up van by the river, wretched and alone.".format(name))
    again(nice, mean, name)



    

def again(nice, mean, name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (Y/N): \n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice, mean, name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter (Y) for 'YES' or (N) for 'NO':\n>>> ")


def reset(nice, mean, name):
    # We must reset the score values
    nice = 0
    mean = 0
    start(nice, mean, name)


if __name__ == "__main__":
    start()








    
