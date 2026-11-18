import time
class Solution:
    def digitSum(s: str, k: int) -> str:
        while len(s)>k:
            tmp=[]
            n = len(s)
            for i in range(0, n, k):
                val = 0
                for j in range(i, min(i + k, n)):
                    val += int(s[j])
                tmp.append(str(val))
            s = "".join(tmp)
        return s
if __name__=="__main__":
    tests=[("11111222223",3),("00000000",3)]
    for t in tests:
        start=time.perf_counter()
        print(Solution.digitSum(*t), end="\t")
        end=time.perf_counter()
        elapsed=end-start
        print(f"Time: {elapsed:.6f}")
