# single try block with multiple except block
try:
  print(x)
except NameError:
  print("x is not defined")
except:
  print("Something went wrong")

# multiple try block with single except block
try:
    ls = []
    print(ls[0])
except IndexError:
    print('index out of range')

# nested try with nested except block
try:
  print('hello guys')
  try:
      print('nested try')
  except:
    print("nested except")
except:
  print("nested only")

# nested try with nested except block with nested finally
try:
  f = open("demo.txt")
  try:
    f.write("gopal k")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
finally:
    print('all task done')
  
# multiple try block with multiple except block
try:
	k = 5//0
	print(k)
except ZeroDivisionError:
	print("Can't divide by zero")
finally:
	print('This is always executed')