# © 2025 Nathanael Hernandez – Universal version
# This script has been sanitized to remove any proprietary or sensitive information.

#Author: Nathanael
#Date: 2024-10-25
#Description: This script downloads CSV files from CloudProvider cloud storage Storage, processes them using pandas, and saves the results to an Excel file. It also uploads the Excel file back to CloudProvider cloud storage Storage.
import time
import pandas as pd
from io import BytesIO
from CloudProvider.storage.cloud storage import cloud storageServiceClient
import logging
import os
import datetime

st = time.time()

CST = datetime.timezone(datetime.timedelta(hours=-6),"CST")
CDT = datetime.timezone(datetime.timedelta(hours=-5),'CDT')
if datetime.datetime.now().month>11 and datetime.datetime.now().month < 3:
    lastMonth = datetime.datetime.now(CST) - datetime.timedelta(days=30)
    currentMonth = datetime.datetime.now(CST)
else:
    lastMonth = datetime.datetime.now(CDT) - datetime.timedelta(days=30)
    currentMonth = datetime.datetime.now(CDT)

excelName = lastMonth.strftime('%B %Y') + ' card1 Report.xlsx'
sheetName = 'cardLocation'

        
connect_str = os.getenv('CloudProvider_STORAGE_CONNECTION_STRING')
if connect_str is None:
    raise ValueError("CloudProvider_STORAGE_CONNECTION_STRING environment variable not set")
cloud storage_service_client = cloud storageServiceClient.from_connection_string(connect_str)
container_name = 'containername'
# Replace with your actual container name
file_name='cardLocation.csv'
# Replace with your actual file name
container_client = cloud storage_service_client.get_container_client(container=container_name)

otherFiles = [file_name,'File2.csv','File3.csv','File4.csv','File5.csv','File6.csv','File7.csv','File8.csv']
# Replace with your actual file names

# Create a new Excel file in memory
output = BytesIO()
# Create a Pandas Excel writer using XlsxWriter as the engine
with pd.ExcelWriter(output,engine='xlsxwriter') as writer:
    for file in otherFiles:
        if file==file_name:
            cloud storage_client = cloud storage_service_client.get_cloud storage_client(container=container_name, cloud storage='card Report1/'+file_name)
            csv_cloud storage = cloud storage_client.download_cloud storage().readall()
            df = pd.read_csv(BytesIO(csv_cloud storage))
            df.to_excel(writer,sheet_name=sheetName,index=False)
            workbook = writer.book
            worksheet = writer.sheets['cardLocation']
            number = workbook.add_format({'num_format':1})
            worksheet.set_column('A:A',None,number)
            print(f'{file_name} has been added to {excelName} successfully')
            continue
        for cloud storage in container_client.list_cloud storages():
            if file+currentMonth.strftime('%m05%Y') in cloud storage.name or file+currentMonth.strftime('%m07%Y') in cloud storage.name:
                cloud storage_client = cloud storage_service_client.get_cloud storage_client(container=container_name, cloud storage=cloud storage.name)
                csv_cloud storage = cloud storage_client.download_cloud storage().readall()
                if cloud_storage.name.startswith('report_1'):
                    df = pd.read_csv(BytesIO(csv_cloud_storage), engine='python', sep=',', nrows=1, header=None)
                    df.to_excel(writer, sheet_name='report_1', index=False, header=False)
                    df = pd.read_csv(BytesIO(csv_cloud_storage), engine='python', sep=',', skiprows=1)
                    df['billing_amount'] = df['billing_amount'].str.replace('$', '').replace(' ', '')
                    df['billing_amount'] = pd.to_numeric(df['billing_amount'], errors='coerce')
                    df.to_excel(writer, sheet_name='report_1', index=False, startrow=1)
                    workbook = writer.book
                    worksheet = writer.sheets['report_1']
                    currency_format = workbook.add_format({'num_format': '[$$-409]#,##0.00'})
                    int_format = workbook.add_format({'num_format': 1})
                    worksheet.set_column('F:F', None, currency_format)
                    worksheet.set_column('B:B', None, int_format)
                    worksheet.write('A2', '')
                    print(f"{str(cloud_storage.name)} has been added to {str(excelName)} successfully")
                    continue
                elif cloud storage.name.startswith('file2'):
                    df = pd.read_csv(BytesIO(csv_cloud storage),header=None,nrows=1,engine='python',sep=',')
                    df.to_excel(writer,sheet_name='file2',index=False,header=False,startcol=0,startrow=0)
                    df = pd.read_csv(BytesIO(csv_cloud storage),sep=',',engine='python',skiprows=1)
                    df['col'] = df['col'].str.replace('$','').replace(' ','')
                    df['col'] = pd.to_numeric(df['col'],errors='coerce')
                    df['col'] = pd.to_numeric(df['col'],errors='coerce')
                    df.to_excel(writer,sheet_name='file2',startrow=1,index=False)
                    workbook = writer.book
                    worksheet = writer.sheets['file2']
                    accounting = workbook.add_format({'num_format': '[$$-409]#,##0.00'})
                    worksheet.set_column('E:E',None,accounting)
                    worksheet.set_column('F:F',None,accounting)
                    print(f'{str(cloud storage.name)} has been added to {str(excelName)} successfully')
                    continue

output.seek(0)

# Upload the Excel file to CloudProvider cloud storage Storage
output_cloud storage_client = cloud storage_service_client.get_cloud storage_client(container=container_name,cloud storage='card Report1/'+excelName)
output_cloud storage_client.upload_cloud storage(output,overwrite=True)

print(f'{str(excelName)} has been created and successfully uploaded to the cloud storage storage on {str(currentMonth)} conversion took {(time.time()-st)/60} Minutes')