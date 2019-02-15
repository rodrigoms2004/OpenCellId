import pandas as pd
from getCellIdData import getCellData

file = './csv_data/data.csv'
df = pd.read_csv(file)

list_temp = []
for key, value in df.iterrows():
    print("############### Key: ", key)

    dict_cellInfo = {}

    dict_cellInfo['mcc'] = value.mcc
    dict_cellInfo['mnc'] = value.mnc
    dict_cellInfo['lac'] = value.lac
    dict_cellInfo['cellid'] = value.cellid
    
    resp = getCellData(dict_cellInfo)
    
    dict_cellInfo['radacctid'] = value.radacctid
    dict_cellInfo['nasipaddress'] = value.nasipaddress
    dict_cellInfo['acctstarttime'] = value.acctstarttime
    dict_cellInfo['acctstoptime'] = value.acctstoptime
    dict_cellInfo['acctinputoctets'] = value.acctinputoctets
    dict_cellInfo['acctoutputoctets'] = value.acctoutputoctets
    dict_cellInfo['calledstationid'] = value.calledstationid
    dict_cellInfo['msisdn'] = value.msisdn
    dict_cellInfo['framedipaddress'] = value.framedipaddress

    dict_cellInfo['status'] = resp['status']

    if (resp['status'] == 'ok'):
        dict_cellInfo['latitude'] = resp['lat']
        dict_cellInfo['longitude'] = resp['lon']
        dict_cellInfo['accuracy'] = resp['accuracy']
        dict_cellInfo['address'] = resp['address']
        print('latitude:', resp['lat'], 
              'longitude:', resp['lon'], 
              'cellid:', resp['cellid'])
    else:
        dict_cellInfo['message'] = resp['message']
        print("Error", resp['message'])
        
    list_temp.append(dict_cellInfo)


df = pd.DataFrame(list_temp)
df.to_csv('./csv_data/results.csv', sep=';', encoding='utf-8')
