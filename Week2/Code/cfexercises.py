# How many times will 'hello' be printed?
# 1)
for i in range(3, 17):
	print 'hello'
	
# 2)
for j in range(12):
	if j % 3 == 0:
		print 'hello'
		
# 3)
for j in range(15):
	if j % 5 == 3:
		print 'hello'
	elif j % 4 == 3:
		print 'hello'
		
# 4)
z = 0
while z != 15:
	print 'hello'
	z = z + 3
	
# 5)
z = 12
while z < 100:
	if z == 31:
		for k in range(7):
			print 'hello'
	elif z == 18:
		print 'hello'
	z = z + 1
	
#What does fooXX do?
def foo1(x=1):
	return x ** 0.5
	
def foo2(x=1, y=1):
	if x > y:
		return x
	return y
	
def foo3(x=1, y=1, z=1):
	if x > y:
		tmp = y
		y = x
		x = tmp
	if y > z:
		tmp = z
		z = y
		y = tmp
	return [x, y, z]
	
def foo4(x=5):
	result = 1
	for i in range(1, x + 1):
		result = result*i
	return result
	
# This is a recursive function, meaning that the function calls itself
# read about it at
# en.wikipedia.org/wiki/Recursion_(computer_science)
def foo5(x=5):
	if x == 1:
		return 1
	return x * foo5(x - 1)

print "foo1(20)"
print foo1(20)
print "foo2(32,7)"
print foo2(32,7)
print "foo3(3,7,6)"
print foo3(3,7,6)
print "foo4(8)"
print foo4(8)
print "foo5(10)"
print foo5(10)
