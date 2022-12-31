# Write a program that takes as input a list of characters in an array and count the number of vowels in the array.

import array


def countVowels(arr):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in range(len(arr)):
        if arr[i] in vowels:
            count += 1
    return count


print(countVowels(array.array('u', ['k', 'a', 'r', 'a', 'c', 'h', 'i'])))
