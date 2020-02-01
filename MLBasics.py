import pandas as pd 
df = pd.read_csv(path)

df.shape
df.describe()
df.head()
df.columns
df = df.dropna(axis = 0)




from sklearn.tree import DecisionTreeRegressor

model = DecisionTreeRegressor(random_state  = 1, max_leaf_nodes = num)
# We can change default parameter max_leaf_nodes sensibly, to controll overfitting
# vs underfitting.  try using (50, 500, 5000)



model.fit(X, y)
new_y = model.predict(nex_X)


from sklearn.metrics import mean_absolute_error

preds = model.predict(some_X)
mean_absolute_error(actual_y, preds)



from sklearn.model_selection import train_test_split

train_X, Val_X, train_Y, val_y = train_test_split(X, y, random_state=1)

model.fit(train_X, train_Y)
preds = model.predict(Val_X)

mean_absolute_error(val_y, preds)     #We want to minimize this error.







from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(random_state = 1)
# We can tweak n_estimators parameter (50, 100)

model.fit()
model.predict()


--------------------------------------------------------------------


# Missing Values

#  We can either drop entire column
Missing_cols = [col for col in X.columns if X[col].isnull().any()]
X = X.drop(Missing_cols, axis = 1)

# Drop rows
X = X.dropna(axis = 0)

#Imputer

from sklearn.impute import SimpleImputer

imputer = SimpleImputer()

# Remember dont impute values of Y, instead drop those rows having missing values of y
imputed_train_X = pd.DataFrame(imputer.fit_transform(train_X))
imputed_test_X = pd.DataFrame(imputer.transform(test_X))

#Imputation removes column names.
imputed_train_X = train_X.columns
imputed_test_X = test_X.columns



#Create an extra column to specify imputed values, do it before imputation.
X[col+' was missing '] = X[col].isnull()



-----------------------------------------------------------------------

# Categorical Variables
dtype == 'object'



# Label encoding is good for tree based model, but not for Regression based model.
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()

label_train_X = train_X.copy()
label_train_X[col] =  encoder.fit_transform(train_X[col])
label_test_X[col] = encoder.transform(test_X[col])



from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(handle_unknown = 'ignore', sparse = False)

encoded_col = pd.DataFrame(encoder.fit_transform(train_X[object_col]))
encoded_col.index = train_X.index



-------------------------------------------------------------------------------------

# XGBoost

from xgboost import XGBRegressor

model = XGBRegressor(n_estimators = 100/1000, learning_rate = 0.05)
model.fit(train_X, train_Y,
	early_stopping_rounds = 5, eval_set = [(test_X, test_y)], 
	verbose = False)


# learning rate helps us to increase value of n_estimators without overfitting data, 
# since we are making preds by multiplying pred of each component model, by a small number 
# (r)












