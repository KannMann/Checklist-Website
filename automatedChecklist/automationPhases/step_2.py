
import pandas as pd

def step2():
    df = pd.DataFrame({'first_names': ["Jim", "Jane"],
                       'city': ['NYC', 'Boston'] 
                        })
    return df

step2().to_csv("output/Phase_2_Output.csv", index=False)