from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('beverages', views.beverages.as_view(), name='beverages'),
    path('checkout', views.checkout, name='checkout'),
    path('gourmet', views.gourmet.as_view(), name='gourmet'),
    path('groceries', views.groceries.as_view(), name='groceries'),
    path('household', views.household.as_view(), name='household'),
    path('contact', views.contact, name='contact'),
    path('faq', views.faq, name='faq'),
    path('offers', views.offers, name='offers'),
    path('packagedfoods', views.packagedfoods.as_view(), name='packagedfoods'),
    path('personalcare', views.personalcare.as_view(), name='personalcare'),
    path('products', views.products, name='products'),
    path('product/<int:pk>', views.product_detail.as_view(), name='product'),
    path('updateItem', views.updateItem, name='updateItem'),
    path('shortcodes', views.shortcodes, name='shortcodes'),
    path('paypage', views.paypage, name='paypage'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('registered', views.registered, name='registered'),
    path('account/', views.account.as_view(), name='account'),
    path('address', views.address, name='address'),
    path('history', views.history, name='history'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='forgot password.html'),
         name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password sent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='reset password.html'),
         name='password_reset_confirm'),
    path('rest_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='reset done.html'),
         name="password_reset_complete")
]
