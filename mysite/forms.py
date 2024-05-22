from django import forms
from .models import *

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите адрес'}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'producer', 'brand', 'category', 'description', 'deal_price', 'client_price', 'quantity']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите наименование'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file', 'placeholder': 'Добавьте файл'}),
            'producer': forms.Select(attrs={'class': 'form-select'}),
            'brand': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Введите описание'}),
            'deal_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите оптовую цену'}),
            'client_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите цену для клиента'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите количество'}),
        }

class EmployForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'store', 'email', 'phone', 'position', 'dismissed', 'blacklisted']
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ФИО'
            }),
            'store': forms.Select(attrs={
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Email'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите телефон'
            }),
            'position': forms.Select(attrs={
                'class': 'form-control'
            }),
            'dismissed': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'blacklisted': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }

        labels = {
            'name': 'ФИО',
            'store': 'Торговая точка',
            'email': 'Email',
            'phone': 'Телефон',
            'position': 'Должность',
            'dismissed': 'Уволен',
            'blacklisted': 'Черный список'
        }


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'email', 'phone', 'status']
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ФИО'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Email'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите телефон'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
        }

        labels = {
            'name': 'ФИО',
            'email': 'Email',
            'phone': 'Телефон',
            'status': 'Статус'
        }

class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = ['store', 'image', 'name', 'description', 'start_date', 'end_date']
        
        widgets = {
            'store': forms.Select(attrs={
                'class': 'form-control'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control-file'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
            'start_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'end_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }

        labels = {
            'store': 'Торговая точка',
            'image': 'Изображение',
            'name': 'Название',
            'description': 'Описание',
            'start_date': 'Дата начала',
            'end_date': 'Дата окончания',
        }

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['store', 'employee', 'day', 'shift_start', 'shift_end', 'comment']
        
        widgets = {
            'store': forms.Select(attrs={'class': 'form-control'}),
            'employee': forms.Select(attrs={'class': 'form-control'}),
            'day': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'shift_start': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'shift_end': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
        }

        labels = {
            'store': 'Торговая точка',
            'employee': 'Сотрудник',
            'day': 'Рабочий день',
            'shift_start': 'Начало смены',
            'shift_end': 'Конец смены',
            'comment': 'Комментарий',
        }

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']
        labels = {
            'name': 'Название',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название бренда',
            }),
        }

class ProducerForm(forms.ModelForm):
    class Meta:
        model = Producer
        fields = ['name', 'contract_date', 'documentation', 'blacklisted']
        labels = {
            'name': 'Название',
            'contract_date': 'Дата заключения контракта',
            'documentation': 'Документация',
            'blacklisted': 'Черный список',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название поставщика',
            }),
            'contract_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'documentation': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
            'blacklisted': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name': 'Название',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название категории',
            }),
        }

class DealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = ['store', 'product', 'agent', 'quantity', 'date']
        labels = {
            'store': 'Торговая точка',
            'product': 'Товар',
            'agent': 'Поставщик',
            'quantity': 'Количество',
            'date': 'Дата',
        }
        widgets = {
            'store': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'agent': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите количество'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.total_price = instance.product.deal_price * instance.quantity
        if commit:
            instance.save()
        return instance

class DecreaseForm(forms.ModelForm):
    class Meta:
        model = Decrease
        fields = ['store', 'product', 'agent', 'quantity', 'date']
        labels = {
            'store': 'Торговая точка',
            'product': 'Товар',
            'agent': 'Клиент',
            'quantity': 'Количество',
            'date': 'Дата',
        }
        widgets = {
            'store': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'agent': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите количество'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.total_price = instance.product.client_price * instance.quantity
        if commit:
            instance.save()
        return instance

class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ['name', 'email', 'phone', 'description', 'blacklisted']
        labels = {
            'name': 'ФИО',
            'email': 'Email',
            'phone': 'Телефон',
            'description': 'Описание',
            'blacklisted': 'В черном списке',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ФИО'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите телефон'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание'}),
            'blacklisted': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['sender', 'recipient', 'content']
        widgets = {
            'sender': forms.Select(attrs={'class': 'form-control'}),
            'recipient': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['sender'].queryset = Employee.objects.all()
        self.fields['recipient'].queryset = Employee.objects.all()

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['client', 'subject', 'description', 'status', 'priority']
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
        self.fields['client'].queryset = Employee.objects.all()