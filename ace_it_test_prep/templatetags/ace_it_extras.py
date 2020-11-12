from django import template

register = template.Library()

@register.filter
def to_char(value):
    return chr(64+value)

@register.filter()
def to_int(value):
    return int(value)

@register.filter()
def verbal_uppercase(value):
    term_list = value.split(" ")
    if len(term_list) == 1:
        return "".join(term_list).upper()
    else:
        term_list[0] = term_list[0].upper()
        term_list[3] = term_list[3].upper()
        return " ".join(term_list)
        
@register.filter
def get_passage(dict, key):
    return dict[key]['text']
    # return key['text']
