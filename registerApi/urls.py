from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from quickstart import views

router = routers.DefaultRouter()
router.register(r'records', views.RecordViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'registerApi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += router.urls