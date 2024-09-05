from django.urls import path
from .views import NoteCreateView, NoteDetailView, NoteUpdateView, NoteListView

urlpatterns = [
    path('notes/', NoteCreateView.as_view(), name='create_note'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='get_note'),
    path('notes/<int:pk>/update/', NoteUpdateView.as_view(), name='update_note'),
    path('notes/search/', NoteListView.as_view(), name='query_notes'),
]
