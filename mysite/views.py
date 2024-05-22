from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import *
from datetime import datetime
from .forms import *
from django.utils.dateparse import parse_date
from django.db.models import Sum, Count
# Create your views here.

def index(request):
    return render(request, 'index.html')

def cabinet(request):
    return render(request, 'cabinet.html')

def store(request):
    stores = Store.objects.all()
    form = StoreForm()
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store')

    context = {'stores': stores, 'form': form}
    return render(request, 'store.html', context)

def store_edit(request, pk):
    store = get_object_or_404(Store, pk=pk)
    if request.method == 'POST':
        form = StoreForm(request.POST, instance=store)
        if form.is_valid():
            form.save()
            return redirect('store')
    else:
        form = StoreForm(instance=store)

    context = {'form': form, 'store': store}
    return render(request, 'store_edit.html', context)

def delete_store(request, pk):
    store = get_object_or_404(Store, pk=pk)
    store.delete()
    return redirect('store')


def schedule(request):
    stores = Store.objects.all()
    # Получаем текущий месяц
    current_month = datetime.now().month
    # Извлекаем параметры из запроса, если они были отправлены
    selected_store_id = request.POST.get('store')
    selected_month = int(request.POST.get('month', current_month))
    # Фильтрация графика работы по выбранной торговой точке и месяцу
    if selected_store_id:
        schedule_data = Schedule.objects.filter(store_id=selected_store_id, shift_start__month=selected_month)
    else:
        schedule_data = Schedule.objects.none() 
    form = ScheduleForm()
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule')
    context = {
        'schedule_data': schedule_data,
        'stores': stores,
        'selected_store_id': selected_store_id,
        'current_month': current_month,
        'selected_month': selected_month,
        'form': form
    }
    return render(request, 'schedule.html', context)

def products(request):
    query = request.GET.get('q')
    if query:
        product_list = Product.objects.filter(name__icontains=query)
    else:
        product_list = Product.objects.all()

    paginator = Paginator(product_list, 10)  # Показывать по 10 товаров на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    product = Product.objects.all()
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')

    context = {'page_obj': page_obj, 'query': query, 'product': product, 'form': form}
    return render(request, 'products.html', context)

def delete_products(request, pk):
    products = get_object_or_404(Store, pk=pk)
    products.delete()
    return redirect('products')

def employ(request):
    workers = Employee.objects.all()
    form = EmployForm()
    if request.method == 'POST':
        form = EmployForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('workers')
    context = {'workers': workers, 'form': form}
    return render(request, 'workers.html', context)

def employ_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employ') 
    else:
        form = EmployForm(instance=employee)
    return render(request, 'employ_edit.html', {'form': form})

def delete_employ(request, pk):
    workers = get_object_or_404(Employee, pk=pk)
    workers.delete()
    return redirect('workers')

def clients(request):
    leads = Lead.objects.all()
    form = LeadForm()
    if request.method == 'POST':
        form = LeadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('clients')
    context = {'leads': leads, 'form': form}
    return render(request, 'clients.html', context)

def delete_clients(request, pk):
    leads = get_object_or_404(Lead, pk=pk)
    leads.delete()
    return redirect('clients')

def promotions(request):
    proms = Promotion.objects.all()
    form = PromotionForm()
    if request.method == 'POST':
        form = PromotionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('promotions')
    context = {'proms': proms, 'form': form}
    return render(request, 'promotions.html', context)

def schedule(request):
    stores = Store.objects.all()
    form = ScheduleForm()
    if request.method == 'POST':
        form = ScheduleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('schedule')
    context = {'stores': stores, 'form': form}
    return render(request, 'schedule.html', context)

def store_schedule(request, store_id):
    store = get_object_or_404(Store, pk=store_id)
    schedule = Schedule.objects.filter(store=store).order_by('day', 'shift_start')

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date:
        start_date = parse_date(start_date)
        schedule = schedule.filter(day__gte=start_date)

    if end_date:
        end_date = parse_date(end_date)
        schedule = schedule.filter(day__lte=end_date)

    return render(request, 'store_schedule.html', {
        'store': store,
        'schedule': schedule,
        'start_date': start_date,
        'end_date': end_date,
    })

def brand(request):
    brands = Brand.objects.all()
    form = BrandForm()
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('brand')
    context = {'brands': brands, 'form': form}
    return render(request, 'brands.html', context)

def delete_brand(request, pk):
    brands = get_object_or_404(Brand, pk=pk)
    brands.delete()
    return redirect('brand')

def producers(request):
    prods = Producer.objects.all()
    form = ProducerForm()
    if request.method == 'POST':
        form = ProducerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('producers')
    context = {'prods': prods, 'form': form}
    return render(request, 'producers.html', context)

def delete_producers(request, pk):
    prods = get_object_or_404(Producer, pk=pk)
    prods.delete()
    return redirect('producers')

def category(request):
    categories = Category.objects.all()
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('category')
    context = {'categories': categories, 'form': form}
    return render(request, 'category.html', context)

def delete_category(request, pk):
    categories = get_object_or_404(Category, pk=pk)
    categories.delete()
    return redirect('category')

def deal(request):
    deals = Deal.objects.all()
    if request.method == 'POST':
        form = DealForm(request.POST)
        if form.is_valid():
            deal = form.save()
            product = deal.product
            product.quantity += deal.quantity
            product.save()
            return redirect('deal') 
    else:
        form = DealForm()
    return render(request, 'deal.html', {'form': form, 'deals':deals})

def decrease(request):
    decreases = Decrease.objects.all()
    if request.method == 'POST':
        form = DecreaseForm(request.POST)
        if form.is_valid():
            decrease = form.save()
            product = decrease.product
            product.quantity -= decrease.quantity
            product.save()
            return redirect('decrease')
    else:
        form = DecreaseForm()
    return render(request, 'decrease.html', {'form': form, 'decreases': decreases})

def partner(request):
    partners = Partner.objects.all()
    form = PartnerForm()
    if request.method == 'POST':
        form = PartnerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('partner')
    context = {'partners': partners, 'form': form}
    return render(request, 'partner.html', context)

def delete_partner(request, pk):
    partners = get_object_or_404(Partner, pk=pk)
    partners.delete()
    return redirect('partner')

def dashboard(request):
    # Сколько товаров по каждой категории
    category_stats = Category.objects.annotate(
        total_products=Count('product'),
        total_value=Sum('product__deal_price')
    )

    # Сколько записей о прибытии и их общая сумма
    deals_count = Deal.objects.count()
    total_deals_value = Deal.objects.aggregate(Sum('total_price'))['total_price__sum']

    # Сколько записей об убытии и их общая сумма
    decreases_count = Decrease.objects.count()
    total_decreases_value = Decrease.objects.aggregate(Sum('total_price'))['total_price__sum']

    # Сколько сотрудников на каждой точке
    store_employee_stats = Store.objects.annotate(
        employee_count=Count('employee')
    )

    # Дополнительные параметры для дашборда
    total_products_count = Product.objects.count()
    total_stores_count = Store.objects.count()
    total_employees_count = Employee.objects.count()

    # Найти самую прибыльную категорию
    most_profitable_category = Category.objects.annotate(
        total_value=Sum('product__deal_price')
    ).order_by('-total_value').first()

    context = {
        'category_stats': category_stats,
        'deals_count': deals_count,
        'total_deals_value': total_deals_value,
        'decreases_count': decreases_count,
        'total_decreases_value': total_decreases_value,
        'store_employee_stats': store_employee_stats,
        'total_products_count': total_products_count,
        'total_stores_count': total_stores_count,
        'total_employees_count': total_employees_count,
        'most_profitable_category': most_profitable_category,
    }

    return render(request, 'dashboard.html', context)

@login_required
def chat(request):
    messages = Message.objects.order_by('-timestamp')
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
            return redirect('chat')
    else:
        form = MessageForm()
    return render(request, 'chat.html', {'messages': messages, 'form': form})

@login_required
def support(request):
    tickets = Ticket.objects.order_by('-id')
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.save()
            return redirect('support')
    else:
        form = TicketForm()
    return render(request, 'support.html', {'tickets': tickets, 'form': form})