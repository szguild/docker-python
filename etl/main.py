from email.policy import default
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
        # 추출 대상 정보 획득 (마스터에 존재하는 전체 상품정보 갱신이 필요할 경우, product.tb_product_m 테이블 정보로 대체)
        cursor.execute("select site_cd, product_id, '' as url from product.tb_product_target where use_yn = 'Y'")
        df_target = pd.DataFrame(cursor.fetchall(), columns=['site_cd', 'product_id', 'url'])
    return df_target

def get_target_url():
    # scrapping 대상
    df_target = get_target()

    # 사이트별 default url 조합
    with open('etl/config.json', 'r', encoding='UTF-8') as f:
        defaultpath = json.load(f)['defaultpath']
    # df_target['url'] = gsshop + df_target['product_id']
    # df_target.loc[df_target['site_id'] == 'gmarket', 'url'] = gmarket + df_target['product_id']
    # print(df_target)
    df_path = pd.DataFrame(columns=['site_cd', 'defaultpath'])
    
    for s in defaultpath:
        df_path.loc[df_path['site_cd'].count()] = [s, defaultpath[s]]

    df_target = pd.merge(df_target, df_path, how='inner', on='site_cd')
    df_target['url'] = df_target['defaultpath'] + df_target['product_id'].astype(str)

    return df_target

def get_product_info(df_xpath, df_target_url):
    df_product_info = pd.DataFrame(columns=['site_cd','product_id','product_nm','price','img_url','page_url'])

def main():
    df_xpath = extract_xpath()

    print(df_xpath)

    df_target_url = get_target_url()
    df_product_info = get_product_info(df_xpath, df_target_url)

if __name__ == '__main__':
    main()