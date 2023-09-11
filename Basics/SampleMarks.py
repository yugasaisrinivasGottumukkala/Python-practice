import random
ID = 1
while (ID <= 5):
	MarksList = []
	for i in range(1,7):
		marks = random.randint(20,100)
		MarksList.append(marks)
	print(MarksList)
	ID+=1