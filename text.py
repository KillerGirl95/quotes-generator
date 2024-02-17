import requests
url = "https://api.quotable.io/random"
res_quo = requests.get(url, params={"maxLength":80})

cont_quo= res_quo.json()["content"]+ "-"+ res_quo.json()["author"]
print (f"content retrived : {cont_quo}")
with open ("quote.txt",'w') as file:
    file.write(cont_quo)
    
