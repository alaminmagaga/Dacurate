# Generated by Django 4.1 on 2022-09-02 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0010_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="profile",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="blog.profile",
            ),
        ),
    ]
