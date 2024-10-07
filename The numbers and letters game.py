import random

vowels = ['A', 'E', 'I', 'O', 'U']
consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

#function for players to choice letters.
def get_letters():
    letters = []
    
    for _ in range(10):
        choice = input("Choose 'vowel' or 'consonant': ").lower()
        if choice == "vowel":  
            letters.append(random.choice(vowels))
        elif choice == "consonant":  
            letters.append(random.choice(consonants))
        else:
            print("Invalid choice. Please enter 'vowel' or 'consonant'.")
    return letters

#display the 10 letters chosen by the player
def display_letters(letters):
    print("Your letters are: ", " ".join(letters))

#let player enter the word they think is the longest
def find_longest_word(letters, word_list):
    longest_word = ""
    for word in word_list:
        avilable_letters = list(letters)
        not_available = True
    for char in word:
        if char in avilable_letters:
            avilable_letters.remove(char)
        else:
            not_available = False
            break
    if not_available and len(word) > len(longest_word):
        longest_word = word
    return longest_word

def calculate_letter_score(longest_word, player_word):
    L = len(longest_word)
    l = len(player_word)
    return 100 - (L - l) * 10

def letters_round(word_list):
    print("Welcome to the Letters Round!")

    letters = get_letters()
    print(f"Your letters are: {' '.join(letters)}")

    player_word = input("Enter the longest word you can make: ").upper() #ask the player for their word

    longest_word = find_longest_word(letters, word_list)
    print(f"The longest possible word was: {longest_word}")


    score = calculate_letter_score(longest_word, player_word)#
    print(f"Your score: {score}")


def generate_numbers():
    small_numbers = list(range(1, 11))
    large_numbers = [25, 50, 75, 100]
    
    numbers = random.sample(small_numbers, 4) + random.sample(large_numbers, 2)
    
    return numbers

def generate_target():
    return random.randint(100, 999)

def numbers_round():
    numbers = generate_numbers()
    target = generate_target()
    
    print(f"Your numbers are: {numbers}")
    print(f"Your target number is: {target}")
    
    guess = int(input("Enter your result: "))
    
    difference = abs(target - guess)
    if difference == 0:
        print("Congratulations! You've hit the target exactly!")
    else:
        print(f"Your guess is {difference} away from the target.")

#combine the letter round and the number round into one game.
def play_game():
    print("Welcome to the 'Des Chiffres et des Lettres' Game!")
    
    print("Letters Round")
    letters_round()
  
    print("Numbers Round")
    numbers_round()
    
    print("Thanks for playing!")

play_game()
