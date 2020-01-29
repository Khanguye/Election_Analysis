while True:
    num = int(input("How many numbers?"))
    for i in range(num):
        print(i)
    ans = input("Would you like continue? y (Countinue), n (Exit)")
    if (ans == "n"):
        break


