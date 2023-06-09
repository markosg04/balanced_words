#v4 with fixed mid_index + better calculation
from english_words import get_english_words_set

letter_weights = {'a': 0, 'b': 1, 'c': 0, 'd': 1, 'e': 0, 'f': 1, 'g': 1, 'h': 1,
                    'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 0, 'n': 0, 'o': 0, 'p': 1,
                    'q': 1, 'r': 0, 's': 0, 't': 1, 'u': 0, 'v': 0, 'w': 0, 'x': 0,
                    'y': 1, 'z': 0}

def calculate_center_of_mass(weights):
    total_mass = sum(item['mass'] for item in weights)
    mass_location_product_sum = sum(item['mass'] * item['index'] for item in weights)
    
    if total_mass == 0:
        return 0

    center_of_mass = mass_location_product_sum / total_mass

    return center_of_mass


def string_to_weights(string, weight_map):
    weights = []
    for i, char in enumerate(string):
        if char in weight_map:
            weight = weight_map[char]
            weights.append({'mass': weight, 'index': i})
    return weights


def is_balanced(word, letter_weights):
    mid_index = 0
  
    if len(word) % 2 != 0:
        mid_index = len(word) // 2
    else: 
        mid_index = (len(word) / 2) - 0.5

    weights = string_to_weights(word, letter_weights)
    center_of_mass = calculate_center_of_mass(weights)
    
    return abs(center_of_mass - mid_index) < 1e-9


def find_balanced_words(words):

    balanced_words = [word for word in words if is_balanced(word, letter_weights)]
    
    return balanced_words


words = get_english_words_set(['web2'], lower=True, alpha=True)  

with open('output.txt', 'w') as f:
        for word in find_balanced_words(words):
            f.write(word + '\n')
