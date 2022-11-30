from django.urls import path
from app2.views import*
app_name='jk'

urlpatterns=[ 
    path('pushpa/',pushpa,name='pushpa'),
    path('meghana/',meghana,name='meghana',)
]