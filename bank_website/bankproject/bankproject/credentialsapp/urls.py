from.import views
from django.urls import path


urlpatterns=[
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('page',views.page,name='page'),
    path('account_create_view',views.account_create_view,name='account_create_view'),
    path('get_branches/<int:district_id>/', views.get_branches,name='get_branches'),



]