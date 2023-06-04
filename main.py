#V1 which is pretty bad and doesn't really find them properly

from english_words import get_english_words_set

def calc_weight(word, letter_weights):
    return sum(letter_weights.get(letter, 0) for letter in word)

def is_balanced(word, letter_weights):
    left = ''
    right = ''
    mid_index = len(word) // 2
    left = word[:mid_index]

    if len(word) % 2 != 0:
        right = word[mid_index + 1:]
    else:
        right = word[mid_index:]


    return calc_weight(left, letter_weights) == calc_weight(right, letter_weights)


def find_balanced_words(words):
    letter_weights = {'a': 0, 'b': 1, 'c': 0, 'd': -1, 'e': 0, 'f': 1, 'g': -1, 'h': 1,
                      'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 0, 'n': 0, 'o': 0, 'p': -1,
                      'q': -1, 'r': 1, 's': 1, 't': 1, 'u': 0, 'v': 0, 'w': 0, 'x': 0,
                      'y': -1, 'z': 0}

    balanced_words = [word for word in words if is_balanced(word, letter_weights)]
    
    return balanced_words


words = get_english_words_set(['web2'], lower=True, alpha=True)  

with open('output.txt', 'w') as f:
        for word in find_balanced_words(words):
            f.write(word + '\n')
