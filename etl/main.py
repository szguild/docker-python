import xpath_generator
import job_logging as logger
import connection
import pandas as pd
import json

conn = connection.PostgresConnect.conn

def extract_xpath():
    job = 'EXTRACT_XPATH'
    status = 'I'
    m = ''

    # xpath 추출
    logger.job_logging(job,status,m)
    
    try:
        df_xpath = xpath_generator.main()
        status = 'S'
        m = 'successfully finished'
    except Exception as e:
        status = 'E'
        m = e
        pass
    finally:
        logger.job_logging(job,status,m)

    return df_xpath

# target 마스터의 사이트코드와 상품ID 추출
def get_target():
    with conn.cursor() as cursor:
        cursor.execute("select site_cd, product_id from tb_product_target where use_yn = 'Y'")
        df_target = pd.DataFrame(cursor.fetchall(), columns=['site_cd', 'product_id'])
    return df_target

def extract_product_info(df):
    # scrapping 대상
    df_target = get_target()

    # 사이트별 default url 조합
    with open('etl/config.json', 'r', encoding='UTF-8') as f:
        gsshop = json.load(f)['defaultpath']['gsshop']
        gmarket = json.load(f)['defaultpath']['gmarket']
    df_target['url'] = gsshop + df_target['product_id']
    df_target.loc[df_target['site_id'] == 'gmarket', 'url'] = gmarket + df_target['product_id']
    print(df_target)

def main():
    df_xpath = extract_xpath()
    extract_product_info(df_xpath)

if __name__ == '__main__':
    main()