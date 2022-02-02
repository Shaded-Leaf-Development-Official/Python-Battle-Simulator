# AUTHOR: Shadewhisker
#
# Copyleft (l) Shaded Leaf Productions
#
# Program Version: 0.8.0 Beta
#
# Codename: IT'S ALIIIVE!!!

import random, time

def main():
    print("Battle sim\n")

    menuChoice = 0
    while menuChoice != 2:
        menuPrint()
        menuChoice = int(input("enter selection here: "))

        if menuChoice == 1:
            battleLoop()
        elif menuChoice == 2:
            print("Thanks for playing! goodbye.\n")
        else:
            print("that's not a valid option.\n")
            menuPrint()
            menuChoice = int(input("Please enter a valid option: "))

def menuPrint():
    print("<===============[MAIN MENU]===============>")
    print("|                                         |")
    print("| 1) Battle!                              |")
    print("| 2) Exit.                                |")
    print("|                                         |")
    print("<=========================================>\n")

def batMenuPrint():
    print("<===============[BATTLE MENU]===============>")
    print("|                                           |")
    print("| 1) Fight!                                 |")
    print("| 2) Defend!                                |")
    print("| 3) Item!                                  |")
    print("| 4) Run!                                   |")
    print("|                                           |")
    print("<===========================================>\n")

def battleLoop():

    enemyName = "Slime"
    enemyHP = 700
    enemyAtk = 40
    enemyDef = 20
    enemySpd = 10

    plrHP = 850
    plrAtk = 35
    plrDef = 30
    plrSpd = 5
    
    battleOver = False

    print("Starting battle! Slime approaches!\n")
    time.sleep(0.5)

    while battleOver == False:

        print("next turn!\n")
        print("checking to see who goes first...\n")
        time.sleep(0.5)
        plrSpdMod = random.randint(1, 3)
        enemySpdMod = random.randint(1, 3)
        spdCheckPlr = plrSpd * plrSpdMod
        spdCheckEnemy = enemySpd * enemySpdMod

        if plrSpdMod > enemySpdMod:
            print("Player goes first!\n")
            batMenuPrint()
            plrInput = int(input("make your selection here: "))
            while plrInput != 1 and plrInput != 2 and plrInput != 3 and plrInput != 4:
                print("that's invalid.\n")
                plrInput = int(input("please enter a valid input: "))

            if plrInput == 1:
                print("you attack!\n")
                plrDmg = 0
                plrAtkMod = random.randint(1, 3)
                plrAtkDmg = plrAtk * plrAtkMod - (enemyDef / 2)
                # crit check
                critNumPlrCheck = random.randint(0, 100)
                if critNumPlrCheck >= 60 and critNumPlrCheck <= 80:
                    print("WHOA!!! you got a CRIT!\n")
                    plrAtkCritBoost = plrAtkDmg * 3
                    plrDmg = plrAtkDmg + plrAtkCritBoost
                    print("you attacked the enemy for", plrDmg, "damage!\n")


                    # damage application

                    enemyHP = enemyHP - plrDmg
                    print("Remaining enemy HP:", enemyHP, "\n")


                    # detect win state

                    if enemyHP <= 0:
                        battleOver = True

                else:
                    plrDmg = plrAtkDmg
                    print("you attacked the enemy for", plrDmg, "damage!\n")


                    enemyHP = enemyHP - plrDmg
                    print("Remaining enemy HP:", enemyHP, "\n")

                    # detect win state

                    if enemyHP <= 0:
                        battleOver = True



        elif plrSpdMod < enemySpdMod:
            print("Slime goes first!\n")
            time.sleep(0.8)
            print("the slime charges forth!\n")
            enemyAtkMod = random.randint(1, 3)
            enemyAtkDmg = enemyAtk * enemyAtkMod - (plrDef / 2)
            # crit check
            critNumEnemyCheck = random.randint(0, 100)
            if critNumEnemyCheck >= 50 and critNumEnemyCheck <= 80:
                print("GADZOOKS!!! the enemy landed a CRIT!\n")
                enemyAtkCritBoost = enemyAtkDmg * 3
                enemyDmg = enemyAtkDmg + enemyAtkCritBoost
                print("the slime attacked you for", enemyDmg, "damage!\n")

                # damage application

                plrHP = plrHP - enemyDmg
                print("Remaining player HP:", plrHP, "\n")

                # detect fail state

                if plrHP <= 0:
                    battleOver = True

            else:
                enemyDmg = enemyAtkDmg
                print("the slime attacked you for", enemyDmg, "damage!\n")

                plrHP = plrHP - enemyDmg
                print("Remaining player HP:", plrHP, "\n")

                # detect fail state

                if plrHP <= 0:
                    battleOver = True


        else:
            firstPickForce = random.randint(1, 2)

            if firstPickForce == 1:
                print("Player goes first!\n")
                batMenuPrint()
                plrInput = int(input("make your selection here: "))
                while plrInput != 1 and plrInput != 2 and plrInput != 3 and plrInput != 4:
                    print("that's invalid.\n")
                    plrInput = int(input("please enter a valid input: "))

                if plrInput == 1:
                    print("you attack!\n")
                    plrAtkMod = random.randint(1, 3)
                    plrAtkDmg = plrAtk * plrAtkMod - (enemyDef / 2)
                    # crit check
                    critNumPlrCheck = random.randint(0, 100)
                    if critNumPlrCheck >= 60 and critNumPlrCheck <= 80:
                        print("WHOA!!! you got a CRIT!\n")
                        plrAtkCritBoost = plrAtkDmg * 3
                        plrDmg = plrAtkDmg + plrAtkCritBoost
                        print("you attacked the enemy for", plrDmg, "damage!\n")

                        # damage application

                        enemyHP = enemyHP - plrDmg
                        print("Remaining enemy HP:", enemyHP, "\n")

                        # detect win state

                        if enemyHP <= 0:
                            battleOver = True

                    else:
                        plrDmg = plrAtkDmg
                        print("you attacked the enemy for", plrDmg, "damage!\n")

                        enemyHP = enemyHP - plrDmg
                        print("Remaining enemy HP:", enemyHP, "\n")

                        # detect win state

                        if enemyHP <= 0:
                            battleOver = True
            else:
                print("Slime goes first!\n")
                time.sleep(0.8)

                print("the slime charges forth!\n")
                enemyAtkMod = random.randint(1, 3)
                enemyAtkDmg = enemyAtk * enemyAtkMod - (plrDef / 2)
                # crit check
                critNumEnemyCheck = random.randint(0, 100)
                if critNumEnemyCheck >= 50 and critNumEnemyCheck <= 80:
                    print("GADZOOKS!!! the enemy landed a CRIT!\n")
                    enemyAtkCritBoost = enemyAtkDmg * 3
                    enemyDmg = enemyAtkDmg + enemyAtkCritBoost
                    print("the slime attacked you for", enemyDmg, "damage!\n")

                    # damage application

                    plrHP = plrHP - enemyDmg
                    print("Remaining player HP:", plrHP, "\n")

                    # detect fail state

                    if plrHP <= 0:
                        battleOver = True

                else:
                    enemyDmg = enemyAtkDmg
                    print("the slime attacked you for", enemyDmg, "damage!\n")

                    plrHP = plrHP - enemyDmg
                    print("Remaining player HP:", plrHP, "\n")

                    # detect fail state

                    if plrHP <= 0:
                        battleOver = True





    



main()
