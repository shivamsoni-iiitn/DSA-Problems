# [Subsequences Start with Vowel and End with Consonant](https://www.geeksforgeeks.org/problems/string-subsequence-game5515/1)
## Medium
Given a string s, return all unique subsequences of s which start with a vowel and end with a consonant. The result must be returned in lexicographically sorted order. If there are no valid subsequences, return an empty list
A subsequence is a sequence that can be derived from the given string by deleting some or no characters without changing the order of the remaining characters. For example, "ac" is a subsequence of "abc".
Note: Vowels are 'a', 'e', 'i', 'o', 'u' and all other lowercase letters are consonants.
Examples:
Input: s = "abc"
Output: ["ab", "abc", "ac"]&nbsp;
Explanation:"ab", "abc" and "ac" are all possible unique subsequences which start with a vowel and end with a consonant.

Input: s = "aab"
Output: ["aab", "ab"]
Explanation: "aab" and "ab" are all possible unique subsequences which start with a vowel and end with a consonant.
Constraints:1&lt;= |s| &lt;=18s consists of only lowercase English letters