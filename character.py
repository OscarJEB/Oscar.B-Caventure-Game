class Character:
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )
    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation
    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")
    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True
    def set_conversation(self, conversation):
        self.conversation = conversation
        # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True
    # Add your code here (first line unindented)
class Enemy(Character):
    enemies_to_defeat = 0
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        Enemy.enemies_to_defeat = Enemy.enemies_to_defeat + 1
    def get_weakness(self, weakness):
        return self.weakness   
    def set_weakness(self, weakness):
        self.weakness = weakness
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item )
            Enemy.enemies_to_defeat = Enemy.enemies_to_defeat - 1
            return True
        else:
            print(self.name + " swallows you, little wimp")
            return False
    def steal(self):
        print("You steal from " + self.name)
        # How will you decide what this character has to steal?
class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.feeling = None
    def pat(self):
        print(self.name + " pats you back!")

    



