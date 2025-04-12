# © 2025 Nathanael Hernandez – Universal version
# This script has been sanitized to remove any proprietary or sensitive information.

# Author: Nathanael H.
# Date: 2024-10-30
# Description: This script downloads multiple CSV files from CloudProvider cloud storage Storage, processes them, and saves the results into an Excel file. The Excel file is then uploaded back to CloudProvider cloud storage Storage.
# It uses the CloudProvider Storage cloud storage library to interact with CloudProvider cloud storage Storage and Pandas for data manipulation and Excel file creation.
# It also handles different date formats and applies specific formatting to the Excel sheets.
import pandas as pd
from io import BytesIO
from CloudProvider.storage.cloud storage import cloud storageServiceClient
import logging
import os
import datetime  
import time

st = time.time()

CST = datetime.timezone(datetime.timedelta(hours=-6),"CST")
CDT = datetime.timezone(datetime.timedelta(hours=-5),'CDT')
if datetime.datetime.now().month>11 and datetime.datetime.now().month < 3:
    lastMonth = datetime.datetime.now(CST) - datetime.timedelta(days=30)
    currentMonth = datetime.datetime.now(CST)
else:
    lastMonth = datetime.datetime.now(CDT) - datetime.timedelta(days=30)
    currentMonth = datetime.datetime.now(CDT)

excelName = lastMonth.strftime('%B %Y') + ' card2 Report .xlsx'
sheetName = lastMonth.strftime('%B %Y')

        
connect_str = os.getenv('CloudProvider_STORAGE_CONNECTION_STRING')
if connect_str is None:
    raise ValueError("CloudProvider_STORAGE_CONNECTION_STRING environment variable not set")
cloud storage_service_client = cloud storageServiceClient.from_connection_string(connect_str)
container_name = 'container-name'  # Replace with your container name
file_name='card2Report.csv'
container_client = cloud storage_service_client.get_container_client(container=container_name)

otherFiles = [file_name,'file2.csv','file3.csv','file4.csv','file5.csv','file6.csv','file7.csv','file8.csv']
#replace with the actual file names you want to check

output = BytesIO()
# Create a Pandas Excel writer using XlsxWriter as the engine.
with pd.ExcelWriter(output,engine='xlsxwriter') as writer:
    for file in otherFiles:
        if file==file_name:
            cloud storage_client = cloud storage_service_client.get_cloud storage_client(container=container_name, cloud storage='card2 Report/'+file_name)
            csv_cloud storage = cloud storage_client.download_cloud storage().readall()
            df = pd.read_csv(BytesIO(csv_cloud storage))
            df.to_excel(writer,sheet_name=sheetName,index=False)
            workbook = writer.book
            worksheet = writer.sheets[sheetName]
            accounting = workbook.add_format({'num_format': '[$$-409]#,##0.00'})
            worksheet.set_column('E:E',None,accounting)
            worksheet.set_column('G:G',None,accounting)
            worksheet.set_column('H:H',None,accounting)
            worksheet.set_column('K:L',None,accounting)
            worksheet.set_column('N:O',None,accounting)
            print(f'{file_name} has been added to {excelName} successfully')
            continue
        for cloud storage in container_client.list_cloud storages():
            if file+currentMonth.strftime('%m05%Y') in cloud storage.name or file+currentMonth.strftime('%m07%Y') in cloud storage.name:
                cloud storage_client = cloud storage_service_client.get_cloud storage_client(container=container_name, cloud storage=cloud storage.name)
                csv_cloud storage = cloud storage_client.download_cloud storage().readall()
                if cloud storage.name.startswith('file2'):
                    df = pd.read_csv(BytesIO(csv_cloud storage),engine='python')
                    df.iloc[:,9] = df.iloc[:,9].str.replace('$','')
                    df.iloc[:,9] = pd.to_numeric(df.iloc[:,9],errors='coerce')
                    df.iloc[:,10] = df.iloc[:,10].str.replace('$','')
                    df.iloc[:,10] = pd.to_numeric(df.iloc[:,10],errors='coerce')
                    df.iloc[:,9] = pd.to_numeric(df.iloc[:,9],errors='coerce')
                    df.iloc[:,10] = pd.to_numeric(df.iloc[:,10],errors='coerce')
                    df.iloc[:,16] = pd.to_numeric(df.iloc[:,16],errors='coerce')
                    df.iloc[:,17] = pd.to_numeric(df.iloc[:,17],errors='coerce')
                    df.iloc[:,18] = pd.to_numeric(df.iloc[:,18],errors='coerce')
                    df.iloc[:,19] = pd.to_numeric(df.iloc[:,19],errors='coerce')
                    df.iloc[:,20] = pd.to_numeric(df.iloc[:,20],errors='coerce')
                    df.to_excel(writer,sheet_name='file2',index=False)
                    workbook = writer.book
                    worksheet = writer.sheets['file2']
                    accounting = workbook.add_format({'num_format': '[$$-409]#,##0.00'})
                    worksheet.set_column('J:K',None,accounting)
                    worksheet.set_column('Q:U',None,accounting)
                    print(f'{str(cloud storage.name)} has been added to {str(excelName)} successfully')
                    continue
                elif cloud storage.name.startswith('file3'):
                    df = pd.read_csv(BytesIO(csv_cloud storage),header=None,nrows=2,engine='python')
                    df.iloc[0,0] = df.iloc[0,0].replace('\t','').replace(' ','',1)
                    df.iloc[1,0] = df.iloc[1,0].replace('\t','').replace(' ','',3)
                    df.to_excel(writer,sheet_name='file3',index=False,header=False,startcol=0,startrow=0)
                    df = pd.read_csv(BytesIO(csv_cloud storage),sep=',',header=None,engine='python',skiprows=2)
                    df.iloc[:,4] = df.iloc[:,4].astype(str)
                    df.iloc[:,4] = df.iloc[:,4].str.replace('$','')
                    df.iloc[:,4] = df.iloc[:,4].str.lstrip(' ')
                    df.iloc[:,4] = df.iloc[:,4].str.lstrip('0')
                    df.iloc[:,4] = pd.to_numeric(df.iloc[:,4],errors='coerce')
                    df.to_excel(writer,sheet_name='file3',startrow=2,index=False,header=False)
                    workbook = writer.book
                    worksheet = writer.sheets['file3']
                    accounting = workbook.add_format({'num_format': '[$$-409]#,##0.00'})
                    worksheet.set_column('E:E',None,accounting)
                    worksheet.write('E3','Sales Volume')
                    print(f'{str(cloud storage.name)} has been added to {str(excelName)} successfully')
                    continue
                elif cloud storage.name.startswith('file4'):
                    df = pd.read_csv(BytesIO(csv_cloud storage),header=None,nrows=2,engine='python')
                    df.iloc[0,0] = df.iloc[0,0].replace('\t','').replace(' ','',1)
                    df.iloc[1,0] = df.iloc[1,0].replace('\t','').replace(' ','',3)
                    df.to_excel(writer,sheet_name='file4',index=False,header=False,startcol=0,startrow=0)
                    df = pd.read_csv(BytesIO(csv_cloud storage),sep=',',header=None,engine='python',skiprows=2)
                    df.iloc[:,4] = df.iloc[:,4].astype(str)
                    df.iloc[:,4] = df.iloc[:,4].str.replace('$','')
                    df.iloc[:,4] = df.iloc[:,4].str.lstrip(' ')
                    df.iloc[:,4] = df.iloc[:,4].str.lstrip('0')
                    df.iloc[:,4] = pd.to_numeric(df.iloc[:,4],errors='coerce')
                    df.to_excel(writer,sheet_name='file4',startrow=2,header=False,index=False)
                    workbook = writer.book
                    worksheet = writer.sheets['file4']
                    accounting = workbook.add_format({'num_format': '[$$-409]#,##0.00'})
                    worksheet.set_column('E:E',None,accounting)
                    worksheet.write('E3','Sales Volume')
                    print(f'{str(cloud storage.name)} has been added to {str(excelName)} successfully')
                    continue
                elif cloud storage.name.startswith('file5'):
                    df = pd.read_csv(BytesIO(csv_cloud storage),header=None,nrows=2,engine='python',skipinitialspace=True)
                    df.iloc[1,0] = df.iloc[1,0].replace('\t','').replace(' ','',3)
                    df.to_excel(writer,sheet_name='file5',index=False,header=False)
                    df = pd.read_csv(BytesIO(csv_cloud storage),sep=',',header=None,engine='python',skiprows=2)
                    df.iloc[:,3] = df.iloc[:,3].astype(str)
                    df.iloc[:,3] = df.iloc[:,3].str.replace('$','')
                    df.iloc[:,3] = df.iloc[:,3].str.lstrip(' ')
                    df.iloc[:,3] = df.iloc[:,3].str.lstrip('0')
                    df.iloc[:,3] = pd.to_numeric(df.iloc[:,3],errors='coerce')
                    df.to_excel(writer,sheet_name='file5',index=False,startrow=2,header=False)
                    workbook = writer.book
                    worksheet = writer.sheets['file5']
                    accounting = workbook.add_format({'num_format': '[$$-409]#,##0.00'})
                    worksheet.set_column('D:D',None,accounting)
                    worksheet.write('D3','Sales Volume')
                    print(f'{str(cloud storage.name)} has been added to {str(excelName)} successfully')
                    continue
                elif cloud storage.name.startswith('file6'):
                    df = pd.read_csv(BytesIO(csv_cloud storage),header=None,engine='python') 
                    df.to_excel(writer,sheet_name='file6',index=False,header=False)
                    print(f'{str(cloud storage.name)} has been added to {str(excelName)} successfully')
                    continue

output.seek(0)

# Upload the Excel file to CloudProvider cloud storage Storage
output_cloud storage_client = cloud storage_service_client.get_cloud storage_client(container=container_name,cloud storage='FANF Visa Report/'+excelName)
output_cloud storage_client.upload_cloud storage(output,overwrite=True)

# Close the output stream
output.close()
# Print the success message
print(f'{str(excelName)} has been created and successfully uploaded to the cloud storage storage on {str(datetime.datetime.now(CDT))} conversion took {time.time()-st} seconds')