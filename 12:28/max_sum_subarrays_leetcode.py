class Solution:
    def max_sum_of_one_subarray(self, sub_nums, len):
        max_sum = 0
        current_sum = 0
        for i in range(len(len)):
            current_sum += sub_nums[i]
        for i in range(len(sub_nums)-len(len)):
            prev_sum = current_sum
            current_sum -= sub_nums[i]
            current_sum += sub_nums[i+len(len)]



    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        