
# coding: utf-8

# In[111]:

import requests
import json
import csv
import sys
from operator import itemgetter
global_list = []
search_term = str(sys.argv[1])
for i in range(1,2):
    url_search = "https://api.stackexchange.com/2.2/search?key=I7TMKoKeq0F3zzkYBt)t1g((&order=desc&page="+str(i)+"&pagesize=10&sort=activity&intitle="+search_term+"&site=stackoverflow"
    raw_response = requests.get(url_search)
    #print(raw_response)
    #print(raw_response.encoding)
    json_response = raw_response.json()
    global_list = json_response["items"] + global_list
#print(global_list)
file_name = search_term + ".txt"
with open(file_name, 'w') as fout:
    json.dump(global_list, fout)
f = open(file_name)
L = json.load(f)
type(L)
list_local = []
for i in L:
    dic_local = {}
    dic_local["user_id"]=i["owner"]["user_id"]
    dic_local["title"] = i["title"]
    dic_local["question_id"] = i["question_id"]
    dic_local["user_name"] = i["owner"]["display_name"]
    dic_local["question_tags"] = i["tags"]
    list_local.append(dic_local)

badge_list = []
for i in range(0,10):
    url_search = "https://api.stackexchange.com/2.2/users/"+str(list_local[i]["user_id"])+"/badges?pagesize=100&key=I7TMKoKeq0F3zzkYBt)t1g((&order=desc&sort=rank&site=stackoverflow"
    raw_response = requests.get(url_search)
    json_response = raw_response.json()
    badges = json_response["items"]
    temp_silver = 0
    temp_bronze = 0
    temp_gold = 0
    for j in badges:
        if(j["rank"]=="bronze"):
            temp_bronze+=1
        elif(j["rank"]=="gold"):
            temp_gold+=1
        elif(j["rank"]=="silver"):
            temp_silver+=1
    #print(badges)
    badge_count = len(json_response["items"])
    list_local[i]["badge_count"] = badge_count
    list_local[i]["silver_count"] = temp_silver
    list_local[i]["gold_count"] = temp_gold
    list_local[i]["bronze_count"] = temp_bronze
    badge_list = json_response["items"] + badge_list
    
for i in range(0,10):
    url_search = "https://api.stackexchange.com/2.2/users/"+str(list_local[i]["user_id"])+"/tags?order=desc&key=I7TMKoKeq0F3zzkYBt)t1g((&sort=popular&site=stackoverflow"
    raw_response = requests.get(url_search)
    json_response = raw_response.json()
    user_tags = json_response["items"]
    tag_list = []
    for j in user_tags:
        tag_list.append(j["name"])
    list_local[i]["user_tags"] = tag_list
    
silver_count = 0 
gold_count = 0
bronze_count = 0
total_count = 0
for i in list_local:
    silver_count+= i["silver_count"]
    gold_count+= i["gold_count"]
    bronze_count+= i["bronze_count"]
    total_count+= i["badge_count"]
#print(list_local)
newlist = sorted(list_local, key=itemgetter("badge_count"), reverse=True)

with open("Analysis1.csv", 'w') as f:
    for i in range(0,len(newlist)):
        # Just use 'w' mode in 3.x
        temp_dic = {"Weightage":newlist[i]["badge_count"],"Question":newlist[i]["title"]}
        print(temp_dic)
        w = csv.writer(f)
        w.writerow(temp_dic.values())
        
print(newlist)
print("Total Badge Count:", total_count)
with open("Analysis3.csv", 'w') as f:
    for i in range(0,len(newlist)):
        # Just use 'w' mode in 3.x
        temp_dic = {"Silver Count":newlist[i]["silver_count"], "Gold Count":newlist[i]["gold_count"], "Bronze Count": newlist[i]["bronze_count"]}
        print(temp_dic)
        w = csv.writer(f)
        w.writerow(temp_dic.values())


# In[112]:

list_local
for i in range(0,10):
    url_questions = "https://api.stackexchange.com/2.2/questions/"+str(list_local[i]["question_id"])+"/answers?order=desc&key=I7TMKoKeq0F3zzkYBt)t1g((&sort=activity&site=stackoverflow"
    search_response = requests.get(url_questions)
    json_search = search_response.json()
    answer_list = json_search["items"]
    list_local[i]["answers_count"] = len(answer_list)
print(list_local)
with open("Analysis4.csv", 'w') as f:
    for i in range(0,len(list_local)):
        # Just use 'w' mode in 3.x
        temp_dic = {"answers_count":list_local[i]["answers_count"],"Question":list_local[i]["title"]}
        print(temp_dic)
        w = csv.writer(f)
        w.writerow(temp_dic.values())


# In[113]:

search_term = "pandas"
final_list = []
for i in range(1,6):
    url_search = "https://api.stackexchange.com/2.2/search?order=desc&key=I7TMKoKeq0F3zzkYBt)t1g((&sort=activity&intitle="+search_term+"&pagesize=100&page="+str(i)+"&site=stackoverflow"
    search_response = requests.get(url_search)
    json_search = search_response.json()
    #print(json_search)
    search_users = json_search["items"]
    for j in search_users:
        empt_dic = {}
        empt_dic["reputation"]=j["owner"]["reputation"]
        empt_dic["user_id"]=j["owner"]["user_id"]
        empt_dic["user_name"]=j["owner"]["display_name"]
        empt_dic["link"]=j["owner"]["link"]
        final_list.append(empt_dic)
#print(final_list)
newlist = sorted(final_list, key=itemgetter("reputation"), reverse=True)
print(newlist)
with open("Analysis2.csv", 'w') as f:
    for i in range(0,len(newlist)):
        # Just use 'w' mode in 3.x
        temp_dic = {"user_id":newlist[i]["user_id"],"user_name":newlist[i]["user_name"],"link":newlist[i]["link"],"reputation":newlist[i]["reputation"]}
        print(temp_dic)
        w = csv.writer(f)
        w.writerow(temp_dic.values())


# In[115]:

for i in range(0,10):
    url_search = "https://api.stackexchange.com/2.2/users/"+str(list_local[i]["user_id"])+"/questions?order=desc&key=I7TMKoKeq0F3zzkYBt)t1g((&pagesie=100&site=stackoverflow"
    raw_response = requests.get(url_search)
    json_response = raw_response.json()
    #print(json_response)
    user_tags = json_response["items"]
    score = 0 
    for j in user_tags:
        score += j["score"]
    list_local[i]["score_count"] = score
#print(list_local)
most_downvoted = sorted(list_local, key=itemgetter("score_count"), reverse=False)
print(most_downvoted)
with open("Analysis5.csv", 'w') as f:
    for i in range(0,len(most_downvoted)):
        # Just use 'w' mode in 3.x
        temp_dic = {"Score":most_downvoted[i]["badge_count"],"user_id":most_downvoted[i]["user_id"],"user_name":most_downvoted[i]["user_name"]}
        print(temp_dic)
        w = csv.writer(f)
        w.writerow(temp_dic.values())


# In[116]:

# print(list_local)
# print(json_response)
# ids_list=[265422,265423]
# string_id = ""
# for id in ids_list:
#     id_temp = str(id)+"%3B"
#     print(id_temp)
#     string_id += id_temp
# string_id = string_id[:-3]
# print(string_id)
# url_ids = "https://api.stackexchange.com/2.2/users/"+string_id+"?order=desc&sort=reputation&site=stackoverflow"
# id_response = requests.get(url_ids)
# json_id = id_response.json()
# print(json_id)


# In[117]:

# import csv

# my_dict = [{"name": "ajay", "last": "mache"},{"name":"ganesh","last":"ramamurthy"}]

# with open('mycsvfile.csv', 'w') as f:
#     for i in range(0,len(my_dict)):
#         # Just use 'w' mode in 3.x
#         temp_dic = {"name":my_dict[i]["name"],"last":my_dict[i]["last"]}
#         print(temp_dic)
#         w = csv.writer(f)
#         w.writerow(temp_dic.values())


# In[ ]:



