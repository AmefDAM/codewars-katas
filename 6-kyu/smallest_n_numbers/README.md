# N smallest elements in original order

**Codewars:** [6 kyu — N smallest elements in original order](https://www.codewars.com/kata/5aec1ed7de4c7f3517000079/)
<br>
**Solution Language:** Python

## Description

Your task is to write a function that does just what the title suggests (so, fair warning, be aware that you are not getting out of it just throwing a lame basic sorting method there) with a list of integers and the expected number n of smallest elements to return.

Also:

the number of elements to be returned cannot be higher than the list length;
elements can be duplicated;
in case of duplicates, just return them according to the original order (see third example for more clarity).
Same examples and more in the test cases:

Array	N	Expected
[1, 2, 3, 4, 5]	3	[1, 2, 3]
[5, 4, 3, 2, 1]	3	[3, 2, 1]
[1, 2, 3, 4, 1]	3	[1, 2, 1]
[1, 2, 3, -4, 0]	3	[1, -4, 0]
[1, 2, 3, 4, 5]	0	[]

## Solution

[smallest_n_numbers.py](./smallest_n_numbers.py)