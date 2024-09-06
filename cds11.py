def calculate_weight(S):
    # Initialize the total weight
    total_weight = 0
    
    # Iterate over each character in the string and sum up the ASCII values
    for char in S:
        total_weight += ord(char)
    
    # Print the total weight
    print(total_weight)

# Sample Input
S = input().strip()

# Function call to calculate and print the weight
calculate_weight(S)



"""Given a string 'S' print the sum of weight of the String. A weight of character is defined as the ASCII value of corresponding character.

Input Description:
You are given a string ‘s’

Output Description:
Print weight

Sample Input :
abc

Sample Output :
294"""
