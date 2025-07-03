states = ['California','Texas','New york','California','Texas']
new_states =[]
[new_states.append(state) for state in states if state not in new_states]
print(new_states)