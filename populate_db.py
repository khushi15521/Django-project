import os
import django
from datetime import date, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskflow.settings')
django.setup()

from django.contrib.auth.models import User
from tasks.models import Task

def populate():
    print("Populating the database with sample data...")
    
    # Create a demo user if it doesn't exist
    if not User.objects.filter(username='demo').exists():
        user = User.objects.create_user(username='demo', email='demo@example.com', password='password123')
        print(f"Created user: demo / password123")
    else:
        user = User.objects.get(username='demo')
        print("Demo user already exists.")

    # Create sample tasks
    tasks = [
        {
            'title': 'Complete Django Presentation',
            'description': 'Finalize the slides and practice the demo for the TaskFlow project.',
            'category': 'Study',
            'priority': 'High',
            'due_date': date.today(),
            'completed': False,
        },
        {
            'title': 'Submit Internship Report',
            'description': 'Write up the final internship report and submit it to the portal.',
            'category': 'Work',
            'priority': 'Medium',
            'due_date': date.today() + timedelta(days=2),
            'completed': False,
        },
        {
            'title': 'Practice Python',
            'description': 'Solve 3 LeetCode problems using Python.',
            'category': 'Coding',
            'priority': 'Low',
            'due_date': date.today() - timedelta(days=1), # Overdue
            'completed': False,
        },
        {
            'title': 'Complete Data Science Assignment',
            'description': 'Finish the Jupyter notebook for the machine learning model.',
            'category': 'Study',
            'priority': 'High',
            'due_date': date.today() + timedelta(days=5),
            'completed': False,
        },
        {
            'title': 'Buy groceries',
            'description': 'Milk, Eggs, Bread, and Coffee.',
            'category': 'Personal',
            'priority': 'Medium',
            'due_date': date.today(),
            'completed': True,
        }
    ]

    for task_data in tasks:
        Task.objects.get_or_create(
            user=user,
            title=task_data['title'],
            defaults=task_data
        )
    
    print("Database populated successfully!")
    print("\nYou can now login with:")
    print("Username: demo")
    print("Password: password123")

if __name__ == '__main__':
    populate()
