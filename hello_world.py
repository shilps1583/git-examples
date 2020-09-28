from datetime import datetime

if __name__ == '__main__':
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	print('hello world. The current time is:', current_time)
