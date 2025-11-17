from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write('Deleting old data...')
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        self.stdout.write('Creating teams...')
        marvel = Team.objects.create(name='Marvel', description='Marvel Team')
        dc = Team.objects.create(name='DC', description='DC Team')

        self.stdout.write('Creating users...')
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel)
        natasha = User.objects.create(name='Natasha Romanoff', email='natasha@marvel.com', team=marvel)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc)
        diana = User.objects.create(name='Diana Prince', email='diana@dc.com', team=dc)

        self.stdout.write('Creating activities...')
        Activity.objects.create(user=tony, type='Running', duration=30, date='2025-11-17')
        Activity.objects.create(user=steve, type='Cycling', duration=45, date='2025-11-16')
        Activity.objects.create(user=natasha, type='Swimming', duration=60, date='2025-11-15')
        Activity.objects.create(user=bruce, type='Boxing', duration=50, date='2025-11-14')
        Activity.objects.create(user=clark, type='Flying', duration=120, date='2025-11-13')
        Activity.objects.create(user=diana, type='Archery', duration=40, date='2025-11-12')

        self.stdout.write('Creating workouts...')
        w1 = Workout.objects.create(name='Push Ups', description='Upper body workout')
        w2 = Workout.objects.create(name='Cardio Blast', description='High intensity cardio')
        w1.suggested_for.set([tony, steve, bruce])
        w2.suggested_for.set([clark, diana, natasha])

        self.stdout.write('Creating leaderboard...')
        Leaderboard.objects.create(user=tony, score=150)
        Leaderboard.objects.create(user=steve, score=120)
        Leaderboard.objects.create(user=natasha, score=110)
        Leaderboard.objects.create(user=bruce, score=130)
        Leaderboard.objects.create(user=clark, score=140)
        Leaderboard.objects.create(user=diana, score=125)

        self.stdout.write('Ensuring unique index on email field for users...')
        with connection.cursor() as cursor:
            cursor.execute('''db.users.createIndex({ "email": 1 }, { unique: true })''')

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
