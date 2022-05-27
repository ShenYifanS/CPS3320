import requests
import pymysql
import time, datetime
import json
import hashlib
import traceback
import sys
from bs4 import BeautifulSoup
import re


def get_conn():
    conn = pymysql.connect(host="127.0.0.1",
                           user="root",
                           password="admin",
                           db="cov",
                           charset="utf8")
    # Create a cursor
    cursor = conn.cursor()  # The result set returned after execution is displayed as a tuple by default
    return conn, cursor


def close_conn(conn, cursor):
    cursor.close()
    conn.close()


def get_tencent_data():
    url_det = 'https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=diseaseh5Shelf'
    url_his = "https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=chinaDayList,chinaDayAddList,nowConfirmStatis,provinceCompare"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    }
    r_det = requests.get(url_det, headers)
    r_his = requests.get(url_his, headers)
    res_det = json.loads(r_det.text)  # json string to dictionary
    res_his = json.loads(r_his.text)
    data_det = res_det['data']['diseaseh5Shelf']
    data_his = res_his['data']

    history = {}  # historical data




    for i in data_his["chinaDayList"]:
        ds = i["y"] + "." + i["date"]
        tup = time.strptime(ds, "%Y.%m.%d")
        ds = time.strftime("%Y-%m-%d", tup)
        confirm = i["confirm"]
        confirm_now = i["nowConfirm"]
        suspect = i["suspect"]
        heal = i["heal"]
        dead = i["dead"]
        history[ds] = {"confirm": confirm, "confirm_now": confirm_now, "suspect": suspect, "heal": heal, "dead": dead}
    for i in data_his["chinaDayAddList"]:
        ds = i["y"] + "." + i["date"]
        tup = time.strptime(ds, "%Y.%m.%d")
        ds = time.strftime("%Y-%m-%d", tup)
        confirm_add = i["confirm"]
        suspect_add = i["suspect"]
        heal_add = i["heal"]
        dead_add = i["dead"]
        history[ds] = {"confirm_add": confirm_add, "suspect_add": suspect_add, "heal_add": heal_add, "dead_add": dead_add}

    details = []  # 当日详细数据
    update_time = data_det["lastUpdateTime"]
    data_country = data_det["areaTree"]
    data_province = data_country[0]["children"]  # Provinces of China
    for pro_infos in data_province:
        province = pro_infos["name"]  # province name
        for city_infos in pro_infos["children"]:
            city = city_infos["name"]  # city name
            confirm = city_infos["total"]["confirm"]  # confirm
            confirm_add = city_infos["today"]["confirm"]  # confirm_add
            # confirm_now = city_infos["total"]["nowConfirm"]  # confirm_now
            heal = city_infos["total"]["heal"]  # heal
            dead = city_infos["total"]["dead"]  # dead
            details.append([update_time, province, city, confirm, confirm_add, heal, dead])
    return history, details


def get_baidu_hot():
    # url = "https://voice.baidu.com/act/virussearch/virussearch?from=osari_map&tab=0&infomore=1"
    url = "https://top.baidu.com/board?tab=realtime"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    }
    res = requests.get(url, headers=headers)
    # res.encoding = "gb2312"
    html = res.text
    soup = BeautifulSoup(html, features="html.parser")
    kw = soup.select("div.c-single-text-ellipsis")
    count = soup.select("div.hot-index_1Bl1a")
    context = []
    for i in range(len(kw)):
        k = kw[i].text.strip()  # Remove left and right spaces
        v = count[i].text.strip()
        #         print(f"{k}{v}".replace('\n',''))
        context.append(f"{k}{v}".replace('\n', ''))
    return context


def get_risk_area():
    # current timestamp
    o = '%.3f' % (time.time() / 1e3)
    e = o.replace('.', '')
    i = "23y0ufFl5YxIyGrI8hWRUZmKkvtSjLQA"
    a = "123456789abcdefg"

    s1 = hashlib.sha256()
    s1.update(str(e + i + a + e).encode("utf8"))
    s1 = s1.hexdigest().upper()

    s2 = hashlib.sha256()
    s2.update(str(e + 'fTN2pfuisxTavbTuYVSsNJHetwq5bJvCQkjjtiLM2dCratiA' + e).encode("utf8"))
    s2 = s2.hexdigest().upper()
    # post request data
    post_dict = {
        'appId': 'NcApplication',
        'key': '3C502C97ABDA40D0A60FBEE50FAAD1DA',
        'nonceHeader': '123456789abcdefg',
        'paasHeader': 'zdww',
        'signatureHeader': s1,
        'timestampHeader': e
    }
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Referer': 'http://bmfw.www.gov.cn/',
        'Origin': 'http://bmfw.www.gov.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'x-wif-nonce': 'QkjjtiLM2dCratiA',
        'x-wif-paasid': 'smt-application',
        'x-wif-signature': s2,
        'x-wif-timestamp': e,
    }
    url = "http://103.66.32.242:8005/zwfwMovePortal/interface/interfaceJson"
    req = requests.post(url=url, data=json.dumps(post_dict), headers=headers)
    resp = req.text
    res = json.loads(resp)
    # print(res)
    utime = res['data']['end_update_time']  # update time
    hcount = res['data'].get('hcount', 0)  # Number of high-risk areas
    mcount = res['data'].get('mcount', 0)  # Number of low-risk areas
    # precise data
    hlist = res['data']['highlist']
    mlist = res['data']['middlelist']

    risk_h = []
    risk_m = []

    for hd in hlist:
        type = "高风险"
        province = hd['province']
        city = hd['city']
        county = hd['county']
        area_name = hd['area_name']
        communitys = hd['communitys']
        for x in communitys:
            risk_h.append([utime, province, city, county, x, type])

    for md in mlist:
        type = "中风险"
        province = md['province']
        city = md['city']
        county = md['county']
        area_name = md['area_name']
        communitys = md['communitys']
        for x in communitys:
            risk_m.append([utime, province, city, county, x, type])

    return risk_h, risk_m


def update_risk_area():
    cursor = None
    conn = None
    try:
        risk_h, risk_m = get_risk_area()
        conn, cursor = get_conn()
        sql = "insert into risk_area(end_update_time,province,city,county,address,type) values(%s,%s,%s,%s,%s,%s)"
        sql_query = 'select %s=(select end_update_time from risk_area order by id desc limit 1)'  # Compare the current maximum timestamp
        cursor.execute(sql_query, risk_h[0][0])
        if not cursor.fetchone()[0]:
            print(f"{time.asctime()}Start updating latest data")
            for item in risk_h:
                cursor.execute(sql, item)
            for item in risk_m:
                cursor.execute(sql, item)
            conn.commit()
            print(f"{time.asctime()}Update the latest data completed")
        else:
            print(f"{time.asctime()}Already Updated")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


def update_hotsearch():
    cursor = None
    conn = None
    try:
        context = get_baidu_hot()
        print(f"{time.asctime()}Start to Update")
        conn, cursor = get_conn()
        sql = "insert into hotsearch(dt,content) values(%s,%s)"
        ts = time.strftime("%Y-%m-%d %X")
        for i in context:
            cursor.execute(sql, (ts, i))
        conn.commit()
        print(f"{time.asctime()}Finish")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


def update_details():
    cursor = None
    conn = None
    try:
        li = get_tencent_data()[1]# 0 is the historical data dictionary, 1 is the latest detailed data list
        conn, cursor = get_conn()
        sql = "insert into details(update_time,province,city,confirm,confirm_add,confirm_now,heal,dead) " \
              "values(%s,%s,%s,%s,%s,%s,%s,%s)"
        sql_query = 'select %s=(select update_time from details order by id desc limit 1)'
        cursor.execute(sql_query, li[0][0])
        if not cursor.fetchone()[0]:
            print(f"{time.asctime()}Start to Update")
            for item in li:
                cursor.execute(sql, item)
            conn.commit()
            print(f"{time.asctime()}Update Finished")
        else:
            print(f"{time.asctime()}Already Update!")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


def update_history():
    cursor = None
    conn = None
    try:
        dic = get_tencent_data()[0]  # 0 is the historical data dictionary, 1 is the latest detailed data list
        print(f"{time.asctime()}开始更新历史数据")
        conn, cursor = get_conn()
        sql = "insert into history values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        sql_query = "select confirm from history where ds=%s"
        for k, v in dic.items():
            # item format {'2020-01-13': {'confirm': 41, 'suspect': 0, 'heal': 0, 'dead': 1}
            if not cursor.execute(sql_query, k):  # 如果当天数据不存在，才写入
                cursor.execute(sql, [k, v.get("confirm"), v.get("confirm_add"), v.get("confirm_now"),
                                     v.get("suspect"), v.get("suspect_add"), v.get("heal"),
                                     v.get("heal_add"), v.get("dead"), v.get("dead_add")])
        conn.commit()  # Commit transaction update delete insert operation
        print(f"{time.asctime()}Update Finish")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


if __name__ == "__main__":
    update_hotsearch()
    # update_risk_area()
    # update_history()
    # update_details()


