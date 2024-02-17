import requests 
app_id= 2086223401739554
resp= requests.get(f"https://graph.facebook.com/{app_id}/accounts")
print(resp)
print(resp.json())