from random import randrange

def guess_the_word(c: str, bag: set, correct_word: str, input_word) -> tuple[bool, set, str, str]:
    for i in range(len(correct_word)):
        if correct_word[i] == c:
            input_word = input_word[:i] + c + input_word[i+1:]
            bag.add(c)
    if correct_word == input_word:
        print(f"You guessed the correct word: {input_word}")
        return True, bag, correct_word, input_word

    print(f"Try again: {input_word}")
    return False, bag, correct_word, input_word  


words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = words[randrange(0,len(words))-1]
guess = len(word) * "_"
guessed_word = False
bag = set()
max_num_tries = max(int(input("How many tries: ")), len(word))
print()
print(f"Number of tries: {max_num_tries}")
while not guessed_word:
    max_num_tries -= 1
    c = input("Enter a char: ")
    if c in bag:
        print("Try new char!!!")
        print(bag)
    guessed_word, c, word, guess = guess_the_word(c, bag, word, guess)
    if max_num_tries < 0:
        print("No more tries!!!")
        print("Game Over!!!")
        break
    print(f"Number of tries left: {max_num_tries}")
    print()
