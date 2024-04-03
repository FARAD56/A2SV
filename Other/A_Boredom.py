a = int(input())

nums = list(map(int,input().split()))

def rob(nums):
    n=len(nums)
        
    freq = [0] * (max(nums)+1) 
    for n in nums:
        freq[n] += n

 
    dp = [0] * (len(freq))
    dp[1] = freq[1]
 
    for i in range(2, len(freq)):
        dp[i]=max(dp[i-1],dp[i-2]+freq[i])

    return dp[len(freq)-1]

print(rob(nums))
