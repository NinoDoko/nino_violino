import subprocess
from midiutil.MidiFile import MIDIFile
soundfont = '/home/ninodoko/moj_repos/nino_violino/block_generator/SGM-V2.01.sf2'

def write_mid_file(mid, file_name = 'test.mid'):
    with open(file_name, 'w+b') as f: 
        mid.writeFile(f)
    return file_name

def add_notes_to_midi(mid, notes):
    file_name = 'test.mid'
    for note in notes:
        mid.addNote(note['track'], note['channel'], note['pitch'], note['start'], note['length'], note['volume'])

    return mid

def add_program_change(mid, block, program):
    s_data = block['structure_data']['timing_data']
#    print 'Adding change for ', block['block_data'], ' with program ', program, ' at ', block['structure_data']['timing_data']['starting_beat']
    for starting_beat in s_data['starting_beats']: 
        mid.addProgramChange(block['block_data']['track'], block['block_data']['track'], starting_beat, program)
    return mid

def midi_to_wav(midi_file):
    print 'I will now use fluidsynth or something to convert it to wav. '
    wav_file = midi_file.split('.')[0] + '.wav'
    cmd = ['fluidsynth', '-F', wav_file, soundfont, midi_file]
    subprocess.call(cmd)
    return wav_file

def handle_midi_changes(mid, block):
    b_data = block['block_data']
    lower_blocks = b_data.get('blocks')

    if lower_blocks: 
        for b in lower_blocks: 
            mid = handle_midi_changes(mid, b)

    block_instrument = b_data.get('instrument', {}).get('program_number', 0)
    if b_data.get('track'):
        add_program_change(mid, block, block_instrument)
        if b_data.get('bpm'): 
            for starting_beat in block['structure_data']['timing_data']['starting_beats']:
                mid.addTempo(b_data['track'], starting_beat, b_data['bpm'])
    return mid
