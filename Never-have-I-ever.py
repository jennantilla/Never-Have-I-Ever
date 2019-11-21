print("""
    _.-._                      _.-._
  _| | | |     N E V E R      | | | |_
 | | | | |                    | | | | |
 | | | | |      H A V E       | | | | |
 | '     | _                _ |     ` |
 :       /'/       I        \`\       ;
 |        /                  \        |
  \      /      E V E R       \      /
   |    |                      |    |
   |    |                      |    |

""")
# ASCII right hand credit: https://www.asciiart.eu/people/body-parts/hand-gestures              

import random
import time

player_nevers = []

comp_nevers = ["broken a bone", "eaten escargot", "gotten a cavity", "done a backflip", "missed a flight", "been to the circus", "gone scuba diving", "gambled in a casino", "won a raffle", "seen the same movie twice in theaters", "climbed a mountain", "lost my cell phone", "been fired", "owned a cat", "failed a class"]

time.sleep(1)
print("What is your name?")
player_1 = input("> ")
player_1 = player_1.title()
player_1 = player_1.strip()
print()
print("It's great to meet you, " + player_1 + "!")
print() 
time.sleep(1)

def instructions():
    """Instructions for game play"""
    print("Would you like instructions on how to play the game? Y/N")
    how_to = input("> ")
    how_to = how_to.title()
    instructions = how_to.startswith("Y")

    if instructions == True:
        print("Each player starts with 10 points.\nTake turns sharing something you've never done before.\nIf you have done that thing, you lose a point!\nIf you haven't, your opponent loses a point!\nThe first player to reach 0 loses.")
        print()
        time.sleep(2)
    else:
        print("Let's begin")
        print()

def has_done(player):
    """Response when player has done that 'never'"""
    print(player + " has " + player_nevers[-1] + ".")

def has_never(player):
    """Response when player has not done that 'never'"""
    print(player + " has never " + player_nevers[-1] + ".")

def human_turn(player):
    """Human answer to Never Have I Ever prompt"""
    time.sleep(1)
    print()
    print(player + ", what have you never done?")
    never = input("Never Have I Ever...")

    while never in player_nevers:
        print()
        print("You've already said that! Choose another!")
        never = input("Never Have I Ever...")
    else:
        player_nevers.append(never)            
        print()

def human_response(player):
    """Human response to Never Have I Ever prompt (2 human players)"""

    print(player + ", have you ever", player_nevers[-1] + "?")

    player_response = input("> ")
    print()

    player_response = player_response.title()
    response_yes = player_response.startswith("Y")
    response_no = player_response.startswith("N")

    if response_yes == True:
        has_done(player)
        player_response = True

        return player_response

    elif response_no == True:
        has_never(player)
        player_response = False 

        return player_response

def comp_turn(player):
    """This is for the computer's random choice of a list of nevers"""
    time.sleep(1)
    print()
    rand_never = random.choice(comp_nevers)
    print("Never have I ever..." + rand_never + ".")
    player_nevers.append(rand_never)
    comp_nevers.remove(rand_never)

def comp_response(player):
    """Computer's randomized response for have/have never"""
    time.sleep(1)
    comp_answers = ["I have", "I have never"]
    choose_answer = random.choice(comp_answers)
    
    if choose_answer == "I have":
        has_done(player)
        choose_answer = True

        return choose_answer

    elif choose_answer == "I have never":
        has_never(player)
        choose_answer = False

        return choose_answer

def decrease_score(score, player):
    """Returns new score total by subtraction"""
    score -= 1 
    time.sleep(1)
    print()
    print(player, "loses a point.")
    print(player, "has", score, "points.")
    
    if score == 9:
        print("""
    _.-._             _.-._
  _| | | |           | | | |_
 | | | | |           | | | | |
 | | | | |           | | | | |
 | '     | _         |     ` |
 :       /'/        / \      ;
 |        /    9    \        |
  \      /           \      /
   |    |             |    |
   |    |             |    |
   
   """)
    
    elif score == 8:
        print("""
    _.-._             _.-._
  _| | | |           | | | |
 | | | | |           | | | | 
 | | | | |           | | | |_
 | '     | _         |     | |
 :       /'/        / \      ;
 |        /    8    \        |
  \      /           \      /
   |    |             |    |
   |    |             |    |
   
   """)

    elif score == 7:
       print("""
    _.-._             _.-.
  _| | | |           | | | 
 | | | | |           | | |  
 | | | | |           | | |_ _
 | '     | _         |   | | |
 :       /'/        / \      ;
 |        /    7    \        |
  \      /           \      /
   |    |             |    |
   |    |             |    |
   
   """)

    elif score == 6:
        print("""
    _.-._             _
  _| | | |           | |  
 | | | | |           | |   
 | | | | |           | |_ _ _
 | '     | _         | | | | |
 :       /'/        / \      ;
 |        /    6    \        |
  \      /           \      /
   |    |             |    |
   |    |             |    |
   
   """)

    elif score == 5:
        print("""
    _.-._             
  _| | | |             
 | | | | |              
 | | | | |            _ _ _ _
 | '     | _         | | | | |
 :       /'/        / \      ;
 |        /    5    \        |
  \      /           \      /
   |    |             |    |
   |    |             |    |
   
   """)

    elif score == 4:
        print("""
    _.-._             
  _| | | |             
 | | | | |              
 | | | | |            _ _ _ _
 | '     |           | | | | |
 :       / \        / \      ;
 |        /    4    \        |
  \      /           \      /
   |    |             |    |
   |    |             |    |
   
   """)

    elif score == 3:
        print("""
    _.-._             
   | | | |             
   | | | |              
  _| | | |            _ _ _ _
 | |     |           | | | | |
 :       / \        / \      ;
 |        /    3    \        |
  \      /           \      /
   |    |             |    |
   |    |             |    |
   
   """)

    elif score == 2:
        print("""
     .-._             
     | | |             
     | | |              
  _ _| | |           _ _ _ _
 | | |   |          | | | | |
 :       / \       / \      ;
 |        /    2   \        |
  \      /           \      /
   |    |             |    |
   |    |             |    |
   
   """)

    elif score == 1:
        print("""
        _             
       | |             
       | |              
  _ _ _| |            _ _ _ _
 | | | | |           | | | | |
 :       / \        / \      ;
 |        /    1    \        |
  \      /           \      /
   |    |             |    |
   |    |             |    |
   
   """)

    elif score == 0:
        print("""
                  
                   
                        
  _ _ _ _             _ _ _ _
 | | | | |           | | | | |
 :       / \        / \      ;
 |        /         \        |
  \      /  G A M E  \      /
   |    |   O V E R   |    |
   |    |             |    |
   
   """)

    return score
    time.sleep(2)

def loser(loser):
    """Ending message for loser of game"""
    time.sleep(1)
    print()
    print(loser, "loses!")
    print(loser + ": you may be the loser, but with all the things you've done, you're definitely the most interesting person in the room!")

def winner(winner):
    """Ending message for winner of game"""
    time.sleep(1)
    print()
    print(winner, "wins!")
    print(winner + ": you may have won, but don't forget to get outside and live a little! Don't let your nevers become regrets!")

def single_player_game_play():
    """This flow is for one human player and the computer"""
    player_2 = "Jarvis"
    player_1_score = 10
    player_2_score = 10
    

    print("I'll play against you!")
    print("You can call me " + player_2 + ".")
    print("Let's begin...")
    time.sleep(1)

    while player_1_score >= 1 and player_2_score >= 1:
        human_turn(player_1)

        machine_response = comp_response(player_2)
        if machine_response == False:
            player_1_score = decrease_score(player_1_score, player_1)
        elif machine_response == True:
            player_2_score = decrease_score(player_2_score, player_2)
        
        comp_turn(player_2)

        player_response = human_response(player_1)
        if player_response == False: 
            player_2_score = decrease_score(player_2_score, player_2)
        elif player_response == True: 
            player_1_score = decrease_score(player_1_score, player_1)

    if player_1_score > player_2_score: 
        loser(player_2)
        winner(player_1)
    elif player_2_score > player_1_score: 
        loser(player_1)
        winner(player_2)
        
def double_player_game_play():
    """This flow is for 2 human players"""
    player_1_score  = 10
    player_2_score = 10

    print("Let's all get acquainted.")
    print("Player 2, what is your name?")

    player_2 = input("> ")
    player_2 = player_2.title()
    player_2 = player_2.strip()
    print()
    print("Let's begin, " + player_1 + " and " + player_2 + ".")

    while player_1_score >= 1 and player_2_score >= 1:
        human_turn(player_1)

        player_response = human_response(player_2)
        if player_response == False:
            player_1_score = decrease_score(player_1_score, player_1)
        elif player_response == True: 
            player_2_score = decrease_score(player_2_score, player_2)

        human_turn(player_2)

        player_response = human_response(player_1)
        if player_response == False:
            player_2_score = decrease_score(player_2_score, player_2)
        elif player_response == True: 
            player_1_score = decrease_score(player_1_score, player_1)
    
    if player_1_score > player_2_score: 
        loser(player_2)
        winner(player_1)
    elif player_2_score > player_1_score: 
        loser(player_1)
        winner(player_2)
   
def player_flow():
    """This takes the number of players entered and chooses the correct game flow"""

    print("How many players do you have?")
    player_count = (input("> "))
    player_count = player_count.title()
    print()

    if player_count == "1" or player_count == "One":
        single_player_game_play()

    elif player_count == "2" or player_count == "Two":
        double_player_game_play()

    else:
        print("Sorry, there is a maximum of two players. Continue with two players only?")
        go_on = input("> ")
        go_on = go_on.title()
        keep_playing = go_on.startswith("Y")

        if go_on == "2" or keep_playing == True:
            print("Nice, let's begin.")
            print()
            double_player_game_play()
        else:
            print("Goodbye!")

instructions()

player_flow()
