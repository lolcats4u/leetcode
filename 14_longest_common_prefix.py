def main():
    str_list = ["c", "acc", "ccc"]

    prefix = longest_common_prefix(str_list)
    print(prefix)


def longest_common_prefix(strs: list):
    prefixes_total = []
    word_prefixes = []
    non_redundant_list = list(set(strs))
    if len(non_redundant_list) == 1:
        return strs[0]

    two_words = non_redundant_list[0:2]
    for index, word in enumerate(two_words):
        if index == 0:
            check_index = 1
        else:
            check_index = 0
        if word in two_words[check_index][0 : len(word)]:
            word_prefixes.append(word)
        if len(word) != 1:
            for index in range(len(word)):
                word_slice = word[:-index]
                if (
                    word_slice in two_words[check_index][0 : len(word_slice)]
                    and word_slice != ""
                    and word_slice not in word_prefixes
                ):
                    word_prefixes.append(word_slice)

    if len(non_redundant_list) == 2:
        all_but_two = two_words
    else:
        all_but_two = non_redundant_list[2:]
    for word in all_but_two:
        for prefix in word_prefixes:
            if prefix not in word[0 : len(prefix)]:
                if prefix in prefixes_total:
                    prefixes_total.remove(prefix)
                    continue
                else:
                    continue
            else:
                prefixes_total.append(prefix)
    try:
        return max(prefixes_total)
    except ValueError:
        return ""


if __name__ == "__main__":
    main()
