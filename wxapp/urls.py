from django.conf.urls import url

from . import views

app_name = 'wxapp'
urlpatterns = [
    #url(r'^UpData?(?P<up_data>\\w*|\\W*|[\\u4e00-\\u9fa5])/$', views.updata, name='updata'),
    url(r'^UpData', views.updata, name='updata'),
    url(r'^DownData', views.downdata, name='downdata'),
]
