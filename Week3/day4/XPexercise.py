import random

def get_words_from_file(file_path):
    with open(file_path, "r") as file:
        words = file.read().splitlines()
    return words

def get_random_sentence(length, words):
    random_words = random.sample(words, length)
    sentence = ' '.join(random_words)
    return sentence.lower()

def main():
    print("Welcome to the Random Sentence Generator!")
    print("This program generates a random sentence based on a word list.")

    file_path = 'Week3/day4/words_list.txt'  # Replace with the actual file path
    words = get_words_from_file(file_path)

    while True:
        try:
            length = int(input("How long would you like the sentence to be (between 2 and 20)? "))
            if 2 <= length <= 20:
                break
            else:
                print("Invalid input. Please enter a number between 2 and 20.")
        except ValueError:
            print("Invalid input. Please enter a number between 2 and 20.")

    sentence = get_random_sentence(length, words)
    print("Random Sentence:", sentence)

if __name__ == '__main__':
    main()


