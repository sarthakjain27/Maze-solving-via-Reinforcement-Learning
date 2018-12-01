from environment import Environment
import sys
import numpy as np
import random as rand
import time
__author__ = 'SARTHAK JAIN'

def init():
    q_dict={}
    for each_val_state in env.valid_states:
        q_dict[each_val_state]=np.zeros(4)
    return q_dict

def select_action(state):
    rand_value=rand.uniform(0,1)
    if rand_value>epsilon:
        return q_dict[state].argmax()
    else:
        return rand.randint(0,3)

def q_learn():
    total=0
    for episode in range(0,int(sys.argv[5])):
        curr_episode_len=0
        env.reset()
        #while curr_episode_len < (int(sys.argv[6])):
        while(True):
            prev_state=env.curr_state
            action=select_action(env.curr_state)
            next_state,reward,istarget=env.step(action)
            q_dict[prev_state][action]=((1-learn_rate)*q_dict[prev_state][action]) + (learn_rate * (reward + (float(sys.argv[8])) *(q_dict[next_state].max())))
            if istarget:
                break
            curr_episode_len+=1
        total+=curr_episode_len
        print("episode {} episode length {}".format(episode+1,curr_episode_len))

    print("Average length per episode {}".format(float(total/(float(sys.argv[5])))))
    return

def write_to_fle():
    with open(sys.argv[2],'w') as v_file, open(sys.argv[3],'w') as q_file, open(sys.argv[4],'w') as p_file:
        for cell in q_dict:
            v_file.write('{} {} {}\n'.format(cell[0],cell[1],q_dict[cell].max()))
            p_file.write('{} {} {}\n'.format(cell[0],cell[1],float(q_dict[cell].argmax())))
            for action,value in enumerate(q_dict[cell]):
                q_file.write('{} {} {} {}\n'.format(cell[0],cell[1],action,value))
    return



if __name__=="__main__":
    start_time = time.time()
    learn_rate=float(sys.argv[7])
    epsilon=float(sys.argv[9])
    env=Environment(sys.argv[1])
    q_dict=init()
    q_learn()
    write_to_fle()
    print("--- %s seconds ---" % (time.time() - start_time))