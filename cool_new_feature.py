if __name__ == '__main__':
	num1 = input('Enter first number: ')
	num2 = input('Enter second number: ')
	sum = float(num1) + float(num2)
	print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
	num = float(input('Enter a number to find the square root: '))
	print('The square root of %0.3f is %0.3f'%(num ,num ** 0.5))
