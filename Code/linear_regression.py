"""
Do not change the input and output format.
If our script cannot run your code or the format is improper, your code will not be graded.

The only functions you need to implement in this template is linear_regression_noreg, linear_regression_invertible，regularized_linear_regression,
tune_lambda, test_error and mapping_data.
"""

import numpy as np
import pandas as pd

###### Q1.1 ######
def mean_absolute_error(w, X, y):
    """
    Compute the mean absolute error on test set given X, y, and model parameter w.
    Inputs:
    - X: A numpy array of shape (num_samples, D) containing test feature.
    - y: A numpy array of shape (num_samples, ) containing test label
    - w: a numpy array of shape (D, )
    Returns:
    - err: the mean absolute error
    """
    #####################################################
    # TODO 1: Fill in your code here #
    #####################################################
    sum_of_errors = 0
    for weighted_label, label in zip(np.dot(X, w), y):
        sum_of_errors += abs(weighted_label - label)
    err = sum_of_errors/len(y)
    return err

###### Q1.2 ######
def linear_regression_noreg(X, y):
    w = None
    w = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, y))
    return w


###### Q1.3 ######
def linear_regression_invertible(X, y):
    """
    Compute the weight parameter given X and y.
    Inputs:
    - X: A numpy array of shape (num_samples, D) containing feature.
    - y: A numpy array of shape (num_samples, ) containing label
    Returns:
    - w: a numpy array of shape (D, )
    """
    #####################################################
    # TODO 3: Fill in your code here #
    #####################################################
    w = None
    N, D = X.shape
    non_invertible = False
    xtx = np.dot(X.T, X)
    if np.amin(np.abs(np.linalg.eigvals(xtx))) <= 10**-5:
        non_invertible = True
    while non_invertible:
        xtx += 10**-1 * np.identity(D)
        if np.amin(np.abs(np.linalg.eigvals(xtx))) <= 10**-5:
            non_invertible = True
        else:
            non_invertible = False
    w = np.dot(np.linalg.inv(xtx), np.dot(X.T, y))
    return w


###### Q1.4 ######
def regularized_linear_regression(X, y, lambd):
    """
    Compute the weight parameter given X, y and lambda.
    Inputs:
    - X: A numpy array of shape (num_samples, D) containing feature.
    - y: A numpy array of shape (num_samples, ) containing label
    - lambd: a float number containing regularization strength
    Returns:
    - w: a numpy array of shape (D, )
    """
  #####################################################
  # TODO 4: Fill in your code here #
  #####################################################
    w = None
    N, D = X.shape
    w = np.dot(np.linalg.inv(np.dot(X.T, X) + lambd*np.identity(D)), np.dot(X.T, y))
    return w

###### Q1.5 ######
def tune_lambda(Xtrain, ytrain, Xval, yval):
    """
    Find the best lambda value.
    Inputs:
    - Xtrain: A numpy array of shape (num_training_samples, D) containing training feature.
    - ytrain: A numpy array of shape (num_training_samples, ) containing training label
    - Xval: A numpy array of shape (num_val_samples, D) containing validation feature.
    - yval: A numpy array of shape (num_val_samples, ) containing validation label
    Returns:
    - bestlambda: the best lambda you find in lambds
    """
    #####################################################
    # TODO 5: Fill in your code here #
    #####################################################
    bestlambda = None
    power_10_range = [10**i for i in range(-19, 20)]
    maes = []
    for l in power_10_range:
        weights = regularized_linear_regression(Xtrain, ytrain, l)
        err = mean_absolute_error(weights, Xval, yval)
        maes.append(err)
    min_mae = min(maes)
    bestlambda = power_10_range[maes.index(min_mae)]
    return bestlambda


###### Q1.6 ######
def mapping_data(X, power):
    """
    Mapping the data.
    Inputs:
    - X: A numpy array of shape (num_training_samples, D) containing training feature.
    - power: A integer that indicate the power in polynomial regression
    Returns:
    - X: mapped_X, You can manully calculate the size of X based on the power and original size of X
    """
    #####################################################
    # TODO 6: Fill in your code here #
    #####################################################
    N, D = X.shape
    resultant = X
    if power > 1:
        for i in range(2, power+1):
            x_new = np.power(X, i)
            resultant = np.concatenate((resultant, x_new), axis = 1)
    return resultant


