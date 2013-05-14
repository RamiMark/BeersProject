from BeersApp import views
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BeersProject.views.home', name='home'),
    # url(r'^BeersProject/', include('BeersProject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^/admin/doc/$', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),

     (r'^search-brand/$',views.search_brand ),
     (r'^search-brand-results/$', views.search_brand_results),
     (r'^$', views.index),
     (r'^product/(\d+)$',views.product),
)
