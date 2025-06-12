from cave import Cave
from character import Enemy, Friend
from character import Character
from item import Item

# Creating Cave objects
cavern = Cave("Cavern")
cavern.set_description("A dank and dirty cave ")
main_dungeon = Cave("Main Dungeon")
main_dungeon.set_description("A large cave with a rack")
grotto = Cave("Grotto")
grotto.set_description("A small cave with ancient graffiti")
#Creating more cave objects (from sketch)
cave_entrance = Cave("Cave Entrance")
cave_entrance.set_description("You start here. You're mind is set on hunting the wumpus. It fills you with determination.")
dead_end = Cave("Dead end")
dead_end.set_description("A blank cave wall with no way ahead")
cold_grotto = Cave("Cold Grotto")
cold_grotto.set_description("A small, cold cave with cold ancient graffiti")
open_cavern = Cave("Open Cavern")
open_cavern.set_description("ph")
tunnel = Cave("Tunnel")
tunnel.set_description("A straight cave to squeeze through")
claustrophobic_tunnel = Cave("Claustrophobic Tunnel")
claustrophobic_tunnel.set_description("An even skinnier tunnel that you have to wiggle through")
speleothem_cave = Cave("Speleothem Cave")
speleothem_cave.set_description("A cave with stalactites that hang from the ceiling dripping down water, and stalagmites that spike up from the floor")
cavity = Cave("Cavity")
cavity.set_description("An open part of the cave with a ledge.")
small_grotto = Cave("Small Grotto")
small_grotto.set_description("A smaller cave with small ancient graffiti")
wet_grotto = Cave("Wet Grotto")
wet_grotto.set_description("A small, wet cave with wet ancient graffiti")
deadly_dungeon= Cave("Deadly Dungeon")
deadly_dungeon.set_description("A cave with a plastic human skeleton on the ground. You feel as though his name was Peter.")
deep_cavern  = Cave("Deep Cavern")
deep_cavern.set_description("A large cave with a massive hole that goes as deep as you can see. The only way across is a rickety wooden bridge, stained with wumpus blood")
lair = Cave("The Wumpus' lair!")
lair.set_description("You found him! Now KILL HIM!!! FOR GLORY!!!")
#directions start
cave_entrance.link_cave(open_cavern, "north")
#bottom line
dead_end.link_cave(cold_grotto, "east")
cold_grotto.link_cave(dead_end, "west")
cold_grotto.link_cave(cavern, "north")
cold_grotto.link_cave(open_cavern, "east")
open_cavern.link_cave(cold_grotto, "west")
open_cavern.link_cave(cavity, "north")
open_cavern.link_cave(grotto, "east")
open_cavern.link_cave(cave_entrance, "south")
grotto.link_cave(open_cavern, "west")
grotto.link_cave(tunnel, "east")
tunnel.link_cave(grotto, "west")
tunnel.link_cave(claustrophobic_tunnel, "north")
#middle line
small_grotto.link_cave(wet_grotto, "north")
small_grotto.link_cave(cavern, "east")
cavern.link_cave(cold_grotto, "south")
cavern.link_cave(small_grotto, "west")
cavern.link_cave(deadly_dungeon, "north")
cavern.link_cave(cavity, "east")
cavern.link_cave(cold_grotto, "south")
cavity.link_cave(cavern, "west")
cavity.link_cave(open_cavern, "south")
speleothem_cave.link_cave(main_dungeon, "north")
speleothem_cave.link_cave(claustrophobic_tunnel, "east")
claustrophobic_tunnel.link_cave(speleothem_cave, "west")
claustrophobic_tunnel.link_cave(tunnel, "south")
#top line
wet_grotto.link_cave(deadly_dungeon, "east")
wet_grotto.link_cave(cavern, "south")
deadly_dungeon.link_cave(wet_grotto, "west")
deadly_dungeon.link_cave(deep_cavern, "east")
deadly_dungeon.link_cave(cavern, "south")
deep_cavern.link_cave(deadly_dungeon, "west")
deep_cavern.link_cave(main_dungeon, "east")
main_dungeon.link_cave(deep_cavern, "west")
main_dungeon.link_cave(lair, "east")
main_dungeon.link_cave(speleothem_cave, "south")
lair.link_cave(main_dungeon, "west")
#characters
forrestWump = Enemy("Forrest Wump", "A smelly Wumpus that looks an awful lot like Tom Hanks")
forrestWump.set_conversation("I'm wumping it")
forrestWump.set_weakness("box of chocolates")
lair.set_character(forrestWump)
josie = Friend("Josie", "A stinky bat")
josie.set_conversation("I LOVE SKZ!!!")
grotto.set_character(josie)
creeper = Enemy("A creeper", "(from Minecraft)")
creeper.set_conversation("SSSSssssssss")
creeper.set_weakness("shield")
deadly_dungeon.set_character(creeper)
ralsei = Friend("Ralsei", "The friendly prince of Darkworld")
ralsei.set_conversation("Hey! Have you seen Susie and Kris anywhere? I'm kind of lost...")
cavern.set_character(ralsei)
krisAndSusie = Friend("Kris and Susie", "A human and an angry purple monster girl")
krisAndSusie.set_conversation("Susie says:'Hey, while we wait for Ralsei to catch up lets ax this fool!\n Krisno warns you about her attacks and you get away.")
deep_cavern.set_character(krisAndSusie)
#items
boxOfChocolates = Item("box of chocolates")
boxOfChocolates.set_description("Life's like this.")
dead_end.set_item(boxOfChocolates)
torch = Item("torch")
torch.set_description("The torch is bright, lighting up the tight cave. It's light fills you with determination")
claustrophobic_tunnel.set_item(torch)
shield = Item("shield")
shield.set_description("A rectangular shield, probably strong enough to withstand an explosion")
cavity.set_item(shield)
bag = []



current_cave = cave_entrance
dead = False
while dead == False:	      
    print("\n")
    current_cave.get_details()    
    inhabitant = current_cave.get_character()
    item = current_cave.get_item()
    if item is not None:
        item.describe()
    if inhabitant is not None:
        inhabitant.describe()
    command = input("> ")
    if command in ["north", "south", "east", "west"]:
        current_cave = current_cave. move (command)  

    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("What will you fight with?")
            fight_with = input()
            if fight_with in bag:
                if inhabitant.fight(fight_with) == True:
                    if Enemy.enemies_to_defeat == 0:
                        print("Congratulations, you have survived another adventure!")
                        dead = True
                    else:
                        print("Bravo, hero you won the fight!")
                        current_cave.set_character(None)
                else:
                    print("Scurry home, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")
    elif command == "pat":
            if inhabitant is not None:
                if isinstance(inhabitant, Enemy):
                    print("I wouldn't do that if I were you…")
                else:
                    inhabitant.pat()
            else:
                print("There is no one here to pat :(")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your bag")
            bag.append(item.get_name())
            current_cave.set_item(None)
