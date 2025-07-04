import main

deepseek_api = "YOUR API KEY"


game = Game_State()



while game.find_winner() == 0:

    2d_height_slices = []
    for height in range(4):
        current_slice = []

        for i in range(16):
            current_slice.append(Game_State.RODS[i][height]) 

        2d_height_slices.append(current_slice)
    print(2d_height_slices)
    prompt = f"You are playing Connect 4 with 3 Dimension so 4x4x4, find the best move for player {„1“ if game.move_1 else „2“}. The game state is represente as the folowing RODS (bottom to top. Left: bottom, right: top): {game.RODS}. 2D sliecs of all points on a height from bottom to top: {2d_height_slices}."
    break    








print(Game_State.winner)