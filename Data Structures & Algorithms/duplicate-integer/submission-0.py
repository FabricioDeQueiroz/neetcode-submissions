class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        itens = []

        for num in nums:
            if num in itens:
                return True
            else:
                itens.append(num)

        return False
