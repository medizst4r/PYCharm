import model
import view

bd_list = model.open_data(model.path)

def menu():
    list_menu = [
        'Показать все контакты',
        'Добавить контакт',
        'Изменить контакт',
        'Удалить контакт',
        'Найти контакт',
        'Сохранить изменения в файле',
        'Выйти из меню'
        ]
    return list_menu

list_menu = menu()

def find_contact(list_bd):
    string_find = str(input('Поиск: '))
    clause = False
    for line in list_bd:
        for val in line.values():
            if string_find == val :
                print(line)
                clause = True
    if clause == False:
        print(f'\tНичего не нашёл.\n')

def processing_request(num):
    match num:
        case 1:
            view.show_all_list(bd_list)
            processing_request(view.show_menu(list_menu))
        case 2:
            model.set_bd(bd_list)
            processing_request(view.show_menu(list_menu))
        case 3:
            id_contact = view.input_change_id()
            model.change_contact(id_contact )
            processing_request(view.show_menu(list_menu))
        case 4:
            model.del_contact(bd_list, view.input_del_id_contac())
            processing_request(view.show_menu(list_menu))
        case 5:
            find_contact(bd_list)
            processing_request(view.show_menu(list_menu))
        case 6:
            model.save_list(bd_list)
            processing_request(view.show_menu(list_menu))
        case 7:
            exit()
