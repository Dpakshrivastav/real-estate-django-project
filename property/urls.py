from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^buying/$', views.BuyingView.as_view(), name='buying'),
    url(r'^finance/$', views.FinanceView.as_view(), name='finance'),
    url(r'^renting/$', views.RentingView.as_view(), name='renting'),
    url(r'^selling/$', views.SellingView.as_view(), name='selling'),
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),
    # url(r'^find_property/$', views.find_property(), name='findproperty'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

]