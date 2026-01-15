# 6.4 Wordle Helper-Part One

## Objective:
In this assignment, you'll develop a program to assist with Wordle puzzles. The program will take a user's guessed word and the scoring results to help narrow down potential solutions from a word bank.

## Simple Wordle Helper 
### Instructions
1. **Import Word Bank:**
    - The New York Times' word bank is provided to you. 
2. **User Input for the Guess:**
    - Write a function *get_guess()* that prompts the user to input their guessed word. Ensure that the input is exactly 5 letters long, contains only alphabetic characters and can be found in the wordbank. If the input is invalid, prompt the user again until they provide a valid guess.
3. **User Input for the Scoring:**
    - Write a function *get_score()* that prompts the user to input the score for their guess. The score should be a 5-character string containing only the characters "G", "Y", and "X".
    - Validate the input to ensure it matches the required format. If the input is invalid, prompt the user again.
4. **Writing Helper Functions to Filter the Word Bank:**
    - Write the following four helper functions to filter the wordbank:

        - *contains_letter(wordbank, letter)*:

            This function should return a list of words from the wordbank that contain the specified letter anywhere in the word.
        
        - *letter_at_position(wordbank, letter, index)*:

            This function should return a list of words from the wordbank where the specified letter is at the exact index.
        - *letter_not_at_position(wordbank, letter, index)*:

            This function should return a list of words from the word_bank where the specified letter is not at the given index.
        - *does_not_contain_letter(wordbank, letter, guess, score)*:
            
            Returns words that do not contain letter, only when allowed by Wordle rules.

            Rules for this function:

            - If the letter appears anywhere in the guess with a "G" or "Y" score, the letter exists in the word.

                - In this case, an "X" or "Y" means “not in this position” → do not remove the letter entirely

            - If all occurrences of the letter in the guess are scored "X":

                - The letter does not appear in the word

                - Remove all words containing the letter

            - If removal is not allowed, return the word bank unchanged
    - These helper functions will be essential for filtering the wordbank based on the user’s input.

5. **Filtering the Word Bank:**

    - Write a function *filter_wordbank(wordbank, guess, score)* that takes the wordbank, the user's guess, and the score as inputs.
    - This function should use the helper functions above to return a new list of words from the word_bank that match the given score criteria:
        - If the score is "G", use letter_at_position() to filter words where the corresponding letter is in the exact position.
        - If the score is "Y", use both contains_letter() and letter_not_at_position() to filter words where the letter is present but not in the specified position.
        - If the score is "X", use does_not_contain_letter() to filter out words that contain the corresponding letter.
6. **Testing the Program:**
    - Test your program by running it multiple times with different guesses and scores. After each round, print out the filtered list of potential words from the word_bank.

7. **Looping for Six Rounds**:
    - Modify your program to loop for six rounds, allowing the user to guess and score multiple times. After each round, update the wordbank with the filtered list of words.

8. **Displaying Remaining Words:**
    - After each guess, display the remaining possible words in the wordbank. If only one word remains, inform the user that the word has been found.
9. **Ending the Program:**
    - The program should end either when the user finds the correct word (when only one word remains) or when the user decides to quit.
