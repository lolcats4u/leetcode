def main():
    strs = ["a"]
    print(be_morelazy(strs))


def be_morelazy(strs: list):
    substrings_in_common_between_1_and_0 = {}
    slice_includes_0_and_1 = strs[:2]
    for index, word in enumerate(slice_includes_0_and_1):
        if len(strs) != 1:
            if index == 0:
                check_index = 1
            else:
                check_index = 0
        else:
            substrings_in_common_between_1_and_0[strs[0]] = len(strs[0])
            break
        word_len = len(word)
        if word_len == 1:
            if word in slice_includes_0_and_1[check_index]:
                substrings_in_common_between_1_and_0[word] = word_len
        else:
            for end_index in range(word_len):
                if end_index == 0:
                    continue
                window = [0, end_index]
                displacement = 0
                while (displacement + end_index) != word_len - 1:
                    start_i = window[0] + displacement
                    end_i = window[1] + displacement
                    moving_slice = word[start_i:end_i]
                    if moving_slice != "":
                        if moving_slice in slice_includes_0_and_1[check_index]:
                            substrings_in_common_between_1_and_0[moving_slice] = len(
                                moving_slice
                            )
                    displacement += 1
            if word in slice_includes_0_and_1[check_index]:
                substrings_in_common_between_1_and_0[word] = word_len
    all_words_in_common = {}
    slice_from_2_to_end = strs[2:]
    if len(strs) != 1:
        for key, value in substrings_in_common_between_1_and_0.items():
            for word_j in slice_from_2_to_end:
                if key not in word_j:
                    continue
                else:
                    all_words_in_common[key] = value
        return max(all_words_in_common, key=all_words_in_common.get)
    else:
        all_words_in_common = substrings_in_common_between_1_and_0
        return all_words_in_common


if __name__ == "__main__":
    main()
