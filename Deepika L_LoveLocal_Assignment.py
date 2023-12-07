#!/usr/bin/env python
# coding: utf-8

# ## Easy 1
# ### Given a string s consisting of words and spaces, return the length of the last word in the string.
# ### A word is a maximal 
# ### substring consisting of non-space characters only.
#  
# ## Example 1:
# ### Input: s = "Hello World"
# ### Output: 5
# ### Explanation: The last word is "World" with length 5.
# ### Example 2:
# ### Input: s = "   fly me   to   the moon  "
# ### Output: 4
# ### Explanation: The last word is "moon" with length 4.

# In[7]:


def len_lastword(s):
    words = s.split()

    if len(words) == 0:
        return 0

    return len(words[-1])

s1 = input()
print(len_lastword(s1))  

s2 = input()
print(len_lastword(s2))  

s3 = input()
print(len_lastword(s3)) 


# ## Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
#  
# ## Example 1:
# ### Input: nums = [3,2,3]
# ### Output: [3]
# ## Example 2:
# ### Input: nums = [1]
# ### Output: [1]
# ## Example 3:
# ### Input: nums = [1,2]
# ### Output: [1,2]

# In[5]:


from collections import Counter

def majority_elements(nums):
    if not nums:
        return []

    n = len(nums)
    threshold = n // 3

    counts = Counter(nums)

    result = [num for num, count in counts.items() if count > threshold]

    return result

num1 = [3, 2, 3]
print(majority_elements(num1))  

num2 = [1]
print(majority_elements(num2)) 

num3 = [1, 2]
print(majority_elements(num3))  


# ## Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.
# ## Example 1:
# ### Input: n = 13
# ### Output: 6
# ## Example 2:
# ## Input: n = 0
# ### Output: 0

# In[1]:


def cou_digit(n):
    count = 0
    factor = 1

    while factor <= n:
        div = factor * 10
        count += (n // div) * factor + min(max(n % div - factor + 1, 0), factor)
        factor *= 10

    return count

# Example usage:
n1 = int(input())
print(cou_digit(n1))  

n2 = int(input())
print(cou_digit(n2)) 


# In[ ]:




