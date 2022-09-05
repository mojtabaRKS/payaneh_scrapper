from bs4 import BeautifulSoup
import random, time, requests, os

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

URL = "https://m.payaneh.ir/bus/index/Tehran/Ilam/1401-06-18"
# URL = "https://m.payaneh.ir/bus/index/Tehran/Babolsar/1401-06-14"

# while True:

# page = requests.get(URL)
# soup = BeautifulSoup(page.content, "html.parser")

# wrapper = soup.find("div", attrs={"class": "row services"})

# if wrapper != None:
API_KEY = os.environ.get("API_KEY")
SENDER = os.environ.get("SENDER")

SMS_URL = f"https://api.kavenegar.com/v1/{API_KEY}/sms/send.json"
MESSAGE = "بلیت اومد سریع برو بخر !!"
RECEIVERS = ",".join(("09212673451", "09024007360"))

REQ = f"{SMS_URL}?receptor={RECEIVERS}&message={MESSAGE}"
requests.get(REQ)
n = random.randint(15, 90)
time.sleep(n)