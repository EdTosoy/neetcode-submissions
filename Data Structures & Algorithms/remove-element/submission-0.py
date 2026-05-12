class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = []
        for n in nums:
            if n != val:
                ans.append(n) 
        nums[:] = ans       
        return len(ans)