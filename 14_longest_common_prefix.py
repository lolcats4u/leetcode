def main():
    str_list = ["a"]
    prefix = longest_common_prefix(str_list)
    print(prefix)


def longest_common_prefix(strs: list):
    prefixes_total = []
    word_prefixes = []

    for word in strs:
        word_prefixes.append(word)
        for end_index in range(len(word)):
            if end_index == 0:
                continue
            else:
                word_slice = word[0:end_index]
                word_prefixes.append(word_slice)
        prefixes_total.append(word_prefixes)
        word_prefixes = []

    prefixes_in_common = {}
    for word_i in prefixes_total:
        for prefix in word_i:
            common_prefix = True
            for word_j in strs:
                if prefix not in word_j:
                    common_prefix = False
            if common_prefix:
                prefixes_in_common[prefix] = len(prefix)
            else:
                common_prefix = True
                continue
    return max(prefixes_in_common, key=prefixes_in_common.get)


if __name__ == "__main__":
    main()
