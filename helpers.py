# function for preprocessing
def process_results(data):
    nested_values = ['video', 'author', 'music', 'stats', 'authorStats']
    skip_values = ['challenges', 'duetInfo', 'textExtra', 'stickersOnItem']

    # Create blank dictionary
    flattened_data = {}

    # loop through each video
    for idx, val in enumerate(data):
        flattened_data[idx] = {}
        #     loop through each value in each video
        for prop_idx, prop_value in val.items():
            #         check if nested
            if prop_idx in nested_values:
                if prop_idx in skip_values:
                    pass
                else:
                    #                 loop through each nested property
                    for nested_idx, nested_val in prop_value.items():
                        flattened_data[idx][prop_idx + '_' + nested_idx] = nested_val

                        #         if not nested, add to flattened dict
            else:
                flattened_data[idx][prop_idx] = prop_value

    return flattened_data