# Задача 44: В ячейке ниже представлен код генерирующий DataFrame,
# которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид.
# Сможете ли вы это сделать без get_dummies?

import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()

random_values = data['whoAmI'].unique()
one_hot_coding = pd.DataFrame()
for value in random_values:
    one_hot_coding[value] = (data['whoAmI'] == value).astype(int)

one_hot_coding.head()

print(one_hot_coding)
