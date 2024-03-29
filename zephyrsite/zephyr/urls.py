from django.urls import path

from . import views

urlpatterns = [
    path('/',views.main_homepage),
    path('',views.main_homepage),
    path('', views.index, name='index'),
    path('testlayout', views.home_view,),#Nothing
    path('register',views.mm,),
    path('register', views.home_view,),#reg form
    path('testh', views.home_test,),#Nothing
    path('incentives', views.inc_test,),#incentives
    path('responsibilities', views.resp_test,),#responsibility
    path('cahome', views.layout_test,),#cahome
    path('home', views.main_homepage,),#cahome
    path('testphonehome', views.phone_home_test,),
    path('testhamburger',views.hamburger),#Phone incentives page
    path('success',views.reg_success),#success page
    path('about',views.about),#about page
    path('help',views.help_page),#about page
    path('symposium',views.symposium),#about page
    path('water_rocket',views.water_rocket),#about page
    path('aerocontraption',views.aerocontraption),#about page
    path('test_button',views.button_test),#about page
    path('competitions',views.competitions),#competitions page
    path('contact',views.contact),#contact page
    path('comingsoon',views.soon),#soon page
    path('safety_in_aerospace',views.safety),#safety page
    path('careers_in_aerospace',views.careers),#soon page
    path('women_in_aerospace',views.women),#soon page
    path('liquid_engine',views.liquid),#soon page
    path('entrepreneurship',views.entrepreneurship),#soon page
    path('lectures',views.lectures),#soon page
    path('formSubmit',views.form_submit),
    path('register_s',views.register_symposium)

]
