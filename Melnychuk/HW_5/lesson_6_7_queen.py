def position(queen):
    mydict = {97: '97', 98: '98', 99: '99', 100: '100', 101: '101', 102: '102', 103: '103', 104: '104'}
    user_choice = list(queen.translate(mydict))
    if len(user_choice) == 3:
        a, b, c = user_choice
        d = a + b
        queen_position = []
        queen_position.append(d)
        queen_position.append(c)
    elif len(user_choice) == 4:
        a, b, c, d = user_choice
        q = a + b + c
        queen_position = []
        queen_position.append(q)
        queen_position.append(d) 
        
    return queen_position

def can_capture(queens):

    my_queen = queens[0]
    enemy_queen = queens[1]
           
    directions = {'top': [0, 1],
                  'bottom': [0, -1],
                  'left': [-1, 0],
                  'right': [1, 0],
                  'top_right': [1, 1],
                  'bottom_right': [1, -1],
                  'top_left': [-1, 1],
                  'bottom_left': [-1, -1]}
    
    for direction_name, direction_step in directions.items():
        
        enemy_queen_position = position(enemy_queen)
        my_queen_position = position(my_queen)
        num_0 = int(my_queen_position[0])
        num_1 = int(my_queen_position[1])    
        
        while 97 <= num_0 <= 104 and 1 <= num_1 <= 8:
            if my_queen_position == enemy_queen_position:
                print(f'Caught! in {direction_name} position.')
                return True
            else: 
                num_0 += direction_step[0]
                num_1 += direction_step[1]
                my_queen_position[0] = str(num_0)
                my_queen_position[1] = str(num_1)
    return False
                
my_queen = input('Enter the position of your queen: ')
enemy_queen = input('Enter the position of the enemy queen: ') 
        
print(can_capture([my_queen, enemy_queen]))
