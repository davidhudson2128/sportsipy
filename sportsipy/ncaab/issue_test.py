from sportsipy.ncaab.roster import Roster, Player

# Player who hasn't played in 2021-22 season
player = Player('quinlan-bennett-1')

print(player('2021-22').points)  # Expected: 0      Actual: 144
print(player('2041-42').points)  # Expected: 0      Actual: 144


