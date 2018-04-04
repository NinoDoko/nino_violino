import block_organizer, copy
from block_parser import block_parser, note_generator, chord_handler, instrument_handler

from violino_conf import configuration as gen_conf
import random, copy

block_template = {
    "block_data" : {
        "blocks" : [],
    },
    "structure_data" : {
        "notes_data" : {
        },
        "timing_data" : {
        },
    }
}

percussion_block = {
    'block_data' : {
        'track' : 9,
        'channel' : 9,
        'blocks' : [
            {'block_data' : {}, 'structure_data' : {'notes_data' : {}, 'timing_data' : {}}}, 
        ]
    },
    'structure_data' : {
        'notes_data' : {
            'chord_root' : 'C1',
            'chord_type' : 'percussion',
        },
        'timing_data' : {}
    }
}


block_template = gen_conf.get('block_template') or block_template


def get_block_bpm(block):
    if random.random() < gen_conf.get('bpm_change_chance', 0): 
        if not gen_conf.get('bpm_range'): 
            raise Exception('bpm_change_chance is set in conf, but bpm_range is set. If you want the BPM to change randomly, enable bpm_change_chance to the chance that each block will change the BPM, such as 0.15 for 15%, and set bpm_range to a range of values that it will choose from, such as range(250, 500, 50)')
        new_bpm = random.choice(gen_conf['bpm_range'])
    else: 
        new_bpm = block['block_data']['bpm']

    return new_bpm


def get_last_timing(base_block):
    if not base_block['block_data']['blocks']: 
        last_timing = {
            'starting_beats' : [0], 
            'number_of_bars' : 0,
            'bar_length' : 0
        }
    else:
        last_timing = base_block['block_data']['blocks'][-1]['structure_data']['timing_data']

    return last_timing

def block_chord_generator(number_of_bars):
    base_root = random.choice(chord_handler.base_notes)

    #Right now we just randomly choose from the configuration. Maybe have an AI to do this for us? 
    chord_choices = gen_conf.get('chord_choices', ['major', 'minor'])
    base_chord = random.choice(chord_choices)
    low_limit = gen_conf.get('lower_chord_diff_limit', 0)
    upper_limit = gen_conf.get('upper_chord_diff_limit', 10)

    chord_progression = chord_handler.make_chord_progression(base_root = base_root, base_chord = base_chord, number_of_chords = number_of_bars, chord_choices = chord_choices, lower_chord_diff_limit = low_limit, upper_chord_diff_limit = upper_limit)


    for i in range(number_of_bars):
        chord = chord_progression[i]
        notes_data = {
            'chord_root' : chord[0] + '3',
            'chord_type' : chord[1],
        }
        yield notes_data

def base_block_timing(number_of_bars, bar_length, base_volume, accents, base_block, number_of_repeats):

    timing_data = {
                'starting_beats' : [i * number_of_bars * bar_length for i in range(number_of_repeats)],
                'bar_length' : bar_length, 
                'number_of_bars' : number_of_bars,
                'base_volume' : base_volume,
                'accents' : accents
    }
    print 'I have a timing data of ', timing_data
    return timing_data

def generate_block(base_block, instrument_pool):
    new_block = copy.deepcopy(block_template)

    #Right now we just randomly choose from the configuration. Maybe have an AI to do this for us? 
    number_of_bars = random.choice(gen_conf.get('bar_number_range', range(4, 7)))
    bar_length = random.choice(gen_conf.get('bar_len_range', range(4, 7)))
    base_volume = random.choice(gen_conf.get('base_volume_range', range(40, 80, 10)))
    number_of_repeats = random.choice(gen_conf.get('number_of_repeats_range', [1]))
    number_block_occurences = random.choice(gen_conf.get('number_block_occurences_range', [1]))

    accents = {} #Temporary, don't even know how to make this work. 
    chord_generator = block_chord_generator(number_of_bars)

    new_block['block_data']['bpm'] = get_block_bpm(base_block)
    new_block['block_data']['block_occurences'] = number_block_occurences
    new_block['structure_data']['timing_data'] = base_block_timing(number_of_bars, bar_length, base_volume, accents, base_block, number_of_repeats)

    for i in range(number_of_bars): 
        instrument = random.choice(instrument_pool)
        instrument = instrument_handler.get_instrument_data(instrument)

        #Channel 10 is reserved for percussions, so we shift all channels to the right. 
        #And to make it more confusing, channe 10 is in musical notations, so because it's 0-indexed here, really we want to have channel = 9 for percussions. 

        if i > 8: 
            i += 1

        block_instrument = {
            'block_data' : {
                'instrument' : instrument,
                'track' : i+1
            }, 
            'structure_data' : {
                'timing_data' : {},
                'notes_data' : next(chord_generator),
            }
        }
        new_block['block_data']['blocks'].append(block_instrument)

    return new_block

def get_percussion():
    number_of_percussion_tracks = gen_conf.get('percussion_tracks', 2)
    percussion = copy.deepcopy(percussion_block)
    percussion['block_data']['blocks'] *= number_of_percussion_tracks
    print 'Percusion bock has blocks ', percussion['block_data']['blocks']

    return percussion

def generate_song():
    number_of_blocks = gen_conf.get('number_of_blocks', 1)
    base_block = copy.deepcopy(block_template)
    base_block['block_data']['bpm'] = random.choice(gen_conf.get('bpm_range', [240]))

    max_number_of_instruments = gen_conf.get('bar_number_range', range(4, 7))[-1]
    instrument_pool = [random.choice(gen_conf.get('instrument_pool', instrument_handler.get_list_of_instruments())) for i in range(max_number_of_instruments)]

    for block in range(number_of_blocks):
        new_block = generate_block(base_block, instrument_pool)
        percussion = get_percussion()
        new_block['block_data']['blocks'].append(percussion)
        base_block['block_data']['blocks'].append(new_block)

    base_block['block_data']['blocks'] = block_organizer.organize_blocks(base_block['block_data']['blocks'])

    block_parser.make_block_music(base_block)

    return base_block


generate_song()
