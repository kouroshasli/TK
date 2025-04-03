from django.db import migrations

def add_sample_skills(apps, schema_editor):
    Skill = apps.get_model('main', 'Skill')
    
    # Programming Languages
    Skill.objects.create(
        name='Python',
        category='programming',
        proficiency=95,
        order=1
    )
    Skill.objects.create(
        name='JavaScript',
        category='programming',
        proficiency=85,
        order=2
    )
    Skill.objects.create(
        name='HTML/CSS',
        category='programming',
        proficiency=90,
        order=3
    )
    
    # Frameworks
    Skill.objects.create(
        name='Django',
        category='frameworks',
        proficiency=95,
        order=4
    )
    Skill.objects.create(
        name='Flask',
        category='frameworks',
        proficiency=85,
        order=5
    )
    Skill.objects.create(
        name='Bootstrap',
        category='frameworks',
        proficiency=90,
        order=6
    )
    
    # Databases
    Skill.objects.create(
        name='PostgreSQL',
        category='databases',
        proficiency=90,
        order=7
    )
    Skill.objects.create(
        name='MySQL',
        category='databases',
        proficiency=85,
        order=8
    )
    Skill.objects.create(
        name='MongoDB',
        category='databases',
        proficiency=80,
        order=9
    )
    
    # Tools
    Skill.objects.create(
        name='Git',
        category='tools',
        proficiency=95,
        order=10
    )
    Skill.objects.create(
        name='Docker',
        category='tools',
        proficiency=85,
        order=11
    )
    Skill.objects.create(
        name='AWS',
        category='tools',
        proficiency=80,
        order=12
    )

def remove_sample_skills(apps, schema_editor):
    Skill = apps.get_model('main', 'Skill')
    Skill.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_sample_skills, remove_sample_skills),
    ] 