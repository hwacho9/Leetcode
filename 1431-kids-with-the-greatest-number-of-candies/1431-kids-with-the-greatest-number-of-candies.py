class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        for i in candies:
            ans.append(i + extraCandies >= max(candies))

        return ans
        