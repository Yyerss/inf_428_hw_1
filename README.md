# inf_428_hw_1
## Day 1
- Completed Task 1.
- Created a GitHub repository and ran the whole project.
- Solved the problems described below:
  - Loops: [Longest Continuous Increasing Subsequence](https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/)
  - Arrays: [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/description/)
  - Sets and Dictionaries: [Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/description/)
- Drew an explanation for each task.
- Wrote a `time_difference` function for Task 3 that calculates the difference between two given clocks, given the midnight transition.
- Wrote tests for the `time_difference` function:
  - `test_same_time`: Checks that the difference between the same clock is 0.
  - `test_midnight_crossing`: Checks if the difference when crossing midnight, such as between 23 and 1 o'clock, is correct.
  - `test_within_same_day`: Checks if the difference is correct when both clocks are within the same day.
  - `test_half_day_difference`: Checks if the difference is correct when the time differs by exactly 12 hours.
