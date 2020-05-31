# Wine-Quality-Predictor
This implements linear regression model from scratch to predict the quality of wine

# Model Evaluation

**Simple Linear Regression**
* Mapping and Power: False 0
* dimensionality of the model parameter is (12,).
* model parameter is  [ 2.03721116e+02  1.09955585e-01 -1.93164831e+00 -4.90845226e-02
                      1.02194195e-01 -5.45232538e-02  4.00189586e-03  1.52537227e-04
                     -2.04673020e+02  9.04608186e-01  6.41578532e-01  1.32320100e-01]
* MAE on train is 0.58
* MAE on val is 0.59
* MAE on test is 0.56

**Handling Non-Invertible Matricies**
* Mapping and Power: False 0
* dimensionality of the model parameter is (12,).
* model parameter is  [ 1.72490981 -0.04898016 -2.05742338 -0.12068529  0.02838304 -0.81308859
                      0.00425276  0.          0.00675103  0.20653332  0.35756603  0.37653797]
* MAE on train is 0.58
* MAE on val is 0.59
* MAE on test is 0.55

*** Regularized Linear Regression ***
* Mapping and Power: False 0
* dimensionality of the model parameter is (12,).
* model parameter is  [ 1.72490981 -0.04898016 -2.05742338 -0.12068529  0.02838304 -0.81308859
                      0.00425276  0.          0.00675103  0.20653332  0.35756603  0.37653797]
* MAE on train is 0.58
* MAE on val is 0.59
* MAE on test is 0.55

**HyperParameter Tuning**
* Mapping and Power: False 0
* BM: (3519, 12)
* Best Lambda =  1e-19
* dimensionality of the model parameter is 12.
* model parameter is  [ 2.03721116e+02  1.09955585e-01 -1.93164831e+00 -4.90845226e-02
                      1.02194195e-01 -5.45232538e-02  4.00189586e-03  1.52537227e-04
                     -2.04673020e+02  9.04608186e-01  6.41578532e-01  1.32320100e-01]
* MAE on train is 0.58
* MAE on val is 0.59
* MAE on test is 0.56

**Polynomial Regression**
* Power = 2
* MX DiM: (4399, 22)
* White Dim: (4399, 23)
* AM: (3519, 23)
* Best Lambda =  1e-05
* dimensionality of the model parameter is 23.
* model parameter is  [ 1.25380814e+02  5.02384266e-01 -2.67773310e+00  9.80340263e-01
                      1.06212461e-01 -3.95578940e+00  2.39784392e-02  7.50076068e-03
                     -3.12000991e+01 -4.86978603e+00  4.09420291e-01 -8.46119515e-01
                     -2.72604969e-02  1.29686830e+00 -1.25860412e+00 -8.91481755e-04
                      1.57808283e+01 -2.28910275e-04 -2.75880957e-05 -8.24960635e+01
                      8.96138511e-01  1.80781412e-01  4.41502041e-02]
* MAE on train is 0.56
* MAE on val is 0.57
* MAE on test is 0.57

* Power = 3
* MX DiM: (4399, 33)
* White Dim: (4399, 34)
* AM: (3519, 34)
* Best Lambda is 0.0001
* MAE on train is 0.56
* MAE on val is 0.58
* MAE on test is 0.58

* Power = 4
* MX DiM: (4399, 44)
* White Dim: (4399, 45)
* AM: (3519, 45)
* Best Lambda is 0.0001
* MAE on train is 0.56
* MAE on val is 0.58
* MAE on test is 1.27

* Power = 5
* MX DiM: (4399, 55)
* White Dim: (4399, 56)
* AM: (3519, 56)
* Best Lambda is 0.01
* MAE on train is 0.55
* MAE on val is 0.57
* MAE on test is 4.99
