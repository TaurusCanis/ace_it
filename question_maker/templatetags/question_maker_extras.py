from django import template

register = template.Library()

@register.filter
def keyvalue(list, key):
    print("list: ", list, " type: ", type(list))
    print("key: ", key)
    try:
        for item in list:
            if key in item:
                return item[key]
    except KeyError:
        return ''

@register.filter
def getattribute(model_object, key):
    return getattr(model_object, key)

@register.filter
def is_list(data):
    print("!!!!!!!@@@@@@@@@########$$$$$$$$%%%%%%%%%%type(data): ", isinstance(data, list))
    return isinstance(data, list)

@register.filter
def to_letter(n):
    return chr(n+64)

@register.filter
def get_random_word(list, index):
    return list[index].word
