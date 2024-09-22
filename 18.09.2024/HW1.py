# Input 10 numbers using loop
# If number > 1000 or number< -1000, continue
# If -9999 break
# If not -9999, print how any positive, how many negative, how many zero, how many divisible by 7
# what is the last positive number, if no print none, what is the last negative number if no print none
# START
positive: int = 0
negative: int = 0
zero: int = 0
divisible7: int = 0
last_positive: int = None
last_negative: int = None

for i in range(10):
    num: int = int(input("Enter a number between -1000 - 1000: "))
    if num == -9999:
        break
    if num > 1000 or num < -1000:
        print("Number is not in range. ")
        num: int = int(input("Enter a number between -1000 - 1000: "))
        continue
    if num % 7 == 0:
        divisible7 += 1
    if 0 < num < 1000:
        positive += 1
        last_positive = num
    elif -1000 < num < 0:
        negative += 1
        last_negative = num
    else:
        zero += 1
if num != -9999:
    print(f"{divisible7} numbers are divisible by 7 ")
    print(f"{positive} numbers are positive")
    print(f"{negative} numbers are negative")
    print(f"the number 0 was entered {zero} times")
    print(f"last positive number is {last_positive}")
    print(f"last negative number is {last_negative}")


# STOP
