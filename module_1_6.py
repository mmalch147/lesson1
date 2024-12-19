my_dict = {
    "Mary": 65,
    "Antin": 45,
    "Valera": 43

}
print(my_dict)
print(my_dict["Mary"])
print(my_dict["Valera"])
my_dict.update({"Maryl": 65, "Antina": 45})
print(my_dict)
a = my_dict.pop("Valera")
print(a)
print(my_dict)

my_set = {2, 4, 2, 1, "Lisa"}
print(my_set)
my_set.update({"a", 5, 5})
print(my_set)
a=my_set.pop()
print(a)