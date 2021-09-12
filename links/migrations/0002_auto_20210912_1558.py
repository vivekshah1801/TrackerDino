# Generated by Django 3.0.8 on 2021-09-12 10:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='tracker',
        ),
        migrations.AddField(
            model_name='link',
            name='uuid',
            field=models.CharField(default='abcd-abcd-abcd-abcd', max_length=100, verbose_name='Tracker link uuid'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='link',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Creator of this link'),
        ),
        migrations.AlterField(
            model_name='link',
            name='is_enabled',
            field=models.BooleanField(default=True, verbose_name='Is the link enable?'),
        ),
        migrations.AlterField(
            model_name='link',
            name='notifications_enabled',
            field=models.BooleanField(default=False, verbose_name='Are notifications enabled for this link?'),
        ),
        migrations.AlterField(
            model_name='link',
            name='visit_count',
            field=models.PositiveIntegerField(default=0, verbose_name='Total visit count for this link'),
        ),
    ]
