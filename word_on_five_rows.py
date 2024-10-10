def print_reverse_diagonal():
    word = input("Enter a word: ")
    grid_size = int(input("Enter a number: "))

    word_length = len(word)
    
    # Ensure the word fits within the grid size
    if word_length > grid_size:
        print("Error: Word length is greater than the grid size.")
        return

    # Iterate through rows
    for i in range(grid_size):
        for j in range(grid_size):
            # Print the word on the reverse diagonal (top-right to bottom-left)
            if j == grid_size - 1 - i:
                print(word, end=" ")
            else:
                print("-", end=" ")
        print()  # Move to the next line after each row

print_reverse_diagonal()
