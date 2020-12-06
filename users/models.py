from django.db import models
from django.contrib.auth.models import User
from PIL import Image

"""
in the image the reason why i put upload to profile pics is to create a new dir for all the pics to be in 
the default means the any profile that has no pics picture would be default.jpg"""


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default1.jpg', upload_to='profile_pics')

    # this is for the database where i am saving the file in admin so i would be able to understand
    def __str__(self):
        return f'{self.user.username}Profile'

    """
    if i did not resize the image my browser might be running slow
    there is already inbuilt self but i am creating my own save to override the first one
    the reason i am doing it is because i want to change the way an item is being save i my database """

    def save(self, **kwargs):
        super().save()

        # but not that if you want to override the saved image you must install Image from PIL
        # here i am opening the image
        img = Image.open(self.image.path)

        # this is to change the size of the image in the profile pics
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            # this is to save the image i changed to this path
            img.save(self.image.path)
