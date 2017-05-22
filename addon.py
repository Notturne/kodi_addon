import xbmcaddon
import xbmcgui

from io import StringIO, BytesIO
from bs4 import BeautifulSoup
import requests

url = 'http://live3s.com'
page = requests.get(url)

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
 
line1 = page
 
xbmcgui.Dialog().ok(addonname, line1)
