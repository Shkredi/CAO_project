import requests
from lxml import html
from convertor import *

URL = 'https://theskylive.com/'


def get_tables():
    """Return all tables as list of "Element table' from the site"""
    req = requests.get(URL)

    tree = html.fromstring(req.text)
    tables = tree.xpath('//table')
    return tables


def encode_table(table):
    """Return list of lists that represent table"""
    encoded_table = []
    for line in table:
        l = []
        for cell in line.text_content().split('\n'):
            text = cell.strip()
            if text:
                l.append(text)
        encoded_table.append(l)

    return encoded_table


def process_table(table):
    """Get all necessary information from table"""
    titles = table[0]
    typ = titles[0]
    r_a_index = titles.index('R.A.')
    decl_index = titles.index('Decl.')
    con_index = titles.index('ConstellationConst')
    if 'MagnitudeMag' in titles:
        mag_index = titles.index('MagnitudeMag')
    else:
        mag_index = titles.index('Magnitude (Estimated)Mag Pred')

    objects = []
    for l in range(1, len(table)):
        line = table[l]
        name = line[0]
        r_a = str_to_hours(line[r_a_index])
        decl = str_to_degree(line[decl_index])
        mag = float(line[mag_index])
        con = line[con_index]
        obj = [typ, name, r_a, decl, mag, con]
        objects.append(obj)

    return objects


def get_all():
    """Get all necessary information from all tables"""
    tables = get_tables()
    special = encode_table(tables[0])
    special[0].insert(0, '')
    sun, moon = process_table(special)
    objects = [sun, moon]
    for i in range(1, 4):
        table = encode_table(tables[i])
        obj = process_table(table)
        objects.extend(obj)

    return objects


if __name__ == '__main__':
    s, m, o = get_all()
    print(s)
    print(m)
    print('\n'.join([str(l) for l in o]))
