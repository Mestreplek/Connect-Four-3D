def check_four(four: list[int]) -> int:
    num : int = four[0]

    for i in four:

        if i == 0:
            return 0
        if i != num:
            return 0
    return num


class Game_State:


    def __init__(self):

        # 0 = nothing. 1 = White, 2 = Black
        # DOWNWARDS RODS
        # RODS LEFT IS DOWN
        self.move_1 = True

        self.RODS = [[0 for j in range(4)] for i in range(16)]


    def find_moves(self):

        available_RODS = []

        for ROD_index,ROD in enumerate(self.RODS):

            for point in ROD:

                if point != 0:
                    available_RODS.append(ROD_index)
                    break

        return available_RODS
    def find_winner(self) -> int:

        #region CHECKRODS

        for ROD in self.RODS:
            winner = check_four(ROD)

            if 0 != winner:

                return winner
        #endregion CHECKRODS


        # region CHECKHEIGHTS
        for height in [0,1,2,3]:
            pass

            # width and length


            # digagonals on 2D # TODO find winner of 2d height slices


        # endregion CHECKHEIGHTS

        # region CHECK3DDIAGONALS

        # endregion CHECK3DDIAGONALS

    def do_move(self,ROD_index) -> bool:


        ROD = self.RODS[ROD_index]
        move_executed = False
        for point_index,point in enumerate(ROD):

            if point == 0:
                self.RODS[ROD_index][point_index] = 1 if self.move_1 else 2
                move_executed = True
                break


        return move_executed





