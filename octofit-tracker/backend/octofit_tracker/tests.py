from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        self.spiderman = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel)
        self.batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.get(name='Spider-Man').email, 'spiderman@marvel.com')

    def test_team_creation(self):
        self.assertEqual(Team.objects.count(), 2)

    def test_activity_creation(self):
        activity = Activity.objects.create(user=self.spiderman, type='Running', duration=30, date='2025-12-30')
        self.assertEqual(Activity.objects.count(), 1)
        self.assertEqual(activity.type, 'Running')

    def test_leaderboard_creation(self):
        marvel = Team.objects.get(name='Marvel')
        lb = Leaderboard.objects.create(team=marvel, points=100)
        self.assertEqual(Leaderboard.objects.count(), 1)
        self.assertEqual(lb.points, 100)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Hero HIIT', description='HIIT for heroes')
        workout.suggested_for.add(self.spiderman)
        self.assertEqual(Workout.objects.count(), 1)
        self.assertEqual(workout.suggested_for.count(), 1)
