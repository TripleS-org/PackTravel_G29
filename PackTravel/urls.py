"""PackTravel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user import views as userView
from search import views as searchViews
from publish import views as publishViews
from requests import views as requestsViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', searchViews.search_index, name = 'search'),
    path('request_ride/<ride_id>', searchViews.request_ride, name = 'request_ride'),
    path('publish/', publishViews.publish_index, name = 'publish'),
    path('index/', userView.index, name ='index'),
    path('index/<username>',userView.index, name='index'),
    path('register/', userView.register, name='register'),
    path('requests/',requestsViews.requested_rides,name='requests'),
    path('cancel_ride/<ride_id>', requestsViews.cancel_ride, name = 'cancel_ride'),
    path('accept_request/<ride_id>/<user>', requestsViews.accept_request, name = 'accept_request'),
    path('reject_request/<ride_id>/<user>', requestsViews.reject_request, name = 'reject_request'),
    path('cancel_accepted_ride/<ride_id>/<user>', requestsViews.cancel_accepted_ride, name = 'cancel_accepted_request'),
    path('delete_ride/<ride_id>', requestsViews.delete_ride, name = 'delete_ride'),
    path('logout/', userView.logout, name='logout'),
    path('login/', userView.login, name='login'),
    path('create_ride/', publishViews.create_ride, name='create_ride'),
    path('ride_page/<ride_id>',publishViews.show_ride,name='showridepage'),
    path('add_forum/',publishViews.add_forum,name='addforum')
]
