import chord_handler, instrument_handler, note_generator, timing_organizer


#The block_parser uses all the other modules in order to process a batch of blocks. Blocks hold the following sort of data: 

{
    "block_data" : {
        "bpm" : 120,
        "instrument" : "piano",
        "blocks" : []
    }
    "structure_data" : {
        "notes_data" : {
            "chord_root" : "A",
            "chord_type" : "major",
        },
        "timing_data" : {
            "starting_beat" : 12, 
            "bar_length" : 4, 
            "number_of_bars" : 4,
            "pattern" : [0, 1, 3],
            "accents" : {0 : 20, 2 : 10},
            "base_volume" : 50,
        },
    }
}

#TODO finish writing up what should be stored in this data. 

#Blocks can hold other blocks, which inherit any data from parent blocks which they don't define. For instance: 

{
    "block_data" : {
        "id" : "main",
        "bpm" : 120, 
        "instrument" : "piano",
        "blocks" : [
            "block_data" : {
                "instrument" : "trumpet", 
                "id" : "chorus",
            },
            "structure_data" : {
                'data' : '...'
            }
        ]
    }
}


def parse_block(block):

    #Returns a list of dicts, depicting bars with data about where the bar starts, and data about each note, like so: [{"start" : 0, "notes" : []}, {"start" : 3, "notes" : []}]
    #Each note has a start, length and volume; start and length are based on the bar pattern, volume is based on the accents
    bars = timing_organizer.get_timings(**block['structure_data']['timing_data'])

    #For each element of the timings, we put a note there. 
    #This should update the existing timings with values for the specific notes: {"start" : 0, "end" : 2, "volume" : 60, "value" : "A"}
    notes = note_generator.generate_notes(bars = bars, **block['structure_data']['notes_data'])

    #Then we update the notes with the instruments, which may modify the volume (for instance, trumpet may be loud, so it should have a multiplier, like {"insturment" : "trumpet", "volume" : 0.5, "program_number" : 123}, not the actual program_number tho.
    notes = instrument_handler.add_instrument_data(notes = notes, instrument_name = block['block_data']['instrument'])

    #We finally have a list of notes in dictionary form with all the data needed to convert them to midi. 
    midi_file = midi_handler.write_notes_to_midi(notes)

    #midi_file should just be a filename. We want to make it into a wav. 
    wav_file = midi_handler.midi_to_wav(midi_file)
    
    #And done!
    return wav_file
