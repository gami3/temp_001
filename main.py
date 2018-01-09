import pandas as pd
import numpy as np
import html5lib
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
%matplotlib inline

nfl_frame = pd.read_html('https://stocks.finance.yahoo.co.jp/stocks/history/?code=9715.T', flavor='bs4')
df = DataFrame(nfl_frame[1],columns=[0,6])
df = df.sort_index(ascending=False)
df = df.rename(columns={0: 'date',6: 'end'}).drop(0).set_index ('date')
df = df.astype({'end': int})

df.plot()
plt.show()
