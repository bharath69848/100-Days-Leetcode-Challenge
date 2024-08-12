<h1>Summary Ranges</h1>
<p>You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).</p>

<p>Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, <br>
  and there is no integer x such that x is in one of the ranges but not in nums.</p>

<p>Each range [a,b] in the list should be output as:<br>
"a->b" if a != b<br>
"a" if a == b</p>

<h3>Example 1</h3>
<p>Input: nums = [0,1,2,4,5,7]<br>
Output: ["0->2","4->5","7"]<br>
Explanation: The ranges are:<br>
[0,2] --> "0->2"<br>
[4,5] --> "4->5"<br>
[7,7] --> "7"</p>

<h3>Example 2</h3>
<p>Input: nums = [0,2,3,4,6,8,9]<br>
Output: ["0","2->4","6","8->9"]<br>
Explanation: The ranges are:<br>
[0,0] --> "0"<br>
[2,4] --> "2->4"<br>
[6,6] --> "6"<br>
[8,9] --> "8->9"</p>

<h3>Constraints:</h3>
<p>0 <= nums.length <= 20<br>
-231 <= nums[i] <= 231 - 1<br>
All the values of nums are unique.<br>
nums is sorted in ascending order.</p>
