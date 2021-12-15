def is_leap (year):
	if year % 4 != 0 :
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	elif year % 3200!= 0:
		return True
	else:
		return False
y = int(input ('請輸入西元年：'))
if is_leap (y) == True:
	print( y ,'年是閏年')
else:
	print( y ,'年不是閏年')