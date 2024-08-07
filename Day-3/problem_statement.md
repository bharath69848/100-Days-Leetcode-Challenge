<h1>Roman to Integer</h1>
<p>You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.</p>

<p>
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.<br>
<br>
Symbol       Value<br>
I             1<br>
V             5<br>
X             10<br>
L             50<br>
C             100<br>
D             500<br>
M             1000<br>
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.<br>
</p>

<p>
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
  The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
</p>

<p>
I can be placed before V (5) and X (10) to make 4 and 9. <br>
X can be placed before L (50) and C (100) to make 40 and 90. <br>
C can be placed before D (500) and M (1000) to make 400 and 900.<br>
</p>

<h3>Example 1</h3>
<p>Input: s = "III"<br>
Output: 3<br>
Explanation: III = 3.</p>

<h3>Example 2</h3>
<p>Input: s = "LVIII"<br>
Output: 58<br>
Explanation: L = 50, V= 5, III = 3.</p>
