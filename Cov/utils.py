import time
import pymysql


def get_conn():
    # Create a connection
    conn = pymysql.connect(host="127.0.0.1",
                           user="root",
                           password="admin",
                           db="cov",
                           charset="utf8")
    # create cursor
    cursor = conn.cursor()  # The result set returned after execution is displayed as a tuple by default
    return conn, cursor


def close_conn(conn, cursor):
    cursor.close()
    conn.close()


def query(sql, *args):
    conn, cursor = get_conn()
    cursor.execute(sql, args)
    res = cursor.fetchall()
    close_conn(conn, cursor)
    return res


def get_c1_data():
    """
    :return: Return the data of div id=c1
    """
    # Because the data will be updated multiple times, take the set of data with the latest timestamp
    sql = """
    SELECT total,total-heal-dead,heal,dead from (
    select sum(confirm) total, 
    (SELECT heal from history ORDER BY ds desc LIMIT 1) heal ,
      sum(dead) dead 
    from details where update_time=(
      select update_time from details order by update_time desc limit 1)
    ) d;
    """
    res = query(sql)
    return res[0]


def get_c2_data():
    """
    :return:  Return data in every province
    """
    # Because the data will be updated multiple times, take the set of data with the latest timestamp
    sql = "select province,sum(confirm_now) from details " \
          "where update_time=(select update_time from details " \
          "order by update_time desc limit 1) " \
          "group by province"
    res = query(sql)
    return res


def get_l1_data():
    sql = "select ds,confirm_add,suspect_add from history"
    res = query(sql)
    return res


def get_l2_data():
    sql = "select end_update_time,province,city,county,address,type" \
          " from risk_area " \
          "where end_update_time=(select end_update_time " \
          "from risk_area " \
          "order by end_update_time desc limit 1) "
    res = query(sql)
    return res


def get_r1_data():
    """
    :return:  Return to the top 5 provinces with the remaining confirmed cases
    """
    sql = 'SELECT province,confirm FROM ' \
          '(select province ,sum(confirm_now) as confirm from details  ' \
          'where update_time=(select update_time from details ' \
          'order by update_time desc limit 1) ' \
          'group by province) as a ' \
          'ORDER BY confirm DESC LIMIT 5'
    res = query(sql)
    return res


def get_r2_data():
    """
    :return:  Return to the most recent 30 hot searches
    """
    sql = 'select content from hotsearch order by id desc limit 30'
    res = query(sql)
    return res
