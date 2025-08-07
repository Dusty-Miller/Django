from django.core.serializers import serialize
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog.models import Post
from .serializers import PostSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.
def example(request):
    return render(request,
                  template_name='example/example.html')
@api_view(['GET','DELETE','PUT'])
def postAPI(request,pk):
    if request.method == 'GET':
        post = Post.objects.get(pk=pk)
        postSerializer = PostSerializer(post)
        return Response(postSerializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        post = get_object_or_404(Post, pk=pk)
        postSerializer = PostSerializer(post,data=request.data)
        if postSerializer.is_valid():
            postSerializer.save()
            return Response(postSerializer.data, status=status.HTTP_204_NO_CONTENT)
    return Response(postSerializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def blogAPI(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        postSerializer = PostSerializer(posts, many=True)
        return Response(postSerializer.data, status=status.HTTP_200_OK)
    else: #request.method == 'POST'
        postSeializer = PostSerializer(data= request.data)
        if postSeializer.is_valid():
            postSeializer.save()
            return Response(postSeializer.data, status=status.HTTP_201_CREATED)
    return Response(postSeializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def helloAPI(request):
    return Response({'hello': 'world'})

@api_view(['POST']) #다섯가지 기능 - 전체리스트,상세보기,생성하기,수정하기,삭제하기
                    # 1.url이 기능의 의미를 가진다.
                    # 2.너무 많은 url을 만들지 말고, method를 활용한다.
                    #GET-전체리스트,한개 상세정보 보기,
                    #POST-새로 생성하기,작성하기(form을 작성해서 제출하기 누른 경우),[제출버튼] --> url에 붙어서 보여진 채로 보내짐 http://naver,com/?name='홍길동'
                    #<form type='post'> [제출버튼] --> http request payload form을 숨겨서 보내짐 http://naver.com/
                    #PUT -> Post를 수정했다면, 전체 항목을 다시 보내줌,
                    #PATCH -> Post를 수정할때 title='수정한 타이틀' 일부 항목만 보내면 됨,
                    #DELETE -> 삭제할때 사용된다.

def hiAPI(request):
    return Response({'hi': 'world'})


