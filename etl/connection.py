import json
import psycopg2 as pg

class PostgresConnect:
    with open('etl/config.json', 'r', encoding='UTF-8') as f:
        config = json.load(f)['postgres']

    # try:
    conn = pg.connect(
        host=config['host'],
        database=config['database'],
        port=config['port'],
        user=config['user'],
        password=config['password']
    )
    print('conn================', conn.str)
    # host=localhost port=5432 user=postgres password=postgres dbname=product
    # except pg.OperationalError as msg:
    #     print("msg=================",msg)
    # except Exception as e:
    #     print("eeeeeeeeee-----", e)

    # finally:
    #     print("final================")
