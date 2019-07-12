from django.conf import settings
from django.db import models
from django.utils import timezone
from django import forms
from .choices import *



class Laptop(models.Model):
    name = models.CharField(max_length=200, default='name')
    company = models.CharField(
        max_length=2,
        choices=companyChoice,
        default='pd',
    )
    inventNumber = models.CharField(max_length=200, default='name')
    serialNumber = models.CharField(max_length=200, default='name')
    owner = models.ForeignKey('Worker', on_delete=models.CASCADE, null=True, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name + ' (' + self.serialNumber + ') ' + self.inventNumber + ' ' + str(self.owner)



class Printer(models.Model):
    name = models.CharField(max_length=200, default='name')
    company = models.CharField(
        max_length=2,
        choices=companyChoice,
        default='pd',
    )
    inventNumber = models.CharField(max_length=200, default='name')
    serialNumber = models.CharField(max_length=200, default='name')
    owner = models.ForeignKey('Worker', on_delete=models.CASCADE, null=True, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name + ' (' + self.serialNumber + ') ' + self.inventNumber


class Shredder(models.Model):
    name = models.CharField(max_length=200, default='name')
    company = models.CharField(
        max_length=2,
        choices=companyChoice,
        default='pd',
    )
    inventNumber = models.CharField(max_length=200, default='name')
    serialNumber = models.CharField(max_length=200, default='name')
    owner = models.ForeignKey('Worker', on_delete=models.CASCADE, null=True, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name + ' (' + self.serialNumber + ') ' + self.inventNumber

class Television(models.Model):
    name = models.CharField(max_length=200, default='name')
    company = models.CharField(
        max_length=2,
        choices=companyChoice,
        default='pd',
    )
    inventNumber = models.CharField(max_length=200, default='name')
    serialNumber = models.CharField(max_length=200, default='name')
    owner = models.ForeignKey('Worker', on_delete=models.CASCADE, null=True, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name + ' (' + self.serialNumber + ') ' + self.inventNumber



class Condition(models.Model):
    name = models.CharField(max_length=200, default='name')
    company = models.CharField(
        max_length=2,
        choices=companyChoice,
        default='pd',
    )
    inventNumber = models.CharField(max_length=200, default='name')
    serialNumber = models.CharField(max_length=200, default='name')
    owner = models.ForeignKey('Worker', on_delete=models.CASCADE, null=True, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name + ' (' + self.serialNumber + ') ' + self.inventNumber

class Telephone(models.Model):
    name = models.CharField(max_length=200, default='name')
    company = models.CharField(
        max_length=2,
        choices=companyChoice,
        default='pd',
    )
    inventNumber = models.CharField(max_length=200, default='name')
    serialNumber = models.CharField(max_length=200, default='name')
    owner = models.ForeignKey('Worker', on_delete=models.CASCADE, null=True, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name + ' (' + self.serialNumber + ') ' + self.inventNumber



class Camera(models.Model):
    name = models.CharField(max_length=200, default='name')
    company = models.CharField(
        max_length=2,
        choices=companyChoice,
        default='pd',
    )
    inventNumber = models.CharField(max_length=200, default='name')
    serialNumber = models.CharField(max_length=200, default='name')
    owner = models.ForeignKey('Worker', on_delete=models.CASCADE, null=True, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name + ' (' + self.serialNumber + ') ' + self.inventNumber



class Dispenser(models.Model):
    name = models.CharField(max_length=200, default='name')

    company = models.CharField(
        max_length=2,
        choices=companyChoice,
        default='pd',
    )
    inventNumber = models.CharField(max_length=200, default='name')
    serialNumber = models.CharField(max_length=200, default='name')
    owner = models.ForeignKey('Worker', on_delete=models.CASCADE, null=True, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name + ' (' + self.serialNumber + ') ' + self.inventNumber

class Microwave(models.Model):
    name = models.CharField(max_length=200, default='name')

    company = models.CharField(
        max_length=2,
        choices=companyChoice,
        default='pd',
    )
    inventNumber = models.CharField(max_length=200, default='name')
    serialNumber = models.CharField(max_length=200, default='name')
    owner = models.ForeignKey('Worker', on_delete=models.CASCADE, null=True, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name + ' (' + self.serialNumber + ') ' + self.inventNumber

class Display(models.Model):
    name = models.CharField(max_length=200, default='name')

    company = models.CharField(
        max_length=2,
        choices=companyChoice,
        default='pd',
    )
    inventNumber = models.CharField(max_length=200, default='name')
    serialNumber = models.CharField(max_length=200, default='name')
    owner = models.ForeignKey('Worker', on_delete=models.CASCADE, null=True, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name + ' (' + self.serialNumber + ') ' + self.inventNumber

class Computer(models.Model):
    name = models.CharField(max_length=200, default='name')

    company = models.CharField(
        max_length=2,
        choices=companyChoice,
        default='pd',
    )
    inventNumber = models.CharField(max_length=200, default='name')
    serialNumber = models.CharField(max_length=200, default='name')
    owner = models.ForeignKey('Worker', on_delete=models.CASCADE, null=True, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name + ' (' + self.serialNumber + ') ' + self.inventNumber



class FileName(models.Model):
    name = models.CharField(max_length=200, default='')
    section = models.CharField(
        max_length=3,
        choices=sectionChoice,
        default='s1',
    )
    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class Document(models.Model):
    fileName = models.ForeignKey('FileName', on_delete=models.CASCADE, null=True, blank=True)
    owner = models.ForeignKey('Worker', on_delete=models.CASCADE, null=True, blank=True)
    reading = models.BooleanField('Чтение', default=False)
    adding = models.BooleanField('Добавление', default=False)
    change = models.BooleanField('Изменение', default=False)
    watch = models.BooleanField('Просмотр', default=False)
    delete = models.BooleanField('Удаление', default=False)
    edit = models.BooleanField('Редактирование', default=False)
    
    def publish(self):
        self.save()

    def __str__(self):
        return str(self.fileName)

class Worker(models.Model):
    name = models.CharField(max_length=200, default='name')
    surname = models.CharField(max_length=200, default='name')
    workerID = models.IntegerField(default=1)
    company = models.CharField(
        max_length=2,
        choices=companyChoice,
        default='pd',
    )

    job = models.CharField(
        max_length=2,
        choices=jobChoice,
        default='pd',
    )


    def publish(self):
        self.save()

    def __str__(self):
        return  self.name +' '+ self.surname