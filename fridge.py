from datetime import date, timedelta
from decimal import Decimal


def add(items, title, amount, expiration_date=None):
    features_str = ('amount', 'expiration_date')
    if expiration_date is not None:
        some_list = str.split(expiration_date, '-')
        date_ = date(int(some_list[0]), int(some_list[1]), int(some_list[2]))
    else:
        some_list = [None]
        date_ = None
    features = (amount, date_)
    features_zip = zip(features_str, features)
    dictionary = {feature[0]: feature[1] for feature in features_zip}
    values = []
    if title not in items.keys():
        list.append(values, dictionary)
        items[title] = values
    else:
        list.append(items[title], dictionary)


def add_by_note(items, note):
    some_list = str.split(note, ' ')
    title = ''
    i = 0
    if len(some_list[-1]) == 10:
        while i != (len(some_list) - 2):
            title = title + some_list[i] + ' '
            i += 1
        title = title.rstrip(' ')
        add(items, title, Decimal(some_list[-2]), some_list[-1])
    else:
        while i != (len(some_list) - 1):
            title = title + some_list[i] + ' '
            i += 1
        title = title.rstrip(' ')
        add(items, title, Decimal(some_list[-1]), None)


def find(items, needle):
    find_list = [item for item in items.keys() if needle.lower() in item.lower()]
    return find_list


def amount(items, needle):
    count = Decimal('0')
    for item in items.keys():
        if needle.lower() in item.lower():
            for i in items[item]:
                count += i['amount']
        else:
            continue
    return count


def expire(items, in_advance_days=0):
    result = []
    date_today = date.today()
    for title, parts in items.items():
        amount = Decimal('0')
        for i in parts:
            if i['expiration_date'] is not None and i['expiration_date'] <= date_today + timedelta(days=in_advance_days):
                amount += i['amount']
        if amount > 0:
            list.append(result, (title, amount))
    return result
