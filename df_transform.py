import numpy as np
import pandas as pd

def transform(train_path, test_path):
    """ Takes train and test dataset paths as arguments, saves the tranformed data sets
    as csv files in the data folder under new names """

    # Load data as dataframes
    train = pd.read_csv(train_path, index_col = 0)
    test = pd.read_csv(test_path, index_col = 0)

    # Drop SalePrice from training set
    train.drop("SalePrice", axis=1, inplace=True)

    # Concat training and test dataframes
    df = pd.concat([train, test], sort=False)

    df = df.set_index('Id')

    # Rename columns that are incompatible with Pandas (periods, etc)

    # Drop all unused columns Here

    # Transformations

    # Split dataframe into test and train by index
    df_finalTrain = df.iloc[0:train.shape[0],:]
    df_finalTest = df.iloc[train.shape[0]:,:]

    # Save dataframes to './data/ProcessedTrain.csv' and './data/ProcessedTest.csv'
    df_finalTrain.to_csv('ProcessedTrain.csv')
    df_finalTest.to_csv('ProcessedTest.csv')