from biblio_apps.models import TypeCategorie
from django import template

register = template.Library()

@register.inclusion_tag("livre_form.html")
def category_subcategory_select(request):
    categories = TypeCategorie.objects.all().order_by('nom_cate')
    return {'categories' : categories}
