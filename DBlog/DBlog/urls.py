from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    (r'^$', 'Stories.blog.views.index'),

    url(
     r'^blog/view/(?P<slug>[^\.]+).html',
     'Stories.blog.views.view_post',
     name='view_blog_post'),
    url(
     r'^blog/category/(?P<slug>[^\.]+).html',
     'Stories.blog.views.view_category',
     name='view_blog_category'),
]
