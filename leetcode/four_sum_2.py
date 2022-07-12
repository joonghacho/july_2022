class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        answer = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                for k in range(len(nums3)):
                    for l in range(len(nums4)):
                        if nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0:
                            answer += 1
        return answer