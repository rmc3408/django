from rest_framework import generics
from company.models import Post
from .serializers import PostSerializer


class CompanyList(generics.ListCreateAPIView):
    queryset = Post.postObj.all()
    serializer_class = PostSerializer
    pass


class CompanyDetail(generics.RetrieveDestroyAPIView):
    pass



