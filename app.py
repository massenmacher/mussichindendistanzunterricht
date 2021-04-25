import pandas as pd
from flask import Flask, render_template
import requests
import datetime
import pandas

app = Flask(__name__)

LK_AGS = '05334'
LK_POP = 557026

def fetchResults():
    days = 5
    date = datetime.datetime.now() - datetime.timedelta(days=days + 7)
    datestr = date.isoformat().split('T')[0]


    whereParams = ['NeuerFall IN(1,0)', f'IdLandkreis = {LK_AGS}', f"MeldeDatum >= TIMESTAMP '{datestr}'"]
    url = 'https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/RKI_COVID19/FeatureServer/0/query'
    params = {
        'where': " AND ".join(whereParams),
        'resultType': 'standard',
        'outFields': 'AnzahlFall,MeldeDatum,Landkreis,IdLandkreis',
        'returnIdsOnly': False,
        'returnUniqueIdsOnly': False,
        'returnCountOnly': False,
        'returnDistinctValues': False,
        'cacheHint': False,
        'orderByFields': 'IdLandkreis,MeldeDatum',
        'groupByFieldsForStatistics': 'IdLandkreis,MeldeDatum,Landkreis',
        'outStatistics': '[{"statisticType":"sum","onStatisticField":"AnzahlFall","outStatisticFieldName":"cases"}]',
        'sqlFormat': 'none',
        'f': 'json'
    }

    response = requests.get(url, params=params)
    rsj = response.json()

    #rsj = {'objectIdFieldName': 'ObjectId', 'uniqueIdField': {'name': 'ObjectId', 'isSystemMaintained': True}, 'globalIdFieldName': '', 'fields': [{'name': 'cases', 'type': 'esriFieldTypeDouble', 'alias': 'cases', 'sqlType': 'sqlTypeFloat', 'domain': None, 'defaultValue': None}, {'name': 'IdLandkreis', 'type': 'esriFieldTypeString', 'alias': 'Landkreis ID', 'sqlType': 'sqlTypeOther', 'length': 256, 'domain': None, 'defaultValue': None}, {'name': 'Meldedatum', 'type': 'esriFieldTypeDate', 'alias': 'Meldedatum', 'sqlType': 'sqlTypeOther', 'length': 0, 'domain': None, 'defaultValue': None}, {'name': 'Landkreis', 'type': 'esriFieldTypeString', 'alias': 'Landkreis', 'sqlType': 'sqlTypeNVarchar', 'length': 2147483647, 'domain': None, 'defaultValue': None}], 'features': [{'attributes': {'cases': 188, 'IdLandkreis': '05334', 'MeldeDatum': 1618272000000, 'Landkreis': 'StadtRegion Aachen'}}, {'attributes': {'cases': 120, 'IdLandkreis': '05334', 'MeldeDatum': 1618358400000, 'Landkreis': 'StadtRegion Aachen'}}, {'attributes': {'cases': 130, 'IdLandkreis': '05334', 'MeldeDatum': 1618444800000, 'Landkreis': 'StadtRegion Aachen'}}, {'attributes': {'cases': 179, 'IdLandkreis': '05334', 'MeldeDatum': 1618531200000, 'Landkreis': 'StadtRegion Aachen'}}, {'attributes': {'cases': 100, 'IdLandkreis': '05334', 'MeldeDatum': 1618617600000, 'Landkreis': 'StadtRegion Aachen'}}, {'attributes': {'cases': 33, 'IdLandkreis': '05334', 'MeldeDatum': 1618704000000, 'Landkreis': 'StadtRegion Aachen'}}, {'attributes': {'cases': 85, 'IdLandkreis': '05334', 'MeldeDatum': 1618790400000, 'Landkreis': 'StadtRegion Aachen'}}, {'attributes': {'cases': 235, 'IdLandkreis': '05334', 'MeldeDatum': 1618876800000, 'Landkreis': 'StadtRegion Aachen'}}, {'attributes': {'cases': 176, 'IdLandkreis': '05334', 'MeldeDatum': 1618963200000, 'Landkreis': 'StadtRegion Aachen'}}, {'attributes': {'cases': 171, 'IdLandkreis': '05334', 'MeldeDatum': 1619049600000, 'Landkreis': 'StadtRegion Aachen'}}, {'attributes': {'cases': 222, 'IdLandkreis': '05334', 'MeldeDatum': 1619136000000, 'Landkreis': 'StadtRegion Aachen'}}, {'attributes': {'cases': 54, 'IdLandkreis': '05334', 'MeldeDatum': 1619222400000, 'Landkreis': 'StadtRegion Aachen'}}]}
    #rsj = {'objectIdFieldName': 'ObjectId', 'uniqueIdField': {'name': 'ObjectId', 'isSystemMaintained': True}, 'globalIdFieldName': '', 'fields': [{'name': 'cases', 'type': 'esriFieldTypeDouble', 'alias': 'cases', 'sqlType': 'sqlTypeFloat', 'domain': None, 'defaultValue': None}, {'name': 'IdLandkreis', 'type': 'esriFieldTypeString', 'alias': 'Landkreis ID', 'sqlType': 'sqlTypeOther', 'length': 256, 'domain': None, 'defaultValue': None}, {'name': 'Meldedatum', 'type': 'esriFieldTypeDate', 'alias': 'Meldedatum', 'sqlType': 'sqlTypeOther', 'length': 0, 'domain': None, 'defaultValue': None}, {'name': 'Landkreis', 'type': 'esriFieldTypeString', 'alias': 'Landkreis', 'sqlType': 'sqlTypeNVarchar', 'length': 2147483647, 'domain': None, 'defaultValue': None}], 'features': [{'attributes': {'cases': 188, 'IdLandkreis': '05334', 'MeldeDatum': 1618272000000, 'Landkreis': 'StadtRegion Aachen'}}, {'attributes': {'cases': 120, 'IdLandkreis': '05334', 'MeldeDatum': 1618358400000, 'Landkreis': 'StadtRegion Aachen'}}, {'attributes': {'cases': 130, 'IdLandkreis': '05334', 'MeldeDatum': 1618444800000, 'Landkreis': 'StadtRegion Aachen'}}, {'attributes': {'cases': 179, 'IdLandkreis': '05334', 'MeldeDatum': 1618531200000, 'Landkreis': 'StadtRegion Aachen'}}, {'attributes': {'cases': 100, 'IdLandkreis': '05334', 'MeldeDatum': 1618617600000, 'Landkreis': 'StadtRegion Aachen'}}, {'attributes': {'cases': 33, 'IdLandkreis': '05334', 'MeldeDatum': 1618704000000, 'Landkreis': 'StadtRegion Aachen'}}, {'attributes': {'cases': 85, 'IdLandkreis': '05334', 'MeldeDatum': 1618790400000, 'Landkreis': 'StadtRegion Aachen'}}, {'attributes': {'cases': 0, 'IdLandkreis': '05334', 'MeldeDatum': 1618876800000, 'Landkreis': 'StadtRegion Aachen'}}, {'attributes': {'cases': 0, 'IdLandkreis': '05334', 'MeldeDatum': 1618963200000, 'Landkreis': 'StadtRegion Aachen'}}, {'attributes': {'cases': 0, 'IdLandkreis': '05334', 'MeldeDatum': 1619049600000, 'Landkreis': 'StadtRegion Aachen'}}, {'attributes': {'cases': 0, 'IdLandkreis': '05334', 'MeldeDatum': 1619136000000, 'Landkreis': 'StadtRegion Aachen'}}, {'attributes': {'cases': 0, 'IdLandkreis': '05334', 'MeldeDatum': 1619222400000, 'Landkreis': 'StadtRegion Aachen'}}]}

    records = []
    for feature in rsj['features']:
        data = feature['attributes']
        record = {
            'cases': data['cases'],
            'date': datetime.datetime.utcfromtimestamp(data['MeldeDatum'] / 1000),
            'county': data['Landkreis'],
            'incidence': data['cases'] / (LK_POP / 100000)
        }
        records.append(record)

    historyDF = pandas.DataFrame(records)
    weekIncidence = historyDF['incidence'].rolling(7).sum()
    historyDF['weekIncidence'] = weekIncidence

    return historyDF

def daysInARow(column, threshold, method='geq'):
    inARow = 0

    rcolumn = column.copy()


    for value in rcolumn[::-1]:
        constraint_satisfied = False

        if method=='geq':
            constraint_satisfied = (value >= threshold)
        elif method == 'g':
            constraint_satisfied = (value > threshold)
        elif method == 'eq':
            constraint_satisfied = (value == threshold)
        elif method == 'l':
            constraint_satisfied = (value < threshold)
        elif method == 'leq':
            constraint_satisfied = (value <= threshold)

        if not constraint_satisfied:
            return inARow
        else:
            inARow += constraint_satisfied

    return inARow

@app.route('/')
def index():
    magic_number_lockdown = 165
    magic_number_lockdown_light = 100

    today = datetime.date.today()

    indicator_days = 3
    indicator_update_until = today - datetime.timedelta(days=indicator_days)

    release_days = 5
    release_update_until = today - datetime.timedelta(days=release_days)

    number_of_last_days = release_days
    updates_until = today - datetime.timedelta(days=number_of_last_days)

    history = fetchResults()
    last_history = history[history["date"] >= updates_until.isoformat()]

    indicator_hisoty = last_history[last_history['date'] >= indicator_update_until.isoformat()]
    days_exceeded_lockdown = daysInARow(last_history['weekIncidence'], magic_number_lockdown)
    days_exceeded_lockdown_light = daysInARow(last_history['weekIncidence'], magic_number_lockdown_light)

    release_history = last_history[last_history['date'] >= release_update_until.isoformat()]
    days_lockdown_relase = daysInARow(last_history['weekIncidence'], magic_number_lockdown, 'l')

    return render_template("index.html",
                           today=today,#.isoformat(),
                           data=last_history,
                           last_update=last_history['date'].iloc[-1],#.isoformat(),
                           lockdown_days = days_exceeded_lockdown,
                           lockdown_light_days = days_exceeded_lockdown_light,
                           lockdown_in_place = (days_exceeded_lockdown >= indicator_days and indicator_hisoty.shape[0] >= 3),
                           lockdown_light_in_place = (days_exceeded_lockdown_light >= indicator_days and indicator_hisoty.shape[0] >= 3),
                           lockdown_start = today + datetime.timedelta(days=2),
                           insufficient_data = indicator_hisoty.shape[0] < indicator_days,
                           location=last_history['county'].iloc[0],
                           magic_number_lockdown = magic_number_lockdown_light,
                           magic_number_lockdown_extended = magic_number_lockdown,
                           release_lockdown=days_lockdown_relase >= release_days
   )


if __name__ == '__main__':
    app.run()
