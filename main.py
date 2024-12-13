def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

def count_words():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        return len(words)

def char_count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lowered = file_contents.lower()
        char_count_dict = {}
        for char in lowered:
            if char in char_count_dict:
                char_count_dict[char] += 1
            elif char not in char_count_dict:
                char_count_dict[char] = 1
        return char_count_dict

def sort_on(dict):
    return dict["num"]

def book_report():
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words()} words found in the document\n")
    char_counts = char_count()
    char_list = [{"char": char, "num": count} for char, count in char_counts.items()]
    char_list.sort(reverse=True, key=sort_on)
    for entry in char_list:
        if entry["char"].isalpha():  # Access the character from the dictionary
            character = entry["char"]
            count = entry["num"]
            print(f"The '{character}' character was found {count} times")
    print("--- End report ---")

book_report()