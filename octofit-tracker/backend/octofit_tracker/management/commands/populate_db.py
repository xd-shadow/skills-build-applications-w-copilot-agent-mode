from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Populate users
        user1 = User.objects.create(_id=ObjectId(), username="john_doe", email="john@example.com", password="password123")
        user2 = User.objects.create(_id=ObjectId(), username="jane_doe", email="jane@example.com", password="password456")

        # Populate teams
        team1 = Team.objects.create(_id=ObjectId(), name="Team Alpha")
        team1.members.add(user1, user2)

        # Populate activities
        Activity.objects.create(_id=ObjectId(), user=user1, activity_type="Running", duration=timedelta(minutes=30))
        Activity.objects.create(_id=ObjectId(), user=user2, activity_type="Cycling", duration=timedelta(minutes=45))

        # Populate leaderboard
        Leaderboard.objects.create(_id=ObjectId(), user=user1, score=100)
        Leaderboard.objects.create(_id=ObjectId(), user=user2, score=150)

        # Populate workouts
        Workout.objects.create(_id=ObjectId(), name="Push-ups", description="Do 20 push-ups")
        Workout.objects.create(_id=ObjectId(), name="Sit-ups", description="Do 30 sit-ups")

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
