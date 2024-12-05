import pandas as pd
df=pd.read_csv('list.csv')
df[['left_list', 'right_list']] = df['left_list  right_list'].str.split(expand=True)
df = df.drop(columns=['left_list  right_list'])
print(df.columns)
df['left_list'] = pd.to_numeric(df['left_list'])
df['right_list'] = pd.to_numeric(df['right_list'])

print(df.head())
print (df.columns)

list_left = df['left_list'].tolist()
list_right = df['right_list'].tolist()

list_left.sort()
list_right.sort()
print(list_left)

result = 0  # Initialize result
for i in range(len(list_left)):  
    cnt = 0  
    for j in range(len(list_right)):  
        if list_left[i] == list_right[j]:  
            cnt += 1  # Count occurrences
    result += list_left[i] * cnt  

print("Result:", result)