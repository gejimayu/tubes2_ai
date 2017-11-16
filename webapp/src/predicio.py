import pandas as pd
import numpy as np

from sklearn.externals import joblib

from src.constants import ALL_COLUMNS


def predicio(user_data):
    columns = [
        'age', 'workclass', 'fnlwgt', 'education', 'education-num',
        'marital-status', 'occupation', 'relationship', 'race', 'sex',
        'capital-gain', 'capital-loss', 'hours-per-week', 'native-country'
    ]

    df = pd.DataFrame(columns=columns)
    df = df.drop(['fnlwgt'], axis=1)

    df.loc[0, 'age'] = user_data['age']
    df.loc[0, 'workclass'] = user_data['workclass']
    df.loc[0, 'education'] = user_data['education']
    df.loc[0, 'education-num'] = user_data['education_number']
    df.loc[0, 'marital-status'] = user_data['marital_status']
    df.loc[0, 'occupation'] = user_data['occupation']
    df.loc[0, 'relationship'] = user_data['relationship']
    df.loc[0, 'race'] = user_data['race']
    df.loc[0, 'sex'] = user_data['sex']
    df.loc[0, 'capital-gain'] = user_data['capital_gain']
    df.loc[0, 'capital-loss'] = user_data['capital_loss']
    df.loc[0, 'hours-per-week'] = user_data['hours_per_week']
    df.loc[0, 'native-country'] = user_data['native_country']

    df = pd.get_dummies(
        df,
        columns=[
            'workclass', 'education', 'marital-status', 'occupation',
            'relationship', 'race', 'sex', 'native-country'
        ])

    missing_columns = set(ALL_COLUMNS) - set(df.columns)
    for column in missing_columns:
        df[column] = 0

    x = np.array(df.drop(['label'], 1))

    knn = joblib.load('model/best.pkl')
    y = knn.predict(x)

    pred = y[0]
    return "Predicted income:<br>&emsp;%s/year" % ("<= 50K"
                                                   if pred == 0 else "> 50K")
