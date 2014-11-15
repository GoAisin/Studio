from django.conf.urls import include, url
from django.contrib import admin
from Studio.views import hello
from Studio.controller.ArticleController import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'Studio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    # url('^hello/$', hello),
    # url('^hello/$', hello),
    url('^article/queryHostArticle', queryHostArticle)
]
