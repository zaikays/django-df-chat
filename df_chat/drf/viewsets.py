from rest_framework import permissions, mixins
from rest_framework.viewsets import GenericViewSet

from df_chat.drf.serializers import ChatRoomSerializer, RoomUserSerializer, ChatMessageSerializer, \
    ChatMessageReactionSerializer
from df_chat.models import ChatRoom, RoomUser, ChatMessage, ChatMessageReaction


class ChatRoomViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer


class RoomUserViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
               mixins.DestroyModelMixin, GenericViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = RoomUser.objects.all()
    serializer_class = RoomUserSerializer


class ChatMessageViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
               mixins.DestroyModelMixin, GenericViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer


class ChatMessageReactionsViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = ChatMessageReaction.objects.all()
    serializer_class = ChatMessageReactionSerializer


class ChatMediaViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    permission_classes = [permissions.AllowAny]
