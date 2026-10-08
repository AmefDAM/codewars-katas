def permute_a_palindrome(input):
    odd_characters = 0

    for char in set(input):
        quantity = input.count(char)

        if quantity % 2 != 0:
            odd_characters += 1

    return odd_characters <= 1