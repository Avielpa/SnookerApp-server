# Generated by Django 5.1.7 on 2025-03-25 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oneFourSeven', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(blank=True, max_length=255, null=True)),
                ('StartDate', models.DateField(blank=True, null=True)),
                ('EndDate', models.DateField(blank=True, null=True)),
                ('Sponsor', models.CharField(blank=True, max_length=255, null=True)),
                ('Season', models.IntegerField(blank=True, null=True)),
                ('Type', models.CharField(blank=True, max_length=50, null=True)),
                ('Num', models.IntegerField(blank=True, null=True)),
                ('Venue', models.CharField(blank=True, max_length=255, null=True)),
                ('City', models.CharField(blank=True, max_length=100, null=True)),
                ('Country', models.CharField(blank=True, max_length=100, null=True)),
                ('Discipline', models.CharField(blank=True, max_length=50, null=True)),
                ('Main', models.IntegerField(blank=True, null=True)),
                ('Sex', models.CharField(blank=True, max_length=10, null=True)),
                ('AgeGroup', models.CharField(blank=True, max_length=10, null=True)),
                ('Url', models.URLField(blank=True, null=True)),
                ('Related', models.CharField(blank=True, max_length=100, null=True)),
                ('Stage', models.CharField(blank=True, max_length=10, null=True)),
                ('ValueType', models.CharField(blank=True, max_length=10, null=True)),
                ('ShortName', models.CharField(blank=True, max_length=100, null=True)),
                ('WorldSnookerId', models.IntegerField(blank=True, null=True)),
                ('RankingType', models.CharField(blank=True, max_length=50, null=True)),
                ('EventPredictionID', models.IntegerField(blank=True, null=True)),
                ('Team', models.BooleanField(default=False)),
                ('Format', models.IntegerField(blank=True, null=True)),
                ('Twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('HashTag', models.CharField(blank=True, max_length=100, null=True)),
                ('ConversionRate', models.FloatField(blank=True, null=True)),
                ('AllRoundsAdded', models.BooleanField(default=False)),
                ('PhotoURLs', models.TextField(blank=True, null=True)),
                ('NumCompetitors', models.IntegerField(blank=True, null=True)),
                ('NumUpcoming', models.IntegerField(blank=True, null=True)),
                ('NumActive', models.IntegerField(blank=True, null=True)),
                ('NumResults', models.IntegerField(blank=True, null=True)),
                ('Note', models.TextField(blank=True, null=True)),
                ('CommonNote', models.TextField(blank=True, null=True)),
                ('DefendingChampion', models.IntegerField(blank=True, null=True)),
                ('PreviousEdition', models.IntegerField(blank=True, null=True)),
                ('Tour', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Type', models.IntegerField(blank=True, null=True)),
                ('FirstName', models.CharField(blank=True, max_length=100, null=True)),
                ('MiddleName', models.CharField(blank=True, max_length=100, null=True)),
                ('LastName', models.CharField(blank=True, max_length=100, null=True)),
                ('TeamName', models.CharField(blank=True, max_length=100, null=True)),
                ('TeamNumber', models.IntegerField(blank=True, null=True)),
                ('TeamSeason', models.IntegerField(blank=True, null=True)),
                ('ShortName', models.CharField(blank=True, max_length=100, null=True)),
                ('Nationality', models.CharField(blank=True, max_length=100, null=True)),
                ('Sex', models.CharField(blank=True, max_length=1, null=True)),
                ('Born', models.DateField(blank=True, null=True)),
                ('SurnameFirst', models.BooleanField(blank=True, null=True)),
                ('FirstSeasonAsPro', models.IntegerField(blank=True, null=True)),
                ('LastSeasonAsPro', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('ID', models.BigIntegerField(primary_key=True, serialize=False)),
                ('Position', models.IntegerField(blank=True, null=True)),
                ('PlayerID', models.IntegerField()),
                ('Season', models.IntegerField(blank=True, null=True)),
                ('Sum', models.IntegerField(blank=True, null=True)),
                ('Type', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Tournament',
        ),
    ]
