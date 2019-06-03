import unittest
import wordsearch_controller


class TestWordsearch(unittest.TestCase):

    def test_word_check(self):
        # set up an instance of the wordsearch controller
        grid_size = 5
        ws = wordsearch_controller.WordSearchController(size=grid_size, duplicate=True)
        ws.read_words_from_file()
        ws.generate_grid()

        # override the grid with a custom one
        ws.grid_list[0][0] = ['q', 'q', 'q', 'q', 'q']
        ws.grid_list[0][1] = ['w', 'o', 'r', 'd', 's']
        ws.grid_list[0][2] = ['q', 'q', 'n', 'q', 'u']
        ws.grid_list[0][3] = ['q', 'a', 'q', 'q', 'c']
        ws.grid_list[0][4] = ['r', 'o', 'q', 'q', 'h']
        for x in range(grid_size):
            for y in range(grid_size):
                ws.grid_list[1][grid_size-y-1][x] = ws.grid_list[0][x][y]
        ws.word_check()

        # check that all of the expected words were found, and no extras
        expected_words = ['row', 'or', 'or', 'ow', 'word', 'words', 'no', 'on', 'us', 'such', 'an', 'and', 'ran']
        assert len(expected_words) == len(ws.found)
        for word in ws.found:
            assert word in expected_words


if __name__ == '__main__':
    unittest.main()