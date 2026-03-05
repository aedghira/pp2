
import json


x = {
  'products': [
    {
      'name': 'Натрия хлорид 0,9%, 200 мл, фл',
      "total_price": 308.00
    },
    {
      'name': 'Борный спирт 3%, 20 мл, фл.',
      "total_price": 51.00
    },
    {
      'name': 'Шприц 2 мл, 3-х комп. (Bioject)',
      "total_price": 32.00
    },
    {
      'name': 'Система для инфузии Vogt Medical',
      "total_price": 120.00
    },
    {
      'name': 'Шприц 5 мл, 3-х комп.',
      "total_price": 310.00
    },
    {
      'name': 'AURA Ватные диски №150',
      "total_price": 461.00
    },
    {
      'name': 'Чистая линия скраб мягкий 50 мл',
      "total_price": 381.00
    },
    {
      "name": 'Чистая линия скраб очищающий абрикос 50 мл',
      "total_price": 386.00
    },
    {
      'name': 'Чистая линия скраб мягкий 50 мл',
      "total_price": 381.00
    },
    {
      'name': 'Nivea шампунь 3в1 мужской 400 мл',
      "total_price": 414.00
    },
    {
      'name': 'Pro Series Шампунь яркий цвет 500мл',
      "total_price": 841.00
    },
    {
      'name': 'Pro Series бальзам-ополаскиватель для длительного ухода за окрашенными волосами Яркий цвет 500мл',
      "total_price": 841.00
    },
    {
      'name': 'Clear шампунь Актив спорт 2в1 мужской 400 мл',
      "total_price": 1200.00
    },
    {
      'name': 'Bio World (HYDRO THERAPY) Мицеллярная вода 5в1, 445мл',
      "total_price": 1152.00
    },
    {
      'name': 'Bio World (HYDRO THERAPY) Гель-мусс для умывания с гиалуроновой кислотой, 250мл',
      "total_price": 1152.00
    },
    {
      'name': '[RX]-Натрия хлорид 0,9%, 100 мл, фл.',
      "total_price": 168.00
    },
    {
      'name': '[RX]-Дисоль р-р 400 мл, фл.',
      "total_price": 163.00
    },
    {
      'name': 'Тагансорбент с ионом серебра №30, пор.',
      "total_price": 1526.00
    },
    {
      'name': '[RX]-Церукал 2%, 2 мл, №10, амп.',
      "total_price": 792.00
    },
    {
      'name': '[RX]-Андазол 200 мг, №40, табл.',
      'total_price': 7330.00
    }
  ],
  'totally': {
    'total': 18009.00
  },
  'payment_method': 'Банковская карта',
  'datetime': '18.04.2019 11:13:58',
}

y = json.dumps(x)
print(y)
