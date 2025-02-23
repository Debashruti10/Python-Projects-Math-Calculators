number_of_sentences = 0
number_of_words = 0
number_of_paragraphs = 0
frequency_of_characters = {}
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Initialize frequency dictionary
for letter in alphabet:
    frequency_of_characters[letter] = 0

with open("text.txt", "r") as txt_file:
    content = txt_file.read()
    
    # Count paragraphs
    paragraphs = content.split('\n\n')
    number_of_paragraphs = len(paragraphs)
    
    # Count sentences, words, and character frequencies
    for paragraph in paragraphs:
        lines = paragraph.split('\n')
        for line in lines:
            number_of_sentences += line.count('.') + line.count('!') + line.count('?')
            words = line.split()
            number_of_words += len(words)
            
            for word in words:
                for c in word:
                    #c = c.lower()
                    if c in alphabet:
                        frequency_of_characters[c] += 1

# Find the most frequent letter
most_common_letter = max(frequency_of_characters, key=frequency_of_characters.get)
most_common_letter_count = frequency_of_characters[most_common_letter]

print(f"letters: {frequency_of_characters}")
print(f"Number of sentences in the text file is: {number_of_sentences}")
print(f"Number of words in the text file is: {number_of_words}")
print(f"Number of paragraphs in the text file is: {number_of_paragraphs}")
print(f"Most common letter: '{most_common_letter}' with {most_common_letter_count} occurrences")
