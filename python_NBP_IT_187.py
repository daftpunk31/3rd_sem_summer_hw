
'''
Holidays Homework IT, 3rd-Sem
Total-50 Problems
'''

'''
Code Owner: K.Surya Prakash
Roll no: 2451-21-737-187
Section: IT-C
'''


# 1st and 2nd Finding if number is even or odd
def even_odd(a):
	if a%2==0:
		#print("{} is an even number.\n".format(a))
		return True
	else:
		#print("{} is an odd number.\n".format(a))
		return False
#print(even_odd(23))



# 3rd Last digit of a number
def last_digit():
	a=int(input("Enter an integer.\n"))
	b=a%10
	print("The last digit of {} is {}.\n".format(a, b))
	return b
#print(last_digit())



# 4th Last second digit of a number
def second_last_digit():
	a=input("Enter an integer.\n")
	b=int(a)
	if len(a)>1:
		c=b%100
		c1=c//10
		print("The second last digit of {} is {}.\n".format(a, c1))
		return c1
#print(second_last_digit())



# 5th Last digit is zero or not
def last_digit_zero():
	a=int(input("Enter an integer to check if last digit is zero.\n"))
	b=a%10
	if b==0:
		print("Yes, the last digit of {} is 0.\n".format(a))
	else:
		print("No, the last digit of {} is {}.\n".format(a, b))
	return b
#print(last_digit_zero())



# 6th Sum of last two digits
def sum_last_two_digit():
	a=input("Enter an integer.\n")
	b=int(a)
	if len(a)>1:
		c=b%100
		c1=c//10
		c2=c%10
		print("The sum of last two digits of {} is {}.\n".format(a, c1+c2))
		return c1+c2
#print(sum_last_two_digit())



# 7th Counting zeros in a number
def count_zeros():
	a=input("Enter an integer.\n")
	count=0
	for i in a:
		i=int(i)
		if i==0:
			count+=1
	print("The number of zeros in {} are {}.\n".format(a, count))
	return count
#print(count_zeros())



#8th and 9th
#Checks how many numbers in a list are even or odd
#pass a list of int elements as parameter
def nums_even_odd(list1):
	#num_ele=int(input("Enter the number of elements being entered.\n"))
	num=0
	count_even=0
	count_odd=0
	#for i in range(num_ele):
		#num=input("Enter the element {}.\n".format(i+1))
		#list1.append(num)
	for n in str(list1):
		n=int(n)
		if n%2==0:
			count_even+=1
		else:
			count_odd+=1
	print("The number of even elements are {}.\n".format(count_even))
	print("The number of odd elements are {}.\n".format(count_odd))
	return count_even, count_odd
#print(nums_even_odd(12345))



# 10th
# Checks if alternate digits in a number are even or odd
def alternate_even_odd(a):
	#a=input("Enter an integer.\n")
	lista=list(str(a))
	even_list=[]
	odd_list=[]
	even_sum=0
	odd_sum=0
	num=0
	for i in range(0,len(lista),2):
		num=int(lista[i])
		if num%2==0:
			even_sum+=num
			even_list.append(lista[i])
		else:
			odd_sum+=num
			odd_list.append(lista[i])
	print("The sum of even numbers in {} is {}.\n".format(a, even_sum))
	print("The sum of odd numbers in {} is {}.\n".format(a, odd_sum))
	return even_sum, odd_sum
#print(alternate_even_odd(234567))



'''
11th Returns the number of unique elements in a number
for ex: if number is 12345, 5 is the answer
 but if number is 1234445, 4 is the answer
 because, all digits except "4" have only one instance
 i.e out of 7 elements, 4 are unique.
'''
def unique_digits(a):
    #a=input("Enter an integer.\n")
    unique_list=[]
    common_list=[]
    common_set=set({})
    count=0
    for i in str(a):
        if str(a).count(i)>1:
            common_set.add(i)
        else:
            unique_list.append(i)
    #print("The number of unique elements in {} is {}.\n".format(a, len(unique_list)))
    #print("The number of common elements in {} is {}.\n".format(a, len(common_set)))
    #if len(unique_list)!=0:
    return len(unique_list)
#print(unique_digits(1234445))



# 12th Sum of all digits in a number
def sum_digits(a):
	sum=0
	for i in str(a):
		sum+=int(i)
	print("Sum of digits in {} is {}.\n".format(a, sum))
	return sum
#print(sum_digits(123))



# 13th and 14th
#Sum of even and odd digits in a number
def sum_even_digits(a):
	even_sum=0
	odd_sum=0
	for i in str(a):
		if ((int(i))%2)==0:
			even_sum+=int(i)
		else:
			odd_sum+=int(i)
	print("Sum of even digits in {} is {}.\n".format(a, even_sum))
	print("Sum of odd_sum digits in {} is {}.\n".format(a, odd_sum))
	return even_sum, odd_sum
#print(sum_even_digits(120))

'''
15th Returns sum of even or odd digits in a number,
depending on user's choice. even_sum in 243 is 6
'''
def sum_even_digits_option(a, opt):
	even_sum=0
	odd_sum=0
	for i in str(a):
		if ((int(i))%2)==0:
			even_sum+=int(i)
		else:
			odd_sum+=int(i)
	if (opt=="even") or (opt=="Even"):
		print("Sum of even digits in {} is {}.\n".format(a, even_sum))

		return even_sum
	elif (opt=="odd") or (opt=="Odd"):
		print("Sum of odd_sum digits in {} is {}.\n".format(a, odd_sum))
		return odd_sum
	else:
		return "Wrong option"
#print(sum_even_digits_option(243,"even"))




#16th sum of powers of each adjacent digit in number
def sum_power_digits(a):
    b=list(str(a))
    sum_a=0
    next_num=""
    for i in b:
        if b.index(i)!=(len(b)-1):
            next_num=b[(b.index(i))+1]
            next_num=int(next_num)
            i=int(i)
            sum_a+=(i**next_num)
        else:
            sum_a+=1
    return sum_a
#print(sum_power_digits(12345))



'''
17th sum of digits of number in cyclic order
ex: 123
(1+2+3)+(2+3)+(3)=14
'''
def cyclic_order_sum(a):
    temp=a
    sum_a=0
    mul=0
    for i in str(a):
        sum_a+=int(i)
    while len(str(a))>1:
        mul=10**(len(str(a))-1)
        a=a%mul
        for x in str(a):
            x=int(x)
            sum_a+=x
    #print("Sum of digits of {} in cyclic manner is {}.\n".format(temp, sum_a))
    return sum_a
#print(cyclic_order_sum(123))



'''
18th Checks if given number is unique or not
returns list of common elements if not unique.
'''
def unique_digits2(a):
    #a=input("Enter an integer.\n")
    unique_list=[]
    common_list=[]
    common_set=set({})
    for i in str(a):
        if str(a).count(i)>1:
            common_set.add(i)
        else:
            unique_list.append(i)
    #print("The number of unique elements in {} is {}.\n".format(a, len(unique_list)))
    #print("The number of common elements in {} is {}.\n".format(a, len(common_list)))
    for j in common_set:
        common_list.append(j)
    if common_list==[]:
        #print("The number {} is a unique number.\n".format(a))
        return unique_list,"it is unique"
    else:
        #print("The number {} is a not unique number because {} are common elements.\n".format(a, common_list))
        #print("{} are common elements.\n".format(common_list))
        return common_list, "not unique"
#print(unique_digits2(127))


'''
same as unique digits but returns a list of 
all digits that appear more than once

useful in filtering out common digits from a list
'''
def common_digits(a):
    #a=input("Enter an integer.\n")
    unique_list=[]
    common_list=[]
    common_set=set({})
    for i in str(a):
        if str(a).count(i)>1:
            common_set.add(i)
        else:
            unique_list.append(i)
    #print("The number of unique elements in {} is {}.\n".format(a, len(unique_list)))
    #print("The number of common elements in {} is {}.\n".format(a, len(common_list)))
    for j in common_set:
        common_list.append(int(j))
    if common_list==[]:
        #print("The number {} is a unique number.\n".format(a))
        pass #unique_list
    else:
        #print("The number {} is a not unique number because {} are common elements.\n".format(a, common_list))
        #print("{} are common elements.\n".format(common_list))
        return common_list
#print(common_digits(1266213))



'''
19th Checks if a number is a Magic Number or not
Adding the digits of a number until the single digit.
If single digit==1 It is a Magic Number. Else, no.
'''
def magic_number(a):
    sqr_sum=0
    num=a
    ans=0
    if a==1:
        return "Magic Number"
    elif a!=1 and a<10:
        return "Black Magic Number"
    elif a>=10:
        ans=a
        while ans!=1 and len(str(ans))!=1:
            for i in str(num):
                sqr_sum+=int(i)
            num=sqr_sum
            ans=sqr_sum
            sqr_sum=0
    if ans==1:
        return "Magic Number"
    else:
        return "Black Magic Number"
#print(magic_number(12345))


# 20 Prime or not
def prime(a):
    factors=[]
    count=0
    for i in range(2,a):
        if a%i==0:
            factors.append(str(i))
            count+=1
        else:
            pass
    if (factors!=[]) and (count!=0):
        return False
    else:
        return True
#print(prime(7))



'''
21st are two given numbers co-prime?
out of all the factors of given two numbers
only "1" should be the common factor between both the numbers.
'''
# ex 13 and 15, 8 and 15
def co_prime(a,b):
	afactors=[]
	bfactors=[]
	onlyone=0
	for i in range(1,a+1):
		if a%i==0:
			afactors.append(str(i))
	for j in range(1,b+1):
		if b%j==0:
			bfactors.append(str(j))
	for k in afactors:
		if k in bfactors:
			onlyone+=1
		else:
			pass
	if onlyone>1:
		return "Not Co-Prime"
	else:
		return "Co-prime"
#print(co_prime(15,8))



'''
22nd Finds if given number is prime and
(given number+2 or given number-2) is also prime.
if either case is true, True is returned
ex: 41, 43
'''
def twin_prime(c): # To use this code prime() should be active
    d=c-2
    e=c+2
    prime_c=prime(c)
    prime_d=prime(d)
    prime_e=prime(e)
    if prime_c==True:
        if (prime_d==True):
            return c,d
        elif (prime_e==True):
            return c,e
        else:
            print("not twin prime")
    else:
        print(c,"is not prime")
#print(twin_prime(13))



# 23rd To find all primes in given range
# prints prime numbers including a and b
def prime_in_range(a, b):  # To use this code prime() should be active
	primes=[]
	for i in range(a,b+1):
		if prime(i)==True:
			primes.append(i)
	return primes, len(primes)
#print(prime_in_range(11,37))



'''
24th Twisted Prime or not
'''
#if a prime number and its reverse is also a prime number
def twisted_prime(a):
	b=str(a)[::-1]
	arev=int(b)
	if ((prime(a)==True) and (prime(arev)==True)):
		return True
	else:
		return False
#print(twisted_prime(13))



'''
25th Factorial of given number.
'''
def factorial(a):
	fact=1
	for i in range(1,a+1):
		fact*=i
	return fact
#print(factorial(5))



'''
26th 
Sum of factorial of each digit in a number
should be equal to the number itself
ex: 145 == 1!+4!+5!
'''
def special_number(a):
	fact_sum=0
	for i in str(a):
		fact_sum+=factorial(int(i))
	if a==fact_sum:
		return True
	else:
		return False
#print(special_number(145))



'''
27th Google it.
0=0,1=1,2=1,3=2,4=3,5=5 etc...
'''
def fibonacci(a):
	if a<0:
		return False
	elif a==0:
		return 0
	elif a==1 or a==2:
		return 1
	else:
		return (fibonacci(a-1)+fibonacci(a-2))
#print(fibonacci(1))



'''
28th Checks if number is a palindrome
# palindrome: Any number that has 0 at the end is not palindrome
'''
#import datetime
def palindrome(a):
    temp=a
    b=0
    sum_rev=0
    while (a!=0):
        b=a%10
        c=b*(10**(len(str(a))-1))
        sum_rev+=c
        a//=10
    if temp==sum_rev:
        return True
    else:
        return False
'''
t0 = datetime.datetime.now()
print(palindrome(101))
t1=datetime.datetime.now()
print("Elapsed time is", t1-t0)
'''

'''
# Simply considers the input as string and
gives the reverse of it.
'''
def palindrome_simple(a):
	rev_a=a[::-1]
	if rev_a==a:
		return True
	else:
		return False
#print(palindrome_simple("102201"))

'''
# Geeks for geeks logic
def palindrome_geeks(a):
	temp=a
	b=0
	rev=0
	while (a!=0):
		b=a%10
		rev=(rev*10)+b
		a//=10
	if temp==rev:
		return True
	else:
		return False
'''
'''
t3 = datetime.datetime.now()
print(palindrome_geeks(101))
t4=datetime.datetime.now()
print("Elapsed time is", t4-t3)
'''



'''
29th Checks if given number is palindrome possible
'''
def is_palindrome(a):
    odd_count_list=[]
    num_count={}
    for i in a:
        num_count[i]=a.count(i)
    for j in num_count:
        if num_count[j]%2==0:
            pass
        else:
            odd_count_list.append(j)
    if len(odd_count_list)==1 or odd_count_list==[]:
        return True
    else:
        return False        
#print(is_palindrome([4,4,5,5,2,2,2]))



# Function to convert integer to list of integers
def int_to_list(a):
	list_int=[]
	for i in str(a):
		i=int(i)
		list_int.append(i)
	return list_int



'''
This is pin generator code v1
total crap
but works...
'''
def pin_generator1(a,b,c):
	a,b,c=int_to_list(a),int_to_list(b),int_to_list(c)
	max_len=len(a)+len(b)+len(c)

	unit_list=[]
	tens_list=[]
	hundreds_list=[]
	max_list=[]
	min_list=[]
	pin_list=[]
	pin=""

	unit_list.append(a[-1])
	unit_list.append(b[-1])
	unit_list.append(c[-1])
	units_min=min(unit_list)
	units_max=max(unit_list)

	tens_list.append(a[-2])
	tens_list.append(b[-2])
	tens_list.append(c[-2])

	tens_min=min(tens_list)
	tens_max=max(tens_list)

	hundreds_list.append(a[-3])
	hundreds_list.append(b[-3])
	hundreds_list.append(c[-3])

	hundreds_min=min(hundreds_list)
	hundreds_max=max(hundreds_list)

	for i in range(3):
		min_list.append(units_min)
		min_list.append(tens_min)
		min_list.append(hundreds_min)
		max_list.append(units_max)
		max_list.append(tens_max)
		max_list.append(hundreds_max)

	pin_list.append(max(max_list))
	pin_list.append(min(hundreds_list))
	pin_list.append(min(tens_list))
	pin_list.append(min(unit_list))

	for j in pin_list:
		pin+=str(j)
	return int(pin)
#print(pin_generator1(123, 582, 175))


'''
Pin-generator v2
Better than v1 but still not efficient
'''
def pin_generator2(a,b,c):
	mainlist=[]
	a,b,c=int_to_list(a),int_to_list(b),int_to_list(c)
	mainlist.append(a)
	mainlist.append(b)
	mainlist.append(c)
	#We now have a main list that 
	#has all three numbers as sub-lists
	unit_list=[]
	ten_list=[]
	hundred_list=[]
	max_list=[]
	pin=""

	for i in range(3):
		if i==0:
			for j in mainlist:
				if len(j)==3:
					hundred_list.append(j[i])
				else:
					return "Not enough digits"
			max_list.append(max(hundred_list))
		elif i==1:
			for k in mainlist:
				if len(k)==3:
					ten_list.append(k[i])
				else:
					return "Not enough digits"
			max_list.append(max(ten_list))
		elif i==2:
			for l in mainlist:
				if len(l)==3:
					unit_list.append(l[i])
				else:
					return "Not enough digits"
			max_list.append(max(unit_list))
	pin=(str(max(max_list))+str(min(hundred_list))+str(min(ten_list))+str(min(unit_list)))
	return int(pin)
#print(pin_generator2(123, 582, 175))



'''
30th Pin Generator V3 Most efficient
Generates a pin using 3 user given numbers
'''
def pin_generator(a,b,c):
	import numpy as np
	mainlist=[]
	a,b,c=int_to_list(a),int_to_list(b),int_to_list(c)
	mainlist.append(a)
	mainlist.append(b)
	mainlist.append(c)
	pin=""
	arr=np.array(mainlist,ndmin=2)
	min_unit=min(arr[0:,2])
	min_ten=min(arr[0:,1])
	min_hun=min(arr[0:,0])
	max_num=0
	for i in arr:
		if max(i)>max_num:
			max_num=max(i)
	pin=str(max_num)+str(min_hun)+str(min_ten)+str(min_unit)
	return int(pin)
#print(pin_generator(472, 691, 358))



'''
31st Hill patter
For instructions check PDF
'''
def hill_patter(rows,val,adder):
	num=0
	a=val
	sums=val
	print(a,"\n")
	for i in range(2,rows+1):
		num=a+adder
		b=""
		for j in range(i):
			b+=str(num)
			b+="+"
		print(b[0:-1],"\n")
		sums+=(num*(i))
		a=num
	return sums
#print(hill_patter(4,1,5))



'''
32nd Swapping values of two variables
without thrid varibale
'''
def sub_one_var(a,b):
	a=a-b
	b=a+b
	a=b-a
	return a,b
#print(sub_one_var(12,24))



'''
33rd Prints fibonacci trianlge
'''
def fibonacci2(a):
	for i in range(1,a+1):
		for j in range(1,i+1):
			print(fibonacci(j),end=" ")
		print("\n")
#print(fibonacci2(4))


'''
34th Converts numbers to words
'''
def num_to_words(a):
	words=""
	word_dict={0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
	for i in str(a):
		i=int(i)
		char=word_dict[i]
		words+=char+" "
	words=words[0:-1]
	return words
#print(num_to_words(112345678))



'''
35th Finds one digit to be removed to make the 
number a palindrome possible
'''
def remove_to_palindrome(a):
    odd_count=set()
    for i in a:
        if a.count(i)%2==0:
            pass
        else:
            odd_count.add(i)
    odd_count=list(odd_count)
    if len(odd_count)==1 or odd_count==[]:
        pass
    else:
        for j in range(1,len(odd_count)):
            for k in a:
                if odd_count[j] in a:
                    a.remove(odd_count[j])
    return a
#print(remove_to_palindrome([1,3,2,1]))



'''
37th
returns the most frequently appeared digit
returns list of digits if they occur same number of times.
'''
def most_frequent_digit(a):
	lista=int_to_list(a)
	common_a=common_digits(a)
	max_count=0
	dicta={}
	sp_list=[]
	'''
	sp_list is used to store numbers that
	appear same number of times
	'''
	for i in common_a:
		dicta[i]=lista.count(i)
		if max_count<dicta[i]:
			max_count=dicta[i]
	if max_count!=0:
		for j in dicta:
			if dicta[j]==max_count:
				sp_list.append(j)
	if (len(sp_list)<=1) and (max_count!=0):
		return sp_list[0]
	elif (len(sp_list)>1) and (max_count!=0):
		return sp_list
	else:
		return a
#print(most_frequent_digit(23))



'''
38th Well, check out the pdf for conditions

Generate series and find next element
i/p:(1,3,6,17)
a,b,c,n
o/p:1 3 6 8 11 13 16 18 21 26 28 31 33 36 38 41 diff: 2 3 2 3......
'''
def generate_series(a,b,c,n):
	n=n-3
	gap_ab=b-a
	gap_bc=c-b
	num=0
	x=c
	diff=""
	series=str(a)+" "+str(b)+" "+str(c)+" "
	for i in range(1,n+1):
		if i%2!=0:
			num=x+gap_ab
			diff+=str(gap_ab)+" "
			series+=(str(num)+" ")
			x=num
		else:
			num=x+gap_bc
			diff+=str(gap_bc)+" "
			series+=(str(num)+" ")
			x=num
	return series
#print(generate_series(4,7,13,5))



'''
39th depending on the option selected by user
a number will be added or subtracted alternatively n
number of times
'''
def alternate_add_sub(n,op):
	num=n
	a=n
	if (op=="op1") or (op=="OP1"):
		for i in range(1,n+1):
			if i%2!=0:
				num-=(a-i)
			else:
				num+=(a-i)
	elif (op=="op2") or (op=="OP2"):
		for i in range(1,n+1):
			if i%2!=0:
				num+=(a-i)
			else:
				num-=(a-i)
	return num

#print(alternate_add_sub(6,"op2"))



'''
40th Checks if the numbers given are stable or unstable.
Generates password by adding all unstable numbers
'''
# Code for unstable or stable password starts here
def count_nums(a):
    #a=input("Enter an integer.\n")
    a=int_to_list(a)
    unique_list=[]
    common_list=[]
    common_dict={}
    for i in a:
        common_dict[i]=a.count(i)
    return common_dict
#print(count_nums(12277))

def same_count(a):
	b=count_nums(a)
	c=min(b)
	d=b[c]
	ans=True
	for i in b:
		if b[i]==d:
			pass
		else:
			ans=False
	return ans
#print(same_count(678))

def stable_unstable():
	#a,b,c,d=int_to_list(a),int_to_list(b),int_to_list(c),int_to_list(d)
	r=int(input("How many numbers?\n"))
	mainlist=[]
	x=0
	for i in range(r):
		print("Enter the element",i+1)
		x=int(input())
		mainlist.append(x)
	password=0
	for i in mainlist:
		if same_count(i)==True:
			pass
		else:
			password+=i
	return password
#print(stable_unstable())



'''
41st In all prime numbers in given range,
counts how many times the desired digit appears
'''
def count_prime_range(x,a,b):
	lista=prime_in_range(a,b)
	count_x=0
	for i in lista:
		i=str(i)
		if str(x) in i:
			count_x+=1
		else:
			pass
	return count_x
#print(count_prime_range(1,11,37))


# 42nd Python code to demonstrate combinations_with_replacement
'''
def two_primes_equal_given_num(a):
	a=int_to_list(a)
	import itertools as it
	return (list(it.permutations(a)))
print(two_primes_equal_given_num(12))

def two_primes_equal_given_num(a):
	import itertools as it
	int_a=a
	a=int_to_list(a)
	x,y="",""
	z=[]
	prime_combi=[]
	two_digit_prime_sum=[]
	for i in list(it.combinations(a, 2)):
		x,y="",""
		for j in i:
			x+=str(j)
		y=x[::-1]
		if prime(int(x))==True:
			prime_combi.append(int(x))
		if prime(int(y))==True:
			prime_combi.append(int(y))
	for k in prime_combi:
		for l in prime_combi:
			if k+l==int_a:
				z=[k,l]
				two_digit_prime_sum.append(z)
			z=[]
	return two_digit_prime_sum
print(two_primes_equal_given_num(71345))
'''




'''
code for 43rd problem starts here
'''
def factors(a):
	factors=[]
	for i in range(1,a+1):
		if a%i==0:
			factors.append(i)
		else:
			pass
	return factors
#print(factors(21))


'''
43rd Finds the sum of two numbers
if their products two numbers and
sum squares of those two numbers are given.
'''
def find_sum43(prod, sqr):
	factors_prod=factors(prod)
	sumij=0
	for i in factors_prod:
		for j in factors_prod:
			if (i*j==prod) and ((i**2)+(j**2)==sqr):
				sumij=i+j
	return sumij
#print(find_sum43(288, 720))



'''
44th Checks if the number is Happy number or not
'''
def happy_number(a):
    sqr_sum=0
    num=a
    ans=0
    if a==1:
        return "Happy Number"
    elif a==0 or a==2 or a==3:
        return "Sad Number"
    elif a<=9 and a!=1:
        num=a**2
        ans=num
        while ans!=1 and len(str(ans))!=1:
            for i in str(num):
                sqr_sum+=int(i)**2
            num=sqr_sum
            ans=sqr_sum
            sqr_sum=0
    elif a>9:
        ans=a
        while ans!=1 and len(str(ans))!=1:
            for i in str(num):
                sqr_sum+=int(i)**2
            num=sqr_sum
            ans=sqr_sum
            sqr_sum=0
    if ans==1:
        return "Happy Number"
    else:
        return "Sad Number"



'''
45th return a list of n happy numbers
'''
def n_happy_numbers(n):
	happy_num_list=[]
	x=1
	while len(happy_num_list)!=n:
		if happy_number(x)=="Happy Number":
			happy_num_list.append(x)
			x+=1
		else:
			x+=1
			pass
	return happy_num_list
#print(n_happy_numbers(20))



'''
46th finds how many times a specific number
appears in factorials of all numbers
of certain range.
'''
def num_count_factorial(a,b):
	counter=0
	x=0
	for i in range(1,b+1):
		x=factorial(i)
		x=str(x)
		if str(a) in x:
			counter+=x.count(str(a))
		else:
			pass
	return counter
#print(num_count_factorial(0,8))



'''
Finding how many factors a number has.
num_factors

factors2() ignores 1 and the number itself as factors.
But in factors() it doesn't, and changing factors()
could alter other codes relying on it.
'''
def factors2(a):
	factors=[]
	for i in range(2,a):
		if a%i==0:
			factors.append(i)
		else:
			pass
	return factors
#print(factors(21))

'''
47th Find all factors of a number
'''
def num_factors(a):
	return len(factors2(a)), factors2(a)
#print(num_factors(12))



'''
48th Abundant number:

Sum of its factors from 1 and not including itself,
should be greater than number itself
'''
def abundant(a):
	sum_a=1 # adding 1 since factors2() doesn't count 1 as factor...
	for i in factors2(a): # calling factors2()
		sum_a+=i
	if sum_a>a:
		return True
	else:
		return False
#print(abundant(72))



'''
49th Multiply two nums without "*" operator
'''
def mul(a,b):
	ans=0
	for i in range(1,b+1):
		ans+=a
	return ans
#print(mul(100,5))



'''
50th Convert float to ratio form
'''
def float_to_ratio2(a):
	from fractions import Fraction
	return (Fraction(a).limit_denominator())
#print(float_to_ratio2(4.2))


'''
#50th Other method: Under Construction
def float_to_ratio(a):
	a=str(a)
	dot_index=a.index(".")
	before_decimal=a[0:dot_index]
	after_decimal=a[dot_index+1:]
	numerator=before_decimal+after_decimal
	denominator=str(10**len(after_decimal))
	temp_numer=numerator
	temp_denom=denominator
	ratio1=numerator+"/"+denominator
	q,r=0,0
	num=0

	# creating a common factors list
	numer_factors=factors(int(numerator))
	denom_factors=factors(int(denominator))
	common_factors=set(numer_factors+denom_factors)
	common_factors=list(common_factors)

	for i in common_factors:
		if int(numerator)%i==0 and int(denominator)%i==0:
			q==int(numerator)//i
			r=int(denominator)//i
			num=i
		else:
			pass
	if num==0 or num==1 or num==int(denominator):
		return ratio1
	else:
		return str(q)+"/"+str(r)
print(float_to_ratio(4.20))
'''



'''
Remaining programs:
36) Add two nums using assembly code
42) How many 2 digit prime = the given number??
'''
