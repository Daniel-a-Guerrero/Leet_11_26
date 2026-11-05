import time
class Solution:
    def generate(n:int)->list[list[int]]:
        result=[]
        prevRow=[]
        for i in range(n):
            currentRow=[1]*(i+1)
            for j in range(1,i):
                currentRow[j]=prevRow[j-1]+prevRow[j]
            result.append(currentRow)
            prevRow=currentRow
        return result
if __name__=="__main__":
    tests=[5,1,3]
    for t in tests:
        start=time.perf_counter()
        print(Solution.generate(t), end="\t")
        end=time.perf_counter()
        elapsed=end-start
        print(f"Time: {elapsed:.6f}")
