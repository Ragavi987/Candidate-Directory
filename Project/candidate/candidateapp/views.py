from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Candidatedirectory
from .serializers import CandidatedirectorySerializer, CandidatedirectoryUpdateSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

'''api overview'''
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'All Candidates': 'api/candidates',
        'View Candidate by ID': 'api/candidates/id',
        'Add': 'api/create',
        'Update': 'api/update/id',
        'Delete': 'api/delete/id'
    }

    return Response(api_urls)


'''api view for get all candidate details'''
@api_view(['GET'])
def view_all_candidates(request):
    # checking for the parameters from the URL
    if request.query_params:
        candidates = Candidatedirectory.objects.filter(**request.query_params.dict())
    else:
        candidates = Candidatedirectory.objects.all()

    # if there is something in items else raise error
    if candidates:
        serializer = CandidatedirectorySerializer(candidates, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


'''api view for get particular candidate details using ID'''
@api_view(['GET'])
def get_candidate_details(request, pk):
    candidate = Candidatedirectory.objects.get(id=pk)
    serializer = CandidatedirectorySerializer(candidate, many=False)
    return Response(serializer.data)


'''api view for create new candidate'''
@api_view(['POST'])
def add_candidate(request):
    errors = list()
    message = 'Error in creating candidate'
    success = False
    code = 500
    errors = list()
    candidate = CandidatedirectorySerializer(data=request.data)

    if candidate.is_valid():
        candidate.save()
        code = 200
        success = True
        message = 'Successfully Created'
    else:
        if candidate.errors:
            for key, value in candidate.errors.items():
                error_ = value[0]
                errors.append({"error": error_})

    return Response({'data':candidate.data, 'message': message, 'success': success, 'errors':errors},status=code)


'''api view for update existing candidate'''
@api_view(['PUT'])
def update_candidate(request, pk):
    errors = list()
    message = 'Error in updating candidate'
    success = False
    code = 500
    errors = list()
    try:
        candidate = Candidatedirectory.objects.get(pk=pk)
    except Exception as e:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = CandidatedirectoryUpdateSerializer(instance=candidate, data=request.data)

    if data.is_valid():
        data.save()
        code = 200
        success = True
        message = 'Successfully Updated'
    else:
        if data.errors:
            for key, value in data.errors.items():
                error_ = value[0]
                errors.append({"error": error_})

    return Response({'data':data.data, 'message': message, 'success': success, 'errors':errors},status=code)


'''api view for delete existing candidate'''
@api_view(['DELETE'])
def delete_candidate(request, pk):
    candidate = get_object_or_404(Candidatedirectory, pk=pk)
    candidate.delete()
    return Response(status=status.HTTP_202_ACCEPTED)