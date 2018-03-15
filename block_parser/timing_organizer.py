import datetime


#Gets a dictionary containing data on how to order notes. 
def get_timings(starting_beat = 0, bar_length = 4, number_of_bars = 4, pattern = [], accent_list = {}, base_volume = 50):
    bars = [{"start" : 0, "base_volume" : base_volume, "notes" : [{"start" : 0, "length" : 1}, {"start" : 1, "length" : 2}, ]}, {"start" : 3, "base_volume" : base_volume, "notes" : [{"start" : 0, "length" : 1}, {"start" : 1, "length" : 2}, ]}]
    bars = handle_accenting(bars, accent_list)
    return bars

#Gets the timed list of notes and increases the volume of the notes based on the accent_list
#Example, in a list with 6 notes, the accent_list {0 : 10, 2 : 20} will increase the 
def handle_accenting(bars, accent_list):
    for bar in bars: 
        for accent in accent_list: 
            bar['notes'][accent] += accent_list[accent]
    return bars
