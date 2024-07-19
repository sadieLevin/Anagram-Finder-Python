from english import ENGLISH_WORDS

input_string = "beans"

def run(input):

    input_dict = deconstruct_string(input)
    identify_all_substrings(input_dict)

def deconstruct_string(input_string):
    output_dict = {}
    for character in input_string:
        if character in output_dict:
            output_dict[character] += 1
        else:
            output_dict.update({character:1})
    return output_dict

def identify_all_substrings(input_dict):
    finished = True
    for element in input_dict:
        if input_dict[element] > 0:
            finished = False
    if finished:
        print("finished early")
        return
    
    for test_word in ENGLISH_WORDS:
        working_input_dict = input_dict.copy()
        test_dict = deconstruct_string(test_word)
        is_valid_substring = True
        for test_letter in test_dict:
            try:
                if test_dict[test_letter] > input_dict[test_letter]:
                    is_valid_substring = False
                else:
                    working_input_dict[test_letter] -= 1
            except:
                is_valid_substring = False
                break
        if is_valid_substring:
            print(test_word)
            #identify_all_substrings()
    print("PROCESS FINISHED")


if __name__ == "__main__":
    run(input_string)