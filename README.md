## Love-Local-Assignment
# Algorithm for Easy1

Step1- Defining the function len_lastword(s):
Step2- Input->string "s"
Step3- Splitting the string "s"into a list of words using the split() method, which separates the string based on spaces.
Step4- If the length of the list of words is 0, it means there are no words in the string. In this case, the function returns 0.
Step5- Otherwise, it returns the length of the last word in the list, accessed using words[-1].
Step6- Taking input and printing the length of the last word:
Step7- Prompt the user to input a string (s1) using input().
Step8- Call the len_lastword function with the input string (s1).
Step9- Print the result, which is the length of the last word in the input string.

# Algorithm for Medium2
The function aims to find majority elements in a list, where a majority element is defined as an element that appears more than n // 3 times (where n is the length of the list). The results for the three test cases are then printed.

Step1- Defining the function majority_elements(nums):
Step2- If the input list nums is empty, return an empty list.
Step3- Next,get the length of the list nums and calculate the threshold as n // 3, where n is the length of nums. This threshold is used to determine if an element is a majority element.
Step4- Use the Counter class to count the occurrences of each element in the list nums.
Step5- Create a list result containing elements from nums where the count of that element is greater than the calculated threshold.
Step6- Return the result list.
Step7- Test the function with three different input lists (num1, num2, and num3):
   Eg.,num1 = [3, 2, 3]: Calls the majority_elements function with num1 and print the result.

# Algorithm for Hard3

Step1- Defining the function cou_digit(n):
Step2- Initialize count to 0, which will be used to store the total count of digits.
Step3- Initialize factor to 1, which represents the current place value.
Step4- Enter a while loop that continues until factor is greater than n.
Inside the loop:
Calculate div as factor * 10.
Update count based on the number of occurrences of the current digit at the current place value.
Update factor by multiplying it by 10.
Step5- Prompt the user to input an integer (n1).
Step6- Call the cou_digit function with the input integer (n1) and print the result.
Step7- Repeat the process for another integer (n2).
