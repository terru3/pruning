SEED = 42
EPOCHS = 20  ## 100 during original training
BATCH_SIZE = 512
LR = 1e-3

PRUNE_PCT = 80

PRUNE_ITERS = 20
# I'm assuming too few iters and the model will be pruned too much each time, causing slow recovery?
# currently 80 PRUNE PCT and 20 PRUNE ITERS means we prune 7.7% each time, that's decently gradual imo

# # if PRUNE_PCT = 10, PRUNE_ITERS = 5, we want 90% of model params left at the end, so each iter we keep 0.9^(1/5) ≈ 97.9% of model
# thus each iter we prune 1-(0.9^(1/5)) ≈ 2.1%
PRUNE_ITER_PCT = (1 - ((1 - PRUNE_PCT / 100) ** (1 / PRUNE_ITERS))) * 100
EPS = 1e-6  # for identifying pruned weights in train

PRINT_ITERS = 30  # frequency to print train loss

# official (for MNIST) uses 20% PRUNE_ITER_PCT for layer0, layer1 and 10% for layer2, for 30 PRUNE_ITERS, and 50k iterations BS 64 each train
# ≈ so between 4.3%-12.3% overall remaining
# another implementation uses 10% for 35 iters and 100 epochs per train, 60 BS   ≈ 2.5% remaining
