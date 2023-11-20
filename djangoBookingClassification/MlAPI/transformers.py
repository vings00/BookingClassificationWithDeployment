from sklearn.base import TransformerMixin, BaseEstimator
import pandas as pd

class ColumnDropper(BaseEstimator, TransformerMixin):
    def __init__(self, columns_to_drop):
        self.columns_to_drop = ['id', 'no_of_previous_bookings_not_canceled', 'arrival_date']

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X.drop(self.columns_to_drop, axis=1, errors='ignore')

class YearEncoder(BaseEstimator, TransformerMixin):
    def __init__(self, column):
        self.column = column

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        if X.shape[0] != 1:
            X = pd.concat([X, pd.get_dummies(X[self.column], drop_first=True)], axis=1)
        else:
            X['2018'] = X[X[self.column] == 2018]
        X = X.drop([self.column], axis=1)
        X.columns = X.columns.astype(str)
        return X