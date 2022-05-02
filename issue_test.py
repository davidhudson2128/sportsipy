from sportsipy.ncaab.roster import Roster, Player
from sportsipy.ncaab.player import AbstractPlayer
from sportsipy.ncaab.teams import Teams
import pandas as pd

# y = []
# unc = Roster('Michigan')
# for player in unc.players:
#     print(player('2021-22').minutes_played)
#     if player('2021-22').minutes_played > 0:
#         y.append([player.player_id, player.name, player('2021-22').points, player('2021-22').total_rebounds,
#                   player('2021-22').assists, player('2021-22').minutes_played])
#
#
#     print(player('2021-22').minutes_played)
#
#
# x = pd.DataFrame(y, columns=['id', 'name', 'pts', 'reb', 'ast', 'mins_played'])
#
# print(f"\n\n")
# print(x)

#######

# y = []
# unc = Roster('Gonzaga')
# for player in unc.players:
#     # print(player('2021-22').minutes_played)
#     # print(player('2021-22').points)
#     print(player.player_id)
#     print(f"Player data: {player._player_data}")
#     if player.player_id == "colby-brooks-1":
#         pass
#         # print(player('2021-22').points)
#         # y.append([player.player_id, player.name, player('2021-22').points, player('2021-22').total_rebounds,
#         #           player('2021-22').assists, player('2021-22').minutes_played])

#
# player = Player("colby-brooks-1")
#
# print(f"HERE {player._player_data}")
#     # print(player('2021-22').minutes_played)

# roster = Roster('Gonzaga')


# player = Player("chet-holmgren-1")
# print(player.points)

all_teams = []
teams = Teams()
for team in teams._teams:
    all_teams.append(team._abbreviation)

for i in range(len(all_teams)):
    if i % 40 == 0:
        roster = Roster(all_teams[i])
        for player in roster.players:
            print(f"\t{player.player_id}")
            print(f"\t{player.points}")

# roster = Roster("Abilene Christian")
# for player in roster:
#     print(player.player_id)


# assert player.points == 0
# assert player.minutes_played == 0

######
# print("\n\n")
# dummy = Player("dumbdumb", "dummy", {})
# # dummy._index = None

# print(dummy.points)




# Code listed on issue page on GitHub:
# y = []
# unc = Roster('North-Carolina')
# for player in unc.players:
#     if player('2020-21').minutes_played > 0:
#         y.append([player.player_id, player.name, player('2020-21').points,player('2020-21').total_rebounds,
#         player('2020-21').assists])
#
# x = pd.DataFrame(y, columns =['id', 'name', 'pts', 'reb', 'ast'])
# print(x)
