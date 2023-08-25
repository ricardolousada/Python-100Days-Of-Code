# Create By Ricardo Lousada
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests

URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

load_dotenv()
#cog_endpoint = os.getenv('COG_SERVICE_ENDPOINT')

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,pt-PT;q=0.8,pt;q=0.7",
    "sec-ch-ua-platform":"Windows",
    "ec-ch-ua":"'Not/A)Brand';v='99', 'Google Chrome';v='115', 'Chromium';v='115'",
    "sec-ch-ua-mobile": "?0"
    #"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}

request = requests.get(url=URL, headers=headers, verify=False)
print(request.text)