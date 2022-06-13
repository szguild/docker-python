import connection
import psycopg2

def job_logging(job_name, status_cd, message):

    conn = connection.PostgresConnect.conn

    with conn.cursor() as cursor:
        
        if status_cd == 'I':
            cursor.execute("insert into product.tb_job_log (job_name, status_cd, start_dt) "
                            "values (%s,%s,now())"
                            ,(job_name, status_cd))

        else:
            cursor.execute("update product.tb_job_log "
                            "set status_cd = %s "
                            "   ,end_dt = now() "
                            "   ,message = %s "
                            "where id = (select max(id) from product.tb_job_log where job_name = %s)",
                            (status_cd, message, job_name))

    conn.commit()