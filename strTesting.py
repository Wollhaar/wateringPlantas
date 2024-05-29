str_bday = "happy birthday"

str_bday = str_bday.capitalize()
pos_bday = str_bday.find(" ")
str_bday = str_bday[:pos_bday] + " " + str_bday[pos_bday + 1:].capitalize()

print(str_bday)