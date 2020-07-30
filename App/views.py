from django.shortcuts import HttpResponse,render
import requests
from bs4 import BeautifulSoup

def index(request):
    url="https://www.mygov.in/corona-data/covid19-statewise-status/"

    r=requests.get(url)
    soup=BeautifulSoup(r.content, 'html.parser')

    s1=soup.find_all("div",class_="field field-name-field-select-state field-type-list-text field-label-above")
    c1=soup.find_all(class_="field field-name-field-total-confirmed-indians field-type-number-integer field-label-above")
    r1=soup.find_all(class_="field field-name-field-cured field-type-number-integer field-label-above")
    d1=soup.find_all(class_="field field-name-field-deaths field-type-number-integer field-label-above")

    statedata=[]

    for i in range(len(s1)):

        statedict={}
    
        try:
            statedict['statename']=s1[i].find("div",class_="field-item even").text  
        except:
            continue

        try:
            statedict['confirm']=c1[i].find("div",class_="field-item even").text
        except:
            continue

        try:
            statedict['recover']=r1[i].find("div",class_="field-item even").text
        except:        
            continue
        
        try:
            statedict['death']=d1[i].find("div",class_="field-item even").text  
        except:
            continue
    
        statedata.append(statedict)

        context={"statedata": statedata} 
    return render(request ,'index.html', context)

def donate(request):
    return render(request,'donate.html') 

def symptoms(request):
    return render(request,'symptoms.html') 
     
def contact(request):
    return render(request,'conatct.html')
    