from django.core import serializers
from django.core.serializers import json
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from ShopSystem.models import goods

#购物清单
List={}

def index(request):
    #首页
    return render(request, "datatable.html", locals())

def getAll(request):
    # f返回所有商品
    list = goods.objects.all()
    json_data = serializers.serialize("json", list)
    return HttpResponse(json_data)


def buyOne(request):
    myid=request.GET['id'];
    ret= goods.objects.get(id=myid)
    #数据库操作
    ret.count = ret.count-1
    ret.save()
    if(ret.count<=0):
        ret.delete()

    #记录数量
    global List

    List[ret.id]=[ret.name,List.get(ret.id,[ret.name,0,ret.price])[1]+1,ret.price]
    return HttpResponse("success")

def buyEnd(request):
    global List
    sum=0#总价
    Ret=[]#购买详情
    for i in List:
        each=List[i]
        Ret.append(each)
        sum=sum+each[1]*each[2]
    # 返回清单
    return render(request, "invoice.html", locals())