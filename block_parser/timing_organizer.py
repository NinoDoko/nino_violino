import datetime


#Gets a dictionary containing data on how to order notes. 
def get_timings(starting_beat = 0, bar_length = 4, number_of_bars = 4, pattern = [], accents = {}, base_volume = 50):
    bars = [{"start" : 0, "base_volume" : base_volume, "notes" : [{"start" : 0, "length" : 1}, {"start" : 1, "length" : 2}, {"start" : 2, "length" : 1}]}, {"start" : 3, "base_volume" : base_volume, "notes" : [{"start" : 0, "length" : 1}, {"start" : 1, "length" : 2}, {"start" : 2, "length" : 1}]}]
    bars = handle_timing(bars)
    bars = handle_accenting(bars, accents)
    return bars

def handle_timing(bars):
    for bar in bars: 
        for note in bar['notes']: 
            note['start'] += bar['start']
 
    return bars
   

#Gets the timed list of notes and increases the volume of the notes based on the accent_list
#Example, in a list with 6 notes, the accent_list {0 : 10, 2 : 20} will increase the 
def handle_accenting(bars, accents):
    for bar in bars: 
        for i in range(len(bar['notes'])): 
            note = bar['notes'][i]
            note['volume'] = bar['base_volume'] + accents.get(i, 0)

    return bars
