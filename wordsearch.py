import argparse
import wordsearch_controller

parser = argparse.ArgumentParser(description='Generate and solve a word search.')
parser.add_argument('-s', '--size', dest='size', type=int, default=15, metavar="int",
                    help='size of the word search (default: 15, max: 100)')
parser.add_argument('-d', '--duplicate', dest='duplicate', action='store_true',
                    help='include all repeat found words in the results (default: false)')
args = parser.parse_args()
if args.size and args.size > 100:
    parser.error("Maximum size is 100.")

ws = wordsearch_controller.WordSearchController(args.size, args.duplicate)
ws.read_words_from_file()
ws.generate_grid()
ws.word_check()
ws.print_grid()
ws.print_results()