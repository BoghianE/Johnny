from rest_framework.generics import ListAPIView, RetrieveAPIView

from .serializers import ArticleSerializer

from articole.models import Articol

class ArticleListView(ListAPIView):
    queryset = Articol.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailView(RetrieveAPIView):
    queryset = Articol.objects.all()
    serializer_class = ArticleSerializer




    
