'''Aleksieiev Valentyn
30/07/2022 HomeWork#3, Task#2
Implement a calculator that translates the amount of information entered by the user in bytes into kilobytes and megabytes.
'''

def bytes_convertor():
    try:
        bytes = int(input('Input number of bytes to convert: '))
    except Exception:
        print('You can input only integer numbers of bytes')
        bytes_convertor()
    return (bytes, bytes//1024, bytes//1024//1024)

byte, kilo_bytes, mega_bytes = bytes_convertor()

print(f'In {byte} bytes = {mega_bytes} MegaBytes, {kilo_bytes} KiloBytes and \
{byte - mega_bytes * 1024 * 1024 - kilo_bytes * 1024} bytes')

