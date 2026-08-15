import random


def compute_difference(n: int) -> int:
    diff = 21 - n
    if diff > 1:
        if (4 - n % 4) != 4:
            num = 4 - (n % 4)
        else:
            num = random.randrange(1, 3)
    else:
        num = 1
    return num


count = 0
your_turn = input("You beginn? Y/N: ").lower()

while input != "e" and count != 21:
    if your_turn == True:
        num = int(input("What is your number: "))
        old_num = count
        while num > 3 and not num < 1 or not num > 3 and num < 1 or num + count > 21:
            if num + count <= 21:
                num = int(input("Number between 1 and 3: "))
            else:
                num = int(input("Number to large: "))
        count += num
        bots_num = compute_difference(count)
        if num > 0 and num < 4 and count < 21:
            count += bots_num

    else:
        bots_num = compute_difference(count)
        print("______________________________________")
        print(f"Bots number: {bots_num}")
        print(f"Sum:         {count + bots_num}")
        if count + bots_num == 21:
            print(f"Sum: {count + bots_num}")
            print("You won!!!!")
            break
        num = int(input("What is your number: "))
        old_num = count
        while num > 3 and not num < 1 or not num > 3 and num < 1 or num + count > 21:
            if num + count <= 21:
                num = int(input("Number between 1 and 3: "))
            else:
                num = int(input("Number to large: "))
        count = count + bots_num + num

    print("______________________________________")
    print(f"Bots number: {bots_num}")
    print(f"Your number: {num}")
    print(f"Old count:   {old_num}")
    print(f"Sum:         {count}")

    if count == 21:
        print()
        print("Game Over!")
