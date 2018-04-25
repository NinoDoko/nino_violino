import random, os

all_words = ''
max_word_len = 7 

namer_path = os.path.dirname(os.path.realpath(__file__))

words_path = namer_path + '/mobyposi.i'

with open(words_path) as f: 
    all_words = f.read()
    all_words = [x.split('|') for x in all_words.replace('\xd7','|').split('\r') if x]

def get_types(all_words): 
    types = []
    for word in all_words: 
        if word[1] not in types: types.append(word[1])
    return types

def get_words_with_type(all_words, t):
    return [x[0] for x in all_words if x[1] == t and len(x[0]) < max_word_len]


def get_name():
    nouns = get_words_with_type(all_words, 'N')
    verbs = get_words_with_type(all_words, 'V')
    verbs = [x for x in verbs if x.endswith('ing')]
    adjectives = [x[0] for x in all_words if x[1] == 'A' and len(x[0]) < max_word_len]

    name = '%s %s %s' % (random.choice(adjectives), random.choice(verbs), random.choice(nouns))
    name = name.replace(' ', '_').lower()
    return name
