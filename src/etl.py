

# import os
# from zipfile import ZipFile
# import pandas as pd

import numpy as np
# from env_setup import auth


# try:
#     import kaggle
# except OSError:
#     # credentials not yet set
#     auth()
#     import kaggle
    

def get_data(outdir):
    '''
    download and unzip titanic data from Kaggle.
    '''
    # kaggle.api.authenticate()
    # kaggle.api.competition_download_files(
    #     'titanic', 
    #     path=outdir
    # )

    # unzip output
    # fp = os.path.join(outdir, 'titanic.zip')
    # with ZipFile(fp) as zf:
    #     zf.extractall(outdir)

    # # remove zip file
    # os.remove(fp)

    X_test = np.load('test/testdata/x_sample.npy')
    Y_test = np.load('test/testdata/y_sample.npy')
    print("success in etl")
    return (X_test, Y_test)


def read_train(datadir):
    '''
    Reads raw training data from disk.
    (Would normally be more complicated!)
    '''
    fp = os.path.join(datadir, 'train.csv')
    return pd.read_csv(fp)


def read_test(datadir):
    '''
    Reads raw test data from disk.
    (Would normally be more complicated!)
    '''

    fp = os.path.join(datadir, 'test.csv')
    return pd.read_csv(fp)

