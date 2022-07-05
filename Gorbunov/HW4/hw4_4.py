# Checking how big sctnt we can install in a square hall with coridor.

hall_area = float(input("Enter hall area :"))
coridor_width = float(input("Enter coridor width :"))
scene_area = float(input("Enter scene area :"))

clean_hall_place = hall_area**0.5-coridor_width
space_for_scene = 3.14*(clean_hall_place/2)**2
max_scene_diamert = 2*(space_for_scene/3.14)**0.5
max_coridor_width = (hall_area**0.5)-2*(scene_area/3.14)**0.5

if coridor_width<hall_area**0.5 and scene_area<space_for_scene:
        print(f"Maximum scene area is {round(space_for_scene,2)}, with scene diametr: \
            {round(max_scene_diamert,2)},\nOr maximum coridor width is: {round(max_coridor_width,2)}")
elif scene_area>space_for_scene:
        print(f"Try to install scene with diametr: {round(max_scene_diamert,2)}. \
            It will be maximum {round(space_for_scene,2)} scene area.")
else: print(f"Check input parameters! Maybe coridor width is to big)\nIt maximum {round(hall_area**0.5,2)}.")