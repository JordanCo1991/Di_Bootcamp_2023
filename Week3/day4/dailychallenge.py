class Text:
    def __init__(self, text):
        self.text = text

    def occurence_word(self, word):
        words = self.text.split(" ")
        count = words.count(word)
        if count == 0 : 
            return None 
        return f"The word {word} was found {count} times"

    def most_common_word(self):
        words = self.text.split()
        word_counts = {}
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1
        most_common = max(word_counts, key=word_counts.get)
        return most_common

    def unique_words(self):
        words = self.text.split()
        unique_words = list(set(words))
        return unique_words

  @classmethod
        def from_file(cls, file): 
            with open(file, "r") as story :
                all_story = story.read()
                return cls(all_story)

text_string = "A good book would sometimes cost as much as a good house."
text = Text(text_string)
print(text.occurence_word("good")) 
print(text.most_common_word())  
print(text.unique_words()) 

t2 = text.from_file('/Users/jordancohen/Code/Di_Bootcamp_2023/Week3/day4/the_stranger.txt')