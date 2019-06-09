from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path, re_path, include

app_name = 'fynd'

urlpatterns = [
    # Examples:
    # url(r'^$', 'fynd.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    path('user/', include('user.urls') ),
    path('admin/', admin.site.urls),
    # url(r'admin', include('admin.site.urls', namespace='admin')),
    # path(r'^admin/', include(admin.site.)),
    re_path('movie/', include('movie.urls'))
]