from django.shortcuts import redirect


def get_widget_attrs(**kwargs):
    context = {'class': 'form-control mb-3'}
    if kwargs:
        context.update(kwargs)
    return context


def redirect_to_products_page(request):
    return redirect('list_product')


def get_avg(array):
    try:
        return round(sum(array) / len(array), 2)
    except ZeroDivisionError:
        return 0
