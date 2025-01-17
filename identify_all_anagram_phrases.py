from english import ENGLISH_WORDS

# Accepts only lowercase letters and spaces
def run(input):
    input_dict = deconstruct_string(input)
    all_possible_substrings = identify_possible_substrings(input_dict)
    identify_all_anagrams(input_dict, found_word_list = [], possible_word_list = all_possible_substrings)
    print("All done!")

# Takes all characters in string, turns them into 
def deconstruct_string(input_string):
    output_dict = {}
    for character in input_string:
        if character not in " ":
            if character in output_dict:
                output_dict[character] += 1
            else:
                output_dict.update({character:1})
    return output_dict

# Makes a subset of the english words dictionary to only include individual words that are anagrams of the input string.
# This cuts down on search time substantially
def identify_possible_substrings(input_dict):
    all_possible_substrings = []
    for test_word in ENGLISH_WORDS:
        working_input_dict_for_all_possible_substrings = input_dict.copy()
        test_dict = deconstruct_string(test_word)
        is_valid_substring = True
        for test_letter in test_dict:
            try:
                if test_dict[test_letter] > input_dict[test_letter]:
                    is_valid_substring = False
                else:
                    working_input_dict_for_all_possible_substrings[test_letter] -= 1
            except:
                is_valid_substring = False
                break
        if is_valid_substring:
            all_possible_substrings.append(test_word)
    return all_possible_substrings

def identify_all_anagrams(input_dict, found_word_list = [], possible_word_list = ENGLISH_WORDS):
    # Checks if base case found, returns None if input dict has no remaining letters
    finished = True
    for element in input_dict:
        if input_dict[element] > 0:
            finished = False
    if finished:
        output_string = ""
        for word in found_word_list:
            for letter in word:
                output_string += letter
            output_string += " "
        print(output_string.strip())
        return
    
    # Checks every english word to see if it could be constructed using input dict's characters
    for test_word in possible_word_list:
        working_input_dict = input_dict.copy()
        test_dict = deconstruct_string(test_word)
        is_valid_substring = True
        for test_letter in test_dict:
            try:
                if test_dict[test_letter] > input_dict[test_letter]:
                    is_valid_substring = False
                    break
                else:
                    working_input_dict[test_letter] -= test_dict[test_letter]
            except:
                is_valid_substring = False
                break

        # Passes any found words back into the function recursively, looking for new ones
        if is_valid_substring:
            temp_found_word_list = found_word_list.copy()
            temp_found_word_list.append(test_word)
            identify_all_anagrams(working_input_dict, temp_found_word_list, possible_word_list)


if __name__ == "__main__":
    run(input("Enter the word or phrase you would like all anagrams of!\n>>> ").lower())