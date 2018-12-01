import sys
import numpy as np
import time
__author__ = 'SARTHAK JAIN'

def create(file):
    with open(file,'r') as f:
        maze=[line.split()[0] for line in f]

        ll_block=[]
        v_initial=np.zeros((len(maze),len(maze[0])))
        target_coord_tup=()
        num_state=0
        for row,each in enumerate(maze):
            for col,each_val in enumerate(each):
                num_state+=1
                if each_val=='G':
                    target_coord_tup=(row,col)
                    num_state-=1
                elif each_val=='*':
                    num_state-=1
                    ll_block.append((row,col))
                    v_initial[row][col]=float("inf")

    return v_initial,target_coord_tup,ll_block,num_state

def get_tuples(row,col,num_row,num_col):

    west_tup=(row,max(col-1,0))
    if (row,col-1) in ll_block:
        west_tup=(row,col)

    north_tup=(max(row-1,0),col)
    if (row-1,col) in ll_block:
        north_tup=(row,col)

    east_tup=(row,min(num_col-1,col+1))
    if (row,col+1) in ll_block:
        east_tup=(row,col)

    south_tup=(min(row+1,num_row-1),col)
    if (row+1,col) in ll_block:
        south_tup=(row,col)

    return west_tup,north_tup,east_tup,south_tup

def write_q_p_file(v_initial,ll_block,target_coord_tup):

    num_row=len(v_initial)
    num_col=len(v_initial[0])
    df=float(sys.argv[6])

    with open(sys.argv[3],'w') as q_file, open(sys.argv[4],'w') as policy_file:
        for row in range(0,num_row):
            for col in range(0,num_col):
                if (row,col) in ll_block:
                    continue

                if (row,col)==target_coord_tup:
                    q_file.write('{} {} {} {}\n'.format(row,col,0,0.0))
                    q_file.write('{} {} {} {}\n'.format(row,col,1,0.0))
                    q_file.write('{} {} {} {}\n'.format(row,col,2,0.0))
                    q_file.write('{} {} {} {}\n'.format(row,col,3,0.0))
                    policy_file.write('{} {} {}\n'.format(row,col,0.0))

                else:
                    ll=[]
                    west_tup,north_tup,east_tup,south_tup=get_tuples(row,col,num_row,num_col)

                    q_file.write('{} {} {} {}\n'.format(row,col,0,(-1+(df*(v_initial[west_tup[0]][west_tup[1]])))))
                    q_file.write('{} {} {} {}\n'.format(row,col,1,(-1+(df*(v_initial[north_tup[0]][north_tup[1]])))))
                    q_file.write('{} {} {} {}\n'.format(row,col,2,(-1+(df*(v_initial[east_tup[0]][east_tup[1]])))))
                    q_file.write('{} {} {} {}\n'.format(row,col,3,(-1+(df*(v_initial[south_tup[0]][south_tup[1]])))))

                    ll.append((-1+(df*(v_initial[west_tup[0]][west_tup[1]]))))
                    ll.append((-1+(df*(v_initial[north_tup[0]][north_tup[1]]))))
                    ll.append((-1+(df*(v_initial[east_tup[0]][east_tup[1]]))))
                    ll.append((-1+(df*(v_initial[south_tup[0]][south_tup[1]]))))

                    policy_file.write('{} {} {}\n'.format(row,col,float(ll.index(max(ll)))))
    return

def perform_value_iteration(v_initial,target_coord_tup,ll_block):
    num_row=len(v_initial)
    num_col=len(v_initial[0])
    df=float(sys.argv[6])
    v_new=np.zeros((num_row,num_col))

    for num_epoch in range(0,int(sys.argv[5])):
        print("epoch number {}".format(num_epoch))
        for row in range(0,num_row):
            for col in range(0,num_col):
                if (row,col)==target_coord_tup:
                    continue

                if(row,col) in ll_block:
                    continue

                west_tup,north_tup,east_tup,south_tup=get_tuples(row,col,num_row,num_col)
                v_new[row][col]=max((-1+(df*(v_initial[west_tup[0]][west_tup[1]]))),(-1+(df*(v_initial[north_tup[0]][north_tup[1]]))),(-1+(df*(v_initial[east_tup[0]][east_tup[1]]))),(-1+(df*(v_initial[south_tup[0]][south_tup[1]]))))
        count=0


        for row in range(0,num_row):
            for col in range(0,num_col):
                if (row,col)==target_coord_tup:
                    continue

                if(row,col) in ll_block:
                    continue

                if abs(v_new[row][col]-v_initial[row][col]) < 0.001:
                    count+=1

        if count==num_states:
            print("v_initial")
            print(v_initial)
            print("v_new")
            print(v_new)
            v_initial=np.copy(v_new)
            break
        print(count)
        print("v_initial")
        print(v_initial)
        print("v_new")
        print(v_new)
        v_initial=np.copy(v_new)
        #print("After {} epoch".format(num_epoch+1))
        #print(v_initial)

    with open(sys.argv[2],'w') as f:
        for row in range(0,num_row):
            for col in range(0,num_col):
                if (row,col) in ll_block:
                    continue
                f.write('{} {} {}\n'.format(row,col,v_initial[row][col]))

    write_q_p_file(v_initial,ll_block,target_coord_tup)
    return

if __name__ == "__main__":
    start_time = time.time()
    v_initial,target_coord_tup,ll_block,num_states=create(sys.argv[1])
    perform_value_iteration(v_initial,target_coord_tup,ll_block)
    print("--- %s seconds ---" % (time.time() - start_time))
