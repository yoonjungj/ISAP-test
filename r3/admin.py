from django.contrib import admin
from django.utils.html import mark_safe
from . import models


# @admin.register(models.R2toR3, models.R3errorRepresentor)
# class ItemAdmin(admin.ModelAdmin):
#     """ Item Admin Definition """

#     list_display = ("name", "used_by")

#     def used_by(self, obj):
#         return obj.r3.count()

#     pass


# class FileInline(admin.TabularInline):
#     model = models.File


# @admin.register(models.R2toR3KR)
# class R2toR3KRAdmin(admin.ModelAdmin):
#     """ R2toR3KR Admin Definition """

#     inlines = (FileInline,)
#     fieldsets = (
#         (
#             "Basic Info",
#             {
#                 "fields": (
#                     "name",
#                     "description",
#                     "country",
#                     "company",
#                 )
#             },
#         ),
#         ("Times", {"fields": ("registration_date", "urgent")}),
#         # (
#         #     "More About the Space",
#         #     {"fields": ("request")},
#         # ),
#         ("Last Details", {"fields": ("client",)}),
#     )
#     list_display = (
#         "name",
#         "country",
#         "company",
#         "registration_date",
#         "urgent",
#         # "count_photos",

#     )
#     list_filter = (
#         "urgent",
#         "client__superhost",
#         "company",
#         "country",
#     )
#     raw_id_fields = ("client",)
#     search_fields = ("=company", "^client__username")
#     #filter_horizontal = ("request")


# @admin.register(models.File)
# class FileAdmin(admin.ModelAdmin):
#     """ Phot Admin Definition """

#     list_display = ("__str__", "get_thumbnail")

#     def get_thumbnail(self, obj):
#         return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

#     get_thumbnail.short_description = "Thumbnail"
