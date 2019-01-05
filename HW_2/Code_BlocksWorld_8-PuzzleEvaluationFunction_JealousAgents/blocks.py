'''
Created on Apr 7, 2018

@author: urvipatel

'''

from search import *


class BlocksWorld:
    
    temp_states = []
    
    def __init__(self, strt, end=None):
        self.blocks = strt.copy()
        if end:
            self.goal = end.copy()
    
    def __hash__(self):
        return hash(7)
    
    def __str__(self):
        retStr = '['
        for b in self.blocks:
            retStr = retStr + b + ','
        retStr = retStr + ']'
        return retStr
    
    def __eq__(self, other):
        return set(self.blocks) == set(other.blocks)
    
    def __lt__(self, other):
        return self.evaluation() < other.evaluation()
    
    def clear_states(self):
        self.temp_states.clear()
    
    def evaluation(self):  #self=current other=goal
        if len(self.blocks) == 1 and len(self.goal) == 1:
            count = 0
            j = 0
            for i in self.blocks[0]:
 #               for j in self.goal[0]:
                if i == self.goal[0][j]:
                        count = count + 1
                        j = j + 1
            return count
        
        elif len(self.blocks) == 1 and len(self.goal) == 2:
            compare = self.goal[0] if len(self.goal[0]) == 2 else self.goal[1]
            if compare in self.blocks[0]:
                return 2
            else:
                return 0
            
        elif len(self.blocks) == 1 and len(self.goal) == 3:
            return 1
        
        elif len(self.blocks) == 2 and len(self.goal) == 1:
            goalStr1 = self.goal[0][0] + self.goal[0][1]
            goalStr2 = self.goal[0][1] + self.goal[0][2]
            if goalStr1 in self.blocks[0] or goalStr2 in self.blocks:
                return 2
            else:
                return 0
        
        elif len(self.blocks) == 2 and len(self.goal) == 2:
            count2 = 0
            if set(self.blocks) == set(self.goal):
                return 3
            else:
                for i in self.blocks[0]:
                    for j in self.goal[0]:
                        if i == j:
                            count2 = count2 + 1
                return count2
        
        elif len(self.blocks) == 2 and len(self.goal) == 3:
            return 1
        
        elif len(self.blocks) == 3 and len(self.goal) == 1:
            return 1
        
        elif len(self.blocks) == 3 and len(self.goal) == 2:
            return 1
         
        elif len(self.blocks) == 3 and len(self.goal) == 3:
            return 3

    def successors (self):
        ret = [] 
        state = self.blocks
        if len(state) == 3:
            for i in range(0, len(state)):
                for j in range(0, len(state)):
                    if i == j:
                        continue
                    res1 = [state[i], state[j]]
                    diff_list = list(set(state) - set(res1))[0]
                    res = BlocksWorld([state[i] + state[j], diff_list], self.goal)
                    
                    found = False
                    for item in self.temp_states:
                        if set(res.blocks) == set(item):
                            found = True
                            break
                    self.temp_states.append(res.blocks)
                    if not found:
                        ret.append(res)
        elif len(state) == 1:
            seq = state[0]
            first = seq[:1]
            second = seq[1:]
            res = BlocksWorld([first, second], self.goal)
            
            found = False
            for item in self.temp_states:
                if set(res.blocks) == set(item):
                    found = True
                    break
            self.temp_states.append(res.blocks)
            if not found:
                ret.append(res)
        else:     
            block_to_stack = state[0] if len(state[0]) == 1 else state[1]
            index = state.index(block_to_stack)
            if index == 0:
                res = BlocksWorld([state[index] + state[1]], self.goal)
            else:
                res = BlocksWorld([state[index] + state[0]],self.goal)
            
            found = False
            for item in self.temp_states:
                if set(res.blocks) == set(item):
                    found = True
                    break
            self.temp_states.append(res.blocks)
            if not found:
                ret.append(res)
            
            block_to_unstack = state[0] if len(state[0]) == 2 else state[1]
            index_to_unstack = state.index(block_to_unstack)
            index_to_append = int(not index_to_unstack)
            r = list(state[index_to_unstack])
            r.append(state[index_to_append])
            res2 = BlocksWorld(r, self.goal)
            
            found = False
            for item in self.temp_states:
                if set(res2.blocks) == set(item):
                    found = True
                    break
            self.temp_states.append(res2.blocks)
            if not found:
                ret.append(res2)
        return ret

def set_start_state(s):
    return BlocksWorld(s)

def set_goal_state(g):
    return BlocksWorld(g)

def get_goal_state():
    return 


def sch():
    print('Enter a start state as a comma separated strings, NO SPACES.  For example, ro,b or rbo or r,b,o')
    begin = input('Enter start state: ')
    end = input('Enter goal state: ')
    begin = begin.split(',')
    end = end.split(',')
    s1 = set(begin)
    s2 = set(end)
    begin = list(s1)
    end = list(s2)
    start = BlocksWorld(begin, end)
    goal = BlocksWorld(end, None)
    
    print('\n\n***** Blocks World - Depth First Search *******')
    ans = search(start, goal, 'dfs', 3000)
    print('Number of states visited: ' + str(ans))
    
    start.clear_states()
    goal.clear_states()
    
    print('\n\n***** Blocks World - Breadth First Search *******')
    ans = search(start, goal, 'bfs', 3000)
    print('Number of states visited: ' + str(ans))
    
    start.clear_states()
    goal.clear_states()
    
    print('\n\n***** Blocks World - Best First Search *******')
    ans = search(start, goal, 'best', 3000)
    print('Number of states visited: ' + str(ans))

sch()
    





