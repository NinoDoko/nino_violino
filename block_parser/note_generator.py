import datetime


#This is the hard part, we have to find a value for every note in the bar using AI or markov chains or stuff. 
def generate_notes_for_bar(bar, chord_root, chord_type):
    for note in bar['notes']: 
        note['value'] = 'A' #TODO hardest part probably


#We update all the bars so their notes will hold data about what pitch the note actually plays. 
def generate_notes(bars, chord_root, chord_type):
    for bar in bars: 
        bar = generate_notes_for_bar(bar, chord_root, chord_type)
    notes = [y for x in bars for y in x['notes']]
    return notes
