"""
Module 2 — Drill 2: Learner Test File

Write your two pytest test functions below.
The autograder will run these as part of the CI check.
"""

import pandas as pd
import numpy as np
from drill_functions import clean_column, compute_revenue


def test_clean_column():

    s = pd.Series([10.0, 20.0, np.nan, 40.0, 50.0])
    
    result = clean_column(s)

    assert result.isna().sum() == 0
    assert result[2] == 30.0

def test_compute_revenue():

    quantity = pd.Series([2, 5, 3])
    price = pd.Series([10.0, 20.0, 5.0])
    
    expected_result = pd.Series([20.0, 100.0, 15.0])
    
    result = compute_revenue(quantity, price)
    
    pd.testing.assert_series_equal(result, expected_result)