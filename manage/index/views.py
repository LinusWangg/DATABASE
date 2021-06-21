from django.shortcuts import render
from django.db import connection
import json
from django.http import HttpResponse,JsonResponse,FileResponse, response
from psycopg2 import connect
from utils.response import wrap_json_response,ReturnCode,CommonResponseMixin
from manage.settings import DATABASES
import psycopg2

# Create your views here.

def primary_data(request):
    return render(request,'index.html')

def primary_data2(request):
    return render(request,'index2.html')

def primary_data3(request):
    return render(request,'index3.html')

def primary_data4(request):
    return render(request,'index5.html')

def dictfetchall(cursor):
    "将游标返回的结果保存到一个字典对象中"
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]

def show_article(request):
    data = {}
    post_data = request.body.decode("utf-8")
    post_data = json.loads(post_data)
    page = post_data.get('page')
    cur = connection.cursor()
    page_from = 10*(page-1)
    cur.execute("select art_title,art_author,art_time,art_type,art_pic from dboper.article_article limit 20 offset %s",[page_from])
    arts = dictfetchall(cur)
    cur.close()
    data['Arts'] = arts

    response = wrap_json_response(data=data,code=ReturnCode.SUCCESS,message='Success!')
    return JsonResponse(data=response,safe=False)

def delete_article(request):
    data = {}
    post_data = request.body.decode("utf-8")
    post_data = json.loads(post_data)
    art_title = post_data.get('art_title')
    cur = connection.cursor()
    try:
        cur.execute("delete from dboper.article_article where art_title = %s",[art_title])
        data['success'] = 1
    except Exception as e:
        data['success'] = 0
    cur.close()
    response = wrap_json_response(data=data,code=ReturnCode.SUCCESS,message='Success!')
    return JsonResponse(data=response,safe=False)

def show_user(request):
    data = {}
    post_data = request.body.decode("utf-8")
    post_data = json.loads(post_data)
    page = post_data.get('page')
    cur = connection.cursor()
    page_from = 10*(page-1)
    cur.execute("select * from dboper.user_user limit 20 offset %s",[page_from])
    arts = dictfetchall(cur)
    cur.close()
    data['users'] = arts

    response = wrap_json_response(data=data,code=ReturnCode.SUCCESS,message='Success!')
    return JsonResponse(data=response,safe=False)

def delete_user(request):
    data = {}
    post_data = request.body.decode("utf-8")
    post_data = json.loads(post_data)
    user_act = post_data.get('user_act')
    cur = connection.cursor()
    try:
        cur.execute("delete from dboper.user_user where user_act = %s",[user_act])
        data['success'] = 1
    except Exception as e:
        data['success'] = 0
    cur.close()
    response = wrap_json_response(data=data,code=ReturnCode.SUCCESS,message='Success!')
    return JsonResponse(data=response,safe=False)

def show_comment(request):
    data = {}
    post_data = request.body.decode("utf-8")
    post_data = json.loads(post_data)
    page = post_data.get('page')
    cur = connection.cursor()
    page_from = 10*(page-1)
    cur.execute("select * from dboper.article_comment limit 20 offset %s",[page_from])
    arts = dictfetchall(cur)
    cur.close()
    data['comments'] = arts

    response = wrap_json_response(data=data,code=ReturnCode.SUCCESS,message='Success!')
    return JsonResponse(data=response,safe=False)

def delete_comment(request):
    data = {}
    post_data = request.body.decode("utf-8")
    post_data = json.loads(post_data)
    comment_id = post_data.get('comment_id')
    cur = connection.cursor()
    try:
        cur.execute("delete from dboper.article_comment where comment_id = %s",[comment_id])
        data['success'] = 1
    except Exception as e:
        data['success'] = 0
    cur.close()
    response = wrap_json_response(data=data,code=ReturnCode.SUCCESS,message='Success!')
    return JsonResponse(data=response,safe=False)

def show_admin(request):
    data = {}
    post_data = request.body.decode("utf-8")
    post_data = json.loads(post_data)
    page = post_data.get('page')
    cur = connection.cursor()
    page_from = 10*(page-1)
    cur.execute("select usename from pg_user")
    pris = dictfetchall(cur)
    for x in pris:
        cur.execute("select * from information_schema.table_privileges where grantee=%s and table_name in ('article_article','article_comment','user_user')",[x['usename']])
        temp = dictfetchall(cur)
        for t in temp:
            x['grantor'] = t['grantor']
            x[t['privilege_type']] = 1
            x[t['privilege_type']+"grantable"] = t['is_grantable']

    cur.close()
    data['pris'] = pris

    response = wrap_json_response(data=data,code=ReturnCode.SUCCESS,message='Success!')
    return JsonResponse(data=response,safe=False)

def delete_admin(request):
    data = {}
    post_data = request.body.decode("utf-8")
    post_data = json.loads(post_data)
    user = post_data.get('user')
    pri = post_data.get('pri')
    cur = connection.cursor()
    try:
        if(pri == "1"):
            cur.execute("revoke all privileges on dboper.article_article from {0} cascade".format(user))
            cur.execute("revoke all privileges on dboper.article_comment from {0} cascade".format(user))
            cur.execute("revoke all privileges on dboper.user_user from {0} cascade".format(user))
        if(pri == "2"):
            cur.execute("revoke select,delete on dboper.article_article to {0}".format(user))
            cur.execute("revoke select,delete on dboper.article_comment to {0}".format(user))
            cur.execute("revoke select,delete on dboper.user_user to {0}".format(user))
        data['success'] = 1
    except Exception as e:
        data['success'] = 0
    connection.commit()
    cur.close()
    response = wrap_json_response(data=data,code=ReturnCode.SUCCESS,message='Success!')
    return JsonResponse(data=response,safe=False)

def give_admin(request):
    data = {}
    post_data = request.body.decode("utf-8")
    post_data = json.loads(post_data)
    user = post_data.get('user')
    pri = post_data.get('pri')
    cur = connection.cursor()
    if(pri == "1"):
        cur.execute("grant all privileges on dboper.article_article to {0} with grant option".format(user))
        cur.execute("grant all privileges on dboper.article_comment to {0} with grant option".format(user))
        cur.execute("grant all privileges on dboper.user_user to {0} with grant option".format(user))
    if(pri == "2"):
        cur.execute("grant select,delete on dboper.article_article to {0}".format(user))
        cur.execute("grant select,delete on dboper.article_comment to {0}".format(user))
        cur.execute("grant select,delete on dboper.user_user to {0}".format(user))
    data['success'] = 1
    connection.commit()
    cur.close()
    response = wrap_json_response(data=data,code=ReturnCode.SUCCESS,message='Success!')
    return JsonResponse(data=response,safe=False)

def add_admin(request):
    data = {}
    post_data = request.body.decode("utf-8")
    post_data = json.loads(post_data)
    user = post_data.get('user')
    pwd = post_data.get('pwd')
    cur = connection.cursor()
    try:
        cur.execute("create user {0} with password %s".format(user),[pwd])
        cur.execute("grant usage on schema dboper to {0}".format(user))
        data['success'] = 1
    except Exception as e:
        data['success'] = 0
    connection.commit()
    cur.close()
    response = wrap_json_response(data=data,code=ReturnCode.SUCCESS,message='Success!')
    return JsonResponse(data=response,safe=False)