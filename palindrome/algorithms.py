#version one was crashing on the negative function
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         string_num = str(x)
#         reversed = int(string_num[::-1])
#         if x == reversed:
#             return True
#         else:
#             return False


# myClass = Solution()
# print(myClass.isPalindrome(-121))

#Version 2 has a lot of variables so not so much effiecient
        
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        string_num = str(x)
        string_reversed = reversed(string_num)
        string_joined = "".join(string_reversed)
        reversed_num = int(string_joined)
        if reversed_num == x:
            return True
        else:
            return False
    
myClass = Solution()
print(myClass.isPalindrome(121))
print(myClass.isPalindrome(-121))

#version three try reducing the varaibles in version 
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reversed_num = int(''.join(reversed(str(x))))
        if reversed_num == x:
                return True
        else:
                return False
        

myClass = Solution()
print(myClass.isPalindrome(121))
print(myClass.isPalindrome(-121))