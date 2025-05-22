from cave import Cave

# Creating Cave objects
cavern = Cave("Cavern")
grotto = Cave("Grotto")
dungeon = Cave("Dungeon")

# Setting a description for the cavern
cavern.set_description("A damp and dirty cave.")

# Printing the description
print(cavern.get_description())  # This will print the description

