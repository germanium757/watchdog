print("Создание файла")
while(True):
    a=input()
    # | Проверка на выход
    if(a=='end'): break
    # | Проверка на меньше чем 3 букв
    if(len(a)<=3): 
        print('Введите слово от 3 символов длиной')
        continue
    
    # | Проверка на наличие цифр
    n=0
    for i in a:
        try: k =float(i)
        except Exception: n+=1
    if(n!=len(a)): 
        print('Введите слово')
        continue
            
    # | Ура, мы дошли сюда
    with open('./files/'+ a +'.txt','w') as con:
        print("Файл создан")
        pass