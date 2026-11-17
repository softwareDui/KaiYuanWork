from utils.db_config import get_db_connection


def querys(sql, params, type='no_select'):
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, tuple(params))
            result = cursor.fetchall() if type != 'no_select' else '执行成功'
        conn.commit()
    return result
