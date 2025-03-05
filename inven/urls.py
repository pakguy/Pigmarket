from django.urls import path 
from django.contrib.auth.views import LoginView
from . import views
from .views import *
# from .views import (
#     InvenListView,
#     InvenCreateView,
#     InvenDetailView,
#     InvenUpdateView,
#     InvenDeleteView
# )

# from .views import (
#     MatingListView,
#     MatingCreateView,
#     MatingDetailView,
#     MatingUpdateView,
#     MatingDeleteView
# )
# from .views import (
#     WeaningListView,
#     WeaningCreateView,
#     WeaningDetailView,
#     WeaningUpdateView,
#     WeaningDeleteView
# )
# from .views import (
#     FarrowingListView,
#     FarrowingCreateView,
#     FarrowingDetailView,
#     FarrowingUpdateView,
#     FarrowingDeleteView
# )


urlpatterns = [

    path('allocate_L', allocate_LListView.as_view(), name='allocate_L-list'),
    path('allocate_L/create/', allocate_LCreateView.as_view(), name='allocate_L-create'),
    path('<int:pk>/details/allocate_L', allocate_LDetailView.as_view(), name='allocate_L-detail'),
    path('<int:pk>/update/allocate_L', allocate_LUpdateView.as_view(), name='allocate_L-update'),
    path('<int:pk>/delete/allocate_L', allocate_LDeleteView.as_view(), name='allocate_L-delete'),
    
    path('Litter', LitterListView.as_view(), name='Litter-list'),
    path('Litter/create/', LitterCreateView.as_view(), name='Litter-create'),
    path('<int:pk>/details/Litter', LitterDetailView.as_view(), name='Litter-detail'),
    path('<int:pk>/update/Litter', LitterUpdateView.as_view(), name='Litter-update'),
    path('<int:pk>/delete/Litter', LitterDeleteView.as_view(), name='Litter-delete'),


    path('list', views.your_view, name='farrowlist'),
    path('birth/<int:birthdetail>/', views.farrowing_details, name='birth_details'),

    path('Inven', InvenListView.as_view(), name='Inven-list'),
    path('Inven/create/', InvenCreateView.as_view(), name='Inven-create'),
    path('<int:pk>/details/Inven', InvenDetailView.as_view(), name='Inven-detail'),
    path('<int:pk>/update/Inven', InvenUpdateView.as_view(), name='Inven-update'),
    path('<int:pk>/delete/Inven', InvenDeleteView.as_view(), name='Inven-delete'),

    path('Mating', MatingListView.as_view(), name='Mating-list'),
    path('Mating/create/', MatingCreateView.as_view(), name='Mating-create'),
    path('<int:pk>/details/Mating', MatingDetailView.as_view(), name='Mating-detail'),
    path('<int:pk>/update/Mating', MatingUpdateView.as_view(), name='Mating-update'),
    path('<int:pk>/delete/Mating', MatingDeleteView.as_view(), name='Mating-delete'),

    path('Weaning', WeaningListView.as_view(), name='Weaning-list'),
    path('Weaning/create/', WeaningCreateView.as_view(), name='Weaning-create'),
    path('<int:pk>/details/Weaning', WeaningDetailView.as_view(), name='Weaning-detail'),
    path('<int:pk>/update/Weaning', WeaningUpdateView.as_view(), name='Weaning-update'),
    path('<int:pk>/delete/Weaning', WeaningDeleteView.as_view(), name='Weaning-delete'),

    path('Farrowing', FarrowingListView.as_view(), name='Farrowing-list'),
    path('Farrowing/create/', FarrowingCreateView.as_view(), name='Farrowing-create'),
    path('<int:pk>/details/Farrowing', FarrowingDetailView.as_view(), name='Farrowing-detail'),
    path('<int:pk>/update/Farrowing', FarrowingUpdateView.as_view(), name='Farrowing-update'),
    path('<int:pk>/delete/Farrowing', FarrowingDeleteView.as_view(), name='Farrowing-delete'),


    path('testP', TestPListView.as_view(), name='testP-list'),
    path('testP/create/', TestPCreateView.as_view(), name='testP-create'),
    path('<int:pk>/details/testP', TestPDetailView.as_view(), name='testP-detail'),
    path('<int:pk>/update/testP', TestPUpdateView.as_view(), name='testP-update'),
    path('<int:pk>/delete/testP', TestPDeleteView.as_view(), name='testP-delete'),

]