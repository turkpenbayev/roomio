from django.db import models


class Device(models.Model):
    hrc_ip = models.CharField(max_length=100)
    hrc_port = models.IntegerField()
    unitId = models.IntegerField()
    deviceName = models.CharField(max_length=100)
    deviceTemplateID = models.IntegerField()
    room = models.IntegerField()

    def __str__(self):
        return self.deviceName


class Tag(models.Model):
    modbusId = models.IntegerField()

    def __str__(self):
        return str(self.modbusId)


class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class DeviceLocation(models.Model):
    device = models.ForeignKey(
        Device, related_name='device_locations', on_delete=models.CASCADE)
    location = models.ForeignKey(
        Location, related_name='device_locations', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.location.name} ({self.device.deviceName})"


class Scene(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class DeviceScene(models.Model):
    device = models.ForeignKey(
        Device, related_name='scenes', on_delete=models.CASCADE)
    scene = models.ForeignKey(
        Scene, related_name='devices', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.scene.name} ({self.device.deviceName})"


class DeviceSceneTag(models.Model):
    device_scene = models.ForeignKey(
        DeviceScene, related_name='tags_and_values', on_delete=models.CASCADE)
    tag = models.ForeignKey(
        Tag, related_name='device_scenes', on_delete=models.CASCADE)
    value = models.IntegerField()

    def __str__(self):
        return f"{self.tag} - Value: {self.value}"
