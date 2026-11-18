import time
import bisect
class Solution:
    def findTheDistanceValue(arr1: list[int], arr2: list[int], d: int) -> int:
        list.sort(arr2)
        print(arr2)
        cnt=0
        for i in arr1:
            p=bisect.bisect_left(arr2,i)
            print(f"p={p}")
            if p==len(arr2) or abs(i-arr2[p])>d:
                if p == 0 or abs(i - arr2[p - 1]) > d:
                    cnt += 1
        return cnt
if __name__=="__main__":
    tests=[([4,5,8],[10,9,1,8],2),([1,4,2,3],[-4,-3,6,10,20,30],3),([2,1,100,3], [-5,-2,10,-3,7],6)]
    for t in tests:
        start=time.perf_counter()
        print(Solution.findTheDistanceValue(t[0],t[1],t[2]), end="\t")
        end=time.perf_counter()
        elapsed=end-start
        print(f"Time: {elapsed:.6f}")
