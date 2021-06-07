check_list = ["зарядка" , "завтрак" "не опоздать на работу" , "пообедать" , "продать"]
for i in check_list:
    print(i)
    n = input("ответ")
    if n.strip() == "да":
        continue
    else:
        print("голодай")
        break