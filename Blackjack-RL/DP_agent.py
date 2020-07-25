import numpy as np 

#generate state space, initial policy, transition probababilities and rewards (0 on each action, 21 -> +1, bust -> -1)
def generate_blackjack_environment():
    #state space comprises of possible hand values all anything below going bust and going bust,
    #legal hand values go from 4 to 21
    #treating going bust (>21) as the same state (22)
    state_space = np.arange(4,23)
    #rewards
    rewards = np.zeros(len(state_space))
    rewards[17] = 5
    rewards[18] = -1
    #generating initial policy
    #policy is a dictionary with 2 sections hit and stick each being a list
    #index of policy list indicates prob of doing that action in equivalent state index
    hit = []
    stick = []
    #policy[0] - hit probabilities for each state
    #policy[1] - stick probablitites for each state
    policy = [[], []]
    for i in range(0, len(state_space)):
        hit.append(0.5)
        stick.append(0.5)
    #hit[17] = 0
    #stick[17] = 1
    #hit[18] = 0
    #stick[18] = 0  
    policy[0] = hit
    policy[1] = stick
    #compiling transition probabilities
    #3D list containing transition probabilities
    #list in form state x action hit/stick(0,1) x transition probabilities
    transition_prob = [
    [[0,0,1/13,1/13,1/13,1/13,1/13,1/13,1/13,1/13,4/13,1/13,0,0,0,0,0,0,0], [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]], #state 0
    [[0,0,0,1/13,1/13,1/13,1/13,1/13,1/13,1/13,1/13,4/13,1/13,0,0,0,0,0,0], [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]], #state 1
    [[0,0,0,0,1/13,1/13,1/13,1/13,1/13,1/13,1/13,1/13,4/13,1/13,0,0,0,0,0], [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]], #state 2
    [[0,0,0,0,0,1/13,1/13,1/13,1/13,1/13,1/13,1/13,1/13,4/13,1/13,0,0,0,0], [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]], #state 3
    [[0,0,0,0,0,0,1/13,1/13,1/13,1/13,1/13,1/13,1/13,1/13,4/13,1/13,0,0,0], [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]], #state 4
    [[0,0,0,0,0,0,0,1/13,1/13,1/13,1/13,1/13,1/13,1/13,1/13,4/13,1/13,0,0], [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]], #state 5
    [[0,0,0,0,0,0,0,0,1/13,1/13,1/13,1/13,1/13,1/13,1/13,1/13,4/13,1/13,0], [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]], #state 6
    [[0,0,0,0,0,0,0,0,1/13,1/13,1/13,1/13,1/13,1/13,1/13,1/13,1/13,4/13,0], [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]], #state 7
    [[0,0,0,0,0,0,0,0,0,1/13,1/13,1/13,1/13,1/13,1/13,1/13,1/13,1/13,4/13], [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]], #state 8
    [[0,0,0,0,0,0,0,0,0,0,1/13,1/13,1/13,1/13,1/13,1/13,1/13,1/13,5/13], [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]], #state 9
    [[0,0,0,0,0,0,0,0,0,0,0,1/13,1/13,1/13,1/13,1/13,1/13,1/13,6/13], [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]], #state 10
    [[0,0,0,0,0,0,0,0,0,0,0,0,1/13,1/13,1/13,1/13,1/13,1/13,7/13], [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]], #state 11
    [[0,0,0,0,0,0,0,0,0,0,0,0,0,1/13,1/13,1/13,1/13,1/13,8/13], [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]], #state 12
    [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1/13,1/13,1/13,1/13,9/13], [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]], #state 13
    [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1/13,1/13,1/13,10/13], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]], #state 14
    [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1/13,1/13,11/13], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]], #state 15
    [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1/13,12/13], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]], #state 16
    [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]], #state 17
    [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]  #state 18
    ]

    return state_space, rewards, policy, transition_prob

#helper function to perform one-step lookaheads returns an array of the value of each action
#length of this in this case is 2 as 2 actions(hit, stick), function will be used to perform policy improvement
def one_step_lookahead(state_space, state, V, discount_factor, rewards, policy, transition_probs):
    action_values = np.zeros(2)
    for action in range(len(action_values)):
        #print(action)
        for i in range(len(state_space)):
            action_values[action] += policy[action][state] * transition_probs[state][action][i] * (rewards[i] + discount_factor * V[i])
    return action_values

#policy evaluation function
def policy_evaluation(policy, state_space, rewards, transition_probs, discount_factor = 1.0, theta = 0.0001, max_iterations = 10000):
    evaluation_iterations = 0
    #initialising value function [V(s)] for each state to 0
    V = np.zeros(len(state_space))
    #this loops until change in value is below threshold (theta) or max_iterations is attained
    for i in range (max_iterations):
        delta = 0
        #iterating through each state
        for state_index in range(len(state_space)):
            #print(state_index)
            v = 0
            for j in range(len(state_space)):
                #calculate value function, seperate calc for each action sepererated, 
                #rewards[j] is immediate reward, V[j] is the value of next states
                #hit calc 
                v += policy[0][state_index] * transition_probs[state_index][0][j] * (rewards[j] + discount_factor * V[j])
                #adding stick calc
                v += policy[1][state_index] * transition_probs[state_index][1][j] * (rewards[j] + discount_factor * V[j])
            #calculating absolute change
            delta = max(delta, np.abs(V[state_index] - v))
            #print(delta)
            #updating value function
            V[state_index] = v
            #print(V[7])
        evaluation_iterations += 1
        if delta < theta:
            print(f'policy evaluated in {evaluation_iterations} iterations')
            return V
    #if algorithm reaches max_iteration before converging to theta
    #print('policy evaluation did not converge to theta, state-values up to that point:')
    #print(V)
    return V

#policy improvement functions, attempting both policy and value iteration
def policy_iteration(policy, state_space, rewards, transition_probs, discount_factor = 1.0, max_iterations = 10000):
    initial_policy = policy
    print('initial policy:')
    print(initial_policy)
    evaluated_policies = 0
    for i in range(max_iterations):
        policy_stable = True
        V = policy_evaluation(policy, state_space, rewards, transition_probs, discount_factor, theta = 0.0001)
        for state in range(len(state_space)):
            action_check = [policy[0][state], policy[1][state]]
            old_action = np.argmax(action_check)
            #using one step lookahead to see if old_action is optimal, by testing all possible actions from state
            action_value = one_step_lookahead(state_space, state, V, discount_factor, rewards, policy, transition_probs)
            print(f'state: {state}, action values:{action_value}')
            #select best action according to values
            new_action = np.argmax(action_value)
            if old_action != new_action:
                policy_stable = False
                #print('UPDATING POLICY')
                #update policy in greedy manner
                update = np.eye(2)[new_action]
                policy[0][state] = update[0]
                policy[1][state] = update[1]
        evaluated_policies += 1
        #if policy isnt changing anymore stops and returns optimal V and policy
        if policy_stable:
            print(f'{evaluated_policies} policy evaluation(s)')
            return V, policy

def value_iteration(policy, state_space, rewards, transition_probs, discount_factor = 1.0, max_iterations = 10000, theta = 0.0001):
    V = np.zeros(len(state_space))
    for i in range (max_iterations):
        delta = 0
        for state in range(len(state_space)):
            #one step lookahead to calculate action values
            action_value = one_step_lookahead(state_space, state, V, discount_factor, rewards, policy, transition_probs)
            best_action_value = np.max(action_value)
            delta = max(delta, np.abs(V[state] - best_action_value))
            V[state] = best_action_value
        if delta < theta:
            print(f'Value iteration converged at iteration {i}')
            break
    #output deterministic policy
    det_policy = np.zeros([len(state_space), 2])
    for state in range(len(state_space)):
        action_value = one_step_lookahead(state_space, state, V, discount_factor, rewards, policy, transition_probs)
        best_action = np.argmax(action_value)
        det_policy[state, best_action] = 1.0
    return V, det_policy

def main():
    state_space, rewards, policy, transition_probs = generate_blackjack_environment()
    #test = policy_evaluation(policy, state_space, rewards, transition_probs)
    #test2 = one_step_lookahead(state_space, state_space, state_space, state_space, rewards)
    V_star, pi_star = policy_iteration(policy, state_space, rewards, transition_probs)
    #V_star_2, pi_star_2 = value_iteration(policy, state_space, rewards, transition_probs)
    print('optimal values:')
    print(V_star)
    #print(V_star_2)
    print('optimal policy:')
    print(pi_star)
    #print(pi_star_2)
    
if __name__ == '__main__':
    main()