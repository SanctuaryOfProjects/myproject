# Generated by Django 4.0.4 on 2024-05-22 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='Название')),
            ],
            options={
                'verbose_name_plural': 'Бренды',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='Название')),
            ],
            options={
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('position', models.CharField(choices=[('старший менеджер', 'Старший менеджер'), ('менеджер', 'Менеджер'), ('тех. персонал', 'Технический персонал'), ('директор', 'Директор'), ('заведующий складом', 'Заведующий складом')], max_length=50, verbose_name='Должность')),
                ('dismissed', models.BooleanField(default=False, verbose_name='Уволен')),
                ('blacklisted', models.BooleanField(default=False, verbose_name='Черный список')),
            ],
            options={
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('status', models.CharField(choices=[('новый', 'Новый'), ('обработанный', 'Обработанный'), ('отклоненный', 'Отклоненный')], max_length=100, verbose_name='Статус')),
            ],
            options={
                'verbose_name_plural': 'Лиды',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('description', models.TextField(verbose_name='Описание')),
                ('blacklisted', models.BooleanField(default=False, verbose_name='В черном списке')),
            ],
            options={
                'verbose_name_plural': 'Партнеры',
            },
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='Название')),
                ('contract_date', models.DateField(verbose_name='Дата заключения контракта')),
                ('documentation', models.FileField(upload_to='supplier_docs/', verbose_name='Документация')),
                ('blacklisted', models.BooleanField(default=False, verbose_name='Черный список')),
            ],
            options={
                'verbose_name_plural': 'Поставщики',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
            ],
            options={
                'verbose_name_plural': 'Торговые точки',
            },
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Начало')),
                ('end_date', models.DateField(verbose_name='Конец')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.employee', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name_plural': 'Стажировка',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255, verbose_name='Тема')),
                ('description', models.TextField(verbose_name='Описание')),
                ('status', models.CharField(choices=[('в работе', 'В работе'), ('обработан', 'Обработан')], max_length=100, verbose_name='Статус')),
                ('priority', models.CharField(choices=[('низкий', 'Низкий'), ('средний', 'Средний'), ('срочный', 'Срочный')], max_length=100, verbose_name='Приоритет')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.employee', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name_plural': 'Служба поддержки',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(blank=True, verbose_name='Рабочий день')),
                ('shift_start', models.TimeField(blank=True, verbose_name='Начало смены')),
                ('shift_end', models.TimeField(blank=True, verbose_name='Конец смены')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.employee', verbose_name='Сотрудник')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.store', verbose_name='Торговая точка')),
            ],
            options={
                'verbose_name_plural': 'График работы',
            },
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='promotions/', verbose_name='Изображение')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('start_date', models.DateField(verbose_name='Дата начала')),
                ('end_date', models.DateField(verbose_name='Дата окончания')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.store', verbose_name='Торговая точка')),
            ],
            options={
                'verbose_name_plural': 'Акции',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('image', models.FileField(blank=True, upload_to='products/', verbose_name='Изображение')),
                ('description', models.TextField(verbose_name='Описание')),
                ('deal_price', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Оптовая цена')),
                ('client_price', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Цена для клиента')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.brand', verbose_name='Бренд')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.category', verbose_name='Категория')),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.producer', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Временная метка')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to='mysite.employee', verbose_name='Получатель')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to='mysite.employee', verbose_name='Отправитель')),
            ],
            options={
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Менеджер',
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.store', verbose_name='Торговая точка'),
        ),
        migrations.CreateModel(
            name='Decrease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('total_price', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Общая цена')),
                ('date', models.DateField(verbose_name='Дата')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.partner', verbose_name='Клиент')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.product', verbose_name='Товар')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.store', verbose_name='Торговая точка')),
            ],
            options={
                'verbose_name_plural': 'Убытие',
            },
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('total_price', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Общая цена')),
                ('date', models.DateField(verbose_name='Дата')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.producer', verbose_name='Поставщик')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.product', verbose_name='Товар')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.store', verbose_name='Торговая точка')),
            ],
            options={
                'verbose_name_plural': 'Прибытие',
            },
        ),
    ]
