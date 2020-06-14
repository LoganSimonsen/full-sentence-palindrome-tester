"""
Try testing with an input that has commas and capital letters, like "A man, a plan, a canal, Panama"

"""
#!/usr/bin/env python3
import re
n = str(input("Please enter a word or sentence: ")).lower()
n = re.sub(r'\W+', '', n)

if(n == n[::-1]):
    print(n, "==", n[::-1], ": is a palindrome")
else:
    print(n, "!=", n[::-1], ": is not palindrome")
