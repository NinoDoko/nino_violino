import random, chord_handler
from markov_values import markov_values


#Extremely rudimentary and not very random. Eventually turn to a better distribution. 
def get_note_from_offsets(offset_list):
    random_val = random.random()
    for i in range(len(offset_list)):
        if offset_list[i] > random_val: 
            return i
        random_val -= offset_list[i]

def get_markov_depth(markov_values):
    i = 0
    while True: 
        try:
            markov_values = markov_values[0]
        except TypeError:  #We expect this to hit an integer which cannot `get()` a value
            return i

        i+= 1

#Temporary - dunno how exactly to get these. 
def get_initial_markov_note_offsets(markov_values):
    markov_depth = get_markov_depth(markov_values)
    markov_len = len(markov_values[0])
    return [random.choice(range(markov_len)) for x in range(markov_len)]

#Returns a generator. Every time you call it, it should return a new note offset based on previous offsets. 
#Offsets are basically how many notes away from the root note the note is, in the current chord. 
def get_next_note_markov(markov_values, chord_root, chord_type):
    offset_list = get_initial_markov_note_offsets(markov_values)
    current_offset_list = []
    
    while True:
        for note_offset in offset_list: 
            current_offset_list = markov_values[note_offset]

        normalized_offset_list = [float(n) / sum(current_offset_list) for n in current_offset_list]
        next_note_offset = get_note_from_offsets(normalized_offset_list)
        offset_list = offset_list[1:] + [next_note_offset]

        next_note = chord_handler.get_note_from_offset(next_note_offset, chord_root, chord_type)
        yield next_note


#This is the hard part, we have to find a value for every note in the bar using AI or markov chains or stuff. 
def generate_notes_for_bar(bar, chord_root, chord_type, note_generator, base_volume):
    for note in bar['notes']: 
        note['value'] = note_generator.next()
        note['pitch'] = chord_handler.get_pitch(note['value'])
    return bar

#We update all the bars so their notes will hold data about what pitch the note actually plays. 
def generate_notes(bars, chord_root, chord_type, base_volume):
    note_generator = get_next_note_markov(markov_values, chord_root, chord_type)
    for bar in bars: 
        bar = generate_notes_for_bar(bar, chord_root, chord_type, note_generator, base_volume)
    notes = [y for x in bars for y in x['notes']]
    return notes
