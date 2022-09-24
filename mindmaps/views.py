from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.db.models import Prefetch

from .serializers import BranchLineSerializer, BranchSerializer, MindmapSerializer, AddMindmapSerializer, SimpleMindmapSerializer, UpdateMindmapSerializer
from .models import Branch, BranchLine, Mindmap

@api_view()
def increment_revisions(request, id):
    try:
        mindmap = Mindmap.objects.get(pk=id)
        mindmap.revisions += 1
        mindmap.save()
        serializer = UpdateMindmapSerializer(mindmap)
        return Response(serializer.data)
    except Mindmap.DoesNotExist:
	    return Response(f"Person with id {id} doesn't exist", status=status.HTTP_404_NOT_FOUND)


class MindmapViewSet(ModelViewSet):

    def get_queryset(self):
        if self.action == 'list':
            return Mindmap.objects.order_by('category','title').all().defer('branches')
        return Mindmap.objects.prefetch_related(
                Prefetch('branches', Branch.objects.order_by('sort_number')), 
                Prefetch('branches__content_line', BranchLine.objects.order_by('sort_number'))) \
            .all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddMindmapSerializer
        if self.request.method == 'PUT':
            return UpdateMindmapSerializer
        if self.action == 'list':
            return SimpleMindmapSerializer
        return MindmapSerializer

class BranchViewSet(ModelViewSet):
    serializer_class = BranchSerializer
    lookup_field = 'sort_number'

    def get_queryset(self):
        return Branch.objects \
            .filter(mindmap_id=self.kwargs['mindmap_pk']) \
            .prefetch_related('content_line') \
            .all()

class BranchLineViewSet(ModelViewSet):
    serializer_class = BranchLineSerializer
    lookup_field = 'sort_number'

    def get_queryset(self):
        return BranchLine.objects.filter(branch__mindmap=self.kwargs['mindmap_pk'],
           branch__sort_number=self.kwargs['branch_sort_number']).all()