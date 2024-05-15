def main():
    num = 123125648941536189767489436515869843
    num_1 = -12344321
    num = 5
    print(isPalindrome(num))


def isPalindrome(num: int) -> bool:
    if num < 0:
        return False
    if 0 <= num < 10:
        return True

    num_list = [int(x) for x in str(num)]
    len_of_num = len(num_list)

    half_length = len_of_num // 2

    left_half = num_list[0:half_length]
    right_half = num_list[(-1 * half_length) :]
    right_half.reverse()

    if left_half == right_half:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
