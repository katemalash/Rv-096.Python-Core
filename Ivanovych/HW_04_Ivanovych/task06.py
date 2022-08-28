SeatNumber=int(input("Enter the number of your seat:"))

if 1 <= SeatNumber <= 54:
    if SeatNumber%2 == 0:
        SeatPosition1 ='upper'
    else:
        SeatPosition1 ='lower'
    if SeatNumber<=36:
        SeatPosition2 ='place in the compartment'
    else:
        SeatPosition2 ='side seat'
    print('You have a ',SeatPosition2,' on the ',SeatPosition1, 'berth ')
else:
 print('You entered wrong number')
