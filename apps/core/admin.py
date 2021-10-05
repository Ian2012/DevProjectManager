from django.contrib import admin

from apps.core.models import Company, Project, Ticket, TicketComment, User


class TicketCommentInline(admin.TabularInline):
    model = TicketComment


class TicketAdmin(admin.ModelAdmin):
    inlines = (TicketCommentInline,)


admin.site.register(User)
admin.site.register(Company)
admin.site.register(Project)
admin.site.register(Ticket, TicketAdmin)
