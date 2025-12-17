# Generated migration for IDOR Lab

from django.db import migrations, models


def seed_idor_users(apps, schema_editor):
    """Seed initial users for the IDOR lab"""
    IDOR_User = apps.get_model('introduction', 'IDOR_User')
    
    users_data = [
        {
            'username': 'admin',
            'email': 'admin@pygoat-corp.com',
            'ssn': '000-00-0001',
            'salary': 500000,
            'role': 'ceo'
        },
        {
            'username': 'john',
            'email': 'john.doe@pygoat-corp.com',
            'ssn': '123-45-6789',
            'salary': 75000,
            'role': 'employee'
        },
        {
            'username': 'sarah',
            'email': 'sarah.smith@pygoat-corp.com',
            'ssn': '987-65-4321',
            'salary': 95000,
            'role': 'manager'
        },
        {
            'username': 'mike',
            'email': 'mike.johnson@pygoat-corp.com',
            'ssn': '456-78-9012',
            'salary': 68000,
            'role': 'employee'
        },
        {
            'username': 'lisa',
            'email': 'lisa.williams@pygoat-corp.com',
            'ssn': '789-01-2345',
            'salary': 120000,
            'role': 'manager'
        },
    ]
    
    for user_data in users_data:
        IDOR_User.objects.create(**user_data)


def reverse_seed(apps, schema_editor):
    """Remove seeded users"""
    IDOR_User = apps.get_model('introduction', 'IDOR_User')
    IDOR_User.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('introduction', '0021_csrf_user_tbl'),
    ]

    operations = [
        migrations.CreateModel(
            name='IDOR_User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200, unique=True)),
                ('email', models.CharField(max_length=200)),
                ('ssn', models.CharField(max_length=11)),
                ('salary', models.IntegerField(default=0)),
                ('role', models.CharField(default='employee', max_length=50)),
            ],
        ),
        migrations.RunPython(seed_idor_users, reverse_seed),
    ]


