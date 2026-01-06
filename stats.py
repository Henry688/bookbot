def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
        print(content)

def get_book_words_count(filepath):
    with open(filepath) as f:
        content = f.read()
        content_length = len(content.split())
        return f"Found {content_length} total words"

def count_unique_characters(filepath):
    list_characters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ",".",",","-","!","?"]
    dict_characters = {}
    for character in list_characters:
        dict_characters[character] = 0
    with open(filepath) as f:
        content_lower = f.read().lower()
        for i in content_lower:
            for character in dict_characters:
                if character == i:
                    dict_characters[character] += 1
                    break
    return dict_characters

def sort_dict(filepath):
    orig_dict = count_unique_characters(filepath)
    list_orig_dict = []

    for character in orig_dict:
        list_orig_dict.append({"character": character, "count": orig_dict[character]})
    #print(list_orig_dict)

    def sort_on(list_orig_dict):
        return list_orig_dict["count"]

    list_orig_dict.sort(reverse = True, key = sort_on)
    #print(list_orig_dict)

    return list_orig_dict