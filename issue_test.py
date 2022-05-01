from sportsipy.ncaab.roster import Roster
import pandas as pd

y = []
unc = Roster('Auburn')
for player in unc.players:
    print(player)
    if player('2020-21').minutes_played > -10:
        y.append([player.player_id, player.name, player('2020-21').points, player('2020-21').total_rebounds, player('2020-21').assists, player('2020-21').minutes_played])
        #
        # x = pd.DataFrame(y, columns=['id', 'name', 'pts', 'reb', 'ast'])
        #
        # print(player.player_id)
        # print(x)


x = pd.DataFrame(y, columns=['id', 'name', 'pts', 'reb', 'ast', 'mins_played'])

print(f"\n\n\n\n\n\n\n\n")
print(x)


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
