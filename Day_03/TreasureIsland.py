print("Welcome to Treasure Island")
print("Your mission is to find the treasure")

left_right = input("You are at a crossroad.  Where do you want to go? Left or Right?").lower()
if left_right == "right":
    swim_wait = input("Do you want to swim or wait?").lower()
    if swim_wait == 'wait':
        color = input("What color do you like? Red, Blue or Yellow?").lower()
        if color == "red":
            print("You Win")
        else:
            print("Game Over")
    else:
            print("Game Over")
else:
            print("Game Over")