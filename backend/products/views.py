from rest_framework import generics
from .models import Audiobook, Review,Genre,Author
from .serializers import AudiobookSerializer, ReviewSerializer,AudiobookMiniSerializer,ReviewCreateSerializer
from rest_framework import pagination
from rest_framework.views import APIView
from rest_framework.response import Response


class AudiobookListView(APIView):
    # add pagination
    pagination_class = pagination.LimitOffsetPagination
    pagination_class.default_limit = 16
    paginator = pagination.LimitOffsetPagination()

   
    serializer_class = AudiobookMiniSerializer
    def get(self,request):
        # get query parms
        genre = request.query_params.get('genre')
        author = request.query_params.get('author')
        rating = request.query_params.get('rating')
        queryset = Audiobook.objects.all()
        if genre:
            queryset = queryset.filter(genre__name=genre)
        if author:
            queryset = queryset.filter(author__name=author)
        if rating:
            queryset = queryset.filter(average_rating__gte=rating)
        
        page = self.paginator.paginate_queryset(queryset, request)
        print(page)
        if page is not None:
            serializer = AudiobookMiniSerializer(page, many=True,context={"request": request})
            unique_genres = Genre.objects.all().values('name').distinct()
            unique_authors = Author.objects.all().values('name').distinct()
            response = self.paginator.get_paginated_response(serializer.data)
            response.data['genres'] = unique_genres
            response.data['authors'] = unique_authors
            page_size = self.paginator.get_limit(request)
            response.data['page_size'] = page_size
            response.data['total_results'] = self.paginator.count
            # total_pages = self.paginator.page.paginator.num_pages
            response.data['total_pages'] = self.paginator.count//page_size



        
            return response
        return Response({})

class AudiobookDetailView(APIView):
    pass
    def get(self,request,pk):
        audiobook = Audiobook.objects.get(id=pk)
        reviews = Review.objects.filter(audiobook=audiobook)

        serializer = AudiobookSerializer(audiobook,context={"request": request})
        reviews_serializer = ReviewSerializer(reviews,many=True)
        return Response({
            'audiobook':serializer.data,
            'reviews':reviews_serializer.data
        })

        

# class ReviewCreateView(generics.CreateAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewCreateSerializer

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

class ReviewCreateView(APIView):
    def post(self,request,pk):
        data = request.data
        data['audiobook'] = pk
        serializer = ReviewCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

