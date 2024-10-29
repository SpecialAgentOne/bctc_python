# This program reads the content of the file which typed by user
# and count the number of characters, words, and lines in a file.

# Getting user input
user_input = input('Please enter file name with extension: ')

# Reading file according to the file name from user
fileread = open(user_input, 'r')

# Initial setup for variables
chars_count = 0
words_count = 0
lines_count = 0

# Loop to run through the file and calculate
for line in fileread:
    # Lines readed by basic python behaviour, where the pointer set in the beginning of the file
    # and run to the end of the line, and where new line "\n" found, it jump down to the new line
    lines_count += 1
    # Count chars amount by len() behavour, return the number of characters in the line include spaces
    # and "\n" and other special characters
    chars_count += len(line)
    # Count words by splitting, it split words as list of words
    words = line.split()
    # Sum of words
    words_count += len(words)

print('File analysis:')
print('Characters in file: ', chars_count)
print('Words in file: ', words_count)
print('Lines in file', lines_count)

fileread.close()