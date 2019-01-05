'''
Created on Apr 21, 2018

@author: urvipatel
'''
import itertools
from search import *

class Jealous:
    AGENTS = ['A1', 'A2', 'A3']
    ACTORS = ['C1', 'C2', 'C3']
    RIVER_MAP = {'C1':'A1', 'C2':'A2', 'C3':'A3'}
    
    def __init__(self, left, right, boat):
        self.left = set(left.copy())
        self.right = set(right.copy())
        self.boat = boat
    
    def __str__(self):
        retStr = '{'
        for b in self.left:
            retStr = retStr + b + ','
        retStr = retStr + '},'
        
        retStr = retStr + '{'
        for c in self.right:
            retStr = retStr + c + ','
        retStr = retStr + '},'
        
        retStr = retStr + str(self.boat)
        return retStr
    
    def __eq__(self, other):
        return self.left == other.left and self.right == other.right and self.boat == other.boat
    
    def __hash__(self):
        return hash(7)
        
    
    def successors(self):
        all_states = []
        if self.boat == 0:
            combos_left = self.generate_combos(self.left)
            for c in combos_left:
                left = set(self.left.copy())
                right = set(self.right.copy())
                lr = self.move(c, left, right)
                all_states.append(Jealous(lr[0], lr[1], 1))
        else:
            combos_right = self.generate_combos(self.right)
            for c in combos_right:
                left = set(self.left.copy())
                right = set(self.right.copy())
                rl = self.move(c, right, left)
                all_states.append(Jealous(rl[1], rl[0], 0))
        good_states = []
        for state in all_states:
            poaching_occurred = self.has_poaching_occurred(state)
            if not poaching_occurred:
                good_states.append(state)
        return good_states
        
    def has_poaching_occurred(self, state):
        left_side = state.left.copy()
        right_side = state.right.copy()
        
        poach_left = self.check_for_poaching(left_side)
        poach_right = self.check_for_poaching(right_side)
        
        return poach_left or poach_right
    
    def check_for_poaching(self, side):
        side_list = list(side)
        only_actors = side.intersection(self.AGENTS)
        only_agents = side.intersection(self.ACTORS)
        if len(only_actors) == 0 or len(only_agents) == 0:
            return 0
        for item in side_list:
            if item.startswith('C'):
                if self.RIVER_MAP[item] in side_list:
                    continue
                else:
                    return 1
    
    def move(self, c, source, dest):
        for item in c:
            source.remove(item)
            dest.add(item)
        return [source, dest]
            
    def generate_combos(self, people):
        combo_iter = itertools.combinations(people, 2)
        single_iter = itertools.combinations(people, 1)
        pairs = [*combo_iter]
        singles = [*single_iter]
        all_combos = pairs + singles
        all_list = []
        for a in all_combos:
            item = set(a)
            all_list.append(item)
        return all_list

    
def sch():
    start = Jealous(['A1', 'A2', 'A3', 'C1', 'C2', 'C3'], [], 0)
    goal = Jealous([], ['A1', 'A2', 'A3', 'C1', 'C2', 'C3'], 1)
    
    print('******** Jealous Agents - Depth First Search *******')
    ans = search(start, goal, 'dfs', 3000, False)
    print('Number of states visited: ' + str(ans))
    
    print('\n\n******** Jealout Agents - Breadth First Search *******')
    ans = search(start, goal, 'bfs', 3000, False)
    print('Number of states visited: ' + str(ans))

sch()
