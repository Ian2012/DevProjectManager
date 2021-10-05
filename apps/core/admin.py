from django.contrib import admin

from .models import Company, Project, Ticket, TicketComment, User, UserStory


class TicketCommentInline(admin.TabularInline):
    model = TicketComment


class TicketAdmin(admin.ModelAdmin):
    inlines = (TicketCommentInline,)
    list_filter = ('user_story', 'state', 'canceled')
    list_display = ('description', 'user_story', 'state', 'canceled')


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'nit', 'phone', 'direction', 'email')


admin.site.register(User)
admin.site.register(UserStory)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Project)
admin.site.register(Ticket, TicketAdmin)
