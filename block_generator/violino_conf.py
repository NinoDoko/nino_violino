import os
conf_path = os.getcwd()

print conf_path
configuration = {
#    'soundfont' : conf_path + '/misc/SGM-V2.01.sf2',
    'soundfont' : conf_path + '/misc/32MbGMStereo.sf2',

    'song_path' : conf_path + '/misc/generated_songs/',

    'bpm_change_chance' : 0.3, 
    'bpm_change_limit' : 2,
    'bpm_range' : range(150, 550, 25), 


    'no_bars_initial' : 5,
    'occurence_multiplier' : 60,

    'number_of_blocks_range' : [3,8], 
    'number_of_repeats_range' : range(1, 5),
    'max_note_len_range' : range(2, 5),

    'base_chords_choices' : ['major', 'minor'],
    'lower_chord_diff_limit' : 1, 
    'upper_chord_diff_limit' : 2,
    'chord_types' : ['major', 'minor'], 
    'instrument_pool_range' : range(2, 9),

    'base_volume' : 10,
#    'instrument_pool' : ['piano'],

}
