def IS_Prime():
	flag=0
	num=int(input("Enter Number: "))
	sum=num/2
	for i in range(2,int(sum)+1):	
		if num%i==0:
			print("False,Not prime")
			flag=1
			break
		
	if flag==0:
		print("True,Prime number")
def main():
	(IS_Prime())

if __name__=="__main__":
	main()
