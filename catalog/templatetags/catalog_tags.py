from django import template
from catalog.helpers import can_view_details as check_can_view_details

register = template.Library()


@register.simple_tag
def can_view_details(user):
    """
    Kullanıcının detayları ve indirme linklerini görme yetkisi olup olmadığını denetler.
    Kullanım: {% can_view_details request.user as user_can_view %}
    """
    return check_can_view_details(user)


@register.filter
def parse_lines(value):
    """
    Çok satırlı metinleri satır satır bölüp temizler (adımlar ve belgeler için).
    """
    if not value:
        return []
    lines = []
    for line in value.splitlines():
        line = line.strip()
        if line:
            if line.startswith('•') or line.startswith('-') or line.startswith('*'):
                line = line[1:].strip()
            lines.append(line)
    return lines
