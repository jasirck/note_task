from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Note

class NoteTests(APITestCase):

    def test_create_note(self):
        url = reverse('create_note')
        data = {'title': 'Test Note', 'body': 'This is a test note.'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_get_note_by_id(self):
        note = Note.objects.create(title='Sample Note', body='Sample Body')
        url = reverse('get_note', args=[note.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_query_notes_by_title(self):
        Note.objects.create(title='Sample Note', body='Sample Body')
        url = reverse('query_notes')
        response = self.client.get(url, {'title': 'Sample'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_update_note(self):
        note = Note.objects.create(title='Old Title', body='Old Body')
        url = reverse('update_note', args=[note.id])
        data = {'title': 'New Title', 'body': 'New Body'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
