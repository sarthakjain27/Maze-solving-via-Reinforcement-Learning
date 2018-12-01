import sys
import numpy as np
__author__ = 'SARTHAK JAIN'

class Environment:
    def __init__(self,file):
        with open(file,'r') as f:
            self.maze=[line.split()[0] for line in f]

        #a list of tuples of valid state
        self.valid_states=[]
        self.ll_block=[]
        self.v_initial=np.zeros((len(self.maze),len(self.maze[0])))
        self.target_coord_tup=()
        self.start_coord_tup=()
        self.curr_state=()
        self.num_row=len(self.v_initial)
        self.num_col=len(self.v_initial[0])
        for row,each in enumerate(self.maze):
            for col,each_val in enumerate(each):
                self.valid_states.append((row,col))
                if each_val=='S':
                  self.start_coord_tup=(row,col)
                  self.curr_state=self.start_coord_tup
                elif each_val=='G':
                    self.target_coord_tup=(row,col)
                elif each_val=='*':
                    self.valid_states.remove((row,col))
                    self.ll_block.append((row,col))
                    self.v_initial[row][col]=float("inf")

    def step(self,action):

        row=self.curr_state[0]
        col=self.curr_state[1]

        if self.curr_state==self.target_coord_tup:
            return self.curr_state,0,1

        next_state=()
        isterm=0
        if action==0:
            next_state=(row,max(col-1,0))
            if (row,col-1) in self.ll_block:
                next_state=(row,col)
        elif action==1:
            next_state=(max(row-1,0),col)
            if (row-1,col) in self.ll_block:
                next_state=(row,col)
        elif action==2:
            next_state=(row,min(self.num_col-1,col+1))
            if (row,col+1) in self.ll_block:
                next_state=(row,col)
        else:
            next_state=(min(row+1,self.num_row-1),col)
            if (row+1,col) in self.ll_block:
                next_state=(row,col)

        self.curr_state=next_state
        if next_state==self.target_coord_tup:
            isterm=1
        return next_state,-1,isterm

    def reset(self):
        self.curr_state=self.start_coord_tup
        return


if __name__ == "__main__":
    envrn=Environment(sys.argv[1])
    with open(sys.argv[3],'r') as f:
        action_seq=[map(int,line.split(' ')) for line in f]

    with open(sys.argv[2],'w') as f:
        for actions in action_seq[0]:
            next_state,reward,istarget=envrn.step(actions)
            f.write('{} {} {} {}\n'.format(next_state[0],next_state[1],reward,istarget))

