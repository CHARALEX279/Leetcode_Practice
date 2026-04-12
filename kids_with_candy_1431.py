#first solution, beat 100% :)
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        boolean_list = []
        max_candy = max(candies)

        for kid in range(len(candies)):
            shared_candy = candies[kid] + extraCandies
            if shared_candy >= max_candy:
                boolean_list.append(True)
            else:
                boolean_list.append(False)

        return boolean_list
