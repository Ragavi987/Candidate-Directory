from django.urls import path, re_path
from candidateapp.views import *

app_name = 'candidateapp'

urlpatterns = [
    path('', ApiOverview, name='candidateapp:home'),
    path('candidates/', view_all_candidates, name='candidateapp:view_all_candidates'),
    path('candidates/<int:pk>/', get_candidate_details, name='candidateapp:get_candidate_details'),
    path('create/', add_candidate, name='candidateapp:add-new-candidate'),
    path('update/<int:pk>/', update_candidate, name='candidateapp:update-candidate'),
    path('delete/<int:pk>/', delete_candidate, name='candidateapp:delete-candidate'),
]

