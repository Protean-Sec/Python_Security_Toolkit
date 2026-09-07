import random
import array
magic_Elements = ["FIRE", "ICE", "LIGHTNING"]
class_list =  ["MAGE", "WARRIOR", "ROGUE"] 

print("Hello adventurer! Ready to start your journey in this dungeon? ")
hero_Name = input("What is your name, hero? ")

def choose_element (element_list):
    while True:
        print(f"A pleasure to meet you {hero_Name}!")
        choice_1 = input("You have 3 magical affinities to choose from! \nFIRE \nICE  \nor LIGHTNING \n")
        choice_1 = choice_1.upper()
        if choice_1 in element_list:
            print(f"Ah! You chose {choice_1} as your magical affinity! An excellent choice! ")
            return choice_1
        
        print("\nInvalid choice! Please look at the options and try again.\n")  

def element_info (chosen_element):
    descriptions = {"FIRE": 
                    "Fire has high offensive power! \nIt applies tick dmg over time! \nHowever it has a high mana cost and very little defensive capabilities\n",
            "ICE": "Ice has excellent defensive capability! \nSlows down enemies over time! \nHighly defensive, not very effective by itself!\n",
            "LIGHTNING": "Lightning has high speed and high chance for critical hits! \nApplies shock to enemies and can chain to multiple targets! \nVery fast but its not the best at defense or offense!\n"
            }
        
    print(descriptions[chosen_element])
       
def choosing_class (class_types):
    
    classes = {
       "MAGE": "A mage starts with 300 mana/magic, 75 HP and 0 defense. \nIts a glass cannon, powerful but very fragile!\nMelee dmg affects mages more!",
       "WARRIOR": "A warrior starts with 110 mana/magic, 175 HP and 5 defense.\nVery powerful but has very little magic.\nAttack speed is twenty percent lower!",
       "ROGUE": "A rogue starts with 150 mana/magic, 100 HP and 2 defense.\nHigh evasion and critical strike chance!\nWeaker against heavy area of effect attacks."
    }
    while True:
        print("Choose a path hero! Your class will affect you in your journey! ")
        class_type = input("You have 3 choices: MAGE, WARRIOR, or ROGUE ").upper()
        if class_type in class_types:
            print(f"You chose {class_type}! ")
            print(classes[class_type])
            return class_type
        
        

        print("\nInvalid choice! Please look at the options and try again.\n")


hero_element = choose_element(magic_Elements)
element_info(hero_element)
hero_class = choosing_class(class_list)
     
    