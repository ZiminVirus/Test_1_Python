# Напишите проект, содержащий функционал работы с заметками.
# Программа должна уметь создавать заметку,
# сохранять её,
# читать список заметок,
# редактировать заметку,
# удалять заметку.
import datetime

text = 0
note_list = []
num_note = 0

while text != 5:
    print ('')
    print('Для того чтобы написать заметку введите 1; \n'
          'Для того чтобы вывести список заметок введите 2; \n'
          'Для того чтобы редактировать какую то заметку нажмите 3, затем номер заметки \n'
          'Для того чтобы удалить заметку нажмите 4, затем введите номер заметки \n'
          'Для того чтобы сохранить данные в файл введите 5 \n'
          'Для того чтобы выйти из программы нажмите 6 \n')
    text = int (input());
    if text == 1:
        num_note = num_note + 1
        print('Введите заголовок заметки')
        title_note = input()
        print ('Введите текст заметки')
        text_note = input()
        dateTime_note = str(datetime.datetime.now())
        note = {"num": num_note, "date": dateTime_note, "title": title_note, "word": text_note}
        note_list.append(note)
    elif text == 2:
        print (*note_list, sep = "\n")
    elif text == 3:
        while True:
            print('Введите номер заметки для редактирования')
            try:
                text_note = int (input())
            except:
                print('Некорректное значение, попробуйте еще раз')
            create_note_dict = note_list[text_note - 1]
            new_num = create_note_dict ['num']
            new_dateTime_note = str(datetime.datetime.now())
            print('Введите новый заголовок')
            new_title_note = input()
            print('Введите новый текст')
            new_text_note = input()
            new_note = {"num": new_num, "date": new_dateTime_note, "title": new_title_note, "word": new_text_note}
            note_list[text_note - 1] = new_note
            print(note_list)
            break
    elif text == 4:
        while True:
            print('Введите номер заметки для удаления')
            try:
                text_note = int(input())
                note_list.remove(note_list[text_note - 1])
            except:
                print('Нет заметки с таким номером, попробуйте еще раз')
            print(note_list)
            break
    elif text == 5:
        with open('log.csv', 'a') as file:
            file.write(f'{note_list} \n')
    elif text == 6:
        break
    else:
        print('Введено не верное значение, попробуйте еще раз')






