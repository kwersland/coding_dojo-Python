class Player:
    def __init__(self, data):
        self.name = data["name"]
        self.age = data["age"]
        self.position = data["position"]
        self.team = data["team"]
    
    # @classmethod
    # def add_players(cls, data):
    #     player_objects = []
    #     for dict in data:
    #         player_objects.append(cls(dict))
    #     return player_objects

    # def __repr__(self):
    #     display = f"Player: {self.name}, {self.age} y/o, pos: {self.position}, team: {self.team}"
    #     return display

kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age":32,
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
}
    

player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

print(player_jason.name, player_kevin.name, player_kyrie.name)

players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
    "age":32,
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33,
    "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32,
    "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    },
    {
    "name": "DeMar DeRozan",
    "age": 32,
    "position": "Shooting Guard",
    "team": "Chicago Bulls"
    }
]

new_team = []
for x in players:
    players[x] = Player(players[x])
    new_team.append(players[x].name)

print(new_team)


