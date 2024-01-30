import typing

type GameState = list[list[bool]]

#  [[1, 1, 1],
#   [0, 0, 0],
#   [1, 1, 1]
# ]
#
diff = [
    { 'dx': 1, 'dy': 1 },
    { 'dx': 0, 'dy': 1 },
    { 'dx': 1, 'dy': 0 },
    { 'dx': -1, 'dy': 1 },
    { 'dx': 1, 'dy': -1 },
    { 'dx': -1, 'dy': 0 },
    { 'dx': 0, 'dy': -1 },
    { 'dx': -1, 'dy': -1 }
]

class ConwayLifeGame:
    """
    Module that simulates Conway's Game of Life
    """
    def __init__(self, columns: int, rows: int, initial_state: GameState):
        if columns < 0 or rows < 0:
            raise ValueError("Width and height must be positive integers")
        if len(initial_state) != rows:
            raise ValueError("Initial state must have the same height as the game")
        
        self.columns = columns
        self.rows = rows 
        self.cells = initial_state

    @staticmethod
    def empty(rows: int, columns: int):
        return ConwayLifeGame(columns, rows, [[False for i in range(columns)] for i in range(rows)])

    def next_state(self):
        for row in range(self.rows):
            for (col, alive) in enumerate(self.cells[row]):
                adjacent = self.get_adjacent_to(row, col)

                alive_neighbors = filter(None, adjacent)
                alive_len = len(list(alive_neighbors))

                # 1) If a cell has exactly three alive adjacent cells
                # then, it comes to life
                if alive_len == 3 and not alive:
                    self.insert_cell(row, col, True)

                # 2) If a cell has more than three or less than two
                # alive adjacent cell then, it dies
                if (alive_len > 3 or alive_len < 2) and alive:
                    self.insert_cell(row, col, False)

                # 3) If a cell has two or three neighbors, then it 
                # is kept alive
                if (alive_len == 2 or alive_len == 3) and alive:
                    self.insert_cell(row, col, True)
                

    def insert_cell(self, row: int, column: int, alive: bool):
        self.cells[row][column] = alive

    def get_cell_or_default(self, row: int, column: int) -> bool:
        try: 
            return self.get_cell(row, column)
        except IndexError:
            return False

    def get_cell(self, row: int, column: int) -> bool:
        return self.cells[row][column]

    def get_adjacent_to(self, row: int, column: int) -> list[bool]:
        adjacent = []
        for val in diff:
            dx = val['dx']
            dy = val['dy']
            adjacent.append(self.get_cell_or_default(row + dx, column + dy))
        return adjacent
    
    def print_cells(self):
        for row in range(self.rows):
            print("[", end="")
            for col in range(self.columns):
                cell = self.get_cell(row, col)
                if col != self.columns-1:
                    print(f"{cell},", end="")
                else:
                    print(cell, end="")
            print("]")


