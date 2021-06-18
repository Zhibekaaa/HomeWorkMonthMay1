todos = []
while True:
    print("1) Добавить задачу")
    print("2) Показать задачу")
    option = int(input())

    if option == 1:
        task = input()
        deadline = input()
        date_added = input()