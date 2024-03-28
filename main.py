# import re
# import requests
# from bs4 import BeautifulSoup

# # Qabul qilingan URL nomini tekshirish uchun funksiya
# def is_valid_url(url):
#     regex = re.compile(
#         r'^https?://'  # http:// yoki https://
#         r'(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*'  # domain nomi
#         r'([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$'  # TLD
#     )
#     return bool(regex.match(url))

# # Xabar matnida phisherga ajratilgan URL'larni aniqlash uchun funksiya
# def find_urls(text):
#     # Regular ifodani ishlatib URL'larni topamiz
#     regex = re.compile(
#         r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))'
#     )
#     urls = []
#     for match in regex.findall(text):
#         url = match[0]
#         if not url.startswith('http'):
#             url = 'http://' + url
#         if is_valid_url(url):
#             urls.append(url)
#     return urls

# # Xabarlarni tekshirish uchun asosiy funksiya
# def check_emails(emails):
#     for email in emails:
#         # Email matnini webdan yuklab olish
#         response = requests.get(email)
#         soup = BeautifulSoup(response.content, 'html.parser')
#         # Xabar matnini olish
#         text = soup.get_text()
#         # Matnda URL topish
#         urls = find_urls(text)
#         if len(urls) == 0:
#             print(f"{email}: Phishing xabari topilmadi")
#         else:
#             print(f"{email}: Phishing xabari topildi")
#             for url in urls:
#                 print(f"\t{url}")

# # Misol uchun email manzillarini ro'yxatini aniqlash
# emails = ['https://www.example.com', 'https://www.phishing.com']

# # Xabarlarni tekshirish
# check_emails(emails)

# import pyzmail
# from bs4 import BeautifulSoup
# import requests
# import phishtank
# import tldextract
# import urllib.request
# import re

# # Xabar yuboruvchisi, qabul qiluvchisi, mavzusi va matnini aniqlash


# def parse_email(email):
#     parsed_email = {}
#     message = pyzmail.PyzMessage.factory(email['BODY[]'])
#     parsed_email['from'] = message.get_address('from')
#     parsed_email['to'] = message.get_address('to')
#     parsed_email['subject'] = message.get_subject()
#     payload = message.text_part.get_payload().decode(message.text_part.charset)
#     parsed_email['text'] = payload
#     return parsed_email

# # HTML kodlari ustida tahlil va phishingga qarshi tekshirish


# def parse_html(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     links = soup.find_all('a')
#     for link in links:
#         url = link.get('href')
#         if is_phishing(url):
#             return True
#     return False

# # URL manzillarini ustida amal bajarish va phishingga qarshi tekshirish


# def is_phishing(url):
#     domain = tldextract.extract(url).domain
#     if domain in phishtank.get_data():
#         return True
#     else:
#         try:
#             response = requests.get(url)
#             html = response.text
#             soup = BeautifulSoup(html, 'html.parser')
#             forms = soup.find_all('form')
#             for form in forms:
#                 if form.has_attr('action'):
#                     action = form.get('action')
#                     if action.startswith('http'):
#                         if tldextract.extract(action).domain in phishtank.get_data():
#                             return True
#         except:
#             pass
#     return False

# # Xabar phishing tushunchasiga yo'l qo'yilgan bo'lsa, xavfli xabar deb qayta ishlovchiga xabar yuborish


# def send_response(is_phishing, email):
#     if is_phishing:
#         response = pyzmail.compose_mail([email['from']], [
#                                         email['to']], 'Phishing alert', 'This email may be a phishing attempt.')
#         pyzmail.send_mail(response)

# import requests
# from bs4 import BeautifulSoup
# import re
# import ssl
# import smtplib
# from email.mime.text import MIMEText

# # E-pochta yuboruvchisi va qabul qiluvchisi
# from_email = "otajon2300@gmail.com"
# to_email = "otash23052000@gmail.com"
# password = "otash2305"

# # Pochta xabariga o'zgartirish kiritish
# msg = MIMEText('This email is safe to open')
# msg['Subject'] = 'Safe Email'
# msg['From'] = from_email
# msg['To'] = to_email

# # Elektron pochta serveri bilan bog'lanish
# context = ssl.create_default_context()
# with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
#     server.login(from_email, password)
#     server.sendmail(from_email, to_email, msg.as_string())

# # Elektron pochta ma'lumotlarini olish va tekshirish
# url = "https://example.com"
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')
# links = soup.find_all('a', href=True)

# # Xabar manzilini tekshirish
# for link in links:
#     if re.match("^https://yourdomain.com", link['href']):
#         continue
#     else:
#         print("Warning: Phishing attempt detected")
#         break

# import requests
# from flask import Flask, jsonify
# from flask_cors import CORS, cross_origin
# from threading import Thread
# from duckduckgo_search import ddg
# from bs4 import BeautifulSoup
# import dateparser
# app = Flask('')
# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'
# app.config['JSON_SORT_KEYS'] = False

# @app.route('/')	
# def home():
# 	return  "I'm alive"

# @app.route('/api/<string:s>', methods=['GET'])
# @cross_origin(origin='*')
# def prayer(s):
#   query = str(s + " prayer time site:muslimpro.com")
#   data = {}
#   urls = ddg(query, max_results=1)
#   try :
#     url = urls[0]['href']
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, "html.parser")
#     city = soup.find("p", attrs ={"class": "location"})
#     dates = soup.find("div", attrs ={"class": "prayer-daily-title-location"})
#     data["city"] = city.get_text()
#     data["date"] = dates.get_text()
#     data["today"] = {}
#     data["tomorrow"] = {}
#     waktu = soup.find_all("span", attrs ={"class": "waktu-solat"})
#     jam = soup.find_all("span", attrs ={"class": "jam-solat"})
#     for x,y in zip(waktu,jam):
#       data["today"][x.get_text()] = y.get_text()
#     names = ["Fajr", "Sunrise", "Dhuhr", "Asr", "Maghrib", "Isha'a"]
#     try:
#       tomorrow = soup.find("tr", attrs={"class": "active"}).find_next("tr").find_all("td", attrs={"class": "prayertime"})
#       for x,y in zip(names,tomorrow):
#         data["tomorrow"][x] = y.get_text()
#     except :
#       month = str(dateparser.parse(data["date"]))[5:7]
#       url = url + '?date=2021-' + str(int(month)+1)
#       response = requests.get(url)
#       soup = BeautifulSoup(response.content, "html.parser")
#       tomorrow = soup.find_all("tr")[1].find_all("td", attrs={"class": "prayertime"})
#       for x,y in zip(names,tomorrow):
#         data["tomorrow"][x] = y.get_text()
#   except Exception as e:
#     print(e)
#     data["Error"] = "Result Not Found"
#   return jsonify(data)

# def run():
# 	app.run(host='0.0.0.0',port=7000)

# t = Thread(target=run)
# t.start()


###############################################

# class OrtaArifmetik:
#     def __init__(self, *sonlar):
#         self.sonlar = sonlar
    
#     def orta_arifmetik_hisobla(self):
#         if len(self.sonlar) == 0:
#             return None
#         return sum(self.sonlar) / len(self.sonlar)

# sonlar = [3, 5, 7, 11, 13]
# orta_arifmetik = OrtaArifmetik(*sonlar)

# natija = orta_arifmetik.orta_arifmetik_hisobla()
# print("Ortacha arifmetigi:", natija)

class Juftlar:
    def __init__(self, *sonlar):
        self.sonlar = sonlar
    
    def ajratib_yoz(self):
        juft_sonlar = [son for son in self.sonlar if son % 2 == 0]
        print("Juft sonlar: ", juft_sonlar)

sonlar = [3, 5, 7, 10, 12, 15, 16]
juftlar = Juftlar(*sonlar)

juftlar.ajratib_yoz()
