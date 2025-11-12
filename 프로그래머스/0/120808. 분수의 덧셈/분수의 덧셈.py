def solution(numer1, denom1, numer2, denom2):
    denom3 = denom1 * denom2 
    numer3 = (numer1 * denom2) + (numer2 * denom1) 
    
    for i in range(1,min(numer3, denom3)+1):
        if (numer3%i==0)&(denom3%i==0):
            div = i
    return [numer3/div,denom3/div]            
    