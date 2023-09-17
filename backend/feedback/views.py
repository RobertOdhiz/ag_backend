from rest_framework import viewsets
from .models import Feedback
from .serializers import FeedbackSerializer
from rest_framework.response import Response
from rest_framework import status

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        feedback_text = serializer.validated_data['feedback_text']

        # If the user is authenticated, use their email
        if request.user.is_authenticated:
            email = request.user.email

        # Save the feedback
        feedback = Feedback(email=email, feedback_text=feedback_text)
        feedback.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        # Return only the email addresses for GET requests
        queryset = Feedback.objects.all().values_list('email', flat=True)
        return Response(queryset)
