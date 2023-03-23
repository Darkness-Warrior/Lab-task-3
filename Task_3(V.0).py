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
        self.__item = item


player = Player("forward", "red team", "blue team flag")
player2 = Player("on the flank", "blue team", "red team flag")


print(player.movement)
print(player.get_team())
print(player.get_item(), "\n")
print(player2.movement)
print(player2.get_team())
print(player2.get_item())
