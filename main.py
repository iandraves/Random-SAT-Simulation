import random
import time

# Initializing variables
ans_key = []
perfect_score = False
tests_taken = 0

# Generating answer key
for x in range(140):
    ans_key.append(random.randint(1, 4))

# Starting timer
start_time = time.time()

while not perfect_score:
    ran_test = []
    for r in ans_key:
        ran_test.append(random.randint(1, 4))
    tests_taken += 1
    print("Tests taken: " + str(tests_taken))
    if ran_test == ans_key:
        perfect_score = True

end_time = time.time()

print("It took: " + str(end_time - start_time) + " seconds")
