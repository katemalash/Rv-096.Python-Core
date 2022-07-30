def is_prime(number):
    """This function determines the primality of a number."""

    for divider in range(2, number):

        if number % divider == 0:
            return False

    return True


number = int(input('Enter number: '))

print(is_prime(number))
