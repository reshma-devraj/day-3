# 3) Count Subarrays with Sum = K
def count_subarrays_sum_k(arr, k):
    mp = {0: 1}
    s = ans = 0
    for v in arr:
        s += v
        ans += mp.get(s - k, 0)
        mp[s] = mp.get(s, 0) + 1
    return ans
