"""eventPlanner URL Configuration

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
from django.urls import path,include,re_path
from apps.user import views as user_views
from apps.post import views as post_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', user_views.HomeView.as_view(), name='home'),
    path('', post_views.AllPostListView.as_view(), name='home'),
    path('about_us', user_views.AboutUsView.as_view(), name="about_us"),
    path('register', user_views.RegistrationView.as_view(), name="register"),
    path('login', user_views.LogInView.as_view(), name="login"),
    path('logout', user_views.LogOutView.as_view(), name="logout"),
    path('post_list', post_views.ListPostView.as_view(), name="post_list"),
    path('all_post_list', post_views.AllPostListView.as_view(), name="all_post_list"),
    path('add_post', post_views.PostCreateView.as_view(), name="add_post"),
    path('delete_post/<int:pk>', post_views.delete_post, name="delete_post"),
    #path('delete_post/<int:pk>', post_views.DeletePostView.as_view(), name="delete_post"),
    path('post_detail/<int:pk>', post_views.PostDetailView.as_view(), name="post_detail"),
    path('post_update/<int:pk>', post_views.PostUpdateView.as_view(), name="post_update"),
    path('my_account', post_views.MyAccountView.as_view(), name="my_account"),
    path('services', post_views.MyServicesView.as_view(), name="services"),
    path('contact', post_views.MyContactView.as_view(), name="contact"),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# debug code
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        #re_path(r'^__debug__/',include('debug_toolbar.urls')),
        #path('__debug__',include('debug_toolbar.urls')),
        path('__debug__',include(debug_toolbar.urls)),
    ] + urlpatterns