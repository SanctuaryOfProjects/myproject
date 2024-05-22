from django.db import models
from django.contrib.auth.models import User

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name_plural = "Менеджер"

# Модель для торговых точек
class Store(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Торговые точки"

class Employee(models.Model):
    EMPLOYEE_TYPES = [
        ('старший менеджер', 'Старший менеджер'),
        ('менеджер', 'Менеджер'),
        ('тех. персонал', 'Технический персонал'),
        ('директор', 'Директор'),
        ('заведующий складом', 'Заведующий складом'),
    ]

    name = models.CharField(max_length=100, verbose_name='ФИО')
    store = models.ForeignKey('Store', on_delete=models.CASCADE, verbose_name='Торговая точка')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    position = models.CharField(max_length=50, choices=EMPLOYEE_TYPES, verbose_name='Должность')
    dismissed = models.BooleanField(default=False, verbose_name='Уволен')
    blacklisted = models.BooleanField(default=False, verbose_name='Черный список')
    
    def __str__(self):
        return f'{self.name} - {self.position}'
    
    class Meta:
        verbose_name_plural = "Сотрудники"

# Модель для обучения сотрудников
class Training(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Сотрудник')
    start_date = models.DateField(verbose_name='Начало')
    end_date = models.DateField(verbose_name='Конец')

    def __str__(self):
        return self.employee
    class Meta:
        verbose_name_plural = "Стажировка"

# Модель для графика работы сотрудников
class Schedule(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name="Торговая точка")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Сотрудник')
    day = models.DateField(verbose_name='Рабочий день', blank=True)
    shift_start = models.TimeField(verbose_name='Начало смены', blank=True)
    shift_end = models.TimeField(verbose_name='Конец смены', blank=True)
    comment = models.TextField(verbose_name='Комментарий')

    def __str__(self):
        return f'{self.employee} - {self.day}'
    class Meta:
        verbose_name_plural = "График работы"

# Модель для клиентов-лидов
class Lead(models.Model):
    LEAD_STATUSES = [
        ('новый', 'Новый'),
        ('обработанный', 'Обработанный'),
        ('отклоненный', 'Отклоненный'),
    ]

    name = models.CharField(max_length=100, verbose_name='ФИО')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    status = models.CharField(max_length=100, choices=LEAD_STATUSES, verbose_name='Статус')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Лиды"

# Модель для партнеров
class Partner(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    description = models.TextField(verbose_name='Описание')
    blacklisted = models.BooleanField(default=False, verbose_name='В черном списке')
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Партнеры"

# Модель для акций
class Promotion(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name='Торговая точка')
    image = models.FileField(upload_to='promotions/', verbose_name='Изображение')
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(verbose_name='Дата окончания')

    def __str__(self):
        return f'{self.name} - {self.store}'
    class Meta:
        verbose_name_plural = "Акции"

# Модель для поставщиков
class Producer(models.Model):
    name = models.CharField(max_length=75, verbose_name='Название')
    contract_date = models.DateField(verbose_name='Дата заключения контракта')
    documentation = models.FileField(upload_to='supplier_docs/', verbose_name='Документация')
    blacklisted = models.BooleanField(default=False, verbose_name='Черный список')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Поставщики"

# Модель для бренда товара

class Brand(models.Model):
    name = models.CharField(max_length=75, verbose_name='Название')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Бренды"

#Модель для категории товара
class Category(models.Model):
    name = models.CharField(max_length=75, verbose_name='Название')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Категории"

# Модель для товаров
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    image = models.FileField(upload_to='products/', verbose_name='Изображение', blank=True)
    producer = models.ForeignKey('Producer', on_delete=models.CASCADE, verbose_name='Поставщик')
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, verbose_name='Бренд')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория') 
    description = models.TextField(verbose_name='Описание')
    deal_price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Оптовая цена')
    client_price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Цена для клиента')
    quantity = models.IntegerField(verbose_name='Количество')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Товары"

# Модель для прибытия
class Deal(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name='Торговая точка')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Товар')
    agent = models.ForeignKey('Producer', on_delete=models.CASCADE, verbose_name='Поставщик')
    quantity = models.IntegerField(verbose_name='Количество')
    total_price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Общая цена')
    date = models.DateField(verbose_name='Дата')

    def __str__(self):
        return f'Сделка №: {self.id}'
    class Meta:
        verbose_name_plural = "Прибытие"

# Модель для убытия
class Decrease(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name='Торговая точка')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Товар')
    agent = models.ForeignKey('Partner', on_delete=models.CASCADE, verbose_name='Клиент')
    quantity = models.IntegerField(verbose_name='Количество')
    total_price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Общая цена')
    date = models.DateField(verbose_name='Дата')

    def __str__(self):
        return f'Сделка №: {self.id}'
    class Meta:
        verbose_name_plural = "Убытие"

# Модель для сообщений в чате
class Message(models.Model):
    sender = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='sent_messages', verbose_name='Отправитель')
    recipient = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='received_messages', verbose_name='Получатель')
    content = models.TextField(verbose_name='Содержание')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Временная метка')

    def __str__(self):
        return f'{self.sender} - {self.recipient}'
    class Meta:
        verbose_name_plural = "Сообщения"

# Модель для запросов в службу поддержки
class Ticket(models.Model):
    STATUS_CHOICES = [
    ('в работе', 'В работе'),
    ('обработан', 'Обработан'),
]

    PRIORITY_CHOICES = [
    ('низкий', 'Низкий'),
    ('средний', 'Средний'),
    ('срочный', 'Срочный'),
]
    client = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Сотрудник')
    subject = models.CharField(max_length=255, verbose_name='Тема')
    description = models.TextField(verbose_name='Описание')
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, verbose_name='Статус')
    priority = models.CharField(max_length=100, choices=PRIORITY_CHOICES, verbose_name='Приоритет')

    def __str__(self):
        return f'{self.client} - {self.subject}'

    class Meta:
        verbose_name_plural = "Служба поддержки"
