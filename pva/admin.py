from django.contrib import admin
from django.utils.html import mark_safe
from . import models


# @admin.register(models.SenderInfoModifer, models.ForeignSADR, models.ForeignReporting,
#                 models.Lltptconverter, models.Downloader, models.FilenameModifier, models.FoldernameModifier)
# class ItemAdmin(admin.ModelAdmin):
#     """ Item Admin Definition """

#     list_display = ("name", "used_by")

#     def used_by(self, obj):
#         return obj.pva.count()

#     pass


# class FileInline(admin.TabularInline):
#     model = models.File


# @admin.register(models.Tracker)
# class TrackerAdmin(admin.ModelAdmin):
#     """ Tracker Admin Definition """

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

#     # def count_photos(self, obj):
#     #     return obj.photos.count()

#     # count_photos.short_description = "Photo Count"


# # @admin.register(models.SenderInfoModifer)
# # class SenderInfoModiferAdmin(admin.ModelAdmin):
# #     """ SenderInfoModifer Admin Definition """

# #     pass


# # @admin.register(models.ForeignSADR)
# # class ForeignSADRAdmin(admin.ModelAdmin):
# #     """ ForeignSADR Admin Definition """

# #     pass

# # @admin.register(models.ForeignReporting)
# # class ForeignReportingAdmin(admin.ModelAdmin):
# #     """ ForeignReporting Admin Definition """

# #     pass

# # @admin.register(models.Lltptconverter)
# # class LltptconverterAdmin(admin.ModelAdmin):
# #     """ Lltptconverter Admin Definition """

# #     pass


# # @admin.register(models.Downloader)
# # class DownloaderAdmin(admin.ModelAdmin):
# #     """ Downloader Admin Definition """

# #     pass

# # @admin.register(models.FilenameModifier)
# # class FilenameModifierAdmin(admin.ModelAdmin):
# #     """ FilenameModifier Admin Definition """

# #     pass


# # @admin.register(models.FoldernameModifier)
# # class FoldernameModifierAdmin(admin.ModelAdmin):
# #     """ FoldernameModifier Admin Definition """

# #     pass


# @admin.register(models.File)
# class FileAdmin(admin.ModelAdmin):
#     """ Phot Admin Definition """

#     list_display = ("__str__", "get_thumbnail")

#     def get_thumbnail(self, obj):
#         return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

#     get_thumbnail.short_description = "Thumbnail"
