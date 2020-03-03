from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_selection import RFECV


def featureRandomForest (df):
    rf_reg = RandomForestRegressor(n_estimators=15, max_depth=3, min_samples_leaf=3, random_state=111)
    selector = RFECV(rf_reg, step=1, cv=5)

    predictors = df.columns


    X = df[predictors]
    y = df['price']

    selector.fit(X, y)
    selector.n_features_

    pd.Series(predictors)[selector.support_.tolist()]
    predictors = pd.Series(predictors)[selector.support_.tolist()].tolist()

    return predictors