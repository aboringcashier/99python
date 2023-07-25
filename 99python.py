        
        
# 99 Python, a program to Calculate "wen 99".. 
# Credits go to me and this cool Chiptune playlist I found on YouTube.


ign = input("What is your IGN: ")
print("Hello, " + ign + "!")
print()

skill = input("What skill did you want to calculate today: ").lower()
print()
if skill == "fishing".lower():
    print("Fishing it is, (TIP: Barbarian Fishing offers Strength/Agility XP as well.)")
    print()
    level = input("What fishing level are you: ")
    print()
    if int(level) in range (1,26):
        print("Completing the quests Sea Slug + Fishing Contest get you to Level 26. Which skips most of the early game grind")
        print()
    elif int(level) in range (27, 35):
        print("Fly fishing for trout and salmon averages around 15-25k XP/Hour.")
        print()
    elif int(level) in range (36, 58):
        print("Tempoross, averages around 30-60k XP/Hour depending on your speed and current level!")
        print()
    elif int(level) in range (59, 71):
        print("3-Tick Barbarian Fishing allows you to earn up to 90-100k XP/Hour.")
        print()
    elif int(level) in range (72, 99):
        print("2-Tick Harpoon Fishing offers up to 100-130k XP/Hour on the road to 99!")
        print()
    
    num1 = int(input("Total XP currently: "))
    num2 = 13034447 - num1
    print("Total XP till level 99:", num2)
    print()
    print("You've got this, ", ign)

    
    
elif skill == "thieving".lower():
    print("Thieving it is.  (TIP: A higher thieving level gets you 2x LOOT.)")
    print()
    level = input("What thieving level are you?: ")
    print()
    if int(level) in range (1, 5):
        print("Thieving men in Lumbridge is the best starting XP. It will take you roughly 49 pickpockets.")
        print()
    elif int(level) in range (6, 25):
        print("Stealing from Bakery Stalls offer you 19k XP/Hour")
        print()
    elif int(level) in range (26, 49):
        print("Stealing from Fruit Stalls offer up to 42k XP/Hour")
        print()
    elif int(level) in range (50, 65):
        print("Stealing artefacts at this level give you around 130k XP/Hour")
        print()
    elif int(level) in range (66, 91):
        print("Blackjacking offers you XP rates from 130k-265k XP/Hour depending on your level")
        print()
    elif int(level) in range (92, 99):
        print("Pyramid Plunder offers up to 270k/Hour depending on your current level.")
        print()
        
    num1 = int(input("Total XP currently: "))
    num2 = 13034447 - num1
    print("Total XP till level 99:", num2)
    print()
    print("You've got this, ", ign)
    
    
    
elif skill == "herblore".lower():
    print("Herblore it is. (TIP: Herblore is a very expensive skill. Plan carefully!)")
    print()
    level = input("What herblore level are you?: ")
    print()
    if int(level) in range (1, 26):
        print("After completing Druidic Ritual, you will need to make 343 Attack Potions.")
        print()
    elif int(level) in range (27, 38):
        print("Energy potions are up next, you will have to make 322 total potions.")
        print()
    elif int(level) in range (39, 99):
        print("Coasting with Prayer Potions will get you to 99, you will have to make 148618 potions.")
        print()
        
    
    num1 = int(input("Total XP currently: "))
    num2 = 13034447 - num1
    print("Total XP till level 99:", num2)
    print()
    print("You've got this, ", ign)
    
    
    
    
    
    
elif skill == "cooking":
    print("Cooking it is. One of the first original SKILLS.")
    print()
    level = input("What cooking level are you?: ")
    print()
    if int(level) in range (1, 4):
        print("Completing the Quest Cook's Assistant boosts you from 1 to 4 Cooking! ")
        print()
    elif int(level) in range (5, 15):
        print("Cooking herring for about an hour will get you to 15 cooking.")
        print()
    elif int(level) in range (16, 24):
        print("Time to cook Trout, which can be fished by barbarian village!")
        print()
    elif int(level) in range (25, 35):
        print("Time to cook Salmon, which can be fished by barbarian village!")
        print()
    elif int(level) in range (36, 100):
        print("Making Jugs of wine offer one of the Best XP/Hour at a wopping 450k/XP Hour!")
        print()
        
        num1 = int(input("Total XP currently: "))
        num2 = 13034447 - num1
        print("Total XP till level 99:", num2)
        print()
        print("You've got this, ", ign)
        
         
    

elif skill == "cooking":
    print("Cooking it is.")

elif skill == "cooking":
    print("Cooking it is.")

elif skill == "cooking":
    print("Cooking it is.")

elif skill == "cooking":
    print("Cooking it is.")

elif skill == "thieving":
    print("thieving it is.")

elif skill == "cooking":
    print("Cooking it is.")

elif skill == "cooking":
    print("Cooking it is.")

elif skill == "cooking":
    print("Cooking it is.")

elif skill == "cooking":
    print("Cooking it is.")

elif skill == "cooking":
    print("Cooking it is.")

elif skill != ("cooking", "fishing", "thieving", "herblore"):
    print("ERROR, no skill selected.")
    
    
# will add more skills to code towards the end of the project completion. 
# not adding combat skills since determining when 99 factors in bossing and other things in-game. 


