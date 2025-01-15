import itertools
# Function to load words from the Scrabble dictionary file
def loadscrabbledictionary(file_path):
#Load words from a Scrabble dictionary file and return them as a set."
    """Load words from a Scrabble dictionary file and return them as a set.
    file_path (str): The path to the Scrabble dictionary file.
    Returns:
    set: A set containing all words from the dictionary, converted to lowercase.
    """
    with open(file_path, 'r') as file:
        return set(word.strip().lower() for word in file)
# Function to generate valid words
def generatevalidwords(letters, dictionary):
#Generate valid words from the letters using the dictionary.
    """Generate valid words from the given letters from the dictionary.This function considers all permutations of the given letters to create possible
    words and checks them against a dictionary of valid Scrabble words.
    letters (str): A string of letters to form words from.
    dictionary (set): A set of valid Scrabble words.
    Returns:
    list: A sorted list of valid words that can be formed from the given letters.
    """
    valid_words = set()# Initialize an empty set to store valid words
    # Generate all permutations for lengths 1 to len(letters)
    for length in range(1, len(letters) + 1):
        """Loop through all possible word lengths:
        - Permutations are generated for lengths 1 to len(letters).
        - Each combination is joined into a single string.
        - If the string is a valid word, it is added to the valid words set."""
        for combination in itertools.permutations(letters, length):
            word = ''.join(combination) # Check if the word exists in the dictionary
            if word in dictionary:
                valid_words.add(word)# Add the word to the valid words set
    return sorted(valid_words) # Return the valid words as a sorted list
# Main function
def main():
    """Main function to load the Scrabble dictionary, generate valid words, and display the results.
    with the function, it Loads the Scrabble dictionary from a file, 
    accepts a set of letters to generate words from.
    generates valid words using the dictionary.
    displays the valid words and the total count."""
# Path to the Scrabble dictionary file
    dictionarypath = "Collins Scrabble Words (2019).txt"
    # Load the dictionary file
    try:
        """Load the dictionary file and handle errors if the file is not found.
        If the file is missing, the program will terminate with an error message."""
        dictionary = loadscrabbledictionary(dictionarypath)
    except FileNotFoundError:
        print(f"Error: Scrabble dictionary file not found.")
        return  
    # Define the letters to use
    letters = "tabind"
    print(f"Generating valid words from the letters: '{letters}'")
    # Generate valid words
    valid_words = generatevalidwords(letters, dictionary)
    # Print the results
    if valid_words:
        """If valid words are found:
        Print each valid word on a new line and display the total number of valid words found."""
        print("\nValid Scrabble Words:")
        for word in valid_words:
            print(word)
        print(f"\nTotal number of valid words: {len(valid_words)}") # Print the count
    else:
        print("No valid words found.")
# Run the program
if __name__ == "__main__":
    main()