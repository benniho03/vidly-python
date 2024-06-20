from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

def random_forest_regression(X_train, X_test, y_train, y_test, input):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    r2_sc = r2_score(y_test, y_pred)        
    predictedValue = model.predict(input)
    return predictedValue[0], r2_sc