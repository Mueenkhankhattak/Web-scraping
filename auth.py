import requests

url = "https://httpbin.org/post"
data = {"title" : "Mueen_test"}
auth = ("user_name" : "mueen" ,"pasword" : "testing")

r = requests.post(url , data=data , auth=auth , timeout=5) 

r_dict = r.json()
print(r_dict["form"])



