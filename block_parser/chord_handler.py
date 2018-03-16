base_notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
notes_list = [x + y for y in  [str(i) for i in range(0, 9)] for x in base_notes]

pitch_offset = 24

def get_pitch(note):
    return notes_list.index(note) + pitch_offset


chords_diffs = {
    'major' : [0, 2, 4, 5, 7, 9, 11, 12],
    'minor' : [0, 2, 3, 5, 7, 8, 10, 12],
    'acoustic' : [0, 2, 4, 6, 7, 9, 10],
    'algerian' : [0, 2, 3, 6, 7, 8, 11, 12, 14, 15, 17],
    'altered' : [0, 1, 3, 4, 6, 8, 10],
    'augmented' : [0, 3, 4, 7, 8, 11],
    'bebop' : [0, 2, 4, 5, 7, 9, 10, 11],
    'blues' : [0, 3, 5, 6, 7, 10],
    'chromatic' : [0, 1, 2, 3, 4, 5,6, 7, 8, 9, 10, 11],
    'double_harmonic' : [0, 1, 4, 5, 7, 8, 11],
    'enigmatic' : [0, 1, 5, 6, 8, 9, 11],
    'flamenco' : [0, 1, 4, 5, 7, 8, 11],
    'gypsy' : [0, 2, 3, 6, 7, 8, 10],
    'half_iminished' : [0, 2, 3, 5, 6, 8, 10],
    'harmonic_major' : [0, 2, 4, 5, 7, 8, 11],
    'harmonic_minor' : [0, 2, 3, 5, 7, 8, 11],
    'hijaroshi' : [0, 4, 6, 7, 11],
    'hungarian_minor' : [0, 2, 3, 6, 7, 8, 11],
    'insen' : [0, 1, 5, 7, 10],
    'iwato' : [0, 1, 5, 6, 10],
    'locrian' : [0, 1, 3, 5, 6, 8, 10],
}


def get_note_from_offset(note_offset, chord_root, chord_type):
    chord_root_index = notes_list.index(chord_root)
    chord_diffs = chords_diffs[chord_type]

    chord_notes = [notes_list[chord_root_index + x] for x in chord_diffs]
    print chord_notes
    note = chord_notes[note_offset]
    return note
