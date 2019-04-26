import inquirer, math, random

userCan = 75
zombiCan = 15

def check():
  if userCan <= 0:
    print("\nLose.\n")
    exit()

  if zombiCan <= 0:
    print("\nWin!\n")
    exit()

  play()

def play():
    global userCan , zombiCan

    questions = [
        inquirer.List("guess",
            message="Try to stay alive! Guess a number between [1-5]",
            choices=["1", "2", "3", "4", "5"]
        )
    ]
    answers = inquirer.prompt(questions)

    if userCan > 0 or zombiCan > 0:

        zombiNum = random.randint(1, 5)

        print("\nZombie rolled " + str(zombiNum))

        if zombiNum == int(answers['guess']):

            zombiCan -= int(answers['guess'])
            print("YOU HIT " + answers['guess'] + " damage")
            print("You have " + str(userCan) + " health left. The Zombie has " + str(zombiCan) + " health left.")

            check()

        else:
            userCan -= zombiNum
            print("OH NO! The zombie slashed you with " + str(zombiNum) + " damage")
            print("You have " + str(userCan) + " health left. The Zombie has " + str(zombiCan) + " health left.")

            check()

play()