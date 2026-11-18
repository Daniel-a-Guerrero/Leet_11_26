import time
import bisect
class Solution:
    def searchInsert(nums: list[int], target: int) -> int:
        return bisect.bisect_left(nums,target)
if __name__=="__main__":
    tests=[([1,3,5,6],5),([1,3,5,6],2),([1,3,5,6],7)]
    for t in tests:
        start=time.perf_counter()
        print(Solution.searchInsert(t[0],t[1]), end="\t")
        end=time.perf_counter()
        elapsed=end-start
        print(f"Time: {elapsed:.6f}")
