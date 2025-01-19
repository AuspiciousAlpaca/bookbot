def main():
    book_path = "books/frankenstein.txt"
    content = get_book_text(book_path)
    word_count = get_word_count(content)
    all_characters = get_character_count(content)
    alphas = get_only_alphas(all_characters)
    character_list = dict_to_list(alphas)
    report = print_report(book_path, word_count, character_list)
    return report

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def get_word_count(content):
    words = content.split()
    return len(words)

def get_character_count(content):
    lowered = content.lower()
    characters = dict()
    for character in lowered:
        if character not in characters:
            characters[character] = 1
        else:
            characters[character] += 1
    return characters

def get_only_alphas(all_characters):
    only_alphas = dict()
    for key, value in all_characters.items():
        if key.isalpha():
            only_alphas[key] = value
    return only_alphas

def sort_on(dict):
    return dict["count"]

def dict_to_list(alphas):
    character_list = []
    for character, count in alphas.items():
        character_list.append({"character": character, "count": count})
    character_list.sort(key=sort_on, reverse=True)
    return character_list

def print_report(book_path, word_count, character_list):
    print(f"|--- Start of report for {book_path} ---|")
    print(f"Total word count: {word_count}\n")
    for dictionary in character_list:
        print(f"The character '{dictionary['character']}' was found {dictionary['count']} times\n")
    print("|--- End of report. Thanks for using Bookbot v0.1 ---|")



main()
