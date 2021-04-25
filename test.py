import datetime
import pandas

import requests

if __name__ == '__main__':
    # url = 'https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/RKI_Landkreisdaten/FeatureServer/0/query'
    # query = {
    #     'f': 'json',
    #     'geometry': {
    #         "spatialReference": {
    #             "latestWkid": 3857,
    #             "wkid": 102100
    #         },
    #         "xmin": 683089.8783231061,
    #         "ymin": 6565862.68138622,
    #         "xmax": 690427.8330384826,
    #         "ymax": 6573200.636101597
    #     },
    #     'outFields': 'RS,GEN,cases,cases7_bl,cases7_bl_per_100k,cases7_lk,cases7_per_100k,cases7_per_100k_txt,cases_per_100k,cases_per_population,county,death7_bl,death7_lk,death_rate,deaths,last_update,recovered',
    #     'returnGeometry': False,
    # }

    #response = requests.get(url, params=query)
    #j = response.json()

    #print(j)

    days = 5
    date = datetime.datetime.now() - datetime.timedelta(days=days + 7)
    datestr = date.isoformat().split('T')[0]

    whereParams = ['NeuerFall IN(1,0)', 'IdLandkreis = 05334', f"MeldeDatum >= TIMESTAMP '{datestr}'"]
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
        'sqlFormat': 'none', 'f': 'json'
    }

    response = requests.get(url, params=params)

    rsj = response.json()

    records = []
    population = 557026
    for feature in rsj['features']:
        data = feature['attributes']
        record = {
            'cases': data['cases'],
            'date': datetime.datetime.utcfromtimestamp(data['MeldeDatum'] / 1000),
            'county': data['Landkreis'],
            'incidence': data['cases'] / (population / 100000)
        }
        records.append(record)

    historyDF = pandas.DataFrame(records)
    weekIncidence = historyDF['incidence'].rolling(7).sum()
    historyDF['weekIncidence'] = weekIncidence

    print(historyDF)
