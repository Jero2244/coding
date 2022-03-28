#! /usr/bin/python3

import requests, bs4

def getElementPrice(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('''html body main#root-app div.ui-vip-core div.ui-pdp-container.ui-pdp-container--pdp div.ui-pdp-container__row.ui-pdp-container__row--reverse.ui-pdp--relative.pb-40 div.ui-pdp-container__col.col-1.ui-pdp-container--column-right.mt-16.pr-16.ui-pdp--relative div.ui-pdp--sticky-wrapper.ui-pdp--sticky-wrapper-right div.ui-pdp-container__row.ui-pdp-component-list.pr-16.pl-16 div.ui-pdp-container__col.col-2.ui-vip-core-container--short-description.ui-vip-core-container--column__right div.ui-pdp-container__row.ui-pdp-container__row--price div.ui-pdp-price.mt-16.ui-pdp-price--size-large div.ui-pdp-price__second-line span.andes-money-amount.ui-pdp-price__part.andes-money-amount--cents-superscript span.andes-money-amount__fraction''')
    return elems[0].text

def getMervalValuation():
    res = requests.get('https://www.expansion.com/mercados/cotizaciones/indices/merval_I.MV.html')
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('html body#invest.Mercados.Indices main#js_526684c061fd3df14c8b4571.main.section.js_navContinua.espana section.row-layout div.container div.fix-c.content-items.desktop div.container ul.content-items.flex-a li.content-item div.content-item section.row-layout div.container article#bloque_apertura_ibex.bloque.apertura_mercados div#datos_principales_indice.valores_principales_ficha.sube ul li.cotizacion')
    return elems[0].text

# url = input('Please enter an URL: ')
# price = getElementPrice(url)
# print(price)

val = getMervalValuation()
print(val)
