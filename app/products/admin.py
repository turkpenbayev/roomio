from django.contrib import admin
from .models import Device, Tag, Location, DeviceLocation, Scene, DeviceScene, DeviceSceneTag

class TagInline(admin.TabularInline):
    model = DeviceLocation.tags.through
    extra = 0

class DeviceLocationInline(admin.TabularInline):
    model = DeviceLocation
    extra = 0

class DeviceSceneTagInline(admin.TabularInline):
    model = DeviceSceneTag
    extra = 0

class DeviceSceneInline(admin.TabularInline):
    model = DeviceScene
    show_change_link = True
    extra = 0

class DeviceAdmin(admin.ModelAdmin):
    inlines = [DeviceLocationInline, DeviceSceneInline]
    list_display = ('deviceName', 'hrc_ip', 'hrc_port', 'unitId', 'deviceTemplateID', 'room')
    list_editable = ('hrc_ip', 'hrc_port', 'unitId', 'deviceTemplateID', 'room')
    search_fields = ('deviceName', 'room')
    list_filter = ('room',)
    list_per_page = 10

class DeviceLocationAdmin(admin.ModelAdmin):
    inlines = [TagInline]

class DeviceSceneAdmin(admin.ModelAdmin):
    inlines = [DeviceSceneTagInline]

admin.site.register(Device, DeviceAdmin)
admin.site.register(Tag)
admin.site.register(Location)
admin.site.register(DeviceLocation, DeviceLocationAdmin)
admin.site.register(Scene)
admin.site.register(DeviceScene, DeviceSceneAdmin)
