# Linear Regression

[scikit-learn](https://bigdata-madesimple.com/how-to-run-linear-regression-in-python-scikit-learn/)
[Real Python: Linear Regression](https://realpython.com/linear-regression-in-python/)
[jbstatistics video](https://www.youtube.com/watch?v=KsVBBJRb9TE)
[]()



Regression explores teh relationship between a quantitative response and explanatory variables.

- Simple Regression: 1 explanatory variable
- Multiple Regression: more than 1 variable

- y: Response/Dependent Variable variable to predict
- x: Explanatory/Independent Variable

Linear Relationships are represented with a line representing the mean given a value of x.




## Scikit-learn

```python
%matplotlib inline

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn

# Data available in module
from sklearn.datasets import load_boston
boston = load_boston()
```

### linear regression object

```python
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
```

### Fit Linear Model

```python
lm.fig(DF, dataColumn)

import numpy as np
from sklearn.linear_model import LinearRegression

# Create Model
model = LinearRegression()
model = LinearRegression().fit(x, y) # one line fit

# Coefficient
r_sq = model.score(x, y)

# Predict Response
y_pred = model.predict(x)



```
#### Model Methods

- model.fit()
- model.intercept_
- model.coef_
- model.predict(x)



### Scatter Plot

```python
plt.scatter(x, y)
plt.xlabel('string')
plt.ylabel('string')
ptl.title('string')
plt.show()
```

lm.predict(DF)[:#]


### test_train_split

- from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = sklearn.cross_validation.train_test_split(x, y, test_size=0.33, random_state=5)

### Polynomial Regression

```python
from sklearn.preprocessing import PolynomialFeatures
transformer = PolynomialFeatures(degree=2, include_bias=False)

# Modify X array
x_ = transformer.transform(x)



```
