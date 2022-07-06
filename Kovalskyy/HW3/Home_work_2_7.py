game_type = ('online', 'offline')

game_tech = ('pc', 'mobile', 'console')

game_genre = ('Action', 'Strategy', 'RPG', 'Puzzle', 'Sport')

game_name = ['One', 'Two', 'Three', 'Four']

games_dict = {game_type:
                        {game_tech: 
                                    {game_genre: game_name}
                        }
             }


#print(games_dict[game_type[1]][game_tech[1]][game_genre[1]][1])

print(games_dict[game_type][game_tech][game_genre])
