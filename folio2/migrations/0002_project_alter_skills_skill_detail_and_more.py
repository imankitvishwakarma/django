# Generated by Django 4.1 on 2022-09-16 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("folio2", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("project_img", models.CharField(max_length=50)),
                ("project_p", models.TextField()),
                ("project_btn", models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name="skills", name="skill_detail", field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="skills",
            name="skill_logo",
            field=models.CharField(max_length=50),
        ),
    ]
