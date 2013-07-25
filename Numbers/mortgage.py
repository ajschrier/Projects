apr=input("What is the APR of the loan?")
termlength=input("What is the length of the loan (in years)?")
loanamount=input("What is the amount of the loan?")

n=termlength/12
c=apr/12

# def payment(l,c,n):
# 	return (l * (c(1+c)^n) / ((1-c)^n - 1))
# 	
# print payment(int(loanamount), c, n)


print c
