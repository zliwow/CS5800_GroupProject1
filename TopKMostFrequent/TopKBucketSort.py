from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        print(freq)
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)
        print(freq)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            print(res)
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


solution = Solution()
print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(solution.topKFrequent([1], 1))
