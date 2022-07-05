# Let's imagine that we want to control all stuff in art gallery. 
# Every piece of art we can describe in a dictionary, which consists
# a type of painting style (we'll make a tuple of different types) 
# as a key and short information about placing as a value.  So, 
# we'll have lots of dictionaries, which we could store in a list.  

painting_styles = ('realism',
                   'hyperrealism',
                   'expressionism',
                   'impressionism',
                   'abstract',
                   'surrealism',
                   'pop art',
                   'naive art',
                   )

Mone_Irises_in_monets_garden = {painting_styles[3]: 'hall 3, second floor'}
Mone_Boulevard_des_capucines = {painting_styles[3]: 'hall 3, second floor'}
Mone_The_avenue = {painting_styles[3]: 'hall 1, second floor'}
Mone_The_avenue_copy = {painting_styles[3]: 'copy, basement, row 1'}
Primachenko_This_beast_is_making_magic = {painting_styles[7]: 'hall 1, first floor'}


paintings_of_the_gallery = [Mone_Irises_in_monets_garden,
                            Mone_Boulevard_des_capucines,
                            Mone_The_avenue,
                            Mone_The_avenue_copy,
                            Primachenko_This_beast_is_making_magic,
                            ]

print(paintings_of_the_gallery)