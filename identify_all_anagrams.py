from english import ENGLISH_WORDS

#accepts only lowercase letters and spaces
input_string = "bananas"

def run(input):
    input_dict = deconstruct_string(input)
    identify_all_substrings(input_dict)
    print("All done!")

#takes all characters in string, turns them into 
def deconstruct_string(input_string):
    output_dict = {}
    for character in input_string:
        if character not in " ":
            if character in output_dict:
                output_dict[character] += 1
            else:
                output_dict.update({character:1})
    return output_dict


def identify_all_substrings(input_dict, found_word_list = []):

    #checks if base case found, returns None if input dict has no remaining letters
    finished = True
    for element in input_dict:
        if input_dict[element] > 0:
            finished = False
    if finished:
        print(found_word_list)
        return
    
    #checks every english word to see if it could be constructed using input dict's characters
    for test_word in ENGLISH_WORDS:
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

        #passes any found words back into the function recursively, looking for new ones
        if is_valid_substring:
            temp_found_word_list = found_word_list.copy()
            temp_found_word_list.append(test_word)
            identify_all_substrings(working_input_dict, temp_found_word_list)



if __name__ == "__main__":
    run(input_string)