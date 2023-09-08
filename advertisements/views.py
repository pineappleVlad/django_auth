from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .filters import AdvertisementFilter
from .models import Advertisement
from .permissions import IsOwnerOrReadOnly
from .serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filterset_class = AdvertisementFilter


    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return []
