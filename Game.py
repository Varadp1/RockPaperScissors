import random
print("Welcome to Rock,Paper,Scissors!!")
print("You will play against a cpu!!")
player_p = 0
cpu_p = 0
while player_p <= 10 and cpu_p <= 10:
  if player_p == 10:
    print("You won the game!!")
    break
  elif cpu_p == 10:
    print("You lose the game!!")
    break
  while True:
    player = input("Rock(r) , Paper(p) , Scissors(s)\n").lower()
    cpu = random.choice(["r", "p", "s"])
    if player == "r":
      if cpu == "r":
        print("You chose 'Rock' and cpu chose 'Rock'")
        print("Its a tie!!")
        print(f"You:{player_p} , Cpu:{cpu_p}")
      elif cpu == "p":
        print("You chose 'Rock' and cpu chose 'Paper'")
        print("You lose!!!")
        cpu_p = cpu_p + 1
        print(f"You:{player_p} , Cpu:{cpu_p}")
      elif cpu == "s":
        print("You chose 'Rock' and cpu chose 'Scissors'")
        print("You Won!!!")
        player_p = player_p + 1
        print(f"You:{player_p} , Cpu:{cpu_p}")
      break
    elif player == "s":
      if cpu == "r":
        print("You chose 'Scissors' and cpu chose 'Rock'")
        print("You lose!!")
        cpu_p = cpu_p + 1
        print(f"You:{player_p} , Cpu:{cpu_p}")
      elif cpu == "p":
        print("You chose 'Scissors' and cpu chose 'Paper'")
        print("You Won!!!")
        player_p = player_p + 1
        print(f"You:{player_p} , Cpu:{cpu_p}")
      elif cpu == "s":
        print("You chose 'Scissors' and cpu chose 'Scissors'")
        print("Tie!!!")
        print(f"You:{player_p} , Cpu:{cpu_p}")
      break
    elif player == "p":
      if cpu == "r":
        print("You chose 'Paper' and cpu chose 'Rock'")
        print("You Won!!")
        player_p = player_p + 1
        print(f"You:{player_p} , Cpu:{cpu_p}")
      elif cpu == "p":
        print("You chose 'Paper' and cpu chose 'Paper'")
        print("Tie!!!")
        print(f"You:{player_p} , Cpu:{cpu_p}")
      elif cpu == "s":
        print("You chose 'Paper' and cpu chose 'Scissors'")
        print("You lose!!!")
        cpu_p = cpu_p + 1
        print(f"You:{player_p} , Cpu:{cpu_p}")
      break
    else:
      print("Please choose a valid input!!!")