# 2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.
# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]


data = list(tuple(input('Input int and str type values through space button: ').split()))

filtered_digits= filter(lambda value: value.replace('.', '').isdigit(), data)
filtered_text = filter(str.isalpha, data)

print(list(filtered_digits))
print(list(filtered_text))
