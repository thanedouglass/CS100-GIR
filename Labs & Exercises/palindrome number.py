def solution(num):
    if num[::-1] == num:
        return "True", num, "is a palindrome"
    else: 
        return "Fale", num, "is not a palindrome"
    
num=(input("Give me a number, any number"))
result=solution(num)
print(result)
