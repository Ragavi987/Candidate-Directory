from django.urls import path, re_path
from candidateapp.views import *

app_name = 'candidateapp'

urlpatterns = [
    path('', ApiOverview, name='home'),
    path('candidates/', view_all_candidates, name='view_all_candidates'),
    path('candidates/<int:pk>/', get_candidate_details, name='get_candidate_details'),
    path('create/', add_candidate, name='add-new-candidate'),
    path('update/<int:pk>/', update_candidate, name='update-candidate'),
    path('delete/<int:pk>/', delete_candidate, name='delete-candidate'),
]

