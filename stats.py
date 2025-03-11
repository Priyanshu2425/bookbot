
def get_num_words(text):
    return len(text.split(" "))

def character_map_builder(text):
    map = {}
    for char in text:
        if map.get(char.lower(), None) is None:
            map[char.lower()] = 1
            continue
        map[char.lower()] += 1
    return map