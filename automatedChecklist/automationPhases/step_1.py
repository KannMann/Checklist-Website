
import pandas as pd

def step1():
    df = pd.DataFrame({'first_names': ["Jim", "Jane"],
                       'last_names': ['Doe', 'AlsoDoe'] 
                        })
    return df

step1().to_csv("output/Phase_1_Output.csv", index=False)