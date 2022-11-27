import pandas as pd
import numpy as np

data = pd.read_csv('ddd.csv', header=None)
data.columns = ['datetime']

data_jun = data.loc[data['datetime'].str.contains('2020-06')]
print(data_jun.shape)

# делим datetime на параметры
data_jun.datetime = data_jun.datetime.apply(pd.to_datetime)
data_jun['day'] = data_jun.datetime.apply(lambda x: x.day)
data_jun['month'] = data_jun.datetime.apply(lambda x: x.month)
data_jun['year'] = data_jun.datetime.apply(lambda x: x.year)
data_jun['hour'] = data_jun.datetime.apply(lambda x: x.hour)
data_jun['min'] = data_jun.datetime.apply(lambda x: x.minute)
data_jun['sec'] = data_jun.datetime.apply(lambda x: x.second)
data_jun['msec'] = data_jun.datetime.apply(lambda x: x.microsecond)
data_jun['weekday'] = data_jun.datetime.apply(lambda x: x.weekday())
data_jun['week'] = data_jun.datetime.apply(lambda x: x.week)

print(data_jun.head())