import random, copy

def get_ending_of_block(timing_data):
    block_end = timing_data['starting_beats'][-1] + timing_data['number_of_bars'] * timing_data['bar_length']
    return block_end

def organize_blocks(blocks):
    total_blocks = []
    for block in blocks: 
        for i in range(block['block_data']['block_occurences']): 
            new_block = copy.deepcopy(block)
            total_blocks.append(new_block)

    random.shuffle(total_blocks)

    for b in range(1, len(total_blocks)): 
        block_t_data = total_blocks[b]['structure_data']['timing_data']
        last_block_t_data = total_blocks[b-1]['structure_data']['timing_data']
        new_starting_beats = [get_ending_of_block(last_block_t_data) + starting_beat for starting_beat in block_t_data['starting_beats']]

        total_blocks[b]['structure_data']['timing_data']['starting_beats'] = new_starting_beats

    return total_blocks    
