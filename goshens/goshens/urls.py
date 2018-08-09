from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from page import views
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^page/', include('page.urls', namespace='page')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^$', views.page_list, name='index'),
    url(r'^who-we-are/', TemplateView.as_view(template_name='page/who_we_are.html'), name='who-we-are'),
    url(r'^what-we-do/', TemplateView.as_view(template_name='page/what_we_do.html'), name='what-we-do'),
    url(r'^where-we-work/', TemplateView.as_view(template_name='page/where_we_work.html'), name='where-we-work'),
    url(r'^contact-us/', TemplateView.as_view(template_name='page/contact.html'), name='contact-us'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
