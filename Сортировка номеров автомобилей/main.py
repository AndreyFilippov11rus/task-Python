import re

numbers = "А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666"
pattern_auto = r'\b\D\d{3}\D{2}\d{3}\b'
pattern_tax = r'\b\D{2}\d+\b'


if __name__ == '__main__':
    numb_auto = re.findall(pattern_auto, numbers)
    numb_tax = re.findall(pattern_tax, numbers)

    print('Список номеров частных автомобилей: ', numb_auto)
    print('Список номеров такси: ', numb_tax)


