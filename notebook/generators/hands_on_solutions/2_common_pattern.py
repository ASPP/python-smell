from string import punctuation

def without_punctuation(words):
    for word in words:
        stripped = word.rstrip(punctuation)
        if len(stripped) > 0:
            yield stripped

words = ['Apple', 'Banana...', 'Carrot!!', '*$', '!Dinosaur']
for word in without_punctuation(words):
    print(word)
