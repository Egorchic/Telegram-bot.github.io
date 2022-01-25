from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import datab
import time
import random

user_agents = [
        'hello_world', 'my_agent', 'best_program',
        'egor_ka', 'ded_insaid',
        'super_tupoi', 'pyton_S',
        'anal_inator', 'dota',
        'parser'
]

list_of_links = {'Суши': "https://yandex.ru/maps/213/moscow/search/Где%20поесть/?filter=auto_generated_food_filter%3Aff0c%3Balternate_vertical%3ARequestWindow&ll=37.617508%2C55.753947&sctx=ZAAAAAgBEAAaKAoSCTIdOj3vzkJAEfGxYIfW4EtAEhIJnZ7k%2F29bxj8RGJooOT78rT8iBgABAgMEBSgKOABAt54BSAFiK3JlbGV2X3JhbmtpbmdfbXNlX2Zvcm11bGE9bXNlX2ZtbDgyODgwMl9leHBiJnJlbGV2X2lycmVsX2ZpbHRlcj0xLjA6aXJyZWxfZm1sODI1OTM1YiRyZWFycj1zY2hlbWVfTG9jYWwvR2VvL1JlbGV2R2VvRml4PTFiNHJlYXJyPXNjaGVtZV9Mb2NhbC9HZW8vUG9zdGZpbHRlci9JcnJlbFRocmVzaG9sZD0wLjZqAnJ1ggEfYXV0b19nZW5lcmF0ZWRfZm9vZF9maWx0ZXI6ZmYzMJ0BzcxMPaABAKgBAL0BsR1Qc8IBiAGGpe2igwHi1umDBsnql8QG4Kn1uQTd0MT7mAL8n9fGBsnSiO7oA7fs2ZcGtO7n7QOIsYWlBPKtm%2FED68X66wOI%2BaHUqAHatNCa6ATZgpWhBpPd3usDp6%2FJ%2FtMF7%2BXK4LsD7Zic0a8EmtCHiPgGgeuu3Z8F%2F%2Fby7bAEh8O7jgT%2B05nbBPSsqe8D6gEA8gEA%2BAEAggIT0JPQtNC1INC%2F0L7QtdGB0YLRjIoCXDE4NDEwNjM5MCQxODQxMDYzODYkMTg0MTA2Mzk2JDE4NDEwNjM5MiQxODQxMDYzODQkMTg0MTA2Mzk0JDM1MTkzMTE0OTM3JDEzODc3ODg5OTYkNzcwOTMxNTM3kgIA&sll=37.617508%2C55.753947&sspn=0.174665%2C0.058569&z=14",
                 'Бизнес-ланчи': "https://yandex.ru/maps/213/moscow/search/Где%20поесть/?filter=auto_generated_food_filter%3Aff1c%3Balternate_vertical%3ARequestWindow&ll=37.616676%2C55.756547&sctx=ZAAAAAgBEAAaKAoSCYnQCDauz0JAEabtX1lp4EtAEhIJAAAAAHBbBkARwDs%2B%2BwD97T8iBgABAgMEBSgKOABA1QFIAWIrcmVsZXZfcmFua2luZ19tc2VfZm9ybXVsYT1tc2VfZm1sODI4ODAyX2V4cGIkcmVhcnI9c2NoZW1lX0xvY2FsL0dlby9SZWxldkdlb0ZpeD0xagJydZ0BzcxMPaABAKgBAL0Ba4J7%2BcIBiAHGxMjzqwH%2BqeCXBKuDtIIFweCf37oBp7ek6%2F4BgMyu%2FwOlmfuZigee1JXiuwXn7IKGBMa00IsMnPzmpQX1mKyGgAPBgryrqwKJmavEBv6n2bsEw5%2FnjwTKh5bGIMaRkboEhrbO1ASJhNC%2FBKSbrNT8Ar7696KyBvyAvs8F6vL3hP4CmISTzrAF6gEA8gEA%2BAEAggIT0JPQtNC1INC%2F0L7QtdGB0YLRjIoCXDE4NDEwNjM5MCQxODQxMDYzODYkMTg0MTA2Mzk2JDE4NDEwNjM5MiQxODQxMDYzODQkMTg0MTA2Mzk0JDM1MTkzMTE0OTM3JDEzODc3ODg5OTYkNzcwOTMxNTM3kgIA&sll=37.616676%2C55.756547&sspn=0.174665%2C0.058565&z=12.57",
                 'Вегетрианские блюда': "https://yandex.ru/maps/213/moscow/search/Где%20поесть/?filter=auto_generated_food_filter%3Aff54%3Balternate_vertical%3ARequestWindow&ll=37.616676%2C55.756547&sctx=ZAAAAAgBEAAaKAoSCYnQCDauz0JAEabtX1lp4EtAEhIJtfoGAHBbBkARHdc4%2BwD97T8iBgABAgMEBSgKOABAt54BSAFiK3JlbGV2X3JhbmtpbmdfbXNlX2Zvcm11bGE9bXNlX2ZtbDgyODgwMl9leHBiJHJlYXJyPXNjaGVtZV9Mb2NhbC9HZW8vUmVsZXZHZW9GaXg9MWoCcnWCAR9hdXRvX2dlbmVyYXRlZF9mb29kX2ZpbHRlcjpmZjFjnQHNzEw9oAEAqAEAvQEGxHBxwgGJAcbEyPOrAf6p4JcEi9GG%2BASxk8fM6APquJPSHcnDzYeFBc7F4LEgwMPL2LwDntSV4rsFqNDEjs0F3cb7m3j%2Bp9m7BNKxm%2FoDxrybpQaGts7UBMGCvKurApH78NHqAfyAvs8F%2Bv6NmooB68mDtAS3jvO0qgLcjZua7wGtme3lA4Cd%2BY4Pvvr3orIG6gEA8gEA%2BAEAggIT0JPQtNC1INC%2F0L7QtdGB0YLRjIoCXDE4NDEwNjM5MCQxODQxMDYzODYkMTg0MTA2Mzk2JDE4NDEwNjM5MiQxODQxMDYzODQkMTg0MTA2Mzk0JDM1MTkzMTE0OTM3JDEzODc3ODg5OTYkNzcwOTMxNTM3kgIA&sll=37.616676%2C55.756547&sspn=0.174607%2C0.156237&z=12.57",
                 'Десерты': "https://yandex.ru/maps/213/moscow/search/Где%20поесть/?filter=auto_generated_food_filter%3Aff50%3Balternate_vertical%3ARequestWindow&ll=37.616676%2C55.756547&sctx=ZAAAAAgBEAAaKAoSCYnQCDauz0JAEabtX1lp4EtAEhIJtfoGAHBbBkARHdc4%2BwD97T8iBgABAgMEBSgKOABAt54BSAFiK3JlbGV2X3JhbmtpbmdfbXNlX2Zvcm11bGE9bXNlX2ZtbDgyODgwMl9leHBiJHJlYXJyPXNjaGVtZV9Mb2NhbC9HZW8vUmVsZXZHZW9GaXg9MWoCcnWCAR9hdXRvX2dlbmVyYXRlZF9mb29kX2ZpbHRlcjpmZjU0nQHNzEw9oAEAqAEAvQHFK1hVwgGKAcbEyPOrAf6p4JcEi97k358CsZPHzOgDzM68igTGtNCLDK6EpbsEhvGpjN0E9vrBsJoCif%2F58ZsEiZmrxAbSsZv6A8aPpMRBj%2B2jxI0HiNrJ9V%2F8gL7PBfPS%2B%2BCoBq24gO4D4brss%2B0DporQ3QPRnOPcqQGOvp7LhwfF4dOH7AW0u%2BL6A8vmupb6A%2BoBAPIBAPgBAIICE9CT0LTQtSDQv9C%2B0LXRgdGC0YyKAlwxODQxMDYzOTAkMTg0MTA2Mzg2JDE4NDEwNjM5NiQxODQxMDYzOTIkMTg0MTA2Mzg0JDE4NDEwNjM5NCQzNTE5MzExNDkzNyQxMzg3Nzg4OTk2JDc3MDkzMTUzN5ICAA%3D%3D&sll=37.616676%2C55.756547&sspn=0.174607%2C0.156237&z=12.57",
                 'Кофейня': "https://yandex.ru/maps/213/moscow/search/Где%20поесть/?filter=auto_generated_food_filter%3Aff04%3Balternate_vertical%3ARequestWindow&ll=37.616676%2C55.756547&sctx=ZAAAAAgBEAAaKAoSCYnQCDauz0JAEabtX1lp4EtAEhIJtfoGAHBbBkARHdc4%2BwD97T8iBgABAgMEBSgKOABAt54BSAFiK3JlbGV2X3JhbmtpbmdfbXNlX2Zvcm11bGE9bXNlX2ZtbDgyODgwMl9leHBiJHJlYXJyPXNjaGVtZV9Mb2NhbC9HZW8vUmVsZXZHZW9GaXg9MWoCcnWCAR9hdXRvX2dlbmVyYXRlZF9mb29kX2ZpbHRlcjpmZjUwnQHNzEw9oAEAqAEAvQFj9pqhwgGQAen%2BsJ2iBcvh%2BaCGAqe3pOv%2BAcvUga2RBcnDzYeFBZnRjaYFlsSIkGjSpZC0pwKT7sqldtmeht7yBf6n2bsE9begy7cC57CiqPIB68mDtASzgJXDxgLhuuyz7QPE8%2BaS5gG4zp3A5wKB6IXm1gOsucbR8QHNs96OBZiEk86wBZmJ0Nv1Aarl0Of0BJL8%2BdKHBOoBAPIBAPgBAIICE9CT0LTQtSDQv9C%2B0LXRgdGC0YyKAlwxODQxMDYzOTAkMTg0MTA2Mzg2JDE4NDEwNjM5NiQxODQxMDYzOTIkMTg0MTA2Mzg0JDE4NDEwNjM5NCQzNTE5MzExNDkzNyQxMzg3Nzg4OTk2JDc3MDkzMTUzN5ICAA%3D%3D&sll=37.616676%2C55.756547&sspn=0.174607%2C0.156237&z=12.57",
                 'Рыба': "https://yandex.ru/maps/213/moscow/search/Где%20поесть/?filter=auto_generated_food_filter%3Aff34%3Balternate_vertical%3ARequestWindow&ll=37.616676%2C55.756547&sctx=ZAAAAAgBEAAaKAoSCYnQCDauz0JAEabtX1lp4EtAEhIJtfoGAHBbBkARHdc4%2BwD97T8iBgABAgMEBSgKOABAt54BSAFiK3JlbGV2X3JhbmtpbmdfbXNlX2Zvcm11bGE9bXNlX2ZtbDgyODgwMl9leHBiJHJlYXJyPXNjaGVtZV9Mb2NhbC9HZW8vUmVsZXZHZW9GaXg9MWoCcnWCAR9hdXRvX2dlbmVyYXRlZF9mb29kX2ZpbHRlcjpmZjA0nQHNzEw9oAEAqAEAvQE0grSTwgGOAcHgn9%2B6Af3smJeBAo3%2BhbSvAZnptqbUA4fO8rq4BIn%2F%2BfGbBOn8na4ptfq0mIYHy6G0oOYCw93TtOsD8rTI%2Fb0C%2Fr%2BfpgSk5dy1twGioam3eeOj9pIEkLHXigWK4Zv%2FA%2Fzmp9vwBaWIvN3kBc7f%2BOj0A%2FGrq56%2FBc7Q%2BvaXBPjsy9UG0pf4nZQE8%2FjnxAbqAQDyAQD4AQCCAhPQk9C00LUg0L%2FQvtC10YHRgtGMigJcMTg0MTA2MzkwJDE4NDEwNjM4NiQxODQxMDYzOTYkMTg0MTA2MzkyJDE4NDEwNjM4NCQxODQxMDYzOTQkMzUxOTMxMTQ5MzckMTM4Nzc4ODk5NiQ3NzA5MzE1MzeSAgA%3D&sll=37.616676%2C55.756547&sspn=0.174607%2C0.156237&z=12.57",
                 'Стейк': "https://yandex.ru/maps/213/moscow/search/Где%20поесть/?filter=auto_generated_food_filter%3Aff38%3Balternate_vertical%3ARequestWindow&ll=37.616676%2C55.756547&sctx=ZAAAAAgBEAAaKAoSCYnQCDauz0JAEabtX1lp4EtAEhIJtfoGAHBbBkARHdc4%2BwD97T8iBgABAgMEBSgKOABAt54BSAFiK3JlbGV2X3JhbmtpbmdfbXNlX2Zvcm11bGE9bXNlX2ZtbDgyODgwMl9leHBiJHJlYXJyPXNjaGVtZV9Mb2NhbC9HZW8vUmVsZXZHZW9GaXg9MWoCcnWCAR9hdXRvX2dlbmVyYXRlZF9mb29kX2ZpbHRlcjpmZjM0nQHNzEw9oAEAqAEAvQHO6v9RwgGKAf6p4JcEmdmxoecDy9SBrZEFm%2FaalAT%2B8POEBfaet%2Fi6A5LBkKLYAcDDy9i8A4eVkqhK84r73qUGidHkywaP7aPEjQfryYO0BLGk553vAcTz5pLmAYG55MeBB82z3o4F7suT8QSZidDb9QGIqZiPKf6LlbqtA9qE2KBI5euY9ATd0MT7mALGvbGnBOoBAPIBAPgBAIICE9CT0LTQtSDQv9C%2B0LXRgdGC0YyKAlwxODQxMDYzOTAkMTg0MTA2Mzg2JDE4NDEwNjM5NiQxODQxMDYzOTIkMTg0MTA2Mzg0JDE4NDEwNjM5NCQzNTE5MzExNDkzNyQxMzg3Nzg4OTk2JDc3MDkzMTUzN5ICAA%3D%3D&sll=37.616676%2C55.756547&sspn=0.174607%2C0.156237&z=12.57",
                 'Фастфуд': "https://yandex.ru/maps/213/moscow/search/Где%20поесть/?filter=auto_generated_food_filter%3Aff20%3Balternate_vertical%3ARequestWindow&ll=37.616676%2C55.756547&sctx=ZAAAAAgBEAAaKAoSCYnQCDauz0JAEabtX1lp4EtAEhIJtfoGAHBbBkARHdc4%2BwD97T8iBgABAgMEBSgKOABAt54BSAFiK3JlbGV2X3JhbmtpbmdfbXNlX2Zvcm11bGE9bXNlX2ZtbDgyODgwMl9leHBiJHJlYXJyPXNjaGVtZV9Mb2NhbC9HZW8vUmVsZXZHZW9GaXg9MWoCcnWCAR9hdXRvX2dlbmVyYXRlZF9mb29kX2ZpbHRlcjpmZjM4nQHNzEw9oAEAqAEAvQGxwjAuwgGRAcTz5pLmAaPasIPEA9myhovaBP6LlbqtA8nDzYeFBbq3jaWBAZHvlNvbBYeVkqhKqOew1pQG%2BZPimpgD9begy7cC8a7mq%2FgBiuGb%2FwOBueTHgQfOtsGK2gHNs96OBdv45MnqBITjkd2YAdqE2KBIqZCMhwX%2F6OKNjwXu%2FaDNuQXnscGgnAbRwLnX4QWTsqHaiQXqAQDyAQD4AQCCAhPQk9C00LUg0L%2FQvtC10YHRgtGMigJcMTg0MTA2MzkwJDE4NDEwNjM4NiQxODQxMDYzOTYkMTg0MTA2MzkyJDE4NDEwNjM4NCQxODQxMDYzOTQkMzUxOTMxMTQ5MzckMTM4Nzc4ODk5NiQ3NzA5MzE1MzeSAgA%3D&sll=37.616676%2C55.756547&sspn=0.174607%2C0.156237&z=12.57",
                 'Завтраки': "https://yandex.ru/maps/213/moscow/search/Где%20поесть/?filter=auto_generated_food_filter%3Aff18%3Balternate_vertical%3ARequestWindow&ll=37.616676%2C55.756547&sctx=ZAAAAAgBEAAaKAoSCYnQCDauz0JAEabtX1lp4EtAEhIJtfoGAHBbBkARHdc4%2BwD97T8iBgABAgMEBSgKOABAt54BSAFiK3JlbGV2X3JhbmtpbmdfbXNlX2Zvcm11bGE9bXNlX2ZtbDgyODgwMl9leHBiJHJlYXJyPXNjaGVtZV9Mb2NhbC9HZW8vUmVsZXZHZW9GaXg9MWoCcnWCAR9hdXRvX2dlbmVyYXRlZF9mb29kX2ZpbHRlcjpmZjIwnQHNzEw9oAEAqAEAvQHnPx12wgGKAen%2BsJ2iBYDMrv8DwrSG3vkBgfu77NcBmdGNpgXf19jqA8a00IsM9vrBsJoChLf6nASIyIvCkQPn1oWpwQL1t6DLtwKGts7UBKKhqbd5g6G1qAT8gL7PBeapqK4Q4brss%2B0DgJ35jg%2FOlY7mA%2BCd69zqBury94T%2BAqrl0Of0BISR4e%2BXBtv45MnqBOoBAPIBAPgBAIICE9CT0LTQtSDQv9C%2B0LXRgdGC0YyKAlwxODQxMDYzOTAkMTg0MTA2Mzg2JDE4NDEwNjM5NiQxODQxMDYzOTIkMTg0MTA2Mzg0JDE4NDEwNjM5NCQzNTE5MzExNDkzNyQxMzg3Nzg4OTk2JDc3MDkzMTUzN5ICAA%3D%3D&sll=37.616676%2C55.756547&sspn=0.174607%2C0.156237&z=12.57",
                 'Паб': "https://yandex.ru/maps/213/moscow/search/Где%20поесть/?filter=auto_generated_food_filter%3Aff14%3Balternate_vertical%3ARequestWindow&ll=37.616676%2C55.756547&sctx=ZAAAAAgBEAAaKAoSCYnQCDauz0JAEabtX1lp4EtAEhIJtfoGAHBbBkARHdc4%2BwD97T8iBgABAgMEBSgKOABAt54BSAFiK3JlbGV2X3JhbmtpbmdfbXNlX2Zvcm11bGE9bXNlX2ZtbDgyODgwMl9leHBiJHJlYXJyPXNjaGVtZV9Mb2NhbC9HZW8vUmVsZXZHZW9GaXg9MWoCcnWCAR9hdXRvX2dlbmVyYXRlZF9mb29kX2ZpbHRlcjpmZjE4nQHNzEw9oAEAqAEAvQHvh8GnwgGKAcbEyPOrAf6p4JcE6f6wnaIF6riT0h3Jw82HhQXAw8vYvAOo0MSOzQXf19jqA4fO8rq4BObSqfGnA%2F6n2bsEnPzmpQWJmavEBoqZw5vQAdKxm%2FoD9ZishoAD%2FIC%2BzwXryYO0BLeO87SqArzl0fe%2BAemvtZOvA8aRkboEm5LMqwaAnfmOD9nY4ObQBeoBAPIBAPgBAIICE9CT0LTQtSDQv9C%2B0LXRgdGC0YyKAlwxODQxMDYzOTAkMTg0MTA2Mzg2JDE4NDEwNjM5NiQxODQxMDYzOTIkMTg0MTA2Mzg0JDE4NDEwNjM5NCQzNTE5MzExNDkzNyQxMzg3Nzg4OTk2JDc3MDkzMTUzN5ICAA%3D%3D&sll=37.616676%2C55.756547&sspn=0.174607%2C0.156237&z=12.57",
                 'Плов': "https://yandex.ru/maps/213/moscow/search/Где%20поесть/?filter=auto_generated_food_filter%3Aff44%3Balternate_vertical%3ARequestWindow&ll=37.616676%2C55.756547&sctx=ZAAAAAgBEAAaKAoSCYnQCDauz0JAEabtX1lp4EtAEhIJtfoGAHBbBkARHdc4%2BwD97T8iBgABAgMEBSgKOABAt54BSAFiK3JlbGV2X3JhbmtpbmdfbXNlX2Zvcm11bGE9bXNlX2ZtbDgyODgwMl9leHBiJHJlYXJyPXNjaGVtZV9Mb2NhbC9HZW8vUmVsZXZHZW9GaXg9MWoCcnWCAR9hdXRvX2dlbmVyYXRlZF9mb29kX2ZpbHRlcjpmZjE0nQHNzEw9oAEAqAEAvQFgPhacwgGIAcbEyPOrAauDtIIF4szQkgSHy6O2cYvRhvgEzsXgsSDn7IKGBJ7UleK7BaWZ%2B5mKB8a00IsMpdjy0Z4D9ZishoADv4q9qhiP7aPEjQeI2sn1X8LL3LwG9tDb%2BQP6%2Fo2aigGtuIDuA9yNm5rvAemvtZOvA9Gc49ypAY6%2BnsuHB5OWho8EyoeWxiDqAQDyAQD4AQCCAhPQk9C00LUg0L%2FQvtC10YHRgtGMigJcMTg0MTA2MzkwJDE4NDEwNjM4NiQxODQxMDYzOTYkMTg0MTA2MzkyJDE4NDEwNjM4NCQxODQxMDYzOTQkMzUxOTMxMTQ5MzckMTM4Nzc4ODk5NiQ3NzA5MzE1MzeSAgA%3D&sll=37.616676%2C55.756547&sspn=0.174607%2C0.156237&z=12.57",
                 'Фо': "https://yandex.ru/maps/213/moscow/search/Где%20поесть/?filter=auto_generated_food_filter%3Aff40%3Balternate_vertical%3ARequestWindow&ll=37.616676%2C55.756547&sctx=ZAAAAAgBEAAaKAoSCYnQCDauz0JAEabtX1lp4EtAEhIJtfoGAHBbBkARHdc4%2BwD97T8iBgABAgMEBSgKOABAt54BSAFiK3JlbGV2X3JhbmtpbmdfbXNlX2Zvcm11bGE9bXNlX2ZtbDgyODgwMl9leHBiJHJlYXJyPXNjaGVtZV9Mb2NhbC9HZW8vUmVsZXZHZW9GaXg9MWoCcnWCAR9hdXRvX2dlbmVyYXRlZF9mb29kX2ZpbHRlcjpmZjQ0nQHNzEw9oAEAqAEAvQHm%2BSrXwgGLAa6i8vy5AdvLo7XJBf%2FCuYiBB6a7%2BtUE5cyO8QP%2B8POEBay16OMDgbDJ%2BgS6t42lgQHw6ZOuzgPDvI3dA9KX%2BJ2UBPyKra3DA6jIhNTXBfjT85d8y4i7rq8FzY319rEE9KPulgXd%2BaCpOJ%2B4xYAEg4byibsG287lvv4CnZqNsQTdmNnepASFs%2Fjm0wTqAQDyAQD4AQCCAhPQk9C00LUg0L%2FQvtC10YHRgtGMigJcMTg0MTA2MzkwJDE4NDEwNjM4NiQxODQxMDYzOTYkMTg0MTA2MzkyJDE4NDEwNjM4NCQxODQxMDYzOTQkMzUxOTMxMTQ5MzckMTM4Nzc4ODk5NiQ3NzA5MzE1MzeSAgA%3D&sll=37.616676%2C55.756547&sspn=0.174607%2C0.156237&z=12.57",
                 'Шаурма': "https://yandex.ru/maps/213/moscow/search/Где%20поесть/?filter=auto_generated_food_filter%3Aff2c%3Balternate_vertical%3ARequestWindow&ll=37.616676%2C55.756547&sctx=ZAAAAAgBEAAaKAoSCYnQCDauz0JAEabtX1lp4EtAEhIJtfoGAHBbBkARHdc4%2BwD97T8iBgABAgMEBSgKOABAt54BSAFiK3JlbGV2X3JhbmtpbmdfbXNlX2Zvcm11bGE9bXNlX2ZtbDgyODgwMl9leHBiJHJlYXJyPXNjaGVtZV9Mb2NhbC9HZW8vUmVsZXZHZW9GaXg9MWoCcnWCAR9hdXRvX2dlbmVyYXRlZF9mb29kX2ZpbHRlcjpmZjQwnQHNzEw9oAEAqAEAvQGbbIViwgEQy%2F6A%2BwS9iM2AYLeaxe%2F7BuoBAPIBAPgBAIICE9CT0LTQtSDQv9C%2B0LXRgdGC0YyKAlwxODQxMDYzOTAkMTg0MTA2Mzg2JDE4NDEwNjM5NiQxODQxMDYzOTIkMTg0MTA2Mzg0JDE4NDEwNjM5NCQzNTE5MzExNDkzNyQxMzg3Nzg4OTk2JDc3MDkzMTUzN5ICAA%3D%3D&sll=37.616676%2C55.756547&sspn=0.174607%2C0.156237&z=12.57",
                 'Паста': "https://yandex.ru/maps/213/moscow/search/Где%20поесть/?filter=auto_generated_food_filter%3Aff28%3Balternate_vertical%3ARequestWindow&ll=37.616676%2C55.753947&sctx=ZAAAAAgBEAAaKAoSCYnQCDauz0JAEabtX1lp4EtAEhIJAAAAAHBbBkARwDs%2B%2BwD97T8iBgABAgMEBSgKOABA1QFIAWoCcnWdAc3MTD2gAQCoAQC9AWuCe%2FnCAYcBxsTI86sB%2FqnglwSrg7SCBYfLo7Zxi9GG%2BATB4J%2FfugGnt6Tr%2FgGAzK7%2FA6WZ%2B5mKB%2BfsgoYEnPzmpQX1mKyGgAPBgryrqwKJmavEBv6n2bsEw5%2FnjwTKh5bGIMaRkboEhrbO1ASJhNC%2FBKSbrNT8Ar7696KyBvyAvs8F6vL3hP4CmISTzrAF6gEA8gEA%2BAEAggIT0JPQtNC1INC%2F0L7QtdGB0YLRjIoCXDE4NDEwNjM5MCQxODQxMDYzODYkMTg0MTA2Mzk2JDE4NDEwNjM5MiQxODQxMDYzODQkMTg0MTA2Mzk0JDM1MTkzMTE0OTM3JDEzODc3ODg5OTYkNzcwOTMxNTM3kgIA&sll=37.616676%2C55.753947&sspn=0.174665%2C0.058569&z=14"
}

def pars_links(link):
    driver = webdriver.Chrome()
    driver.get(url = link)
    driver.maximize_window()
    time.sleep(1)

    driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[4]/div[6]/div[1]/div[2]/div[1]/div/div/div/div[2]/button').click()
    time.sleep(2)

    search_tries = 0
    actions_pars = ActionChains(driver)
    i = 2

    links = []

    search_list_view = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[9]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div/ul')

    while True:
        time.sleep(0.5)
        try:
            search_snippet = search_list_view.find_element(By.XPATH,f"/html/body/div[1]/div[2]/div[9]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div/ul/div[{i}]")
            actions_pars.move_to_element(search_snippet).perform()
            time.sleep(0.5)
            rest_link = search_snippet.find_element(By.CLASS_NAME, "search-snippet-view__link-overlay").get_attribute('href')
            print(rest_link)

        except NoSuchElementException:
            print(f"Can not find {i} element")
            if search_tries > 4:
                break
            search_tries += 1
            time.sleep(5)
            continue

        search_tries = 0
        links.append(rest_link)

        i += 1

    driver.close()
    driver.quit()
    return links

def pars_data(link, category):
    cords = []
    latlon = ''
    tries = 0
    fl = 0
    opt = webdriver.ChromeOptions()
    opt.add_argument(f'user-agent={random.choice(user_agents)}')
    new_driver = webdriver.Chrome(options=opt)

    while True:
        try:
            new_driver.get(url=link)
            break
        except Exception:
            print('Can not load the page')
            new_driver.close()
            new_driver.quit()
            if tries > 5:
                fl = 1
                break
            time.sleep(3)
            tries += 1
            continue

    if fl == 1:
        return

    time.sleep(1)

    new_list = new_driver.find_element(By.CLASS_NAME, 'business-card-view__main-wrapper')
    title = new_list.find_element(By.CLASS_NAME, 'orgpage-header-view__header')
    address = new_list.find_element(By.CLASS_NAME, 'orgpage-header-view__address').get_attribute('title')
    try:
        rating = new_list.find_element(By.CLASS_NAME, 'business-rating-badge-view__rating').text
    except NoSuchElementException:
        rating = 'Нет оценок'
    container = new_driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/ymaps/ymaps[2]')
    time.sleep(1)

    for i in range(0, 4):
        try:
            el_in_container = container.find_element(By.XPATH, '/html/body/div[1]/div[1]/ymaps/ymaps[2]/ymaps/ymaps[2]')
            cords = el_in_container.find_element(By.XPATH,
                                                 '/html/body/div[1]/div[1]/ymaps/ymaps[2]/ymaps/ymaps[2]/ymaps[1]/div/div/div').get_attribute(
                'data-coordinates')
            break

        except Exception as ex:
            print(ex, category, title)
            time.sleep(0.2)

    try:
        latlon = cords.split(',')
    except Exception as ex:
        print(ex)
        new_driver.close()
        new_driver.quit()
        return

    datab.add(category, title.text, address, rating, latlon[0], latlon[1])

    new_driver.close()
    new_driver.quit()
    return

def main():
    for el in list_of_links:
        urls = pars_links(list_of_links[el])

        for url in urls:
            pars_data(url, el)

if __name__ == '__main__':
    main()

# i1 = 0
# i2 = 1
# t = 0
# times = 1
#
#
# while True:
#     if i1 == 0:
#         driver = webdriver.Chrome()
#         action = ActionChains(driver)
#         driver.get('https://yandex.ru/maps/213/moscow/search/Где%20поесть/')
#         time.sleep(1)
#         action.move_to_element(driver.find_element(By.XPATH,f"/html/body/div[1]/div[2]/div[9]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div[{i2}]/div/div[2]")).click().perform()
#         time.sleep(2)
#
#         pars(driver, driver.find_element(By.XPATH,f"/html/body/div[1]/div[2]/div[9]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div[{i2}]/div/div[2]").text)
#         driver.close()
#         driver.quit()
#
#         i2 += 1
#
#         driver = webdriver.Chrome()
#         action = ActionChains(driver)
#         driver.get('https://yandex.ru/maps/213/moscow/search/Где%20поесть/')
#         time.sleep(1)
#         action.move_to_element(driver.find_element(By.XPATH,f"/html/body/div[1]/div[2]/div[9]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div[{i2}]/div/div[2]")).click().perform()
#         time.sleep(2)
#
#         pars(driver, driver.find_element(By.XPATH,f"/html/body/div[1]/div[2]/div[9]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div[{i2}]/div/div[2]").text)
#
#         i2 += 1
#         driver.close()
#         driver.quit()
#     else:
#         driver = webdriver.Chrome()
#         action = ActionChains(driver)
#         driver.get('https://yandex.ru/maps/213/moscow/search/Где%20поесть/')
#         time.sleep(1)
#         while t < times - 1:
#             try:
#                 if t == 0:
#                     action.move_to_element(driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[9]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div/div[3]/div/div[2]/div[2]/div/span")).click().perform()
#                     time.sleep(1)
#                 else:
#                     action.move_to_element(driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[9]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div/div[3]/div/div[2]/div[3]/div/span")).click().perform()
#                     time.sleep(1)
#             except NoSuchElementException:
#                 action.move_to_element(driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[9]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div[21]/div/div[2]")).click().perform()
#                 time.sleep(2)
#
#                 pars(driver, driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[9]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div[21]/div/div[2]").text)
#                 driver.close()
#                 driver.quit()
#                 quit()
#             t += 1
#         t = 0
#
#         action.move_to_element(driver.find_element(By.XPATH,f"/html/body/div[1]/div[2]/div[9]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div[{i2}]/div/div[2]")).click().perform()
#         time.sleep(2)
#
#         pars(driver, driver.find_element(By.XPATH,f"/html/body/div[1]/div[2]/div[9]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div[{i2}]/div/div[2]").text)
#         driver.close()
#         driver.quit()
#
#         i2 += 1
#
#         driver = webdriver.Chrome()
#         action = ActionChains(driver)
#         driver.get('https://yandex.ru/maps/213/moscow/search/Где%20поесть/')
#         time.sleep(1)
#         while t < times - 1:
#             if t == 0:
#                 action.move_to_element(driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[9]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div/div[3]/div/div[2]/div[2]/div/span")).click().perform()
#                 time.sleep(1)
#             else:
#                 action.move_to_element(driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[9]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div/div[3]/div/div[2]/div[3]/div/span")).click().perform()
#                 time.sleep(1)
#             t += 1
#         t = 0
#
#         action.move_to_element(driver.find_element(By.XPATH,f"/html/body/div[1]/div[2]/div[9]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div[{i2}]/div/div[2]")).click().perform()
#         time.sleep(2)
#
#         pars(driver, driver.find_element(By.XPATH,f"/html/body/div[1]/div[2]/div[9]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div[{i2}]/div/div[2]").text)
#
#         driver.close()
#         driver.quit()
#
#         i2 += 1
#     times += 1
#     i1 += 1




