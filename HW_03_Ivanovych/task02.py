#Implement a calculator that translates the amount of information entered by the user in bytes into kilobytes and megabytes

Size_in_bytes = int(input('Enter size (bytes): '))

kilobytes = round(Size_in_bytes / 1024, 3)
megabytes = round(kilobytes / 1024, 3)

print(f'Kilobytes = {kilobytes}\nMegabytes = {megabytes}')
