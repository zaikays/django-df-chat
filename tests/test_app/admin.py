from django.contrib import admin

from df_chat.models import ChatRoom, ChatMembers, ChatMessage, MemberStatus
from tests.test_app.models import ChatUser, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(MemberStatus)
class MemberStatusAdmin(admin.ModelAdmin):
    pass


class ChatUserInline(admin.TabularInline):
    model = ChatMembers


@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'title')
    inlines = (ChatUserInline,)


@admin.register(ChatMembers)
class ChatMembersAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'chat_group', )


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'message', )