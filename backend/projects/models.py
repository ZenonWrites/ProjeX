from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    company_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name

class Project(models.Model):

    class Priority(models.TextChoices):
        HIGH = 'HIGH', 'High'
        MEDIUM = 'MEDIUM', 'Medium'
        LOW = 'LOW', 'Low'

    class Status(models.TextChoices):
        ON_GOING = 'ON_GOING', 'On Going'
        DUE = "DUE", 'Due'
        COMPLETED = 'COMPLETED', 'Completed'
        TO_DO = 'TO_DO', 'To Do'

    name = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    start_date = models.DateField()
    due_date = models.DateField()
    estimated_hours = models.DecimalField(max_digits=7, decimal_places=2, null= True, blank=True)

    priority = models.CharField(
        max_length=10,
        choices=Priority.choices,
        default=Priority.MEDIUM
    )

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.TO_DO
    )

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='projects')
    project_leader= models.ForeignKey(User, on_delete=models.SET_NULL, null=True,related_name='projects')

    def __str__(self):
        return self.name