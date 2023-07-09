import os
import Config
import webbrowser
import requests

def logon_status():
  if (os.path.isfile(Config.USER_CONFIG_PATH)):
    return True
  else:
    return False

def Fetch_Announcement():
  pass

def Determine_The_Key(key):
  return True

def Create_User_Config(key):
  pass

def Click_Home():
  webbrowser.open_new('https://frp.mybailu.net/')

def User_Name():
  return "114514"

def User_mail():
  return "114514@114514.com"

def User_ID():
  return "114514"

def User_Time():
  return "114514-06-06"

def User_UsersGroup():
  return "admin"


def MapInformation_RemainingTraffic():
  return "114514"

def MapInformation_UsedToday():
  return "114514"

def MapInformation_BroadbandSpeeds():
  return "114514Mbps 上行 114514Mbps 下行"

def MapInformation_NumberTunnels():
  return "114514"

def MapInformation_CreateTunnel():
  return "114514"

def MapInformation_TotalCheckin():
  return "114514"

def MapInformation_GetTraffic():
  return "114514"

def MapInformation_LastCheckin():
  return "114514-06-06 06:06:06"
