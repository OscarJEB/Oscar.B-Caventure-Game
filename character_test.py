from character import Character
from character import Enemy
forrestWump = Enemy("Forrest Wump", "A smelly Wumpus")

forrestWump.describe()
forrestWump.set_conversation ("Come closer.I can’t see you!")
forrestWump.talk()
forrestWump.set_weakness("vegemite")
print("What will you fight with?")
fight_with = input()
forrestWump.fight(fight_with)
