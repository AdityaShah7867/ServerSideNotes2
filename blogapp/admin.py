from django.contrib import admin
from .models import UserAccount, Subject, Module, Notes, Comment, CmntReply, Reminder

class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'is_mod', 'is_nUser', 'is_staff', 'coins_scored', 'rank')
    list_filter = ('is_mod', 'is_nUser', 'is_staff', 'coins_scored', 'rank')
    search_fields = ('email', 'name')
    ordering = ('-coins_scored',)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher', 'teacherurl')
    list_filter = ('name',)
    search_fields = ('name', 'teacher')

class ModuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'sub')
    list_filter = ('name',)
    search_fields = ('name', 'sub__name')

class NotesAdmin(admin.ModelAdmin):
    list_display = ('nDetail','desc', 'mod', 'file', 'author', 'status', 'typeN',  'sub')
    list_filter = ('mod', 'author', 'status', 'typeN', 'sub')
    search_fields = ('desc', 'mod', 'author__name', 'typeN', 'sub__name')
    ordering = ('status',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('toU', 'fromU', 'note', 'cmnt', 'cmntDate')
    list_filter = ('toU', 'fromU', 'note', 'cmntDate')
    search_fields = ('toU__name', 'fromU__name', 'note__desc', 'cmnt')

class CmntReplyAdmin(admin.ModelAdmin):
    list_display = ('cmtRply', 'cmntR', 'frR')
    list_filter = ('cmtRply',)
    search_fields = ('cmtRply__name', 'cmntR', 'frR')

admin.site.register(UserAccount, UserAccountAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Notes, NotesAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(CmntReply, CmntReplyAdmin)
admin.site.register(Reminder)