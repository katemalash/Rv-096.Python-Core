figure_1 = '*'
figure_2 = '.'

rectangle_height = int(input('Enter the number: '))
rectangle_width = int(input('Enter the number once more: '))

figures_row_1 = []
for i in range(rectangle_width):
    figures_row_1.append(figure_1)

figures_row_2 = []
for i in range(rectangle_width):
    if i in range(1) or i in range(rectangle_width-1, rectangle_width):
        figures_row_2.append(figure_1)
    else:
        figures_row_2.append(figure_2)
      
# figures_row_2.pop(0)
# figures_row_2.pop(-1)
# figures_row_2.insert(0, figure_1)
# figures_row_2.append(figure_1)

print(*figures_row_1)
for i in range(rectangle_height - 2):
    print(*figures_row_2)
print(*figures_row_1)