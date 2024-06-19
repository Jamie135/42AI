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
model = MyLR(thetas, alpha=0.01, max_iter=1000)
model.fit_(Xpill, Yscore)
print(f"Fitted thetas: {model.fit_(Xpill, Yscore)}\n")


# Predict values
Y_model1 = model.predict_(Xpill)
print(f"Y_model1: {Y_model1}\n")

# Calculate MSE
mse1 = MyLR.mse_(Yscore, Y_model1)

print(f"MSE Model: {mse1}\n")

# Plot the data and the hypothesis
plt.scatter(Xpill, Yscore, color='blue', label='$S_{real}$(pills)')
plt.plot(Xpill, Y_model1, color='green', label='$S_{predict}$(pills)', linestyle='dashed')
for i in range(len(Xpill)):
    plt.scatter(Xpill[i], Y_model1[i], color='green', marker='x')
plt.xlabel('Quantity of blue pill (in micrograms)')
plt.ylabel('Space driving score')
plt.legend()
plt.grid(True)
plt.title('Space driving score as a function of the quantity of blue pill (in micrograms)')
plt.show()


# Step 3: Plot the Loss Function
theta0_vals = [-50, 0, 50, 100]
theta1_vals = np.linspace(-10, 10, 100)
plt.figure(figsize=(12, 8))

# for each θ0, we will compute the loss J(θ) for various θ1 values
for theta0 in theta0_vals:
    # list to store all loss values for the current θ0
    losses = []
    for theta1 in theta1_vals:
        # set the mode's thetas to the current θ0 and θ1
        model.thetas = np.array([[theta0], [theta1]])
        # predict the the output using the current thetas and Xpill
        y_hat = model.predict_(Xpill)
        # compute the loss using the prediction and Yscore
        # then append the result to the losses list
        loss = model.loss_(Yscore, y_hat)
        losses.append(loss)
    # plot the list of losses against all θ1 values for the current θ0
    plt.plot(theta1_vals, losses, label=f'J(θ0={theta0},θ1)')

plt.xlabel('θ1')
plt.ylabel('cost function J(θ0,θ1)')
plt.title('Evolution of the loss function J as a function of θ1 for different values of θ0')
plt.legend()
plt.grid(True)
plt.show()



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
