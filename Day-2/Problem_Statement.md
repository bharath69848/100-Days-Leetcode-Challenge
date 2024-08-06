<h1>Merge String Alternately</h1>
<p>You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.</p>

<h3>Example 1:</h3>
<p>
Input: word1 = "abc", word2 = "pqr"<br>
Output: "apbqcr"<br>
Explanation: The merged string will be merged as so:<br>
word1:  a   b   c<br>
word2:    p   q   r<br>
merged: a p b q c r
</p>

<h3>Example 2:</h3>
<p>
Input: word1 = "ab", word2 = "pqrs"<br>
Output: "apbqrs"<br>
Explanation: Notice that as word2 is longer, "rs" is appended to the end.<br>
word1:  a   b <br>
word2:    p   q   r  s<br>
merged: a p b q  r s
</p>

<h3>Example 3:</h3>
<p>
Input: word1 = "abcd", word2 = "pq"<br>
Output: "apbqcd"<br>
Explanation: Notice that as word1 is longer, "cd" is appended to the end.<br>
word1:  a   b   c   d<br>
word2:    p   q <br>
merged: a p b q c d
</p>

<h3>Constraints:</h3>
<p>1 <= word1.length, word2.length <= 100<br>
word1 and word2 consist of lowercase English letters.</p>
