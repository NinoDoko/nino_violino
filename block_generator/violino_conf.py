import os
conf_path = os.getcwd()

print conf_path
configuration = {
    'soundfont' : conf_path + '/misc/SGM-V2.01.sf2',
    'song_path' : conf_path + '/misc/generated_songs/',

    'bpm_change_chance' : 0.15, 
    'bpm_range' : range(300, 700, 50), 

    'number_of_blocks' : 5, 
    'bar_number_range' : range(2, 8),
    'bar_len_range' : range(3, 12),
    'number_of_repeats_range' : range(2, 5),
    'number_block_occurences_range' : range(1, 5),
    'max_note_len_range' : range(2, 5),

    'base_chords_choices' : ['major', 'minor'],
    'lower_chord_diff_limit' : 1, 
    'upper_chord_diff_limit' : 2,
    'chord_types' : ['major', 'minor'], 
    'instrument_pool_range' : range(3, 7),

    'base_volume' : 10,
#    'instrument_pool' : ['piano'],

}
