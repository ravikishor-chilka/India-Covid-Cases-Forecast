import requests
from bs4 import BeautifulSoup
dead_count=[]
confirm_count=[]
recover_count=[]
state_name=[]


url="https://visalist.io/emergency/coronavirus/india-country"

r=requests.get(url)
soup=BeautifulSoup(r.content, 'html.parser')
s1=soup.find_all(class_="v-list-item v-list-item--link theme--dark")
#print(s1)

for head in s1:
    try:
        st=head.find(class_="body-2 text-truncate").text
        state_name.append(st)  
    except:
        continue    

#print(state_name)
state_final=([s.replace('\n', '') for s in state_name])
state_final.insert(0,"INDIA")
#print((state_final))
#print(len(state_final))
for i in s1:
    try:
        confirm=i.find(class_="pink--text text--accent-3").text
        confirm_count.append(confirm)
    except:
        continue    
print(len(confirm_count))
for i in s1:
    try:
        recover=i.find(class_="green--text text--accent-3").text
        recover_count.append(recover)
    except:
        continue
#print(len(recover_count))   
for i in s1:
    try:
        death=i.find(class_="grey--text").text
        dead_count.append(death)  
    except:
        continue
#print(len(dead_count))
statedata=[]
statedict={}
for i in range(0,len(state_name)):
    

    statedict["state"].append(state_name[i])
    statedict["Confirm"].append(confirm_count[i])
    statedict["Recover"].append(recover_count[i])
   
#print(state_dict)