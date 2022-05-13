from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyse(request):
    text=request.POST.get('utext','')
    removepun=request.POST.get('removerpunctuation','off')
    fullcaps=request.POST.get('fullcaps','off')
    spaceremover=request.POST.get('spaceremover','off')
    newlineremover=request.POST.get('newlineremover','off')
    charactercount=request.POST.get('charactercount','off')
    p='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''

    if removepun=='on':
        atext = ""
        for i in text:
            if i not in p:
                atext=atext+i
        text=atext

    if fullcaps=='on':
        atext = ""
        for i in text:
            atext=atext+i.upper()
        text = atext

    if spaceremover=='on':
        atext = ""
        for i in text:
            if i !=' ':
                atext=atext+i
        text = atext

    if newlineremover=='on':
        atext = ""
        for i in text:
            if i !='\n' and i!='\r':
                atext=atext+i
        text = atext

    if charactercount=='on':
        atext = ""
        count=0
        for i in text:
            if i.isalpha()==True:
                count+=1
        atext=text+"\nTotal No of Character  is  "+str(count)
    params = {'atext': atext, 'uname': 'Text Utilization'}

    return render(request,'analyse.html',params)

def about(request):
    return render(request,'about.html')