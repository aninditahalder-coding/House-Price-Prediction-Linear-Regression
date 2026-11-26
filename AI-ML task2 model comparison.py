#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as mlt

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

from sklearn.metrics import mean_squared_error,r2_score
from sklearn.linear_model import Ridge






# In[5]:


#loading the datasets
data=fetch_california_housing(as_frame=True)
#combine input features and target variable
df=pd.concat([data.data,data.target.rename("HousePrice")],axis=1)
df.head()


# In[6]:


#seperate the input features and target variable
X=df.drop("HousePrice", axis=1)
y=df["HousePrice"]
#display the shapes
print("Features shape=",X.shape)
print("Target Shape=",y.shape)




# In[7]:


#splitting the dataset into training and testing
X_train, X_test,y_train, y_test=train_test_split(X,y,test_size=0.2,random_state=42)

#display the shapes
print("X_train =",X_train.shape)
print("X_test =",X_test.shape)
print("y_train =",y_train.shape)
print("y_test =",y_test.shape)



# In[8]:


#create the standardscaler object
scaler=StandardScaler()
X_train_scaled=scaler.fit_transform(X_train)
#transform the testing data
X_test_scaled=scaler.transform(X_test)
#Display the shapes
print("Scaled training data=",X_train_scaled.shape)
print("Scaled test data=",X_test_scaled.shape)



# In[9]:


#linear regression model
lr_model=LinearRegression()
lr_model.fit(X_train_scaled,y_train)
print("Linear regression model trained successfully")


# In[10]:


#making predictions using the lr trained model
lr_predictions=lr_model.predict(X_test_scaled)
#display first 5 predicytions
print("Fisrt 5 predicted house prices")
print(lr_predictions[:5])



# In[11]:


#calculate the mean absolute error
mae=np.mean(np.abs(y_test-lr_predictions))
#caculate rmse
rmse=np.sqrt(mean_squared_error(y_test,lr_predictions))
#calculate r2 square
r2=r2_score(y_test,lr_predictions)

#display the evaluated results
print("Linear regression model evaluation")
print("MAE=",mae)
print("RMSE=",rmse)
print("R2 Score:", r2)


# In[18]:


#create ridge regression
from sklearn.linear_model import Ridge
ridge_model=Ridge(alpha=1.0)


# In[23]:


#train the ride-regression model
ridge_model.fit(X_train,y_train)
print("Ridge regression model trained successfully")


# In[26]:


# Generate predictions
ridge_predictions = ridge_model.predict(X_test)
# Calculate MAE
ridge_mae = np.mean(np.abs(y_test - ridge_predictions))

# Calculate RMSE
ridge_rmse = np.sqrt(mean_squared_error(y_test,ridge_predictions))

# Calculate R2 Score
ridge_r2 = r2_score(y_test, ridge_predictions)

# Display evaluation results
print("Ridge Regression Model Evaluation")
print("MAE:", ridge_mae)
print("RMSE:", ridge_rmse)
print("R2 Score:", ridge_r2)


# In[27]:


#decision tree regression
dt_model=DecisionTreeRegressor(random_state=42)
dt_model.fit(X_train,y_train)
print("Decision tree modeled successfully")


# In[28]:


dt_predictions=dt_model.predict(X_test)
print("First 5 Decision tree predictions ")
print(dt_predictions[:5])


# In[29]:


dt_mae=np.mean(np.abs(y_test-dt_predictions))
dt_rmse=np.sqrt(mean_squared_error(y_test,dt_predictions))
dt_r2=r2_score(y_test,dt_predictions)
print("Decision tree model evaluation")
print("MAE=",dt_mae)
print("RMSE=",dt_rmse)
print("R2 Score=",dt_r2)


# In[30]:


# Create a dictionary to store model evaluation results

results = {
    "Model": ["Linear Regression", "Ridge Regression", "Decision Tree"],
    "MAE": [mae, ridge_mae, dt_mae],
    "RMSE": [rmse, ridge_rmse, dt_rmse],
    "R2 Score": [r2, ridge_r2, dt_r2]
}

# Convert dictionary into DataFrame
results_df = pd.DataFrame(results)

# Display comparison table
results_df


# In[34]:


import matplotlib.pyplot as plt
plt.figure(figsize=(8,5))
plt.bar(results_df["Model"],results_df["MAE"])
plt.title("MAE comparison")
plt.xlabel("Models")
plt.ylabel("Mean Absolute Error")
plt.xticks(rotation=15)

plt.show()


# In[35]:


plt.figure(figsize=(8,5))

plt.bar(results_df["Model"], results_df["RMSE"])

plt.title("RMSE Comparison")
plt.xlabel("Models")
plt.ylabel("Root Mean Squared Error")
plt.xticks(rotation=15)

plt.show()


# In[36]:


plt.figure(figsize=(8,5))

plt.bar(results_df["Model"], results_df["R2 Score"])

plt.title("R2 Score Comparison")
plt.xlabel("Models")
plt.ylabel("R2 Score")
plt.xticks(rotation=15)

plt.show()


# In[37]:


best_model = results_df.loc[results_df["R2 Score"].idxmax()]

print("Best Performing Model:")
print(best_model)


# In[38]:


results_df.to_csv("model_comparison.csv", index=False)

print("Model comparison saved successfully!")


# In[49]:


if best_model["Model"]=="Linear Regression":
    best_predictions=y_pred
elif best_model["Model"] == "Ridge Regression":
    best_predictions = ridge_predictions
else:
    best_predictions = dt_predictions



# In[40]:


plt.figure(figsize=(8,5))
plt.scatter(y_test, best_predictions, alpha=0.5)
plt.xlabel("Actual House Prices")
plt.ylabel("Predicted House Prices")
plt.title("Actual vs Predicted House Prices")

plt.show()


# In[50]:


if best_model["Model"] == "Linear Regression":
    final_model = model

elif best_model["Model"] == "Ridge Regression":
    final_model = ridge_model

else:
    final_model = dt_model

print("Best model selected successfully!")


# In[42]:


import pickle
with open("best_house_price_model.pkl", "wb") as file:
    pickle.dump(final_model, file)

print("Best model saved successfully!")


# In[43]:


with open("best_house_price_model.pkl", "rb") as file:
    loaded_model = pickle.load(file)

print("Model loaded successfully!")


# In[45]:


sample_predictions = loaded_model.predict(X_test[:5])

print("Predicted House Prices:")
print(sample_predictions)


# In[46]:


print("FINAL MODEL PERFORMANCE")
print("------------------------")

print("Best Model:", best_model["Model"])
print("MAE:", best_model["MAE"])
print("RMSE:", best_model["RMSE"])
print("R2 Score:", best_model["R2 Score"])


# In[47]:


comparison = pd.DataFrame({
    "Actual Price": y_test[:5].values,
    "Predicted Price": sample_predictions
})

print(comparison)


# In[48]:


comparison.to_csv("prediction_comparison.csv", index=False)

print("Prediction comparison saved successfully!")

