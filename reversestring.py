"""
557. Reverse Words in a String III
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

"""
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split(" ")[::-1])[::-1]

#Best Practice

class Solution:
    def reverseWords(self, s: str) -> str:
        output = []

        list = s.split()

        for x in list:
            rev = x[::-1]
            output.append(rev)

        return ' '.join(output)