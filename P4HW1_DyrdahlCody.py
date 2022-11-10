# CTI-110
# P4HW1 - Score List
# Cody Dyrdahl
# 11/10/22
#
# Get input for module test scores 1 through 6
# Create a list with scores
# Perform operations min, max, sum, and average on the list
# Display results
#
#create list
#declare variables
#get user input for how many scores
#create while loop for the scores
#create nested while loop with if else statement for invalid input
# calculate minimum, modified list, average
#if elif statement to determine letter grade
#print minimum, modified list, average, and letter grade
#
listscores = []
score_average = 'x'
module_scores = 0
num_scores = int(input("How many scores do you need to enter: "))
current_num_scores = 0
while(True):
  while(current_num_scores < num_scores):
    module_scores = float(input('Enter score #{}: '.format(current_num_scores+1)))
    while(True):
      if(module_scores < 0 or module_scores > 100):
        print('\nINVALID Score entered!!!!\nScore should be between 0 and 100')
        module_scores = float(input('Enter score #{} again: '.format(current_num_scores+1)))
      else:
        listscores.append(module_scores)
        break
    current_num_scores+=1
  if(current_num_scores == num_scores):
     break
minElement = min(listscores)
listscores.remove(min(listscores))
average = sum(listscores)/len(listscores)
if(average <= 100 and average >=90):
  score_average = 'A'
elif(average <= 89 and average >=80):
  score_average = 'B'
elif(average <= 79 and average >=70):
  score_average = 'C'
elif(average <= 69 and average >=60):
  score_average = 'D'
else:
  score_average = 'F'
print('---------------Results--------------')
print('Lowest Score:     ', minElement)
print('Modified List:    ', listscores)
print('Score Average:    ', average)
print('Grade:            ', score_average)
print('------------------------------------')
