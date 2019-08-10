import random

guesses = ""
infile = open("c:\\words.txt", "r")
lines = infile.readlines()
word = random.choice(lines)
word = word[:len(word)-1]
turns = len(word)*2

while turns > 0:
    failed = 0
    for chr in word:
        if chr in guesses:
            print(chr,end="")
        else:
            print("*", end="")
            failed += 1
    if failed == 0:
        print("\nYou Win")
        break
    print("")
    guess = input("Enter a alphabet: ")

    if guess not in word:
        turns -= 1
        print("남은 기회는 " + str(turns) + "회 입니다.")
        if turns == 0:
            print("You Lose\n정답은 "+word)
            break
    else:
        guesses += guess
        print("남은 기회는 " + str(turns) + "회 입니다.")

infile.close()
