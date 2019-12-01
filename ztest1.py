import pandas as pd

dict = {
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98]}

brics = pd.DataFrame(dict)

brics.index = ["BR", "RU", "IN", "CH", "SA"]

# Square brackets
## Column access
print(brics[["country", "capital"]])
print('\n')

## Row access: only through slicing
print(brics[1:4])
print('\n')

# loc (label-based)
## Row access
print(brics.loc[["RU", "IN", "CH"]])
print('\n')

## Column access
print(brics.loc[:, ["country", "capital"]])
print('\n')

## Row & Column access
print(brics.loc[["RU", "IN", "CH"], ["country", "capital"]])
print('\n')
