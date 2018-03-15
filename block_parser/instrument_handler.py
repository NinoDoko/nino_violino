import json

def get_all_instrument_data(instruments_file = 'instruments.json'):
    with open(instruments_file) as f:
        instruments = json.load(f)
    return instruments

def get_instrument_data(instrument_name):
    instruments = get_all_instrument_data()
    instrument = [x for x in instruments if x['instrument_name'] == instrument_name]
    if not instrument: 
        raise Exception("Instrument " + str(instrument_name) + " not found in json. All instrument names are : " + str([x['instrument_name'] for x in instruments]))

    return instrument[0]


def add_instrument_data_to_notes(notes, instrument_name):
    instrument = get_instrument_data(instrument_name)

    for note in notes:
        note['program_number'] = instrument['program_number']
        note['volume'] *= instrument['volume']

    return notes
