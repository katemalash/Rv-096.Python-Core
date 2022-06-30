amount_bytes = float(input("Enter amount in bytes: "))

amount_kilobytes = amount_bytes / 1024
amount_megabytes = amount_bytes / 1048576

print("Bytes in kilobytes:", amount_kilobytes)
print("Bytes in megabytes:", amount_megabytes)