from rest_framework import viewsets
from .serializer import TaskSerialize
from .models import Task


class TaskView(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions for Task model:
    - list (GET /tasks/)
    - create (POST /tasks/)
    - retrieve (GET /tasks/{id}/)
    - update/partial_update (PUT/PATCH /tasks/{id}/)
    - destroy (DELETE /tasks/{id}/)
    """
    
    # Define the base queryset and serializer
    queryset = Task.objects.all()
    serializer_class = TaskSerialize

    def get_queryset(self):
        """
        Optionally filter the queryset by:
        - title keyword search
        - date match
        - sorting by date
        """
        queryset = super().get_queryset()

        # Get filter parameters from query string
        search = self.request.query_params.get('search')              
        search_date = self.request.query_params.get('search_date')     
        sort_by_date = self.request.query_params.get('sort_by_date')   

        # Filter by title if 'search' parameter is provided
        if search:
            queryset = queryset.filter(title__icontains=search)

        # Filter by date if 'search_date' parameter is provided
        if search_date:
            queryset = queryset.filter(date=search_date)

        # Sort by date if requested
        if sort_by_date == 'true':
            queryset = queryset.order_by('date')

        return queryset
