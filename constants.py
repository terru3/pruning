SEED = 42
EPOCHS = 100
BATCH_SIZE = 512
LR = 1e-3

#### TODO: REMINDER to self that for now we are training a regular model till convergence
PRUNE_PCT = 0

PRUNE_ITERS = 5
# # if PRUNE_PCT = 10, PRUNE_ITERS = 5, we want 90% of model params left at the end, so each iter we keep 0.9^(1/5) ≈ 97.9% of model
# thus each iter we prune 1-(0.9^(1/5)) ≈ 2.1%
PRUNE_ITER_PCT = ( 1 - ( (1 - PRUNE_PCT/100)**(1/PRUNE_ITERS) ) ) * 100
EPS = 1e-7 # for identifying pruned weights in train

PRINT_ITERS = 30  # frequency to print train loss