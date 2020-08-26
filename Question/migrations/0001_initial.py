from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentence', models.CharField(max_length=100)),
                ('isPositive', models.SmallIntegerField(default=-1)),
                ('isActivated', models.SmallIntegerField(default=-1)),
                ('isTagged', models.BooleanField(default=0)),
            ],
        ),
    ]
