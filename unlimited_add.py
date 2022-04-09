elements=[]

while True:
	try:
		limit=int(input('Enter how many numbers you want to add: '))
	except ValueError:
		print("Invalid input, Enter numbers only\n")
		continue
	break
	
count=1

for j in range(limit):
		while True:
			try:
				if count==1:
					print("Enter", count,"st number: ")
				elif count==2:
					print("Enter", count,"nd number:")
				elif count==3:
					print("Enter", count,"rd number:")
				else:
					print("Enter", count, "th number:")
				in1=int(input())
				count+=1
			except ValueError:
				print("Invalid input\n")
				continue
			break
		elements.append(in1)
		
num_sum=0

for k in range(0,len(elements)):
	num_sum=num_sum+elements[k]
print("Result=",num_sum)