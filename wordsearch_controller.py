import random
import string

from collections import defaultdict


class WordSearchController():

    def __init__(self, size=15, duplicate=False):
        self.grid_size = size
        self.list_repeat_words = duplicate
        self.words = defaultdict(list)
        self.grid_list = []
        self.found = []

    def read_words_from_file(self):
        """
            Reads from the "words.txt" file in the same directory.
            Splits up all the words into separate lists based on
            their first letter.
        """
        words_file = open("words.txt", "r")
        for line in words_file:
            self.words[line[0]].append(line.rstrip())
        words_file.close()

    def generate_grid(self):
        """
            Generates two grids.
            The first is a randomized grid of size grid_size.
            The second is the first grid but with all letter placements rotated.
        """
        for _ in range(2):
            self.grid_list.append([['' for x in range(self.grid_size)] for y in range(self.grid_size)])
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                self.grid_list[0][x][y] = random.choice(string.ascii_lowercase)
                self.grid_list[1][self.grid_size-y-1][x] = self.grid_list[0][x][y]

    def print_grid(self):
        """
            Prints out the generated grid
        """
        print ("Generated word search of size " + str(self.grid_size) + "x" + str(self.grid_size) + ":\n")
        for row in self.grid_list[0]:
            print (' '.join(char for char in row))
        print ('\n')

    def word_check(self):
        """
            Method to find all valid words in the grid.
            Checks the normal grid first, each line both normal and reversed,
            and then the same for the rotated version.

            For all unique letters in each line, check if any word starting
            in that letter can be found in the line or the reversed line.
        """
        for grid in self.grid_list:
            # horizontal and vertical check
            for row in grid:
                line = ''.join(char for char in row)
                line_reverse = line[::-1]
                unique = set(row)
                for char in unique:
                    for word in self.words[char]:
                        if word in line:
                            self.found.append(word)
                        if word in line_reverse:
                            self.found.append(word)
            # diagonals check
            # there are double the number of diagonal lines,
            # so it checks in both directions.
            for x in range(self.grid_size):
                char_list_down = []
                char_list_up = []
                for y in range(self.grid_size-x):
                    char_list_down.append(grid[y+x][y])
                    if x>0:
                        char_list_up.append(grid[y][y+x])
                line_down = ''.join(char for char in char_list_down)
                line_up = ''.join(char for char in char_list_up)
                line_down_reverse = line_down[::-1]
                line_up_reverse = line_up[::-1]
                unique_down = set(char_list_down)
                unique_up = set(char_list_up)
                for char in unique_down:
                    for word in self.words[char]:
                        if word in line_down:
                            self.found.append(word)
                        if word in line_down_reverse:
                            self.found.append(word)
                for char in unique_up:
                    for word in self.words[char]:
                        if word in line_up:
                            self.found.append(word)
                        if word in line_up_reverse:
                            self.found.append(word)

    def print_results(self):
        """
            Prints the found words.
            If duplicate is set to true, it will print every instance
            of each word that appears.
            If false, it will print each found word only once.
        """
        if len(self.found) == 0:
            print ("No valid words found.")
        else:
            print ("Valid words found in this search:\n")
            if self.list_repeat_words:
                print (self.found)
            else:
                found_set = set(self.found)
                print (found_set)