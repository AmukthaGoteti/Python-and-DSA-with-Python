"""
    Problem Statement:
        Given a string text, you want to use the characters of text to 
        form as many instances of the word "balloon" as possible.
        You can use each character in text at most once. 
        Return the maximum number of instances that can be formed.
    
    Difficulty: Easy
    URL: https://leetcode.com/problems/maximum-number-of-balloons/description/?envType=daily-question&envId=2026-06-22
"""
from collections import Counter

text = input("Enter the text: ")

count = Counter(text)

max_balloons = min(
    count['b'],
    count['a'],
    count['l'] // 2,
    count['o'] // 2,
    count['n']
)

print(f"Maximum number of instances of 'balloon' that can be formed: {max_balloons}")