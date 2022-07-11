# Implement a calculator that translates the amount of information /
#  entered by the user in bytes into kilobytes and megabytes
number_bytes = int(input("Please, enter the number of bytes "))

number_KB = int(number_bytes/1024)
number_MB = int(number_bytes/1048576)
print(number_KB, end='')
print(" KB")
print(number_MB, end='')
print(" MB")