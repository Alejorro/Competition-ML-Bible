import pandas as pd


def cleaner(df):

    df.drop(columns=["table","depth","y","z"], axis=1, inplace=True)
    df = df.replace("Premium", 1).replace("Ideal", 2).replace("Very Good", 3).replace("Very Good", 4).replace("Fair", 5).replace("Good", 6)
    df = df.replace("IF", 1).replace("VVS1", 2).replace("VVS2", 3).replace("VS1", 4).replace("VS2", 5).replace("SI1", 6).replace("SI2", 7).replace("I1", 8)

    return df