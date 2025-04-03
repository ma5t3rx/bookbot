def count_words(text):
    words = text.split()
    return len(words)
def count_characters(text):
    chars_dict = {}
    for char in text:
        char = char.lower()
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict
def sort_dict(chars_dict):
    def sort_on(tuple_item):
        return tuple_item[1]
    list_dict = list(chars_dict.items())
    list_dict.sort(reverse=True, key=sort_on)
    result = []
    for char, count in list_dict:
        result.append({"char": char, "count": count})
    return result
