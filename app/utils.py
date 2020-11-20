import math
from urllib.parse import urlencode

from django.core.paginator import Paginator
from django.template.loader import render_to_string


def set_pagination(request, items, item_numer=10):
    if not items:
        return True, "These is no items"

    params = request.GET
    item_len = len(items)
    page = int(params.get("page")) if "page" in params else 1
    pages_number = math.ceil(item_len / item_numer)

    if page > pages_number or page <= 0:
        return False, "Page not found"

    paginator = Paginator(items, item_numer)
    items = paginator.get_page(page)

    url_params = dict()
    for key in params:
        if key != 'page':
            url_params[key] = params[key]

    page_range = None
    if page in range(1, 7) and pages_number >= 7:
        page_range = [i for i in range(1, 8)]
        page_range += ['...']
    elif page >= 7 and (page + 6) < pages_number:
        page_range = ['...']
        page_range += [i for i in range(page - 3, page + 4)]
        page_range += ['...']
    elif page in range(pages_number - 7, pages_number + 1):
        page_range = ['...']
        page_range += [i for i in range(pages_number - 7, pages_number + 1)]

    context = dict(items=items, page_range=page_range, last=pages_number, url_params=urlencode(url_params))
    items.pagination = render_to_string('app/partial/pagination.html', context)
    return items, {'current_page': page, 'items': item_len, 'items_on_page': item_numer}
