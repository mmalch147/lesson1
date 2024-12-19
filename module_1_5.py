immutable_var = 1, 2, 'cucumber', 'banana'
print(immutable_var)


#Изменить элементы кортежа immutable_var нельзя, потому что кортеж — это неизменяемая структура данных в Python.
#После создания кортежа его элементы нельзя изменить, добавить или удалить.
# Попытка изменить элементы кортежа приведёт к ошибке.


mutable_list = [1, 2, 'a', 'b', 'Modified']
mutable_list[3] = 0
print(mutable_list)