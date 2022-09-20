from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
  # Boolean fiels to select the type of account
   is_admin = models.BooleanField(default=False)
   is_staff= models.BooleanField(default=False)

   @property
   def token(self):
      """
      Allows us to get a user's token by calling `user.token` instead of
      `user.generate_jwt_token().

      The `@property` decorator above makes this possible. `token` is called
      a "dynamic property".
      """
      return self._generate_jwt_token()


   def _generate_jwt_token(self):
     """
      Generates a JSON Web Token that stores this user's ID and has an expiry
      date set to 60 days into the future.
      """
     dt=datetime.now()+timedelta(days=60)

     token=jwt.encode({
       'id': self.pk,
       'exp':int(dt.strftime('%s'))
     },settings.SECRET_KEY,algorithm='HS256')

     return token.decode('utf-8')









