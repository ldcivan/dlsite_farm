# DLFarm已关闭，本项目已失效
# DLFarm has been closed, this repo has been out of date

# dlsite_farm

基于python的dlfarm自动签到程序
DLfarm auto check in script

## 用途 Use to...
定期获取少量dlsite点数，防止点数过期.

Get some DL points to prevent expiration of DL pts.

## 用法 Usage
* 更改`req_headers`中的cookie为你自己登录dlsite后的cookie，理论上只需要`__DLsite_SID`的值即可。

  Use your own cookie in DLsite.com. You only need get `__DLsite_SID` in cookie string to use the script.

* 之后运行程序，程序会立即进行一次签到；之后若不关闭程序，程序会在当地时间每天六点打卡。

  Then run the script, the script will immediately check in for once. And if you do not stop the script, it will check in at 6 a.m. (local time) everyday.

  注意，dlfarm每日数据刷新时间为日本时间（UTC+9）上午5时，如果需要调整打卡时间，请自行调整`schedule.every().day.at("06:00").do(checkin)`一行。

  Notice: DLfarm renew its data at 5 a.m. (UTC+9). If you want to change the checkin time, adjust `schedule.every().day.at("06:00").do(checkin)` by yourself.
