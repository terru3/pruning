# Roadmap

This roadmap documents action items such as features or bugs to be developed/fixed.

_Updated: 16 Jan 2024, 02:15 GMT_

## Pruning

| Status | Item                                                                                                                                                          |
| :----: | :------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   ✔    | Create README and ROADMAP                                                                                                                                     |
|   ✔    | Train original model to convergence                                                                                                                           |
|   ✔    | Conduct LTH pruning experiments (did not train each pruned model to convergence, however, only 20 epochs due to compute restrictions)                         |
|   ❌   | Implement early stopping criteria rather than training a fixed amount                                                                                         |
|   ❌   | Implement [supermask-related variants/optimizations](https://arxiv.org/abs/1905.01067) (e.g. "large final same sign" criteria, "freeze_init_zero_all" action) |
