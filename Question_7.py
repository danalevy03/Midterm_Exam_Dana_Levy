import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
# continue here

#Continue by removing the numbers greater than 50 from the list and replacing the other numbers with "XX"

for i in range(len(random_numbers)): #iterating through the list
    if random_numbers[i] > 50: #checking if the number is greater than 50
        random_numbers[i] = "XX" #replacing the number with "XX"
    else: #if the number is not greater than 50
        random_numbers[i] = random_numbers[i] #keeping the number as it is

print(random_numbers) #printing the list


