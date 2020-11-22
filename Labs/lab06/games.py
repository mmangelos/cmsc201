# File:        games.py
# Author:      Mitchell Angelos
# Date:        3/4/19
# Section:     12
# E-mail:      a242@umbc.edu
# Description: This program simulates a voting system for some games, then
#              prints the total votes.

VOTE_SENTINEL_VALUE = 0

def main():

    #list of games to vote on
    games = ["Twister", "Dodgeball", "Capture the Flag", "Hide and Seek",
             "Croquet", "Ring Toss", "Ping Pong"]

    gameCount = 1
    #prints the games available
    while gameCount < 8:
        print(str(gameCount) + " - " + games[gameCount - 1])
        gameCount += 1

    votes = [0, 0, 0, 0, 0, 0, 0]
    gameVote = int(input("What is your favorite game? ('0' to stop): "))
    #gets the votes from the user and stops when the user enters 0.
    while gameVote != VOTE_SENTINEL_VALUE:
        votes[gameVote - 1] += 1
        gameVote = int(input("What is your favorite game? ('0' to stop): "))

    #used for testing the list of votes
    #print("votes:", votes)

    printCount = 0
    #prints out the games and their corresponding votes.
    while printCount < 7:
        print(games[printCount] + " has " + str(votes[printCount]) + " votes")
        printCount += 1

main()
