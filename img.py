import sys
import requests 
# from PIL import Image
# from io import BytesIO
import os
import random 

# Set the current working directory to the directory of the script
current_directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_directory)

api_key="pvjYhb7dcLtCEgAFLKjp8pm4VlVulnYzkvPcvkghkJT45QER2KBi3YS3"
base_url="https://api.pexels.com/v1/search"

search_query= "landscape with sky"
params= {'query':search_query,'per_page': 20}
head= {'Authorization':api_key}

response= requests.get(base_url, params=params, headers=head)
print (response, "\nresponse size: ", sys.getsizeof(response))
print ("reqs remaining: ", response.headers['X-Ratelimit-Remaining'])

rnd= random.randint(0,response.json()['per_page'])
if response.status_code==200:
    img= response.json()['photos'][rnd]
    prt_img= img['src']['portrait']

# to save the image from the links generated 
# totally another req 

res= requests.get(prt_img)
with open ("quo_img.jpg", "wb") as file:
    file.write(res.content)    # response.content() -> result in binary