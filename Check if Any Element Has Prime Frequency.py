class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        def checkPrime(val):
            if val <= 1:
                return False
            for i in range(2, int(sqrt(val) + 1)):
                if val % i == 0:
                    return False
            return True

        for val in counter.values():
            prime = checkPrime(val)
            if prime:
                return True
        return False
