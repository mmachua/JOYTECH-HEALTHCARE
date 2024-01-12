from django.urls import path
from .views import EquipmentListView, EquipmentDetailView, add_equipment , ChatbotView

app_name = 'inventory'

urlpatterns = [
    path('equipment/', EquipmentListView.as_view(), name='equipment-list'),
    #path('equipment/<int:pk>/', EquipmentDetailView.as_view(), name='equipment-detail'),
    path('equipment/<int:pk>/', EquipmentDetailView.as_view(), name='equipment-detail'),
    # ... other URLs ...
    path('equipment/add/', add_equipment, name='add-equipment'),
    # ... other URLs ...
    path('chatbot/', ChatbotView.as_view(), name='chatbot'),
    
]
