# Reinforcement-Learning
This repository contains code for the implementation of value iteration and q learning for the purpose of solving a maze. Please refer to hw8.pdf for detailed explanation of the problem statement.

The maze is given as an input file to both the algorithms. '.' in maze represents reachable state, 'asterik' in maze represents cannot move to this state, 'S' represents start state and 'G' represents target state.

0->left
1->up
2->right
3->down

1) Value Iteration:

The code implements synchronous value iteration. 
For the purpose of running the code: 
python value_iteration.py tiny_maze.txt value_output.txt q_value_output.txt policy_output.txt 5 0.9

Input parameter 5 represents the number of epochs for which you wish to run your algorithm.
Input parameter 6 represents the discount factor.

The output files: 
value_output.txt contains the value function values for each valid state of the maze.
q_value_output.txt contains the q-value for each action possible from each of the valid states.
policy_output.txt contains the actions taken at each valid state to reach the target. 


2) Q Learning:

For the purpose of Q-learning we assume that we don't have model of the world and we act and get reward from the environment. The algorithm doesn't explicitly have access to the state transition and reward functions as we had for value iteration and relies on the environment for that purpose. Therefore we implement an environment class and import it in our q_learning algorithm. The environment class has functions that replicates the state transition probabilities and provide rewards and next state to the q_learning algorithm.

python environment.py medium_maze.txt output.feedback action_seq.txt

This is for testing the environment file for given maze and the action sequence and the corresponding output. 

python q_learning.py tiny_maze.txt value_output.txt q_value_output.txt policy_output.txt 1000 20 0.8 0.9 0.05

1. <maze input>: path to the environment input .txt described previously
2. <value file>: path to output the values V (s)
3. <q value file>: path to output the q-values Q(s; a)
4. <policy file>: path to output the optimal actions (s)
5. <num episodes>: the number of episodes your program should train the agent for. One episode is a sequence of states, actions and rewards, which ends with terminal state or ends when the maximum episode length has been reached.
6. <max episode length>: the maximum of the length of an episode. When this is reached, we terminate the current episode.
7. <learning rate>: the learning rate alpha of the q learning algorithm
8. <discount factor>: the discount factor 
9. <epsilon>: the value epsilon for the epsilon-greedy strategy
