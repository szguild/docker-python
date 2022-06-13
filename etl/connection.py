import json
import psycopg2 as pg

class PostgresConnect:
    with open('etl/config.json', 'r', encoding='UTF-8') as f:
        config = json.load(f)['postgres']

        conn = pg.connect(
            host=config['host'],
            database=config['database'],
            port=config['port'],
            user=config['user'],
            password=config['password']
        )
