from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$',
                           'redditanalyzer.views.home',
                           name='home'),

                       url(r'^redditanalysis$',
                           'redditanalyzer.views.analysis',
                           name='analysis'),

                       url(r'^my-queries$',
                           'redditanalyzer.views.show_old_queries',
                           name='queries'),

                       url(r'^login',
                           'authentication.views.login',
                           name='login'),

                       url(r'^register',
                           'authentication.views.register',
                           name='register'),

                       url(r'^logout$',
                           'authentication.views.logout',
                           name='logout'),
                       )
