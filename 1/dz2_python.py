# example 1
# Была не закрыта скобка в методе print
# print("Hello, Amy"
print("Hello, Amy")

# example 2
# Ошибка с форматированием строк, нужно использовать %d
age = 15
# print("Amy is %s years old" % age)
print("Amy is %d years old" % age)

# example 3
# Пропустили в методе print кавычки и поставлен лишний пробел
color = input("Input your favorite color: ")
# print(f Her favorite color is {color}")
print(f"Her favorite color is {color}")
