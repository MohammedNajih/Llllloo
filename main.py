import requests,user_agent,json,flask,telebot,random,os,sys
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
import json
from flask import Flask, request
import requests , telebot , pyfiglet
from telebot import apihelper 
from telebot import types
from gdolib import *
import datetime 
from datetime import datetime
import datetime

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)



#-----------[ Colors ]-----------
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
E = "\033[0;90m" #رمادي
#------------------------------[Start CoDe]------------------------------
now = datetime.datetime.today()

now = datetime.datetime.today()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
t=(mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss)


hours = (now.hour)
x = datetime.datetime.now()
g= datetime.datetime(2022, 7, 25, 00, 00 ,0)

if (x.strftime("%x"))>(g.strftime("%x")):
 print('\n\n')
 print("     "+'source  has been stopped. ✅Dv : @W_2_X 🥷✅')
 print('\n\n')
 print(x)
 
 sys.exit(0)
 

if (x.strftime("%x"))==(g.strftime("%x")):
   print('')
   if(x.strftime("%X"))>(g.strftime("%X")):
    print('\n\n')
    print("     "+'sand to @W_2_X  Thanks🖤' )
    print('\n\n')
    print(x)
    
    sys.exit(0)
   else:
    print('')  
else:
    print('')
print('')



token = input(f'{X} [{C}⌯{X}] {C}ENTER TOKEN{X} » ' + C)
print(Z+'Go to your bot baby 🦖🔥.')
@bot.message_handler(commands = ["start"])

def Start(message):
 Name = message.chat.first_name
 #User = message.from_user.username 
 iD = message.chat.id
 url = f"https://t.me/{message.from_user.username}"
 A = types.InlineKeyboardMarkup(row_width=2)
 B = types.InlineKeyboardButton(text ="• 𝙲𝙰𝙷𝙽𝙽𝙴𝙻 •" , url = "t.me/Wv7BoT")
 C = types.InlineKeyboardButton(text ="• 𝗱𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 ◔͜͡◔" , url = "t.me/C_c_C_u")
 F = types.InlineKeyboardButton(text ="⌯ 𝚂𝚃𝙰𝚁𝚃 𝙲𝙷𝙴𝙰𝙺 ⌯",callback_data="y")
 A.add(B,C,F)
 bot.send_photo(message.chat.id,url, """• 𝚆𝙴𝙻𝙲𝙾𝙼𝙴  🦖🔥•
 عبود قال لي اقولك انه يحبك🥺🥺🔥
•━━━━━━━━━━━━•
⌯ 𝚂𝙴𝚁 › {}
⌯ Ch : @WV7BoT
⌯ 𝙸𝙳 › {}
•━━━━━━━━━━━━•""".format(Name,iD), parse_mode = "markdown" , reply_markup = A)


@bot.callback_query_handler(func=lambda call: True)

def answer(call):
    if call.data =="y":
    	bu(call.message)
    if call.data =="G":
    	bot_2(call.message)
    if call.data == "D":
    	bot_3(call.message)
    if call.data == "O":
    	user_3(call.message)
    if call.data == "i":
    	user_5(call.message)
    if call.data == "l":
    	user_6(call.message)
    if call.data == "F":
    	DV(call.message)
    if call.data == "B":
    	soon_tik(call.message)
    if call.data == "q":
    	soon_insta(call.message)
    if call.data == "jk":
    	hit_TikTok(call.message)
    if call.data == "pl":
    	hit_insta(call.message)
    if call.data == "po":
    	hit_face(call.message)
    	
def bu(message):
	O0 = types.InlineKeyboardMarkup(row_width=1)
	Psg = types.InlineKeyboardButton(text = "Bot - ## ༻",callback_data = 'G')
	Pby = types.InlineKeyboardButton(text = "Bot - ### ༻", callback_data= 'D')
	Pda = types.InlineKeyboardButton(text = "User - #_#_# ༻",callback_data = 'O')
	P = types.InlineKeyboardButton(text = "User - ##### ༻",callback_data = 'i')
	u = types.InlineKeyboardButton(text = "User - ###### ༻",callback_data = 'l')
	c = types.InlineKeyboardButton(text = "User - TikTok ༻",callback_data = 'B')
	y = types.InlineKeyboardButton(text = "User - Instagram༻",callback_data = 'q')
	oi = types.InlineKeyboardButton(text = "Hit - avaliable TikTok ༻",callback_data = 'jk')
	cl = types.InlineKeyboardButton(text = "Hit - avaliable  Instagram༻",callback_data = 'pl')
	xc = types.InlineKeyboardButton(text = "Hit - avaliable  Facbook༻",callback_data = 'po')
	j = types.InlineKeyboardButton(text = "مراسله المطور🦖.",callback_data = 'F')
	O0.add(Psg,Pby,Pda,P,u,c,y,oi,cl,xc,j)
	bot.send_message(message.chat.id,text="⌯ 𝙿𝙻𝙴𝙰𝚂𝙴 𝙲𝙷𝙾𝙾𝚂𝙴 ⸙",parse_mode='markdown',reply_markup=O0)


def bot_2(message):
	h = types.InlineKeyboardMarkup()
	dd = types.InlineKeyboardButton(text = " 𝗱𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 ◔͜͡◔", url = "t.me/C_c_C_u")
	h.add(dd)
	hit , bd = 0 , 0
	while True:
		litters = 'QWERTYUIOPASDFGHJKLZXCVNBM1234567890'
		c = random.choice(litters)
		o = random.choice(litters)
		username = c+o+'bot'
		url = f"https://t.me/{username}"
		req = requests.get(url)
		if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
			hit+=1
			bot.send_message(message.chat.id, text=f"⌯ New User »  @{username} . ",parse_mode = "markdown",reply_markup=h)
		else:
			bd+= 1 
			bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"• Hi Check Username Bot\n<~>~>~>~>~>~>~>~>~>\n• Error User : {bd}\n• Done User : {hit}\n• In User : @{username}\n<~>~>~>~>~>~>~>~>~>\nFrOm @C_C_C_u - @Wv7BoT .")
	


def bot_3(message):
	h = types.InlineKeyboardMarkup()
	dd = types.InlineKeyboardButton(text = " 𝗱𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 ◔͜͡◔", url = "t.me/C_c_C_u")
	h.add(dd)
	hit , bd = 0 , 0
	while True:
		litters = 'QWERTYUIOPASDFGHJKLZXCVNBM1234567890'
		c = random.choice(litters)
		o = random.choice(litters)
		l = random.choice(litters)
		username = c+o+l+'bot'
		url = f"https://t.me/{username}"
		req = requests.get(url)
		if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
			hit+=1
			bot.send_message(message.chat.id, text=f"⌯ New User » @{username} .",parse_mode = "markdown",reply_markup=h)
		else:
			bd+= 1 
			bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"• Hi Check Username Bot\n<~>~>~>~>~>~>~>~>~>\n• Error User : {bd}\n• Done User : {hit}\n• In User : @{username}\n<~>~>~>~>~>~>~>~>~>\nFrOm @C_C_C_u - @Wv7BoT .")
			
			
def user_3(message):
	h = types.InlineKeyboardMarkup()
	dd = types.InlineKeyboardButton(text = " 𝗱𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 ◔͜͡◔", url = "t.me/C_c_C_u")
	h.add(dd)
	hit , bd = 0 , 0
	while True:
		litters = 'QWERTYUIOPASDFGHJKLZXCVNBM'
		nmder = '1234567890'
		c = random.choice(litters)
		o = random.choice(nmder)
		i = random.choice(litters)
		e = c+'_'+o+'_'+i
		s = c+'_'+i+'_'+o
		
		d =[e,s]
		username = random.choice(d)
		url = f"https://t.me/{username}"
		req = requests.get(url)
		if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
			hit+=1
			bot.send_message(message.chat.id, text=f"⌯ New User » *`{username}`* . ",parse_mode = "markdown",reply_markup=h)
		else:
			bd+= 1 
			bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"• Hi Check Username \n<~>~>~>~>~>~>~>~>~>\n• Error User : {bd}\n• Done User : {hit}\n• In User : @{username}\n<~>~>~>~>~>~>~>~>~>\nFrOm @C_C_C_u - @Wv7BoT .")
			
			
			
def user_5(message):
	h = types.InlineKeyboardMarkup()
	dd = types.InlineKeyboardButton(text = " 𝗱𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 ◔͜͡◔", url = "t.me/C_c_C_u")
	h.add(dd)
	hit , bd = 0 , 0
	while True:
		litters = 'QWERTYUIOPASDFGHJKLZXCVNBM'
		nmder = '1234567890'
		c = random.choice(litters)
		o = random.choice(nmder)
		i = random.choice(litters)
		e = c+o+o+o+o
		s = c+i+c+i+i
		d = i+c+c+i+c
		j = c+o+i+c+c
		d =[e,s,d,j]
		username = random.choice(d)
		url = f"https://t.me/{username}"
		req = requests.get(url)
		if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
			hit+=1
			bot.send_message(message.chat.id, text=f"⌯ New User » @{username} . ",parse_mode = "markdown",reply_markup=dd)
		else:
			bd+= 1 
			bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"• Hi Check Username \n<~>~>~>~>~>~>~>~>~>\n• Error User : {bd}\n• Done User : {hit}\n• In User : @{username}\n<~>~>~>~>~>~>~>~>~>\nFrOm @C_C_C_u - @Wv7BoT .")
	
	
	
def user_6(message):
	h = types.InlineKeyboardMarkup()
	dd = types.InlineKeyboardButton(text = " 𝗱𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 ◔͜͡◔", url = "t.me/C_c_C_u")
	h.add(dd)
	hit , bd = 0 , 0
	while True:
		litters = 'QWERTYUIOPASDFGHJKLZXCVNBM'
		nmder = '1234567890'
		c = random.choice(litters)
		o = random.choice(nmder)
		i = random.choice(litters)
		e = c+i+o+c+c+c
		s = c+i+c+i+i+c
		d = i+c+c+i+c+o
		j = c+o+i+c+c+i
		v = c+o+o+o+o+o
		k = c+c+o+i+c+c
		x = [e,s,d,j,v,k]
		username = random.choice(x)
		url = f"https://t.me/{username}"
		req = requests.get(url)
		if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
			
			hit+=1
			bot.send_message(message.chat.id, text=f"⌯ New User » @{username} . ",parse_mode = "markdown",reply_markup=h)
		else:
			bd+= 1 
			bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"• Hi Check Username \n<~>~>~>~>~>~>~>~>~>\n• Error User : {bd}\n• Done User : {hit}\n• In User : @{username}\n<~>~>~>~>~>~>~>~>~>\nFrOm @C_C_C_u - @Wv7BoT .")
			
			
def soon_tik(message):
    h = types.InlineKeyboardMarkup()
    dd = types.InlineKeyboardButton(text = " 𝗱𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 ◔͜͡◔",url = "t.me/C_c_C_u")
    h.add(dd)
    hit = 0
    bd = 0
    all = '1234567890qwertyuiopasdfghjklzxcvbnm._'
    
    while True:
     a = random.choice(all)
     s = random.choice(all)
     d = random.choice(all)
     f = random.choice(all)
     c = a+s+d+f
     user = c
     tiko = f'https://www.tiktok.com/@{user}?'
     hea = {
         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'ar',
                        'cookie': 'bm_sz=D629F4942531777D6F7147A73605EDCB~YAAQhVQqLrT8ldN3AQAAvY4T+ArC4uvjnuxrV9pt2l0rKHkp1yqSFyVmqphzleo0kRsXlfI+NbB+LOM88S46yTNKJFjRIpTtPq9rKwsrBBAAkfcyq8+RZH7/Zf6msaZJtLNn/zxAtwnratRpub7m5xD5rufF7yyEZj5G5HxIutar/qCFiClDrwMZN4g39vBR; tt_webid_v2=6935404800675710465; tt_webid=6935404800675710465; tt_csrf_token=FHAWXV6vFZXlSM2eXSRS_6r1; MONITOR_WEB_ID=6935404800675710465; R6kq3TV7=AGOZE_h3AQAArT8QptQP5vh_zveCf-y5-BiUgB0w7IMZfUWedXYgJcIz57M8|1|0|75dd6b518f206372e6d404294a187c94b8126b35; s_v_web_id=verify_kltf64da_CijHZlfi_FdX3_4WE8_9Wwj_IAzVIICoeMBw; csrf_session_id=b2c399a35aae464682b040c14d913de2; bm_mi=DA047E87F2170B8EAEED36DFA89B7EEF~bFZTXUHt/x7P3I0BVhrEb4Td9L8oZ2GpyXZfW+xchO9i3D+JVDz88ASSnmIDwoAj9eNBEr2CRBfBybeh1gzxhUQkMpaXPauZmHFnxobirm+t2tUztvSHjRe7wVmEAzher5o6mgZFo3yICvGZj7Gl0DyAKf9IiMHUCT+P8WchaRo1zn2Tw+i7zcYmVNPFfKCWvBcFurSr7yHOl1W8DBZeM4NciHkWUQ4ZfRSnka5nPBc31710HS6gQL31mYIk5MCC2YzSf89SGSJodJGAkp1fZA==; bm_sv=7C1373BFC9FD4E0464B305E04E391F85~zYvKe8AvrP//Bh3yGBkN9hPkGyzM7JmwI5oyhbcxUHmMaMVX7A54ASSE97V9odLFyKW4B+RTI+2G3FqAeKElYXB+bw5DGu2vwRq89tI2ByGHuHWfJNmJPt+MLaUA1zVjxulAySr/HmXVp82syg2Hct0OfKH5FotWYANjWbWlwVU=; ak_bmsc=546A35303DC5B1DC24F699698FF233DC2E2A54854E2B0000EF813F605E1F4B1A~plMbX0Ui2pNYPSS/i1qPeHNc2xCUddsUFoAOF7Gbmm02GwXrVhn+fZfkeLsnlVZk33Fr4MD6SaesEjx/FclzePXXzOhSiJQ2GdQ996OpIB8lX+kjgVtkeQBXxQ139Neumt8jckA7jT81sgEzIDOZmLO6/KSDSaK95vwDjYEALYND6n9oYpmykVu2KGQYzRg6WueWyO0OrXSINNYmdYO7SF8ktYdO0didVcLX8JwAsFOIli2c6Ou6lhvuvoQeJClQQg; _abck=16220A303EE334985E7B40A39E10EC7F~0~YAAQhVQqLgT9ldN3AQAAwyUV+AUdqGmQv3CIqQnIyXwZFxf1lLyDf3M0i4kSrb/oGfOh9haoEWo2QxMzarNFIHPVzvja0C0ozETE+OS5CBaAx9+79ehyau7EX/wo3QgpVs1CS4v3sh0hclzVhl5LlwXtkCE3e3RCdvbNHXJiBpRf/+MD9HGuPlG1Ns83Auxj/eN8lMXLP3lQng/5xGgcDwXlNWO97iimgzB7FFhMa8cvLh5+7ua4P5HQ3T6O2WJAZZHsqK58z/u1W8NjeSUXh0dqrerPIc10L2hIcOpo6dGkFdG/SX/n9oqWpS4O8A3V640cN3rXoCb9JQFJZBrdRV/qJcpLt2ZdHby+/Igbtq1TFf6CD55L6DCvH8Q1pb1qA8z2zv9Rx1xyiXTnsYwY/YxCqyQrMPvK~-1~-1~-1',
                        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'none',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36'
    }
     reqsnd = requests.session().get(tiko, headers=hea)
     if reqsnd.status_code == 404:
	    	 hit+= 1
	    	 bot.send_message(message.chat.id, text=f"⌯ New User » @{user} . ",parse_mode = "markdown",reply_markup=h)
     else:
         bd+= 1 
         bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"• Hi Check Username TikTok \n<~>~>~>~>~>~>~>~>~>\n• Error User : {bd}\n• Done User : {hit}\n• In User : @{user}\n<~>~>~>~>~>~>~>~>~>\nFrOm @C_C_C_u - @Wv7BoT .")



def soon_insta(message):
    h = types.InlineKeyboardMarkup()
    dd = types.InlineKeyboardButton(text = " 𝗱𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 ◔͜͡◔",url = "t.me/C_c_C_u")
    h.add(dd)
    hit = 0
    bd = 0
    all = '1234567890qwertyuiopasdfghjklzxcvbnm._'
    try:
    	v = 'https://www.instagram.com/accounts/emailsignup/'
    	req = requests.get(v,headers={"user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}).cookies.get_dict()
    	mid = req['mid']
    	ig = req['ig_did']
    	i = req['ig_nrcb']
    	csrf = req['csrftoken']
    except requests.exceptions.ConnectionError:
    	v = 'https://www.instagram.com/accounts/emailsignup/'
    	req = requests.get(v,headers={"user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}).cookies.get_dict()
    	mid = req['mid']
    	ig = req['ig_did']
    	i = req['ig_nrcb']
    	csrf = req['csrftoken']
    while True:
     a = random.choice(all)
     s = random.choice(all)
     d = random.choice(all)
     f = random.choice(all)
     g = random.choice(all)
     l = random.choice(all)
     v = l+l+g+l+l
     b = g+f+g+f+g
     m = g+g+'_'+f+f
     j = g+'.'+g+f+g
     k = l+l+'_'+g+g
     c = [v,b,m,j,k]
     user = random.choice(c)
     url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
     head = {"accept": '*/*',
'accept-encoding': "gzip, deflate, br",
"accept-language": "ar,en;q=0.9",
"content-length": "383",
"content-type": "application/x-www-form-urlencoded",
"cookie": f'mid={mid}; ig_did={ig}; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; datr=1AowYgO84Ejd51RFZGIapmbk; ig_direct_region_hint="CLN\05453358207778\0541688796486:01f71cfca83b40e08f4455a3c69feeefeadf41a6c7a76553e488c59b2ae8ae624b229f08"; shbid="15813\05453358207778\0541689148844:01f7d1c6791d8190c1c1903a32c63fda8a72a91405faad7bc23f83066265b367c4fc04ef"; shbts="1657612844\05453358207778\0541689148844:01f7abef005a2c35962e3880fd1de92c761afc12b8c5849e063f0c368c972e163af643b0"; rur="LDC\05453358207778\0541689148887:01f7fd3581f7650425803d85c4caa8eff267ad008011b894b92ab54fb7968b071ab81cca"; csrftoken={csrf}',
'origin': "https://www.instagram.com",
"referer": "https://www.instagram.com/accounts/emailsignup/",
"sec-ch-prefers-color-scheme": "light",
"sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform": "Windows",
"sec-fetch-dest": "empty",
"sec-fetch-mode": "cors",
"sec-fetch-site": "same-origin",
"user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
"viewport-width": "617",
"x-asbd-id": "198387",
"x-csrftoken": csrf,
"x-ig-app-id": "936619743392459",
"x-ig-www-claim": "0",
"x-instagram-ajax": "d66974950786",
"x-requested-with": "XMLHttpRequest"}
     time_now=int(datetime.now().timestamp())
     dat = {'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time_now}:112233$$ggfff',
"email": "ejdjdhdgdbsj@gmail.com",
"username": user,
"first_name": "wdkdjfejfgw",
"client_id": "Yemn3AAEAAGx56yZBU5-oiVvPQ4e",
"seamless_login_enabled": "1",
"opt_into_one_tap": "false"}
     re = requests.post(url,headers=head,data=dat).text
     if "This username isn't available. Please try another." in re:
     	bd+= 1
     	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"• Hi Check Username TikTok \n<~>~>~>~>~>~>~>~>~>\n• Error User : {bd}\n• Done User : {hit}\n• In User : @{user}\n<~>~>~>~>~>~>~>~>~>\nFrOm @C_C_C_u - @Wv7BoT .")
     	
     else:
     	hit+= 1
     	bot.send_message(message.chat.id, text=f"⌯ New User » @{user} . ",parse_mode = "markdown",reply_markup=h)
    
    
    
def hit_face(message):
    bd = 0; hit = 0
    h = types.InlineKeyboardMarkup()
    dd = types.InlineKeyboardButton(text = " 𝗱𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 ◔͜͡◔",url = "t.me/C_c_C_u")
    h.add(dd)
    while True:
        email = gdo_drow.get_email().split('@')[0]+"@gmail.com"
        gmail = check_email.gmail(email)
        if gmail['status']=='Success':
            tik = check_email.face(email)
            if tik['status']=='Success':
            	hit+= 1
            	bot.send_message(message.chat.id, text=f"⌯ New hit Face » {email} . ",parse_mode = "markdown",reply_markup=h)
        else:
            	bd+= 1 
            	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"• Hi Check available  Face \n<~>~>~>~>~>~>~>~>~>\n• Error email : {bd}\n• Done email : {hit}\n• In email : {email}\n<~>~>~>~>~>~>~>~>~>\nFrOm @C_C_C_u - @Wv7BoT .")
    
    
    
def hit_TikTok(message):
    bd = 0; hit = 0
    h = types.InlineKeyboardMarkup()
    dd = types.InlineKeyboardButton(text = " 𝗱𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 ◔͜͡◔",url = "t.me/C_c_C_u")
    h.add(dd)
    while True:
        email = gdo_drow.get_email().split('@')[0]+"@gmail.com"
        gmail = check_email.gmail(email)
        if gmail['status']=='Success':
            tik = check_email.tiktok(email)
            if tik['status']=='Success':
            	hit+= 1
            	bot.send_message(message.chat.id, text=f"⌯ New hit TikTok » {email} . ",parse_mode = "markdown",reply_markup=h)
        else:
            	bd+= 1 
            	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"• Hi Check available  TikTok \n<~>~>~>~>~>~>~>~>~>\n• Error email : {bd}\n• Done email : {hit}\n• In email : {email}\n<~>~>~>~>~>~>~>~>~>\nFrOm @C_C_C_u - @Wv7BoT .")
     


def hit_insta(message):
    bd = 0; hit = 0
    h = types.InlineKeyboardMarkup()
    dd = types.InlineKeyboardButton(text = " 𝗱𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 ◔͜͡◔",url = "t.me/C_c_C_u")
    h.add(dd)
    while True:
        email = gdo_drow.get_email().split('@')[0]+"@gmail.com"
        gmail = check_email.gmail(email)
        if gmail['status']=='Success':
            tik = check_email.instagram(email)
            if tik['status']=='Success':
            	hit+= 1
            	bot.send_message(message.chat.id, text=f"⌯ New hit Insta » {email} . ",parse_mode = "markdown",reply_markup=h)
        else:
            	bd+= 1 
            	bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text=f"• Hi Check available  Insta \n<~>~>~>~>~>~>~>~>~>\n• Error email : {bd}\n• Done email : {hit}\n• In email : {email}\n<~>~>~>~>~>~>~>~>~>\nFrOm @C_C_C_u - @Wv7BoT .")
			


def DV(message):
    h = types.InlineKeyboardMarkup()
    dd = types.InlineKeyboardButton(text = " 𝗱𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 ◔͜͡◔",url = "t.me/C_c_C_u")
    h.add(dd)
    z = 'دا اذا قالك عيب اعرف انو طلبك مرفوض😂🔥.'
    a = 'لو طلبت طلب غبي حيقولك عيب 🤷.'
    m = 'ينهار اسود ع الساعه الزفت دي عايز اي🙁💔'
    u = 'شتريد ابوي نايم عوفه'
    o = 'لو عندك اقتراح قولو لو عايز تضف شي قول متستحيش🦖🔥.'
    i = 'بلنسبه لك مطور بنسبالي ابويا🔥😂'
    t = [m,u,o,i,z,a]
    Name = message.chat.first_name
    txt = random.choice(t)
    bot.send_message(message.chat.id, text=f"Welcome 🦖{Name}🦖\n {txt}",parse_mode = "markdown",reply_markup=h)

def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://zonyo.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
