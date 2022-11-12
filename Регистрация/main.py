def check_count(account):
    try:
        if len(account) < 3:
            raise IndexError
        if not account[0].isalpha():
            raise NameError
        if '.' not in account[1] and '@' not in account[1]:
            raise SyntaxError
        if 10 > int(account[2]) > 99:
            raise ValueError
    except IndexError:
        with open('registrations_bad.log', 'a', encoding='utf-8') as bad:
            bad.write(' '.join(account) + '\t\tНЕ присутствуют все три поля\n')
    except NameError:
        with open('registrations_bad.log', 'a', encoding='utf-8') as bad:
            bad.write(' '.join(account) + '\t\tПоле «Имя» содержит НЕ только буквы\n')
    except SyntaxError:
        with open('registrations_bad.log', 'a', encoding='utf-8') as bad:
            bad.write(' '.join(account) + '\t\tПоле «Имейл» НЕ содержит @ и . (точку)\n')
    except ValueError:
        with open('registrations_bad.log', 'a', encoding='utf-8') as bad:
            bad.write(' '.join(account) + '\t\tПоле «Возраст» НЕ является числом от 10 до 99\n')
    else:
        with open('registrations_good.log', 'a', encoding='utf-8') as good:
            good.write(' '.join(account)+'\n')


with open('registrations.txt', 'r', encoding='utf-8') as data_account:
    for line in data_account:
        account = []
        account = line.split()
        check_count(account)


