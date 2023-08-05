import os
import app.Config as Config
import webbrowser
import requests

def logon_status():
  "获取用户是否登录"
  # return True
  if (os.path.isfile(Config.USER_CONFIG_PATH)):
    return True
  else:
    return False

def Fetch_Announcement():
  "获取网站公告信息"
  try:
    data = str(requests.post(Config.Read_Json(Config.API_CONFIG_PATH,"api-Announcement"),verify=False,data={"key": Config.key}).text)
    return data
  except:
    return "无法连接服务器,可能是您的网络运营商问题"

def Remove_User():
  os.remove(Config.USER_CONFIG_PATH)

def Determine_The_Token(Token):
  "判断访问密钥是否正确,Token为访问密钥"
  try:
    data = {"key": Config.key,"Token": str(Token)}
    return_text = str(requests.post(Config.Read_Json(Config.API_CONFIG_PATH,"api-Token"),verify=False,data=data).text)
    if (return_text == "True"):
      return True
    else:
      return False
  except:
    return False

def Create_User_Config(Token):
  "创建用户并写入json,Token为访问密钥"
  Config.Create_Json(Config.USER_CONFIG_PATH, Config.Create_User_Json())

def Click_Home():
  "打开官网"
  webbrowser.open_new('https://frp.mybailu.net/')

def User_Name():
  "用户名"
  return "114514"

def User_mail():
  "注册邮箱"
  return "114514@114514.com"

def User_ID():
  "用户ID"
  return "114514"

def User_Time():
  "用户注册时间"
  return "114514-06-06"

def User_UsersGroup():
  "用户所在组"
  return "admin"


def MapInformation_RemainingTraffic():
  "剩余流量"
  return "114514"

def MapInformation_UsedToday():
  "今日已用"
  return "114514"

def MapInformation_BroadbandSpeeds():
  "宽带速率"
  return "666Mbps 上行 666Mbps 下行"

def MapInformation_NumberTunnels():
  "隧道数量"
  return "114514"

def MapInformation_CreateTunnel():
  "创建隧道"
  return "20"

def MapInformation_TotalCheckin():
  "总计签到"
  return "114514"

def MapInformation_GetTraffic():
  "获得流量"
  return "114514"

def MapInformation_LastCheckin():
  "上次签到时间"
  return "114514-06-06 06:06:06"
