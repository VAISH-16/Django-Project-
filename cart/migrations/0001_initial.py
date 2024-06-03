# Generated by Django 5.0.4 on 2024-05-21 14:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0002_remove_course_course_category_course_course_picture_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart')),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='courses',
            field=models.ManyToManyField(through='cart.CartItem', to='courses.course'),
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('first_name', models.CharField(default='', max_length=100)),
                ('last_name', models.CharField(default='', max_length=200)),
                ('address_line_1', models.TextField()),
                ('address_line_2', models.TextField()),
                ('city', models.CharField(default='', max_length=100)),
                ('state', models.CharField(default='', max_length=100)),
                ('phoneno', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('order', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cart.orders')),
            ],
        ),
    ]