def position(figure):
    mydict = {97: '97', 98: '98', 99: '99', 100: '100', 101: '101', 102: '102', 103: '103', 104: '104'}
    user_choice = list(figure.translate(mydict))
    if len(user_choice) == 3:
        a, b, c = user_choice
        d = a + b
        figure_position = []
        figure_position.append(d)
        figure_position.append(c)
    elif len(user_choice) == 4:
        a, b, c, d = user_choice
        q = a + b + c
        figure_position = []
        figure_position.append(q)
        figure_position.append(d) 
        
    return figure_position  #['97', '5']

def can_capture(figures):

    my_knight = figures[0]
    enemy_figure = figures[1]
  
    enemy_figure_position = position(enemy_figure)
    my_knight_position = position(my_knight)
                        
    if abs(int(my_knight_position[0]) - int(enemy_figure_position[0])) == 2 and abs(int(my_knight_position[1]) - int(enemy_figure_position[1])) == 1:
        #print('Caught!')
        return True  
    elif abs(int(my_knight_position[0]) - int(enemy_figure_position[0])) == 1 and abs(int(my_knight_position[1]) - int(enemy_figure_position[1])) == 2:
        #print('Caught!')
        return True
    else:
        #print("Can't beat this figure")
        return False
        
my_knight = (input('Enter the position of your knight: ')).lower()
enemy_figure = (input('Enter the position of the enemy figure: ')).lower()

print(can_capture([my_knight, enemy_figure]))

