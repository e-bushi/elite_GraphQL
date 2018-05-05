from django.db import models
# Create your models here.


#MODEL OF THE BASIC USER
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField()

    def __str__(self):
        return self.username

#MODEL OF THE TEAMS THAT USERS CREATE
class Squad(models.Model):
    squad_name = models.CharField(max_length=30)

    players = models.ManyToManyField(User)

    def __str__(self):
        return self.squad_name

#------------------------------------------------------------


#MODEL OF LEAGUES THAT ARE CREATED BY ADMINS
class League(models.Model):
    league_name = models.CharField(max_length=30)
    league_description = models.TextField(max_length=128, null=True)
    season_dates = models.DateField(null=True)

    teams = models.ManyToManyField(Squad)

    def __str__(self):
        return self.league_name


#MODEL OF THE AGE GROUPS WITHIN THE LEAGUE
class Groups(models.Model):
    age_group = models.CharField(max_length=9, null=True)
    age_range = models.CharField(max_length=4)

    league = models.ForeignKey(League, on_delete=models.CASCADE)
