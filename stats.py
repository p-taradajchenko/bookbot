def get_num_words(text):
    return len(text.split())

def get_chars_dict(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(item):
    return item["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    list = []
    for char in num_chars_dict:
        list.append({"char": char, "num": num_chars_dict[char]})
        list.sort(key=sort_on, reverse=True)
    return list