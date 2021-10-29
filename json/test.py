import pandas as pd
import requests

df = pd.read_csv(r'E:\Hub Spoke cloud\21.06.2021-sku\test data\JSON\Final Sku Gen_Dunamis.csv')
url = 'https://tcesffb3s8.execute-api.ap-south-1.amazonaws.com/dev/rpa/rpaoutput'

n = 1
for j, i in df.iterrows():
    json_data = i.to_json()
    print(json_data)
    res = requests.post(url=url, json=json_data)
    print(res)
    print('\n\n')
    n += 1
    if n == 3:
        break
        
  other programm
  import pandas as pd
import requests

df = pd.read_csv('/home/rudransh/Downloads/Final Sku Gen_Dunamis.csv')
url = 'https://tcesffb3s8.execute-api.ap-south-1.amazonaws.com/dev/rpa/rpaoutput'

n = 1
for j, i in df.iterrows():
    json_data = i.to_json()
    print(json_data)
    res = requests.post(url=url, json=json_data)
    print(res)
    # print('\n\n')
    # n += 1
    # if n == 3:
    #     break
    
    
    
    
other program


import matplotlib.colors as mcolors
from os import listdir, chdir
import pandas as pd
import datetime
import requests
import json



# In[2]:


colors = list(mcolors.cnames.keys())
post_url = 'https://tcesffb3s8.execute-api.ap-south-1.amazonaws.com/dev/rpa/rpaoutput'


# In[3]:


def shortner(given_color:str):
    given_color = given_color.lower()
    
    for color in colors:
        if color in given_color:
            rfs = given_color.split(color)
            sc = color[:2] + color[-1]
            rl = rfs[0] + sc + rfs[1]
            if rl == None:
                return given_color
            else:
                return rl


# In[4]:

# function to convert HKD to AUD

def final_price(input_price, input_currency):
    src_price = int(input_price)
    product_price = 0
    aud = 1
    if input_currency == 'HKD':
        aud = 0.18
    try:
        product_price = src_price * aud
    except Exception as ex:
        print(ex)
    return int(product_price)

# chdir('..')


# In[5]:


def generate_sku():
    try:
        fieldnames = ['retailer_sku', 'vendor_sku', 'quantity', 'cost', 'leadtime', 'vendor_name', 'purchase_name']
        # filename = 'FPPL.xlsx'
        filename = 'Dunamis.xlsx'
        template_df = pd.read_excel(filename, 'Lookup')
        input_folder_name = 'input'
        final_df = pd.DataFrame(columns=fieldnames)
        for file in listdir(input_folder_name):
            file_path = f'{input_folder_name}/{file}'

            print(f'Reading file {file}..')

            fn_list = file.lower().split('.')

            extention = fn_list[-1]

            file_name = '_'.join(fn_list)

            final_datetime = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")

            file_sv_name = file_name + '-' + final_datetime

            print(file_sv_name)
            print(type(file_sv_name))

            if extention == 'csv':
                df = pd.read_csv(file_path)
            elif extention == 'xlsx' or extention == 'xls':
                df = pd.read_excel(file_path)
                ind = df.columns[0]
                df[ind] = df[ind].fillna(method='ffill')

            cols = df.columns.values[1:]
            brand = cols[0]

            count = 0
            start = False

            for index, row in df.iterrows():
                if df.columns[0] == 'Brand':
                    start = True

                if start:
                    vals = row.values
                    brand = vals[0]
                    model = vals[1]
                    cost = final_price(vals[2], 'HKD')

                    avg = 1000
                    # cost = 570
                    leadtime = 2
                    vendor = 'Dunamis'
                    purchase = model

                    remark1 = vals[3]
                    try:
                        remark2 = shortner(vals[3])
                    except Exception as e:
                        remark2 = None
                    if remark2 == None:
                        remark2 = remark1

                    rs = f'{brand}-{model}-{remark1}'.replace(' ', '-').replace('-nan', '').replace('--', '-').replace(',',
                                                                                                                       '').lower()
                    # rs = f'{brand}-{model}-{remark1}'.replace(' ', '-').replace('-nan', '').replace('--', '-').replace(',', '').title()

                    val = template_df.loc[template_df[template_df.columns[0]] == rs][template_df.columns[1]]
                    if len(val) > 0:
                        vs = val.values[0]
                    else:
                        vs = 'NA'

                    formated_data = [vs, rs, avg, cost, leadtime, vendor, purchase]

                    final_df = final_df.append(pd.DataFrame([formated_data], columns=fieldnames), ignore_index=True)
                else:
                    if row.values[0] == 'Brand':
                        start = True
        final_df.to_csv("Final Sku Gen_Dunamis.csv", index=False)
        # add a new column to final_df
        final_df['vendorId'] = 1
        # convert the dat frame object to json
        final_df.to_json('temp.json', orient='records')
        # post to API.
        try:
             with open('temp.json') as content:
                 #doc_content = json.load(content)
                 doc_content = content.read()
                 result = requests.post(url=post_url, data=doc_content)
                 if result.status_code == 200:
                     print('data posted successfully.')
        except Exception as ex:
             print(ex)
    except IndentationError as e:
        print('\nError..\n')
        print(e, end='\n\n')





generate_sku()
print('done')





