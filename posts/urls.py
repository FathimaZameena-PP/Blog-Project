
from django.urls import path,include
from . import views

app_name='posts'

urlpatterns = [
    path('', views.allPost_view, name="all_posts"),
    path('new-post/',views.newpost,name="new_post"),
    path('<slug:slug>',views.post_detail, name="page")
]
