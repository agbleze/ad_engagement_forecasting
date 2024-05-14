#%%
import pandas as pd
import matplotlib.pyplot as plt



#%%
data = "data/Train.csv"

sub_data_path = "data/SampleSubmission.csv"


#%%
df = pd.read_csv(data)

#%%
df.describe()

#%%
df.info()

#%%
sub_df = pd.read_csv(sub_data_path)

#%%
sub_df.info()

#%%
df.head(10)

#%%
sub_df.ID.nunique()

#%%
df.ID.nunique()

#%%
df.clicks.plot()

#%%
df.ID.unique()

#%%
df[df.ID=='ID_5da86e71bf5dee4cf5047046'].clicks.plot()
#%%

df.groupby("ID")["clicks"].plot()



#%%
"""
ID should be used to group data

"""









# %%
