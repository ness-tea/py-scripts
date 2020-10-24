import requests
from bs4 import BeautifulSoup
import sys


url = 'https://www.atptour.com/en/rankings/singles'
html = BeautifulSoup((requests.get(url)).text, features='html.parser')

player_cells = html.find_all(class_="player-cell")

print("------------- ATP Rank Standings -------------" + '\n')
print("Hi Vanessa! What would you like to do? :)" + '\n')
print("(1) LIST all ATP rankings as of current.")
print("(2) Query for the rank of a PLAYER")
print("(3) Query for the player of a RANK")
print("(4) EXIT.... :( ")
    

while(True):
    response = str(input('\n' + "What would you like to do? (L/P/R/E): "))
    
    if response == "1" or response[0] == 'l' or response[0] == 'L':
        mapping = "----------"

        print('\n' + "Here's a list of the current ATP rankings:" + '\n')
        for i in range(len(player_cells)):
            player = player_cells[i].a['data-ga-label']

            if (i+1) > 9 and (len(mapping) == 10):
                mapping = mapping[1:len(mapping)]

            if (i+1) > 99 and (len(mapping) == 9):
                mapping = mapping[1:len(mapping)]
                
            print("Rank " + str(i+1) + " " + mapping + " " + str(player))

    elif response == "2" or response[0] == 'p' or response[0] == 'P':
        print("")
        player = str(input("Which player would you like to query?: "))

        player_exists = False
        
        for i in range(len(player_cells)):
            if player.capitalize() in player_cells[i].a['data-ga-label'].split():
                print(str(player_cells[i].a['data-ga-label']) + "'s current ranking is:     " + str(i+1))
                player_exists = True

        if not(player_exists):
            print("Sorry, that player is either not in the top 100, does not exist.... or has retired :( ")

    elif response == "3" or response[0] == 'r' or response[0] == 'R':
        print("")
        rank = int(input("What rank would you like to query? (e.g. 3): "))

        if rank > 100 or rank < 1:
            print("Sorry, we can only track the top 1-100 ATP players. You are unfortunately out of range :( Perhaps try google?")
        else:
            player = player_cells[rank-1].a['data-ga-label']
            print("The currently player with this rank is:     " + str(player))
        
    elif response == "4" or response[0] == 'e' or response[0] == 'E':
        print("Thanks for stopping by! Happy Tennis-ing :) ")
        sys.exit()

    else:
        print("Doesn't sound like a valid option... abort abort.")

    end = str(input('\n' + "Would you like to continue? (Y/N) : "))
    if end[0] == 'Y' or end[0] == 'y':
        continue
    elif end[0] == 'N' or end[0] == 'n':
        print("Thanks for stopping by! Happy Tennis-ing :) ")
        break
        

    
        
        
