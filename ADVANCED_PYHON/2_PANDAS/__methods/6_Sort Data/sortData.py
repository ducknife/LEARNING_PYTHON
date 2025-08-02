import pandas as pd
import os

data = {
    'age' : [20, 21, 22, 21, 24, 25]
}

df = pd.DataFrame(data)
PATH = os.path.join(os.path.dirname(__file__), 'testPandasSort.csv')
PATH1 = os.path.join(os.path.dirname(__file__), 'testPandasSort1.csv')
df.sort_values('age').to_csv(PATH, index=False)
df.sort_values('age', ascending=False).to_csv(PATH1, index=False)