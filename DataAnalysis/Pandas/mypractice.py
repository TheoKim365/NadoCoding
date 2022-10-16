import pandas as pd
import sys

url = ['icashier.alipay.com/catalog/2758186/detail.aspx', 
    'icashier.alipay.com/catalog/2758186/detail.aspx', 
    'icashier.alipay.com/catalog/2758186/detail.aspx', 
    'vk.com']
df = pd.DataFrame(url, columns = ['url'])
df['add'] = [1,2,3,4]

df['url'] = df['url'].replace({'icashier': 'aliexpress'}, regex=True)

df['url'] = df['url'].replace({'aliex': 'align'}, regex=True)

df['url'] = df['url'].replace({'align': 'alive'}, regex=True)

df['url'] = df['url'].replace({'gn': 've'}, regex=True)

df['url'] = df['url'].replace({'log': 'lofe'}, regex=True)

print(df)
sys.exit()
