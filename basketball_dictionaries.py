import players

class Player:
    def __init__(self, player_info):
        self.name = player_info["name"]
        self.age = player_info["age"]
        self.position = player_info["position"]
        self.team = player_info["team"]
    
    @classmethod
    def get_team(cls, team_list):
        new_team = []
        for player in team_list:
            new_team.append(Player(player))
        return new_team


kevin_durant = Player(players.players_list[0])
jason_tatum = Player(players.players_list[1])
kyrie_irving = Player(players.players_list[2])


new_team = []
for player in players.players_list:
    new_team.append(Player(player))

the_nuggets = Player.get_team(players.players_list)

print(the_nuggets)

for player in the_nuggets:
    print(player.name)