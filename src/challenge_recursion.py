import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression, SGDRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error  
import matplotlib.pyplot as plt


"""Data cleaning part i'm not happy with it cause of lack of time i wasn't able to make a good cleaner
I dropped to mutch columns i would have fixed some more so i could have a better score
"""
def data_clean(properties):
    
    columns_to_drop = ['id', 'Street', 'Housenumber', 'Box', 'Floor', 'Subtype', 'Lacation area',
                    'District', 'Province', 'Type of sale', 'Kitchen type', 'Furnished',
                    'Fireplace', 'Terrace', 'Garden', 'Facades', 'Condition', 'EPC score',
                    'Latitude', 'Longitude', 'Property url','Construction year']

    properties.drop(columns=columns_to_drop, inplace=True)

    properties.drop_duplicates(inplace=True)


    properties.dropna(inplace=True)


    text_columns = properties.select_dtypes(include='object').columns
    properties.drop(columns=text_columns, inplace=True)


    correlation_matrix = properties.corr().abs()
    correlated_features = correlation_matrix.where(np.triu(np.ones(correlation_matrix.shape), k=1).astype(bool)).stack().sort_values(ascending=False)
    highly_correlated = correlated_features[correlated_features > 0.8].index.get_level_values(0).unique()
    properties.drop(columns=highly_correlated, inplace=True)

    properties.head()
    properties.corr()
    return properties



def data_analyse(properties):

    """Assuming properties is my dataset we will use it to define our features and target
    After that we will do a split of our test data and train data.    
    """
    X = properties[['Habitable surface', 'Bedroom Count','Garden surface']].values
    y = properties['Price'].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    """First we will do our Polynomial Linear Regression
    We start by making a PolynomialFeature and make a new train and test features with our polynomial that is ^2
    Then we will a new regressor and fit our X_poly and y_train
    """
    poly = PolynomialFeatures(degree=2, include_bias=True)
    X_poly_train = poly.fit_transform(X_train)
    X_poly_test = poly.transform(X_test)

    regressor_poly = LinearRegression()
    regressor_poly.fit(X_poly_train, y_train)

    print("Polynomial Regression Training score:", regressor_poly.score(X_poly_train, y_train))
    print("Polynomial Regression Testing score:", regressor_poly.score(X_poly_test, y_test))

    """I tried some Stotisastic regression but failed a bit got a very low score. """
    regressor_sgd = SGDRegressor(max_iter=10000, random_state=42)  # Initialize SGDRegressor
    regressor_sgd.fit(X_train, y_train)

    print("SGD Regression Training score:", regressor_sgd.score(X_train, y_train))
    print("SGD Regression Testing score:", regressor_sgd.score(X_test, y_test))

    """Next up i did a descision tree regressor this one had a high score the Test set is bit on the low end for score but my training set
    has a pretty good score of 90%. 
    """
    regressor_tree = DecisionTreeRegressor(random_state=42)
    regressor_tree.fit(X_train, y_train)

    print("Decision Tree Regression Training score:", regressor_tree.score(X_train, y_train))
    print("Decision Tree Regression Testing score:", regressor_tree.score(X_test, y_test))

    """Sort the data based on 'Habitable surface' for better plotting"""
    sort_indices = np.argsort(X_train[:, 0])
    X_train_sorted = X_train[sort_indices]
    y_train_sorted = y_train[sort_indices]

    sort_indices = np.argsort(X_test[:, 0])
    X_test_sorted = X_test[sort_indices]
    y_test_sorted = y_test[sort_indices]

    """Next up we plotting all our graphs and try to make a prediction line for all our predictions
    So we will make a graph for evry test and training set and  for our poly,SDG, tree"""
    plt.figure(figsize=(8, 4))
    plt.scatter(X_train_sorted[:, 0], y_train_sorted, color='red', label='Actual (Train)')
    plt.plot(X_train_sorted[:, 0], regressor_poly.predict(poly.transform(X_train_sorted)), color='blue', label='Predicted (Train)')
    plt.title('Features vs price (Polynomial Regression - Training Data)')
    plt.xlabel('Habitable surface')
    plt.ylabel('Price in Mil')
    plt.xlim(0, 2500)
    plt.legend()
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 4))
    plt.scatter(X_test_sorted[:, 0], y_test_sorted, color='red', label='Actual (Test)')
    plt.plot(X_test_sorted[:, 0], regressor_poly.predict(poly.transform(X_test_sorted)), color='blue', label='Predicted (Test)')
    plt.title('Features vs price (Polynomial Regression - Test Data)')
    plt.xlabel('Habitable surface')
    plt.ylabel('Price in Mil')
    plt.xlim(0, 2500)
    plt.legend()
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 4))
    plt.scatter(X_train_sorted[:, 0], y_train_sorted, color='red', label='Actual (Train)')
    plt.plot(X_train_sorted[:, 0], regressor_sgd.predict(X_train_sorted), color='blue', label='Predicted (Train)')
    plt.title('Features vs price (SGD Regression - Training Data)')
    plt.xlabel('Habitable surface')
    plt.ylabel('Price in Mil')
    plt.xlim(0, 2500)
    plt.legend()
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 4))
    plt.scatter(X_test_sorted[:, 0], y_test_sorted, color='red', label='Actual (Test)')
    plt.plot(X_test_sorted[:, 0], regressor_sgd.predict(X_test_sorted), color='blue', label='Predicted (Test)')
    plt.title('Features vs price (SGD Regression - Test Data)')
    plt.xlabel('Habitable surface')
    plt.ylabel('Price in Mil')
    plt.xlim(0, 2500)
    plt.legend()
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 4))
    plt.scatter(X_train_sorted[:, 0], y_train_sorted, color='red', label='Actual (Train)')
    plt.plot(X_train_sorted[:, 0], regressor_tree.predict(X_train_sorted), color='blue', label='Predicted (Train)')
    plt.title('Features vs price (Decision Tree Regression - Training Data)')
    plt.xlabel('Habitable surface')
    plt.ylabel('Price in Mil')
    plt.xlim(0, 2500)
    plt.legend()
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 4))
    plt.scatter(X_test_sorted[:, 0], y_test_sorted, color='red', label='Actual (Test)')
    plt.plot(X_test_sorted[:, 0], regressor_tree.predict(X_test_sorted), color='blue', label='Predicted (Test)')
    plt.title('Features vs price (Decision Tree Regression - Test Data)')
    plt.xlabel('Habitable surface')
    plt.ylabel('Price in Mil')
    plt.xlim(0, 2500)
    plt.legend()
    plt.tight_layout()
    plt.show()

    """We gonna predict a sample input for SDG, Polynomial, and tree Regression"""
    sample_input = np.array([[1000, 3, 20]])  
    sample_input_poly = poly.transform(sample_input)
    predicted_price_poly = regressor_poly.predict(sample_input_poly)
    print("Predicted Price (Polynomial Regression):", predicted_price_poly[0])

    predicted_price_sgd = regressor_sgd.predict(sample_input)
    print("Predicted Price (SGD Regression):", predicted_price_sgd[0])

    predicted_price_tree = regressor_tree.predict(sample_input)
    print("Predicted Price (Tree regression):", predicted_price_tree[0])

    """We will calculate all mean squared errors"""

    y_train_pred_poly = regressor_poly.predict(X_poly_train)
    y_test_pred_poly = regressor_poly.predict(X_poly_test)
    mse_poly_train = mean_squared_error(y_train, y_train_pred_poly)
    mse_poly_test = mean_squared_error(y_test, y_test_pred_poly)

    y_train_pred_sgd = regressor_sgd.predict(X_train)
    y_test_pred_sgd = regressor_sgd.predict(X_test)
    mse_sgd_train = mean_squared_error(y_train, y_train_pred_sgd)
    mse_sgd_test = mean_squared_error(y_test, y_test_pred_sgd)

    y_train_pred_tree = regressor_tree.predict(X_train)
    y_test_pred_tree = regressor_tree.predict(X_test)
    mse_tree_train = mean_squared_error(y_train, y_train_pred_tree)
    mse_tree_test = mean_squared_error(y_test, y_test_pred_tree)

    print("Polynomial Regression Training MSE:", mse_poly_train)
    print("Polynomial Regression Testing MSE:", mse_poly_test)

    print("SGD Regression Training MSE:", mse_sgd_train)
    print("SGD Regression Testing MSE:", mse_sgd_test)

    print("Decision Tree Regression Training MSE:", mse_tree_train)
    print("Decision Tree Regression Testing MSE:", mse_tree_test)

    return properties