from django.urls import path
from find_guide.views import Find_GuideList

app_name = 'find_guide'

urlpatterns = [
    path('', Find_GuideList.as_view(), name='list'),
]
