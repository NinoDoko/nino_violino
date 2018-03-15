import datetime

def note_to_midi(note):
    print 'Converting ', note, ' to midi. '
    return note

def all_notes_to_midi(notes):
    notes = [note_to_midi(note) for note in notes]
    return notes

def write_notes_to_midi(notes):
    print 'Opening midi file for writing'
    notes = all_notes_to_midi(notes)
    print 'Now I have a bunch of notes ready to write!'
    return 'some_filename.mid'

def midi_to_wav(midi_file):
    print 'I will now use fluidsynth or something to convert it to wav. '
    wav_file = midi_file.split('.')[0] + '.wav'
    return wav_file
