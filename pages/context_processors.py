from . import models

def get_pages(request):

    pages = models.Page.objects.filter(visible=True).order_by('order').values_list('id', 'title', 'slug')

    return {
        'pages': pages
    }