import os
import json

# 程序目录
PATH = os.getcwd() + "\\"

# CSS文件路径
BLFRPCss_PATH = PATH + "CSS\\BLFRP.css"
NavigationBarCss_PATH = PATH + "CSS\\NavigationBar.css"
Logon_QwidgetCss_PATH = PATH + "CSS\\Logon_Qwidget.css"

# 软件图标
BLFRPIcon = PATH + "Icon\\BLFRPIcon.png"
BLFRPLogo = PATH + "Icon\\BLFRPLogo.png"

# 按钮图标
Button_HomePageIcon = PATH + "Icon\\HomePageIcon.svg"
Button_LogIcon = PATH + "Icon\\LogIcon.svg"
Button_TunnelIcon = PATH + "Icon\\TunnelIcon.svg"
Button_SettingsIcon = PATH + "Icon\\SettingsIcon.svg"
Button_ConcerningIcon = PATH + "Icon\\ConcerningIcon.svg"
Button_UserIcon = PATH + "Icon\\user.svg"
Button_ClickHomeIcon = PATH + "Icon\\ClickHome.svg"

# 用户须知
NotoceToUsers_text = """
因未阅读网站公告导致的业务损失或奇葩问题,或者没带眼镜提出的问题一律不予回复,多次询问将直接拉黑
域名需要过白的节点,请联系管理员并注明用途
用户速率*带宽倍率=实际获得速率
带端口限制的节点,指的是远程端口受限,本地端口无任何限制
您可不时关注节点列表,节点可能随时上新
香港及国外节点晚高峰丢包属正常现象,对建站影响不大
免费节点不保证稳定性,特别是PLC类型节点,但我们建议使用PLC类型节点进行大文件传输.
使用人数过多的节点,容易造成卡顿,如 泉州 节点,我们无法保证其完全可用性
节点距离您的地理位置越近,延迟越低
禁止搭建任何色情,暴力,血腥,或违反国家法律的服务(如外挂软件),查到即封
仅标明支持建站的节点允许您建站,无注明节点可能无法建站
使用配置文件即表示您有能力解决遇到的任何问题!
如遇隧道启动时端口占用,请尝试操作 隧道管理强制下线 若仍旧无法解决请群内联系管理员
本软件为开源软件,请从BLFRP官网下载本软件,通过其他渠道下载本软件造成的损失我们概不负责
"""

# 版本信息
VERSION = "BLFRP 1.0.0.0 Bata"

# 配置文件
CONFIG_PATH = PATH + "Config\\Config.json"
USER_CONFIG_PATH = PATH + "Config\\User.json"
API_CONFIG_PATH = PATH + "Config\\API.json"

User_Json = {
  "KEY": "",
  "name": "",
  "ID": "",
  "EnrollMail": "",
  "EnrollTime": "",
  "UsersGroup": "",
}


def Write_Json(path, name1, name2):
  "修改Json格式文件"
  with open(path, "w") as f:
    data = json.load(f)
  data[name1] = name2
  with open(path, "w") as f:
    json.dump(data, f, indent=4)


def Read_Json(path, name1):
  "读取Json格式文件"
  with open(path, "r") as f:
    data = json.load(f)
  return data[name1]

# API访问密钥
key = Read_Json(API_CONFIG_PATH,"key")

