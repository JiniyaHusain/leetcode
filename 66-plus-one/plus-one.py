class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        for i in range(n-1,-1,-1):
            if digits[i]==9:
                if i!=0:
                    if digits[i-1]!=9:
                        digits[i-1]+=1
                        for j in range(i,n):
                            digits[j]=0
                        return digits
                else:
                    digits.insert(0,1)
                    for j in range(1,n+1):
                        digits[j]=0
                    return digits
            else:
                digits[i]+=1
                return digits
                
        