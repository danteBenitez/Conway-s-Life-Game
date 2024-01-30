import unittest
from game import ConwayLifeGame

class TestGame(unittest.TestCase):

    def test_created(self):
        game = ConwayLifeGame.empty(10, 10)
        self.assertEqual(game.rows, 10, 'Rows was not 10')
        self.assertEqual(game.columns, 10, 'Columns was not 10')
        self.assertEqual(len(game.cells), 10, 'Number of rows do not match')
        self.assertEqual(len(game.cells[0]), 10, 'Number of columns do not match')
        for row in game.cells:
            self.assertEqual(len(row), 10, 'Some row does not match the expected length')

    def test_adjacent(self):
        # Start with an empty game
        game = ConwayLifeGame.empty(10, 10)
        # Fill the middle with an alive cell
        game.insert_cell(5, 5, True)
        # Adjacents must be all False
        adjacent = game.get_adjacent_to(5, 5)
        self.assertEqual(len(adjacent), 8)
        self.assertListEqual(adjacent, [False for i in range(8)])

        # Fill the upper one with a alive cell
        # and check for only exactly one alive adjacent cell
        game.insert_cell(4, 5, True)
        adjacent = game.get_adjacent_to(4, 5)
        self.assertEqual(len(adjacent), 8)
        self.assertCountEqual([True] + [False for i in range(7)], adjacent)

if __name__ == '__main__':
    unittest.main()
