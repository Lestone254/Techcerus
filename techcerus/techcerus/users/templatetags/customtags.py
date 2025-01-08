from django import template
register = template.Library()

@register.filter(name='cut')
def cut(con):
    try:
        chunks = con.split(',')
        return chunks
    except:
        return None