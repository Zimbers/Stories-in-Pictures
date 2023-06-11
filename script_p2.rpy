    
label start:
    play music hacalo
    scene bg ulica
    with fade
    m 'Program files'
    window hide
    n '''Вывод текста на весь экран'''
    nvl hide

    menu:
        m "ты пойдешь со мной ?"
        "да":
            jump pohod


        "нет":
            jump nopohod
                           
