""" Kenrick Zhang | TEJ3M1 | 16/04/2023 | Python Unit 1 Project | Mr Leung's Lab """

from random import choice, randint

elements = {'h': 'hydrogen',
            'he': 'helium',
            'li': 'lithium',
            'be': 'beryllium',
            'b': 'boron',
            'c': 'carbon',
            'n': 'nitrogen',
            'o': 'oxygen',
            'f': 'fluorine',
            'ne': 'neon',
            'na': 'sodium',
            'mg': 'magnesium',
            'al': 'aluminum',
            'si': 'silicon',
            'p': 'phosphorus',
            's': 'sulfur',
            'cl': 'chlorine',
            'ar': 'argon',
            'k': 'potassium',
            'ca': 'calcium',
            'sc': 'scandium',
            'ti': 'titanium',
            'v': 'vanadium',
            'cr': 'chromium',
            'mn': 'manganese',
            'fe': 'iron',
            'co': 'cobalt',
            'ni': 'nickel',
            'cu': 'copper',
            'zn': 'zinc',
            'ga': 'gallium',
            'ge': 'germanium',
            'as': 'arsenic',
            'se': 'selenium',
            'br': 'bromine',
            'kr': 'krypton',
            'rb': 'rubidium',
            'sr': 'strontium',
            'y': 'yttrium',
            'zr': 'zirconium',
            'nb': 'niobium',
            'mo': 'molybdenum',
            'tc': 'technetium',
            'ru': 'ruthenium',
            'rh': 'rhodium',
            'pd': 'palladium',
            'ag': 'silver',
            'cd': 'cadmium',
            'in': 'indium',
            'sn': 'tin',
            'sb': 'antimony',
            'te': 'tellurium',
            'i': 'iodine',
            'xe': 'xenon',
            'cs': 'cesium',
            'ba': 'barium',
            'la': 'lanthanum',
            'ce': 'cerium',
            'pr': 'praseodymium',
            'nd': 'neodymium',
            'pm': 'promethium',
            'sm': 'samarium',
            'eu': 'europium',
            'gd': 'gadolinium',
            'tb': 'terbium',
            'dy': 'dysprosium',
            'ho': 'holmium',
            'er': 'erbium',
            'tm': 'thulium',
            'yb': 'ytterbium',
            'lu': 'lutetium',
            'hf': 'hafnium',
            'ta': 'tantalum',
            'w': 'tungsten',
            're': 'rhenium',
            'os': 'osmium',
            'ir': 'iridium',
            'pt': 'platinum',
            'au': 'gold',
            'hg': 'mercury',
            'tl': 'thallium',
            'pb': 'lead',
            'bi': 'bismuth',
            'po': 'polonium',
            'at': 'astatine',
            'rn': 'radon',
            'fr': 'francium',
            'ra': 'radium',
            'ac': 'actinium',
            'th': 'thorium',
            'pa': 'protactinium',
            'u': 'uranium',
            'np': 'neptunium',
            'pu': 'plutonium',
            'am': 'americium',
            'cm': 'curium',
            'bk': 'berkelium',
            'cf': 'californium',
            'es': 'einsteinium',
            'fm': 'fermium',
            'md': 'mendelevium',
            'no': 'nobelium',
            'lr': 'lawrencium',
            'rf': 'rutherfordium',
            'db': 'dubnium',
            'sg': 'seaborgium',
            'bh': 'bohrium',
            'hs': 'hassium',
            'mt': 'meitnerium',
            'ds': 'darmstadtium',
            'rg': 'roentgenium',
            'cn': 'copernicium',
            'nh': 'nihonium',
            'fl': 'flerovium',
            'mc': 'moscovium',
            'lv': 'livermorium',
            'ts': 'tennessine',
            'og': 'oganesson'
           }

grades = ("F", "D", "C", "B", "A", "Mr. Leung Level")

compounds_tuple = ( "Sodium chloride",
                    "Calcium chloride",
                    "Potassium iodide",
                    "Lithium fluoride",
                    "Aluminum oxide",
                    "Magnesium nitride",
                    "Copper sulfide",
                    "Zinc phosphide",
                    "Silver bromide",
                    "Iron (II) oxide",
                    "Lead (II) sulfide",
                    "Tin (IV) oxide",
                    "Cadmium selenide",
                    "Barium chloride"
                  )

compounds_detailed = {"Sodium chloride":("Sodium chloride", "NaCl", {"na": 1, "cl": 1}),
                      "Calcium chloride":("Calcium chloride", "CaCl2", {"ca": 1, "cl": 2}),
                      "Potassium iodide":("Potassium iodide", "KI", {"k": 1, "i": 1}),
                      "Lithium fluoride":("Lithium fluoride", "LiF", {"li": 1, "f": 1}),
                      "Aluminum oxide":("Aluminum oxide", "Al2O3", {"al": 2, "o": 3}),
                      "Magnesium nitride":("Magnesium nitride", "Mg3N2", {"mg": 3, "n": 2}),
                      "Copper sulfide":("Copper sulfide", "CuS", {"cu": 1, "s": 1}),
                      "Zinc phosphide":("Zinc phosphide", "Zn3P2", {"zn": 3, "p": 2}),
                      "Silver bromide":("Silver bromide", "AgBr", {"ag": 1, "br": 1}),
                      "Iron (II) oxide":("Iron (II) oxide", "FeO", {"fe": 1, "o": 1}),
                      "Lead (II) sulfide":("Lead (II) sulfide", "PbS", {"pb": 1, "s": 1}),
                      "Tin (IV) oxide":("Tin (IV) oxide", "SnO2", {"sn": 1, "o": 2}),
                      "Cadmium selenide":("Cadmium selenide", "CdSe", {"cd": 1, "se": 1}),
                      "Barium chloride":("Barium chloride", "BaCl2", {"ba": 1, "cl": 2})
                     }

def main():
  banned = False
  in_lab = True
  safety = False
  current_grade = randint(0, len(grades) - 1)
  
  while in_lab:
    print("\nWelcome to Mr. Leung's Lab. Make sure to follow WHMIS at all times!")
    print(f"Your current grade is a {grades[current_grade]}, about a {current_grade}.\nHelp Mr. Leung synthesize chemicals for higher grades!\n")
  
    input_choice = input("Select an option to start below:" + "\n1. Put on safety equipment" + "\n2. Take off safety equipment" + "\n3. Start synthesizing chemicals" + "\n4. Leave the lab\n")
    if not input_choice.isnumeric():
      print(f"{input_choice} is not an option.")
      continue

    input_choice = int(input_choice)
    
    if input_choice == 1:
      if safety:
        print("You already have your safety equipment on, but thank you for double-checking!")
      else:
        safety = True
        print("You put your safety equipment on. Thank you for following WHMIS!")
    elif input_choice == 2:
      if safety:
        safety = False
        print("You took off your safety equipment.")
      else:
        print("You don't have any safety equipment to take off.")
    elif input_choice == 3 and not banned:
      # evaluates the input_choice == 3 of entering the lab, but also boolean banned to check if the student has already tried to enter the lab without WHMIS and was told off by Mr. Leung
      
      if safety:
        compound_choice = choice(compounds_tuple)
        
        print(f"Let's start, shall we?\n\nWhat I need you to do is type the atomic symbol for each atom of the element you want add to the final compound. They must be input in order, left to right.\n\nI want you to synthesize {compound_choice}.")

        done_synthesis = False

        input_compound = []

        extended_compound = ""
        
        while not done_synthesis:

          element_input = input("Enter the atomic symbol of an element to add or type 'create' to finish: ").strip().lower()

          if element_input == "create":
            done_synthesis = True

            if correct(input_compound, compound_choice):
              if current_grade < len(grades) - 1:
                current_grade += 1
                
                print(f"That's correct! For your good work, I have moved your grade up to a {grades[current_grade]}. Keep it up!")
                
              else:
                print(f"That's correct! All your work is so great, I can't even move your grade up past {grades[current_grade]}. Keep up the amazing work!")

            else:
              for i in input_compound:
                extended_compound += elements[i] + " "
  
              print(f"Well, you synthesized {extended_compound}for sure. Not quite what I was looking for. You stay at a {grades[current_grade]}.")

          elif element_input in elements:
            input_compound.append(element_input)

          else:
            print(f"I'm not sure what element {element_input} is. No wonder you have a {grades[current_grade]}.")
      
      else:
        print("You didn't follow WHMIS. Get out of my lab!")
        in_lab = False
        banned = True
    
    elif input_choice == 4:
      if safety:
        print("Where do you think you're going with my equipment on?")
      else:
        print("Come again!")
        in_lab = False

    else:
      print(f"{input_choice} is not an option.")

def correct(input_compound, compound_choice):

  compounded = {}

  for element in input_compound:
    # iterates each element in the list input_compound and stores into element so that it can be added to the count for the dictonary compounded
    if element in compounded:
      compounded[element] = compounded[element] + 1
    else:
      compounded[element] = 1

  if compounded == compounds_detailed[compound_choice][2]:
    return True
  else:
    return False

while True:
  # keeps the game running until its not, just to ensure that the game doesn't exit prematurely
  main()

  input_choice = input("You have left the lab. Type 'leave' to leave the school or anything else to return to the lab: ").strip().lower()

  if input_choice == "leave":
    print("Stay safe!")
    break