from django.conf.urls import include, url
from .views import test
from .views import test2

urlpatterns = [
    url(r'^hello/',test),
    url(r'hello1/',test2)

]