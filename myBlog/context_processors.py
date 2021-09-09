from .models import Category


def get_category_list(request):
    category_list = Category.objects.all()
    return {
        'category_list': category_list,
    }
