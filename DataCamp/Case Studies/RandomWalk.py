# 3 of case study

import numpy as np
np.ramdom.seed(123)


# Initializing random_walk
random_walk= [0]

for x in range(100):
    # Setting step: last element in random_walk
    step = random_walk[-1]
    # Roll the dice
    dice = np.random.randint(1,7)

    # Determining next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # appending next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)
