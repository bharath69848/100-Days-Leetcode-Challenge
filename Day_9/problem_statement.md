<h1>Two Sum</h1>
<p>Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].</p>

<p>Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.<br>
You may assume that each input would have exactly one solution, and you may not use the same element twice.<br>
You can return the answer in any order.</p>

<p>Each range [a,b] in the list should be output as:<br>
"a->b" if a != b<br>
"a" if a == b</p>

<h3>Example 1</h3>
<p>Input: nums = [2,7,11,15], target = 9<br>
Output: [0,1]<br>
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].</p>

<h3>Example 2</h3>
<p>Input: nums = [3,2,4], target = 6<br>
Output: [1,2]</p>

<h3>Example 3</h3>
<p>Input: nums = [3,3], target = 6<br>
Output: [0,1]</p>

<h3>Constraints:</h3>
<p>2 <= nums.length <= 104<br>
-109 <= nums[i] <= 109<br>
-109 <= target <= 109<br>
Only one valid answer exists.</p>
