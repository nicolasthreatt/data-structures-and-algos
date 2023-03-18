"""
Cracking the Coding Interview: 1.9

String Rotation:
    - Assume you have a method isSubstring which checks if one word is a substring of another
    - Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one
      call to isSubstring (e.g., "waterbottle" is a rotation of "erbottlewat")
"""


# Algorithm Used: List Slicing
# Time Complexity: O(n)
# Memory Complexity: O(n)
def isSubstring(s1: str, s2: str) -> str:
    if len(s1) != len(s2):
        return False

    listS1 = list(s1)
    listS2 = list(s2)

    numRotations = 0
    while numRotations < len(listS1):
        if listS1 == listS2:
            return numRotations
        
        tail = listS1[-1]

        listS1[1:] = listS1[:len(listS1) - 1]
        listS1[0] = tail

        numRotations += 1
        
    return numRotations


print(isSubstring("waterbottle", "erbottlewat"))
