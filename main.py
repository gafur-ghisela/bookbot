from collections import Counter

def count_words(text):
    words = text.split()  
    return len(words)     

def count_characters(text):
    text = text.lower()  
    character_counts = Counter(text)  
    return character_counts

def generate_report(file_path, word_count, character_counts):
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")

    for char, count in character_counts.most_common():
        if char.isalpha():  
            print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

try:
    file_path = "books/frankenstein.txt"
    with open(file_path, "r") as file:
        content = file.read()  

        word_count = count_words(content)
        character_counts = count_characters(content)
        
        generate_report(file_path, word_count, character_counts)
        
except FileNotFoundError:
    print("The file 'frankenstein.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

