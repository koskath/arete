# Slide 16 of Lecture 12 contains a table with information about the Hyper-parameters.

Columns: ML Algorithm, Main HPs, Optional HPs, HPO methods, Libraries

Row 1:
- Column ML Algorithm: Linear regression
- Column Main HPs: –
- Column Optional HPs: –
- Column HPO methods: –
- Column Libraries: –

Row 2:
- Column ML Algorithm: Ridge & lasso
- Column Main HPs: alpha
- Column Optional HPs: –
- Column HPO methods: BO-GP
- Column Libraries: Skopt

Row 3:
- Column ML Algorithm: Logistic regression
- Column Main HPs: penalty, C, solver
- Column Optional HPs: –
- Column HPO methods: BO-TPE, SMAC
- Column Libraries: Skopt, Hyperopt, SMAC

Row 4:
- Column ML Algorithm: KNN
- Column Main HPs: n_neighbors
- Column Optional HPs: weights, p, algorithm
- Column HPO methods: BOs, Hyperband
- Column Libraries: Hyperband

Row 5:
- Column ML Algorithm: SVM
- Column Main HPs: C, kernel, epsilon (for SVR)
- Column Optional HPs: gamma, coef0, degree
- Column HPO methods: BO-TPE, SMAC, BOHB
- Column Libraries: Hyperopt, SMAC, BOHB

Row 6:
- Column ML Algorithm: NB
- Column Main HPs: alpha
- Column Optional HPs: –
- Column HPO methods: BO-GP
- Column Libraries: Skopt

Row 7:
- Column ML Algorithm: DT
- Column Main HPs: criterion, max_depth, min_samples_split, min_samples_leaf, max_features
- Column Optional HPs: splitter, min_weight_fraction_leaf, max_leaf_nodes
- Column HPO methods: GA, PSO, BO-TPE, SMAC, BOHB
- Column Libraries: TPOT, Optunity, SMAC, BOHB

Row 8:
- Column ML Algorithm: RF & ET
- Column Main HPs: n_estimators, max_depth, criterion, min_samples_split, min_samples_leaf, max_features
- Column Optional HPs: splitter, min_weight_fraction_leaf, max_leaf_nodes
- Column HPO methods: GA, PSO, BO-TPE, SMAC, BOHB
- Column Libraries: TPOT, Optunity, SMAC, BOHB

Row 9:
- Column ML Algorithm: XGBoost
- Column Main HPs: n_estimators, max_depth, learning_rate, subsample, colsample_bytree
- Column Optional HPs: min_child_weight, gamma, alpha, lambda
- Column HPO methods: GA, PSO, BO-TPE, SMAC, BOHB
- Column Libraries: TPOT, Optunity, SMAC, BOHB

Row 10:
- Column ML Algorithm: Voting
- Column Main HPs: estimators, voting
- Column Optional HPs: weights
- Column HPO methods: GS
- Column Libraries: Sklearn

Row 11:
- Column ML Algorithm: Bagging
- Column Main HPs: base_estimator, n_estimators
- Column Optional HPs: max_samples, max_features
- Column HPO methods: GS, BOs
- Column Libraries: sklearn, Skopt, Hyperopt, SMAC

Row 12:
- Column ML Algorithm: AdaBoost
- Column Main HPs: base_estimator, n_estimators, learning_rate
- Column Optional HPs: –
- Column HPO methods: BO-TPE, SMAC
- Column Libraries: Hyperopt, SMAC

Row 13:
- Column ML Algorithm: Deep learning
- Column Main HPs: number of hidden layers, 'units' per layer, loss, optimizer, Activation, learning_rate, dropout rate, epochs, batch_size, early stop patience
- Column Optional HPs: number of frozen layers (if transfer learning is used)
- Column HPO methods: PSO, BOHB
- Column Libraries: Optunity, BOHB

Row 14:
- Column ML Algorithm: K-means
- Column Main HPs: n_clusters
- Column Optional HPs: init, n_init, max_iter
- Column HPO methods: BOs, Hyperband
- Column Libraries: Skopt, Hyperopt, SMAC, Hyperband

Row 15:
- Column ML Algorithm: Hierarchical clustering
- Column Main HPs: n_clusters, distance_threshold
- Column Optional HPs: linkage
- Column HPO methods: BOs, Hyperband
- Column Libraries: Skopt, Hyperopt, SMAC, Hyperband

Row 16:
- Column ML Algorithm: DBSCAN
- Column Main HPs: eps, min_samples
- Column Optional HPs: –
- Column HPO methods: BO-TPE, SMAC, BOHB
- Column Libraries: Skopt, Hyperopt, SMAC, BOHB

Row 17:
- Column ML Algorithm: Gaussian mixture
- Column Main HPs: n_components
- Column Optional HPs: covariance_type, max_iter, tol
- Column HPO methods: BO-GP
- Column Libraries: Skopt

Row 18:
- Column ML Algorithm: PCA
- Column Main HPs: n_components
- Column Optional HPs: svd_solver
- Column HPO methods: BOs, Hyperband
- Column Libraries: Skopt, Hyperopt, SMAC, Hyperband

Row 19:
- Column ML Algorithm: LDA
- Column Main HPs: n_components
- Column Optional HPs: solver, shrinkage
- Column HPO methods: BOs, Hyperband
- Column Libraries: Skopt, Hyperopt, SMAC, Hyperband
