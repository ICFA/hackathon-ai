from django.urls import path
from flairest_campus import views

'''
home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="flairest_campus/home.html",
)

home_list_view = views.HomeListView.as_view(
    context_object_name="message_list",
    template_name="flairest_campus/index2.html",
)

urlpatterns = [
    path("", home_list_view, name="home"), # path("", views.home, name="home"),
    path("hello/<name>", views.hello_there, name="hello_world"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("log/", views.log_message, name="log"),
    path('media/', views.home_page, name="media"),
    path('uni/', UniCreate.as_view())
]
'''

urlpatterns = [
    path('', views.sber_view, name='sber_page')
]