from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        user = User.objects.create(name='Tony Stark', email='tony@stark.com', team=team)
        self.assertEqual(user.email, 'tony@stark.com')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='DC', description='DC Team')
        self.assertEqual(team.name, 'DC')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        user = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=team)
        activity = Activity.objects.create(user=user, type='Running', duration=30, date='2025-11-17')
        self.assertEqual(activity.type, 'Running')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Push Ups', description='Upper body workout')
        self.assertEqual(workout.name, 'Push Ups')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        user = User.objects.create(name='Natasha Romanoff', email='natasha@marvel.com', team=team)
        leaderboard = Leaderboard.objects.create(user=user, score=100)
        self.assertEqual(leaderboard.score, 100)
