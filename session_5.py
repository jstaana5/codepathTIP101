# problem 1
'''class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False
        
        
my_Pokemon= Pokemon("Pikachu", ["Electric"])
print(my_Pokemon.name)
print(my_Pokemon.types)
'''

'''class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,   # Output: "name": "Squirtle",
            "types": self.types, # Output: "types": ["Water"],
            "is_caught": self.is_caught # Output: "is_caught": False
        })
        
squirtle = Pokemon("Squirtle", ["Water"], True)
# Pokemon.print_pokemon(squirtle)

squirtle.print_pokemon()'''


# problem 3

'''class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,   # Output: "name": "Squirtle",
            "types": self.types, # Output: "types": ["Water"],
            "is_caught": self.is_caught # Output: "is_caught": False
        })
        
squirtle = Pokemon("Squirtle", ["Water"])
squirtle.is_caught = True
print(squirtle.is_caught)'''

# problem 4
'''class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,   # Output: "name": "Squirtle",
            "types": self.types, # Output: "types": ["Water"],
            "is_caught": self.is_caught # Output: "is_caught": False
        })
    def catch(self):
            self.is_caught = True
        


my_pokemon = Pokemon("rattata", ["Normal"])
my_pokemon.print_pokemon()

my_pokemon.catch()
my_pokemon.print_pokemon()'''

# problem 5

class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,   # Output: "name": "Squirtle",
            "types": self.types, # Output: "types": ["Water"],
            "is_caught": self.is_caught # Output: "is_caught": False
        })
    def catch(self):
        self.is_caught = True
            
    def choose(self):
        if self.is_caught == True:
            print(self.name + " I choose you!")
        else:
            print(self.name + " is Wild. Catch them if you can!")
        


my_pokemon = Pokemon("Rattata", ["Normal"])
my_pokemon.print_pokemon()

my_pokemon.choose()
my_pokemon.catch()
my_pokemon.choose()