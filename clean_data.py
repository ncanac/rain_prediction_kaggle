import dask.dataframe as dd

train_df = dd.read_csv("data/train.csv")

train_under300_df = train_df[train_df['Expected'] < 300]

train_under300_df.to_csv("train_filter1.csv")
