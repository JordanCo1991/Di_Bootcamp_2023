word_sequence = input("Enter a comma-separated sequence of words: ")
words = [word.strip() for word in word_sequence.split(",")]
sorted_words = sorted(words)
sorted_sequence = ",".join(sorted_words)
print(sorted_sequence)
