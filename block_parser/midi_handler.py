from midiutil.MidiFile import MIDIFile

def write_mid_file(mid, file_name = 'test.mid'):
    with open(file_name, 'w+b') as f: 
        mid.writeFile(f)

def write_notes_to_midi(notes):
    print 'Opening midi file for writing'
    mid = MIDIFile(100)
    file_name = 'test.mid'
    for note in notes:
        mid.addNote(0, 0, note['pitch'], note['start'], note['length'], note['volume'])
#        mid.addNote(track = 0, channel = 0, pitch = 120, self.track, self.channel, self.pitch, self.time, self.duration, self.volume)

    write_mid_file(mid, file_name = file_name)
    return file_name

def midi_to_wav(midi_file):
    print 'I will now use fluidsynth or something to convert it to wav. '
    wav_file = midi_file.split('.')[0] + '.wav'
    return wav_file
