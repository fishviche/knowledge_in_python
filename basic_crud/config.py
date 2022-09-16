import json
with open('config.json') as json_data_file:
    config = json.load(json_data_file)
DSN =  "user={} password={} host={} port={} dbname={}".format(
    config.get('database', {}).get('user'),
    config.get('database', {}).get('password'),
    config.get('database', {}).get('host'),
    config.get('database', {}).get('port'),
    config.get('database', {}).get('name')
)