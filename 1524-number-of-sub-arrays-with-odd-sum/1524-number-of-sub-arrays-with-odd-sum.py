class Solution(object):
    def numOfSubarrays(self, arr):
        mod = 10**9 + 7
        odd_count = 0
        even_count = 1
        current_sum = 0
        result = 0
        
        for num in arr:
            current_sum += num
            if current_sum % 2 == 0:
                result = (result + odd_count) % mod
                even_count += 1
            else:
                result = (result + even_count) % mod
                odd_count += 1
                
        return result