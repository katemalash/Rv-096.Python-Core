
def convert_to_kilobytes(amount_of_bytes):

    amount_in_kilobytes = amount_of_bytes / 1024
    return amount_in_kilobytes


def convert_to_megabytes(amount_of_bytes):

    amount_in_megabytes = amount_of_bytes / (1024**2)
    return amount_in_megabytes


amount_in_bytes = int(input("Enter your amount in bytes: "))

amount_of_kilobytes = convert_to_kilobytes(amount_in_bytes)
amount_of_megabytes = convert_to_megabytes(amount_in_bytes)

print(f'Your amount in kilobytes is {round(amount_of_kilobytes, 5)}')
print(f'Your amount in megabytes is {round(amount_of_megabytes, 5)}')
