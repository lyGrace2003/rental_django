# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from django.http.response import JsonResponse
# from rental.serializers import FriendSerializer, BelongingSerializer, BorrowedSerializer
# from rental.models import Friend, Belonging, Borrowed

# @csrf_exempt
# def friendAPI(request, id =0):
#     if request.method == 'GET':
#         friend = Friend.objects.all()
#         friend_serializer = FriendSerializer(friend, many=True)
#         return JsonResponse(friend_serializer.data, safe=False)
#     elif request.method == 'POST':
#         friend_data = JSONParser().parse(request)
#         friend_serializer = FriendSerializer(data=friend_data)
#         if friend_serializer.is_valid():
#             friend_serializer.save()
#             return JsonResponse("Added Successfully", safe=True)
#         return JsonResponse("Failed to add", safe=False)
#     elif request.method == 'PUT':
#         friend_data = JSONParser().parse(request)
#         friend = Friend.objects.get(id=id)
#         friend_serializer = FriendSerializer(friend, data=friend_data)
#         if friend_serializer.is_valid():
#             friend_serializer.save()
#             return JsonResponse("Updated Successfully", safe=False)
#         return JsonResponse("Failed to update")
#     elif request.method == 'DELETE': 
#         friend = Friend.objects.get(id=id)
#         friend.delete()
#         return JsonResponse("Deleted Successfully", safe=False)
    
# def belongingAPI(request, id =1):
#     if request.method == 'GET':
#         belonging = Belonging.objects.all()
#         belonging_serializer = BelongingSerializer(belonging, many=True)
#         return JsonResponse(belonging_serializer.data, safe=False)
#     elif request.method == 'POST':
#         belonging_data = JSONParser().parse(request)
#         belonging_serializer = BelongingSerializer(data=belonging_data)
#         if belonging_serializer.is_valid():
#             belonging_serializer.save()
#             return JsonResponse("Added Successfully", safe=True)
#         return JsonResponse("Failed to add", safe=False)
#     elif request.method == 'PUT':
#         belonging_data = JSONParser().parse(request)
#         belonging = Belonging.objects.get(id=id)
#         belonging_serializer = BelongingSerializer(belonging, data=belonging_data)
#         if belonging_serializer.is_valid():
#             belonging_serializer.save()
#             return JsonResponse("Updated Successfully", safe=False)
#         return JsonResponse("Failed to update")
#     elif request.method == 'DELETE': 
#         belonging = Belonging.objects.get(id=id)
#         belonging.delete()
#         return JsonResponse("Deleted Successfully", safe=False)
    
# def borrowedAPI(request, id = 2):
#     if request.method == 'GET':
#         borrowed = Borrowed.objects.all()
#         borrowed_serializer = BorrowedSerializer(borrowed, many=True)
#         return JsonResponse(borrowed_serializer.data, safe=False)
#     elif request.method == 'POST':
#         borrowed_data = JSONParser().parse(request)
#         borrowed_serializer = BorrowedSerializer(data=borrowed_data)
#         if borrowed_serializer.is_valid():
#             borrowed_serializer.save()
#             return JsonResponse("Added Successfully", safe=True)
#         return JsonResponse("Failed to add", safe=False)
#     elif request.method == 'PUT':
#         borrowed_data = JSONParser().parse(request)
#         borrowed = BorrowedSerializer.objects.get(id=id)
#         borrowed_serializer = BorrowedSerializer(borrowed, data=borrowed_data)
#         if borrowed_serializer.is_valid():
#             borrowed_serializer.save()
#             return JsonResponse("Updated Successfully", safe=False)
#         return JsonResponse("Failed to update")
#     elif request.method == 'DELETE': 
#         borrowed = Borrowed.objects.get(id=id)
#         borrowed.delete()
#         return JsonResponse("Deleted Successfully", safe=False)
