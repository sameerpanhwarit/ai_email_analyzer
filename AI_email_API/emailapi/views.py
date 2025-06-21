from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import EmailAnalysis
from .serializers import EmailAnalysisSerializer
from .ai_utils import analyze_email  

class AnalyzeEmailView(APIView):
    def post(self, request):
        serializer = EmailAnalysisSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data['text']

            summary, sentiment, urgency = analyze_email(text)

            analysis = EmailAnalysis.objects.create(
                text=text,
                summary=summary,
                sentiment=sentiment,
                urgency=urgency
            )
            output = EmailAnalysisSerializer(analysis)
            return Response(output.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
