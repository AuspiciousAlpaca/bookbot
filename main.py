from datetime import datetime


def main():
    file_path = "books/frankenstein.txt"
    content = get_text(file_path)
    word_count = get_word_count(content)
    alpha_characters = get_character_count(content)
    character_list = dict_to_list(alpha_characters)
    report = return_report(file_path, word_count, character_list)
    return report

# grabs the file's content as a string
def get_text(file_path):
    with open(file_path) as f:
        return f.read()

# splits the content into words and counts them
def get_word_count(content):
    words = content.split()
    return len(words)

# checks for alphabet characters in the content and adds them to a dictionary
def get_character_count(content):
    lowered = content.lower()
    characters = dict()
    for character in lowered:
        if character.isalpha():
            if character not in characters:
                characters[character] = 1
            else:
                characters[character] += 1
    return characters

# sorting logic
def sort_on(dict):
    return dict["count"]

# turning the dictionary into a list and sorting for highest count
def dict_to_list(alpha_characters):
    character_list = [{"character": character, "count": count} for character, count in alpha_characters.items()]
    character_list.sort(key=sort_on, reverse=True)
    return character_list

# formats and outputs the report as a text file
def return_report(file_path, word_count, character_list):
    with open("reports/report.txt", "w") as f:
                f.write(f"|--- Start of report for {file_path} created: {datetime.now().strftime("%d/%m/%Y, %H:%M:%S")} ---|\n")
                f.write(f"Total word count: {word_count}\n")
                for dictionary in character_list:
                    f.write(f"The character '{dictionary['character']}' was found {dictionary['count']} times\n")
                f.write("|--- End of report. Thanks for using Bookbot v0.1 ---|")

main()
