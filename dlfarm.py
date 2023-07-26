import requests
import json
import schedule
import time


ajax_url = "https://www.dlsite.com/home/event/dlfarm/ajax"
show_data = {'act': 'show'}
draw_data = {'act': 'draw'}
req_headers = {
    "Cookie": "__DLsite_SID=xxxxxxx;"  # TODO 更改此处为你的cookie
}


def get(url, data, headers):
    response = requests.get(url, params=data, headers=headers)
    print(response.text)
    return json.loads(response.text)


def post(url, data, headers):
    response = requests.post(url, data=data, headers=headers)
    print(response.text)
    return json.loads(response.text)


def checkin():
    print("开始打卡：DLfarm")
    try:
        show_result = get(ajax_url, show_data, req_headers)
        if show_result["class"][1] == 'end':
            print('已经签过到了')
        elif show_result["class"][1] == 'logout':
            print("cookie失效")
        elif show_result["class"][1] == "logged_in":
            draw_result = get(ajax_url, draw_data, req_headers)
            if draw_result["class"][0].startswith("type_"):
                print("打卡成功，获得的奖励为：" + draw_result["name"] +
                      "\n结果参考：\nはずれ(type_01) = 0pt, ひまわり/並レア(type_05) = 1pt, 超レア() = 10pt, 激レア() = 100pt")
            elif draw_result["class"][0] == "error":
                print("打卡发生错误，可能是已经打过卡了")
            else:
                print("打卡过程发生未知错误：" + draw_result["class"][0])
        else:
            print("获取打卡状态时发生未知错误+" + show_result["class"][1])
    except:
        print("打卡失败(可能是网络异常)，将在1分钟后重试")
        time.sleep(60)
        checkin()

"""
note: 
はずれ(type_01) = 0pt, 並レア() = 1pt, 超レア() = 10pt, 激レア() = 100pt
"""

checkin()

# 定义定时任务
schedule.every().day.at("06:00").do(checkin)

# 无限循环执行定时任务
while True:
    schedule.run_pending()
    time.sleep(1)
