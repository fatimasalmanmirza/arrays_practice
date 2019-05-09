def is_palindrome(num):
  
  if str(num)[::-1] == str(num):
    
    return True
  return False



print(is_palindrome(121))
print(is_palindrome(-121))
print(is_palindrome(10))