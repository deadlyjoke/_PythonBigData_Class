import random

def play_game():

  print("=====猜數字遊戲開始=========\n\n")
  min = 1
  max = 99
  count = 0
  random_number = random.randint(min,max)
  #print(random_number)
  while True:
    input_number = int(input(f"請輸入數字({min}~{max}):"))
    count += 1
    if(input_number == random_number):
      print(f"賓果!猜對了, 答案是:{input_number}")
      print(f"您猜了:{count}次")
      break
    elif(input_number>random_number):
      print(f"再小一點")
      max = input_number - 1
    elif(input_number<random_number):
      print(f"再大一點")
      min = input_number + 1

    print(f"您已經猜了:{count}次\n")

while(True):
  play_game()
  play_again = input("是否要再玩一次? (y/n):")
  if (play_again == 'n'):
    break

print("Game Over")