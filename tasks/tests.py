from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import Task

class TaskModelTest(TestCase):

    def setUp(self):
        """
        Set up a test task instance to be used in test methods.
        """
        self.task = Task.objects.create(
            title="Test Task",
            description="This is a test task",
            completed=False,
            date="2025-12-31"
        )

    def test_task_creation(self):
        """
        Test task creation and validate field values.
        """
        self.assertEqual(self.task.title, "Test Task")
        self.assertEqual(self.task.description, "This is a test task")
        self.assertFalse(self.task.completed)

    def test_is_overdue(self):
        """
        Test if the task is correctly marked as overdue.
        """
        overdue_task = Task.objects.create(
            title="Overdue Task",
            description="This task is overdue",
            completed=False,
            date="2020-12-31"
        )
        self.assertTrue(overdue_task.is_overdue())  # Ensure overdue task is detected


class TaskApiTests(TestCase):

    def setUp(self):
        """
        Create a task instance for API tests and prepare the URL for task listing.
        """
        self.task = Task.objects.create(
            title="API Task",
            description="Test task for the API",
            completed=False,
            date="2025-06-15"
        )
        self.url = reverse('task-list-create')  # Adjust to the actual URL name

    def test_create_task(self):
        """
        Test that a POST request creates a new task.
        """
        data = {
            'title': 'New Task',
            'description': 'Description of new task',
            'completed': False,
            'date': '2025-06-20'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)  # Ensure task count is incremented

    def test_list_tasks(self):
        """
        Test that a GET request lists all tasks.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Ensure only 1 task is returned in the response

    def test_task_detail(self):
        """
        Test that a GET request returns the details of a specific task.
        """
        task_url = reverse('task-detail', kwargs={'pk': self.task.id})
        response = self.client.get(task_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.task.title)  # Validate title

    def test_delete_task(self):
        """
        Test that a DELETE request removes a task from the database.
        """
        task_url = reverse('task-detail', kwargs={'pk': self.task.id})
        response = self.client.delete(task_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)  # Ensure task is deleted from the database

    def test_update_task(self):
        """
        Test that a PATCH request updates an existing task's attributes.
        """
        task_url = reverse('task-detail', kwargs={'pk': self.task.id})
        data = {
            'title': 'Updated Task',
            'completed': True
        }
        response = self.client.patch(task_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Task')  # Ensure title is updated
        self.assertTrue(response.data['completed'])  # Ensure 'completed' field is updated to True
