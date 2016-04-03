import requests
import json
import csv

data = {}
data["user_token"] = "YPv-QkHTVHq_rxP3yZ7i"
with open("listdeal.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # print(row["lat"], row["long"])
        data["picture_url"] = row["img"]
        data["description"] = row["description"]
        data["location_lat"] = row["lat"]
        data["location_long"] = row["long"]
        data["post_type"] = "crawl"
        data["crawl_user_name"] = "Hotdeal.vn"
        data["crawl_user_email"] = "crawler@hotdeal.vn"
        data["crawl_user_avatar"] = "http://www.hotdeal.vn/favicon.ico"
        # print json.dumps(data)
        r = requests.post("http://solomo-api.herokuapp.com/api/v1/posts.json",data)
        break

# http://www.hotdeal.vn/favicon.ico
# r = requests.get("http://solomo-api.herokuapp.com/api/v1/posts.json",data)
# print r.content