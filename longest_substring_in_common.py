def main():
    strs = ["flower", "flow", "flight"]
    print(be_morelazy(strs))


def be_morelazy(strs: list):
    substrings_in_common_between_1_and_0 = {}
    slice_includes_0_and_1 = strs[:2]
    # Find all the substrings in common between the first two words
    for index, word in enumerate(slice_includes_0_and_1):
        if len(strs) != 1:
            # look if substrings of each of the first two words, are contained in both words
            if index == 0:
                check_index = 1
            else:
                check_index = 0
        else:
            # if there is only one string, then the longest substring in common is itself
            return strs[0]
        word_len = len(word)
        if word_len == 1:
            # if the length of a word is one, then it is the only possible substring of that word
            if word in slice_includes_0_and_1[check_index]:
                substrings_in_common_between_1_and_0[word] = word_len
        else:
            for end_index in range(word_len):
                if end_index == 0:
                    continue
                window = [0, end_index]
                displacement = 0
                while (displacement + (end_index - window[0])) < word_len:
                    start_i = window[0] + displacement
                    end_i = window[1] + displacement
                    moving_slice = word[start_i:end_i]
                    if moving_slice != "":
                        if moving_slice in slice_includes_0_and_1[check_index]:
                            substrings_in_common_between_1_and_0[moving_slice] = len(
                                moving_slice
                            )
                    displacement += 1
            # check if whole word is a common substring
            if word in slice_includes_0_and_1[check_index]:
                substrings_in_common_between_1_and_0[word] = word_len
    all_words_in_common = {}
    slice_from_2_to_end = strs[2:]
    # Now we check all the other words in the list
    if len(slice_from_2_to_end) > 0:
        for key, value in substrings_in_common_between_1_and_0.items():
            for word_j in slice_from_2_to_end:
                if key not in word_j:
                    continue
                else:
                    all_words_in_common[key] = value
        try:
            return max(all_words_in_common, key=all_words_in_common.get)
        except ValueError:
            # For case of no common substrings, the all_words_in_common dict is empty, and will not have a max
            return ""
    else:
        try:
            return max(all_words_in_common, key=all_words_in_common.get)
        except ValueError:
            if len(substrings_in_common_between_1_and_0) == 1:
                for key, _ in substrings_in_common_between_1_and_0.items():
                    return key
            else:
                return ""


if __name__ == "__main__":
    main()
