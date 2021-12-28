class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        mid = len(candies)//2
        min_candy = len(set(candies))

        return min(mid, min_candy)