# 1 
# 1 1 
# 1 1 1 
# 1 1 1 1 
# 1 1 1 1 1
for row in range(1, 6, 1):
    for col in range(1, row+1, 1):
        print("1", end=" ")
    print()

print()
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
index = 1
for row in range(1, 5, 1):
    for col in range(1, row+1, 1):
        print(index, end=" ")
        index += 1
    print()

print()
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 
for row in range(0, 5, 1):
    for col in range(1, 6-row, 1):
        print("*", end=" ")
    print()

print()
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
for row in range(1, 6, 1):
    for spc in range(1, 6-row, 1):
        print(end=" ")
    for col in range(1, row+1, 1):
        print("*",end=" ")
    print()

print()
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 
for row in range(1, 6, 1):
    for spc in range(1, 6-row, 1):
        print(end=" ")
    for col in range(1, row+1, 1):
        print("*",end=" ")
    print()
for row in range(1, 6, 1):
    for spc in range(0, row):
        print(end=" ")
    for col in range(0, 5-row):
        print("*",end=" ")
    print()