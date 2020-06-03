# # from django.db import models
# # https://medium.com/@ksarthak4ever/django-signals-b20a4152a27b
# from django.db import models
# # to customize authentication and authorization
# from django.contrib.auth.models import User

# # django signals ---applications to get notified when certain events occur
# # Another common use case is when you have extended the Custom Django User by using the Profile strategy through a one-to-one relationship.
# from django.db.models.signals import post_save
#  # When the signal sends its message, each connected receiver gets called. Receivers’ function signatures should match what the signal’s send()
#  #  method uses. You connect a receiver to a signal using the @receiver decorator:
# from django.dispatch import receiver
# # one to one : This is used when one record of a model A is related to exactly one record of another model B. This field can be useful as
# #  a primary key of an object if that object extends another object in some way.
# #  CASCADE means actually telling Django to delete the referenced record
# # .upload_to     define in pillow library
# # This attribute provides a way of setting the upload directory
# class Profile(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='profiles',default='profiles/default.jpg')

#     def __str__(self):
#         return self.user.username