def calc_sum(n):
    if(n==0):
        return 0
    return n+calc_sum(n-1)
    
result=calc_sum(5)
print(result)