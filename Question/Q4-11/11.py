"""
Ask number of games played in a tournment. Ask the user number of games won and number of game loss.Caluculate of the tie and total points.(1 win= 4point, 1 tie = 2points)

"""
games_played=int(input("Enter games played = "))
games_won=int(input("Enter games won = "))
games_lost=int(input("Enter games lost = "))

games_tie=games_played-games_won-games_lost
print(f"Games tied = {games_tie}")

total_points=(games_won*4)+(games_tie*2)
print(total_points)