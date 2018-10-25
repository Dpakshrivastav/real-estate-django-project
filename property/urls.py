from django.conf.urls import url
from . import views

from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^buying/$', views.BuyingView.as_view(), name='buying'),
    url(r'^finance/$', views.FinanceView.as_view(), name='finance'),
    url(r'^renting/$', views.RentingView.as_view(), name='renting'),
    url(r'^selling/$', views.SellingView.as_view(), name='selling'),
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),
    url(r'^search/$', views.find_property, name='search'),
    url(r'^propertylist/$', views.houselist, name='houselist'),
    url(r'^predict/$', views.predict, name='predict'),
    url(r'^mortagage/$', views.mortagage, name='mortagage'),
    url(r'^homevalue/$', views.homevalue, name='homevalue'),
    url(r'^contactus/$', views.contactus, name='contactus'),
    # url(r'^find_property/$', views.find_property(), name='findproperty'),
    url(r'^(?P<house_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^pageadmin/$', views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'property/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'index'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^addhouse/$', views.add, name='add'),
    url(r'^detail/$', views.adddetail, name='adddetail'),

]