from datetime import date, datetime, timedelta
from .models import Task

def notifications_processor(request):
    if not request.user.is_authenticated:
        return {}
    
    notifications = []
    today = date.today()
    now = datetime.now()
    
    # 1. Overdue tasks
    overdue_count = Task.objects.filter(user=request.user, due_date__lt=today, completed=False).count()
    if overdue_count > 0:
        notifications.append({
            'title': 'Overdue Tasks',
            'message': f'You have {overdue_count} overdue task(s) to catch up on.',
            'type': 'warning',
            'icon': 'alert-triangle'
        })
        
    # 2. Today's tasks
    today_count = Task.objects.filter(user=request.user, due_date=today, completed=False).count()
    if today_count > 0:
        notifications.append({
            'title': "Today's Agenda",
            'message': f'You have {today_count} task(s) due today. Stay focused!',
            'type': 'info',
            'icon': 'calendar'
        })
    else:
        # Suggest adding tasks if none for today
        if now.hour < 12:
            time_of_day = "morning"
        elif now.hour < 17:
            time_of_day = "afternoon"
        else:
            time_of_day = "evening"
            
        notifications.append({
            'title': f'Good {time_of_day}!',
            'message': "You don't have any tasks scheduled for today. Why not add some?",
            'type': 'success',
            'icon': 'sun'
        })
        
    # 3. Upcoming tasks (next 3 days)
    upcoming_count = Task.objects.filter(
        user=request.user, 
        due_date__gt=today, 
        due_date__lte=today + timedelta(days=3),
        completed=False
    ).count()
    
    if upcoming_count > 0:
        notifications.append({
            'title': 'Upcoming Tasks',
            'message': f'You have {upcoming_count} task(s) due in the next few days.',
            'type': 'primary',
            'icon': 'clock'
        })

    return {
        'notifications': notifications,
        'unread_notifications_count': len(notifications)
    }
