import requests
with open("acc_lng_tkn.txt",'r') as token:
    tkn= token.read()
page_id= 200338043161983
img= "final_img.jpg"
params= {'access_token':tkn, 'caption':"nothing matters"}
url= f'https://graph.facebook.com/v18.0/me/photos?url={img}&access_token={tkn}'

response= requests.post(url, params=params, files={'source':img})
print (response)
print (response.json())

# cnf_tkn= "EAAMsgeFZBegUBO2i19EnE40P9JZAgIPVxgc0ZA1RZAjD5djxXfKHjJU9lIV8itPAXzydU9PatZBja1UWTT2miO5wi0JycQqtwQ4Q7ZCNdq1xiCnxntzPvtj9xUgTU3EqvivUz2DEkaYuV1NioUt4ZBy0CyXoP79Y99qXuslURts51n87hqaCAcqbuAd"


