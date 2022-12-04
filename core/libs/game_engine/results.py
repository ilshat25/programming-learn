class ExecuteResult:

    @staticmethod
    def _determine_result(way, level):
        if way and way[-1][0] == level.get_x_finish() and way[-1][1] == level.get_y_finish():
            return 1
        return 0

    def __init__(self, way, level):
        self.win = ExecuteResult._determine_result(way, level)
        self.way = way
        self.num = level.get_num()

    def __repr__(self):
        return f'{self.win}, {self.way}, {self.num}'
