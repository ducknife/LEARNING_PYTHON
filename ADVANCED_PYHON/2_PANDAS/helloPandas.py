import pandas as pd
import os
from datetime import datetime as dt

df = pd.DataFrame.from_dict({'Hello' : 'hi', 'Halo' : 'Skibidi'}, orient='index')
df2 = pd.DataFrame({'Hello' : 'hi', 'Halo' : 'Skibidi'}, index=['a', 'b'])
path = os.path.join(os.path.dirname(__file__), 'helloPandas.csv')
path2 = os.path.join(os.path.dirname(__file__), 'helloPandas2.csv')
df.to_csv(path, index=False)
df2.to_csv(path2, index=False)

# now = dt.now().strftime(f"%d/%m/%Y - %H:%M:%S {'AM' if dt.now().hour <= 12 else 'PM'}, Mission Completed!")
# print(now, 'Hí hê hê hê')