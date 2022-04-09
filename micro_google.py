#first you need to install google library.
#go to terminal & enter 'pip install google'.
import webbrowser
from googlesearch import search
print("----Welcome To Sharif's Google----\n".center(50))
print("Search:".center(50))
inp=input("".center(20))
print("\nWait Karo This Is Low budget Google...")
l1=list()
for j in search(inp,stop=5):
	
	l1.append(j)
print("\nChoose site to open:\n")
for i,k in enumerate(l1):
	i+=1
	print(f"{i}. {k}\n")
while True:
	try:
		inp2=int(input("Enter number: "))
		if inp2<1: continue
	except ValueError:
		print("Enter numbers only".center(50))
		continue
	break
webbrowser.open(l1[inp2-1])

