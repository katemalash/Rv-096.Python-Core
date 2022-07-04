

def bytes_converter():
    amount_in_bytes = int(input("Enter your amount in bytes: "))
    amount_in_kilobytes = amount_in_bytes / 1024
    amount_in_megabytes = amount_in_bytes / 1048576
    return print(f'Your amount in kilobytes will be {round(amount_in_kilobytes, 2)}. Your amount in megabytes will be \
{round(amount_in_megabytes, 2)}')


bytes_converter()
