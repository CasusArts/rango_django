from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings

from rango import views

app_name = 'rango'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),

    # Category Operations
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),

    # Page Operations
    url(r'^category/add_page/$', views.add_page, name='add_page'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),

    # Registration and Login
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name="logout"),
    url(r'^restricted/$', views.restricted, name="restricted"),
    #url(r'^accounts/$', include('registration.backends.simple.urls')),
]
