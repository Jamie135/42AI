import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from my_linear_regression import MyLinearRegression as MyLR
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("are_blue_pills_magics.csv")
Xpill = np.array(data['Micrograms']).reshape(-1, 1)
print(f"\nXpill: {Xpill}\n")
Yscore = np.array(data['Score']).reshape(-1, 1)
print(f"Yscore: {Yscore}\n")

# Initialize and fit linear regression models
thetas = np.array([[0.0], [0.0]])
linear_model1 = MyLR(thetas, alpha=0.01, max_iter=1000)
linear_model1.fit_(Xpill, Yscore)
print(f"thetas: {linear_model1.fit_(Xpill, Yscore)}\n")


# Predict values
Y_model1 = linear_model1.predict_(Xpill)
print(f"Y_model1: {Y_model1}\n")

# Calculate MSE
mse1 = MyLR.mse_(Yscore, Y_model1)

print(f"MSE Model 1: {mse1}\n")

# Plot the data and the hypothesis
plt.scatter(Xpill, Yscore, color='blue', label='$S_{real}$(pills)')
plt.plot(Xpill, Y_model1, color='green', label='$S_{predict}$(pills)', linestyle='dashed')
for i in range(len(Xpill)):
    plt.scatter(Xpill[i], Y_model1[i], color='green', marker='x')
plt.xlabel('Quantity of blue pill (in micrograms)')
plt.ylabel('Space driving score')
plt.legend()
plt.title('Space driving score as a function of the quantity of blue pill (in micrograms)')
plt.show()


# Plot the loss function J(theta) in function of the theta values



# SUBJECT EXAMPLE
linear_model1 = MyLR(np.array([[89.0], [-8]]))
linear_model2 = MyLR(np.array([[89.0], [-6]]))
Y_model1 = linear_model1.predict_(Xpill)
Y_model2 = linear_model2.predict_(Xpill)
print(MyLR.mse_(Yscore, Y_model1))
# 57.60304285714282
print(mean_squared_error(Yscore, Y_model1))
# 57.603042857142825
print(MyLR.mse_(Yscore, Y_model2))
# 232.16344285714285
print(mean_squared_error(Yscore, Y_model2))
# 232.16344285714285
