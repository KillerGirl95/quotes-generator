# # import requests
# # from PIL import Image
# # from io import BytesIO

# # img_link= "https://images.pexels.com/photos/2802300/pexels-photo-2802300.jpeg"
# # img_response= requests.get(img_link)
# # if (img_response.status_code==200):
# #     image= Image.open(BytesIO(img_response.content))
# #     image.save("thenameichose.png")
# #     print("image saved")

# # import datetime, time
# # from io import BytesIO
# # timestamp= datetime.datetime.now().timestamp()
# # print(timestamp)
# # print (time.time())
# # x=(f"{time.time()}.jpg")
# # print(x)


# # a= "Nothing could be worse than the fear that one had given up too soon "
# with open ("quote.txt",) as file:
#     x= file.readline()
#     print (x)
    
import sys
import requests 
import json
import random

api_key="pvjYhb7dcLtCEgAFLKjp8pm4VlVulnYzkvPcvkghkJT45QER2KBi3YS3"
base_url="https://api.pexels.com/v1/search"

search_query= "landscape with sky"
params= {'query':search_query,'per_page': 20}
head= {'Authorization':api_key}

response= requests.get(base_url, params=params, headers=head)
print (response, "\nresponse size: ", sys.getsizeof(response))
print ("reqs remaining: ", response.headers['X-Ratelimit-Remaining'])
print (response.json())

with open ("resp_json.txt", "w") as file:
    json.dump(response.json(), file)


i= 0
rnd = random.randint(9,response.json()['per_page'])
if response.status_code==200:
    print(response)
    photo= response.json()['photos'][rnd]
    # :
    #     org_img= img['src']['original']
    #     prt_img= img['src']['portrait']

# # to save the image from the links generated 
# res= requests.get(prt_img)
# 