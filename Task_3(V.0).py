class Player:
    def __init__(self, movement, team, item):
        self.__movement = movement
        self.__team = team
        self.__item = item

    @property
    def movement(self):
        return self.__movement

    @movement.setter
    def movement(self, movement):
        self.__movement = movement

    def get_team(self):
        return self.__team

    def set_team(self, team):
        self.__team = team

    def get_item(self):
        return self.__item

    def set_item(self, item):
        self.item = item


player = Player("forward", "red team", "blue team flag")
player2 = Player("on the flank", "blue team", "red team flag")

print(player.movement)
print(player.team)
print(player.item, "\n")
print(player2.movement)
print(player2.team)
print(player2.item)
