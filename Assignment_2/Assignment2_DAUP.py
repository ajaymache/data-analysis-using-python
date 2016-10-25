
# coding: utf-8

# In[126]:

import requests
import base64
import json
import sys
from operator import itemgetter
input_search_term = str(sys.argv[1])
url_search = "https://api.twitter.com/1.1/search/tweets.json?q=%40"+input_search_term+'&'+"count=100"
encoded = base64.b64encode(b'r2lWKOZO0am3LQtcqcPwpa4mp:VwiK7mnF3ufJXWaiHSbTe14PfSyEEQzJrqiEQEhE8Knh4yVqkm')
#print(encoded)
client_auth = requests.auth.HTTPBasicAuth("r2lWKOZO0am3LQtcqcPwpa4mp", "VwiK7mnF3ufJXWaiHSbTe14PfSyEEQzJrqiEQEhE8Knh4yVqkm")
post_data = {"grant_type": "client_credentials",
                 "Authorization": "Basic cjJsV0tPWk8wYW0zTFF0Y3FjUHdwYTRtcDpWd2lLN21uRjN1ZkpYV2FpSFNiVGUxNFBmU3lFRVF6SnJxaUVRRWhFOEtuaDR5VnFrbQ=="}
response = requests.post("https://api.twitter.com/oauth2/token", auth=client_auth, data=post_data)
#print(response)
token_json = response.json()
access_token = token_json["access_token"]
token_type = token_json["token_type"]
# print(access_token)
# print(token_type)
headers = {"Authorization": "Bearer " + access_token}
response_get = requests.get(url_search,headers=headers)
# print(response_get)
me_json = response_get.json()
temp_list = []
tweets = me_json["statuses"]

def media_analysis(temp_dic):
    count=0
    countPhoto=0
    countVideo=0
    countAnimatedGifs=0
    countMultiPhoto=0
    for x in range(0,len(tweets)):
        if 'media' in tweets[x]['entities'].keys():
                
                if tweets[x]['entities']['media'][0]['type'].lower() == 'photo':
                    countPhoto+=1
                    count+=1
                elif tweets[x]['entities']['media'][0]['type'].lower() == 'video':
                    countVideo+=1
                    count+=1
                elif tweets[x]['entities']['media'][0]['type'].lower() == 'multi photos':
                    countMultiPhoto+=1
                    count+=1
                elif tweets[x]['entities']['media'][0]['type'].lower() == 'animated gifs':    
                    countAnimatedGifs+=1
                    count+=1
    if count == 0:
         print("")
    else:
        temp_dic["Number of Media Files"] = count
        temp_dic["Number of Photos"] = countPhoto
        temp_dic["Number of Videos"] = countVideo
        temp_dic["Number of animated GIFs"] = countAnimatedGifs
        temp_dic["Number of Multi Photos"] = countMultiPhoto

for tweet in tweets:
    temp_dic = {}
    for keys in tweet:
        if(keys=="created_at" or keys=="favorite_count" or keys=="retweeted" or keys=="text" or keys=="retweet_count"):
#         temp_dic = {keys:me_json["statuses"][0][keys]}
            temp_dic[keys]= tweet[keys]
#             print(keys, "-----", tweet[keys])
    user_tweet = tweet["user"]
    for keys in user_tweet:
#     print(keys, "********", user_tweet[keys])
        if(keys=="favourites_count" or keys=="followers_count" or keys=="friends_count" or keys=="listed_count" or
          keys=="statuses_count" or keys=="verified" or keys=="name" or keys=="screen_name" or keys=="location" or
          keys=="created_at"):
            temp_dic[keys]= user_tweet[keys]
    user_mentions = tweet["entities"]["user_mentions"]
#     print(user_mentions)
#     print(len(user_mentions))
    temp_dic["No of Users Mentioned"] = len(user_mentions)
    media_analysis(temp_dic)
    temp_list.append(temp_dic)
# print("###############", temp_list)
# print(len(temp_list))
file_name = input_search_term + ".txt"
with open(file_name, 'w') as fout:
    json.dump(temp_list, fout)
f = open(file_name)
L = json.load(f)
type(L)
newlist = sorted(L, key=itemgetter("retweet_count"), reverse=True)
print("Analysis 1: The top 10 Tweets based on the number of times this tweets has been retweeted. \n")
for top_10 in range(0,10):
    print(newlist[top_10]["text"], "Retweet Count:", newlist[top_10]["retweet_count"], "\n")
#     print(rt_count["retweet_count"])
print("\n\n")
retweet_total_count = 0
average_friends_count = 0
average_media_count = 0
average_photo_count = 0
average_video_count = 0
average_animated_GIF_count = 0
average_multi_photos_count = 0
average_no_of_users_mentioned = 0
average_followers_count = 0
for loc in L:
#     print(loc["retweet_count"])
    retweet_total_count+=loc["retweet_count"]
    average_friends_count+=loc["friends_count"]
    average_media_count+=loc["Number of Media Files"]
    average_photo_count+=loc["Number of Photos"]
    average_video_count+=loc["Number of Videos"]
    average_animated_GIF_count+=loc["Number of animated GIFs"]
    average_multi_photos_count+=loc["Number of Multi Photos"]
    average_no_of_users_mentioned+=loc["No of Users Mentioned"]
    average_followers_count+=loc["followers_count"]
    
print("Analysis 2: The average Retweet count from all the tweets for the given particular search term occuring in those tweets. \n")
print("Average Retweet Count:", retweet_total_count/(len(L)), "\n\n\n")

print("Analysis 3: The average Friends count for all the users tweetting tweets containing the search term. \n")
print("Average Friends Count:", average_friends_count/(len(L)), "\n\n\n")

print("Analysis 4: The average no of Medie files like photo, videos, animated GIF's for tweets containing the search term. \n")
print("Averhae Number of Media Files:", average_media_count/(len(L)), "\n")
print("Average Number of Photos:", average_photo_count/(len(L)), "\n")
print("Average Numver of Videos:", average_video_count/(len(L)), "\n")
print("Average Number of animated GIFS:", average_animated_GIF_count/(len(L)), "\n")
print("Average Number of Multi Photos:", average_multi_photos_count/(len(L)), "\n\n\n")

print("Analysis 5: The average no of users tagged in the original tweet with @ annotation." "\n")
print("Avregae No of Users Mentioned:", average_no_of_users_mentioned/(len(L)), "\n\n\n")

print("Analysis 6: The avergae no of followers the users have containing the search term in their tweets." "\n")
print("Average No of Followers:", average_followers_count/(len(L)), "\n")







