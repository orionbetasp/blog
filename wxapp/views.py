from django.shortcuts import render, get_object_or_404
from .models import wxapp
from django.http import HttpResponse
import logging
import json

# 生成一个以当前文件名为名字的logger实例
logger = logging.getLogger(__name__)
# 生成一个名为collect的logger实例
collect_logger = logging.getLogger("collect")

def updata(request):
    name = request.GET.get('name')
    data = request.GET.get('list')
    
    logger.info(name + '上传数据:' + data)

    try:
        if(name):
            #models.wxapp.objects.create(name=name, data=data)
            change = wxapp(name=name, data=data)
            change.save()
            return HttpResponse(name + 'の数据已同步!')
    except Exception as e:
        logger.error('Failed to updata', exc_info=True)
        return HttpResponse("服务器处理失败，联系他看看。")


def downdata(request):
    name = request.GET.get('name')

    logger.info(name + '下载数据')

    try:
        if(name):
            user_data = wxapp.objects.get(name=name)

            json_str = json.dumps({'name' : user_data.name, 'list' : user_data.data})
            logger.info('返回数据：' + json_str)

            return HttpResponse(json_str)
    except Exception as e:
        logger.error('Failed to downdata', exc_info=True)
        tmpJson = r'{"name":"你之前有没有上传数据，心里没点B数嘛！"}'
        return HttpResponse(tmpJson)