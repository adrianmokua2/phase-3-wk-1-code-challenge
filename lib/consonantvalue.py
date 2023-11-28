#!/usr/bin/env python3
def highest_value(characterString):
    # This dictionary assigns numeric values to each letter of the alphabet
    alphabetNumbers = {'a': 0, 'b': 2, 'c': 3, 'd': 4, 'e': 0,
                        'f': 6, 'g': 7, 'h': 8, 'i': 0, 'j': 10,
                        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 0,
                        'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
                        'u': 0, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
                        
    # Initializing two counters to help track values
    constantValue = 0
    maxConstant = 0

    # Iterating through each letter in the input string
    for character in characterString:
        # Checking if the letter isn't a vowel (a, e, i, o, u)...
        if character not in "aeiou":
            # ...adding the assigned value to the counter
            constantValue += alphabetNumbers[character]
        else:
            # If a vowel is found, checking if the current value is the highest so far,
         #updating it if needed, and then resetting the counter for the next round
            maxConstant = max(maxConstant, constantValue)
            constantValue = 0
            
   # Displaying the highest value found for consonant substrings
    print(f"The highest value of consonant substrings is: {maxConstant}")
    return maxConstant



# Finding the highest value of consonant substrings in the provided string
highest_value("zazz")