def resolver(guess, solution):
    response = []
    letters = set(solution)
    occurrences = {}

    for letter in solution:
        occurrences[letter] = occurrences.get(letter, 0) + 1

    for index in range(5):
        if guess[index] == solution[index]:
            response += "g"
            occurrences[guess[index]] -= 1
        else:
            response += "b"

    for index in range(5):
        if response[index] != "g" and guess[index] in letters:
            if occurrences[guess[index]] > 0:
                response[index] = "y"
                occurrences[guess[index]] -= 1

    return "".join(response)