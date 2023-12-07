# process data, for each map, our data is a list of tuples (destination_range_start, source_range_start, range_length)

named_map = {
    'seed-to-soil map:': 'seed2soil',
    'soil-to-fertilizer map:': 'soil2fertilizer',
    'fertilizer-to-water map:': 'fertilizer2water',
    'water-to-light map:': 'water2light',
    'light-to-temperature map:': 'light2temperature',
    'temperature-to-humidity map:': 'temperature2humidity',
    'humidity-to-location map:': 'humidity2location'
}

data = {}

with open('input_full.txt') as f:
    # read the seeds
    line = f.readline()
    seeds = [int(seed) for seed in line.split(":")[1].strip().split(" ")]


    # read the data for each map
    current_name = None
    d = None
    start = False
    while True:
        line = f.readline()
        if line == '\n':
            if start:
                data[current_name] = d
                start = False
        elif line == '':
            break
        else:
            line = line.strip()
            if line in named_map:
                start = True
                current_name = named_map[line]
                d = []
            else:
                if start:
                    nums = [int(num) for num in line.split(' ')]
                    d.append(nums)   
    # append the last d
    if start:
        data[current_name] = d



# now process the maps
def map_one_seed(seed, d):
    """
    Parameters:
        seed: seed to be mapped
        d: is a list of tuple (destination_range_start, source_range_start, range_length)
    Return:
        the mapped seed
    """
    for dest, src, length in d:
        if seed >= src and seed < src + length:
            return dest + seed - src
    return seed

def map_seeds(seeds, d):
    """
    Parameters:
        seeds: a list of seeds to be mapped
        d: is a list of tuple (destination_range_start, source_range_start, range_length)
    Return:
        the mapped seeds
    """
    return [map_one_seed(seed, d) for seed in seeds]

# iterate through each seed and map
mapped = seeds

for _, d in data.items():
    mapped = map_seeds(mapped, d)



print(min(mapped))

