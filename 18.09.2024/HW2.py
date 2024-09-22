# START
jumps: int = 0
sum_meter: float = 0
new_world_record: float = None
name: str = None
highest_jump: float = 0
for i in range(7):
    meter: float = float(input("What height did the gymnast make?: "))
    if meter < 5.8:
        continue
    if meter >= 5.80:
        sum_meter += meter
        jumps += 1
    if meter > 6.23:
        new_world_record = meter
        name: str = input("The world record wes beat, what is the name of the gymnast who beat it?: ")
        sum_meter += meter
    if meter > highest_jump:
        highest_jump = meter
avg_meter = sum_meter // jumps

print(f"There were {jumps} good scores and their average is {avg_meter}.")
print(f"The highest jump was {highest_jump} meters. ")
print(f"New world record: {new_world_record}, {name} was the one who beat it!")

# STOP
