import random
import array
magic_Elements = ["FIRE", "ICE", "LIGHTNING"]

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
                    "Fire has high offensive power! \nApplies tick dmg over time! \nHowever it has a  high mana cost and very little defensive capabilities\n",
            "ICE": "Ice has excellent defensive capability! \nSlows down enemies over time! \nHighly defensive, not very effective by itself!\n",
            "LIGHTNING": "Lightning has high speed and high chance for critical hits! \nApplies shock to enemies and can chain to multiple targets! \nVery fast but its not the best at defense or offense!\n"
            }
        
    print(descriptions[chosen_element])
           


hero_element = choose_element(magic_Elements)
element_info(hero_element)
     
    