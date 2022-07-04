info_in_bytes = int(input('Please enter the number of bytes: '))
info_in_kilobytes = info_in_bytes / 1024
info_in_megabytes = info_in_kilobytes / 1024
print(f'This equals to: \n{round(info_in_kilobytes, 2)} kilobytes \n{round(info_in_megabytes, 2)} megabytes')