"""
Daily Coding Problem: #7 (Medium) - Facebook
Date: 07/09/2023

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable.
"""


# Algorith Used: Dynamic Programming, Bottom-Up
# Time Complexity: O(n)
# Space Complexity: O(n)
def decode_dp(message: str) -> int:
    # Initialize the number of decodings
    # Each element in the array represents the number of decodings for the substring
    # from the beginning of the message to the current index
    num_decodings = [0] * (len(message) + 1)

    # There is always only one way to decode the first character
    num_decodings[0] = 1

    # Iterate through the message from the second character to the end since
    # the first character has already been decoded with only one way
    for i in range(1, len(message) + 1):
        # If the current character is not 0, add the number of decodings
        # of the previous character to the current character
        if message[i - 1] != '0':
            num_decodings[i] += num_decodings[i - 1]
        # If the current character is not the first character and the previous character
        # and the current character are less than 27, add the number of decoding.
        # This signifies a two-digit number.
        if i != 1 and message[i - 2] != '0' and int(message[i - 2:i]) < 27:
            num_decodings[i] += 1

    # Return the last element in the array that represents the number of decodings.
    # If the last character is 0, return the second to the last element in the array.
    # This is because there is no way to decode a 0.
    for i in range(len(message) - 1, -1, -1):
        if message[i] != '0':
            return num_decodings[-(len(message) - i)]

    # If the message is all 0s, return 0
    return num_decodings[-1]


# Algorith Used: Greedy
# Time Complexity: O(n)
# Space Complexity: O(1)
def decode_greedy(message: str) -> int:
     # Initialize the number of decodings
    num_decodings = 0

    # Iterate through the message
    for i in range(len(message)):
        # If the current character is 0, skip it
        if message[i] == '0':
            continue

        # If the current character is not 0, add the number of decodings
        if message[i] != '0':
            num_decodings += 1

        # If the current character is not the last character and the current character and the next character are
        # less than 27, add the number of decodings
        if i != len(message) - 1 and int(message[i:i + 2]) < 27:
            i += 1

    # Return the number of decodings
    return num_decodings


if __name__ == '__main__':
    message = '111'
    assert decode_dp(message) == 3
    assert decode_greedy(message) == 3

    message = '12'
    assert decode_dp(message) == 2
    assert decode_greedy(message) == 2

    message = '226'
    assert decode_dp(message) == 3
    assert decode_greedy(message) == 3

    message = '0'
    assert decode_dp(message) == 0
    assert decode_greedy(message) == 0

    message = '10'
    assert decode_dp(message) == 1
    assert decode_greedy(message) == 1

    message = '120'
    assert decode_dp(message) == 2
    assert decode_greedy(message) == 2

    message = '1111'
    assert decode_dp(message) == 4
    assert decode_greedy(message) == 4

    print('Passed all tests!')
