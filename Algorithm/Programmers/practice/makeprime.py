def solution(nums):
    
    # Sieve of Eratos
    def prime_list(m: int, n: int, mode: int) -> list:
        sieve: list = [True for _ in range(n + 1)] 

        p: int = int(n ** 0.5)
        for i in range(2, p + 1):
            if sieve[i] == True:          
                for j in range(i + i, n + 1, i):
                    sieve[j] = False
                    
        # mode == 0 : return T/F Table in range
        if mode == 0:
            return sieve
        
        # mode == 1 : return var list in range
        elif mode == 1:
            if m == 1 : m = 2
            return [i for i in range(m, n + 1) if sieve[i] == True]
    
    prime_check: list = prime_list(2, 1000000, 0)

    answer: int = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if prime_check[nums[i] + nums[j] + nums[k]]:
                    answer += 1

    return answer