'''
Created on Apr 7, 2018

@author: urvipatel
'''
# CSC 380/480 Winter 2018
# A comparison of eight-puzzle using various forms of search.
# In this version, the evaluator for best-first is a count
# of the number of tiles that are in the correct position
# Built on a generalized state finder in search.py
#
# To run this, DO NOT load eight_puzzle_state.py -- instead, open
# search.py and press the F5 key to load it.

from random import shuffle    # to randomize the order in which successors are visited

class eight_puzzle_state:
    def __init__(self, tiles):
        self.tiles = tiles.copy()
        #self.tiles = tiles

    def __str__(self):
        answer = ''
        for i in range(9):
            answer += '{} '.format(self.tiles[i])
            if (i+1)%3 == 0:
                answer += '\n'
        return answer
    
    def __repr__(self):
        return 'eight_puzzle_state({})'.format(self.tiles)

    def __eq__(self, other):
        return self.tiles == other.tiles

    def __hash__(self):
        return hash(self.tiles[0])
    
    def successors(self):
        successor_states = [ ]
        neighbors = {0:[1,3],1:[0,2,4],2:[1,5],3:[0,4,6],4:[1,3,5,7],5:[2,4,8],6:[3,7],7:[4,6,8],8:[5,7]}
        zero_loc = self.tiles.index(' ')
        for loc in neighbors[zero_loc]:
            state = eight_puzzle_state(self.tiles)
            state.tiles[zero_loc] = state.tiles[loc]
            state.tiles[loc] = ' '
            successor_states.append(state)
        return successor_states

    # returns an int between 0 (no tiles in place) to 8 (all in place)
    def evaluation(self):
        wrong = 0
        for i in range(8):
            if self.tiles[i] != goal_state().tiles[i]:
                wrong += 1
        return wrong

    #def __lt__(self, other):
    #    return self.evaluation() < other.evaluation()
    
    def __lt__(self, other):
        return self.evaluation_2() < other.evaluation_2()
    
    def evaluation_2(self):
        board = self.tiles.copy()
        goal = goal_state().tiles.copy()
        board[board.index(' ')] = '0' # Replace str '' with int value of zero
        board = list(map(int, board))
        goal[goal.index(' ')] = '0'
        goal = list(map(int, goal)) # Convert to list of ints
        ret = sum(abs(b%3 - g%3) + abs(b//3 - g//3) for b, g in ((board.index(i), goal.index(i)) for i in range(1, 9)))
        return ret
        
    
def goal_state(ignore=None):
    return eight_puzzle_state(['1', '2', '3', '8', ' ', '4', '7', '6', '5'])

# from random import shuffle   random puzzle is too many moves from goal state
from random import randint

# make a start state which is n moves from goal state
def start_state(n=5):
    already_visited = [ goal_state() ]
    state = goal_state()
    # max number of moves from start state to goal state
    for i in range(n):
        successors = state.successors()
        for s in successors:
            if s in already_visited:
                successors.remove(s)
        shuffle(successors)
        state = successors[0]
        already_visited.append(state)
    return state


def random_eight_puzzle_state():
    tiles = ['1', '2', '3', '4', '5', '6', '7', '8', ' ']
    shuffle(tiles)
    return eight_puzzle_state(tiles)
