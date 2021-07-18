from django.urls import path
from voting import views
urlpatterns = [
     path('',views.index, name='index'),
     path('votingregistration/',views.votingregistration, name='votingregistration'),
     path('registration/',views.registration, name='registration'),
     path('voting/',views.voting, name='voting'),
     path('view_result/',views.view_result, name='view_result'),
     path('feedback/',views.feedback, name='feedback'),
     path('contact/',views.contact, name='contact'),
     path('login/',views.login, name='login'),
     path('add_candidate/',views.add_candidate, name='add_candidate'),
     path('view_voter/',views.view_voter, name='view_voter'),
     path('delete_voter/<pk>',views.delete_voter, name='delete_voter'),
     path('edit_voter/<pk>',views.edit_voter, name='edit_voter'),
     path('update_voter_data/',views.update_voter_data, name='update_voter_data'),
     path('verify_voter/',views.verify_voter, name='verify_voter'),
     path('delete_user/<pk>',views.delete_user, name='delete_user'),
     path('voter_details/',views.voter_details, name='voter_details'),
     path('delete_details/<pk>',views.delete_details, name='delete_details'),
     path('news_panel/',views.news_panel, name='news_panel'),
     path('logout/',views.logout, name='logout')
]