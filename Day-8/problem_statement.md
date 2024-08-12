<h1>Product of Array Except Self</h1>
<p>Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].</p>

<p>The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.<br>
You must write an algorithm that runs in O(n) time and without using the division operation.</p>

<p>Each range [a,b] in the list should be output as:<br>
"a->b" if a != b<br>
"a" if a == b</p>

<h3>Example 1</h3>
<p>Input: nums = [1,2,3,4]<br>
Output: [24,12,8,6]</p>

<h3>Example 2</h3>
<p>Input: nums = [-1,1,0,-3,3]<br>
Output: [0,0,9,0,0]</p>

<h3>Constraints:</h3>
<p>2 <= nums.length <= 105<br>
-30 <= nums[i] <= 30<br>
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.</p>
