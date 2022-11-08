date = input("Введите дату в формате 'дд.мм.гггг': ")
date = date.replace(".", "/")
l = list(date)
l[0], l[3] = l[3], l[0]
l[1], l[4] = l[4], l[1]
d = "".join(l)
print(d)