my_file = open("test_file.txt", "w")

my_file.write("First Line\n")
my_file.write("Second Line")
my_file = open("test_file.txt")

content = my_file.read()

my_file.close()

print(content)
