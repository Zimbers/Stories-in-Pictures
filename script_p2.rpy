    
label start:
    play music hill
    scene bg ulica
    with fade
    m 'Program files'
    window hide
    n '''Вывод текста на весь экран'''
    nvl hide

    menu:
        m "ты педик ?"
        "да":
            jump pedik


        "нет":
            jump nopedik 
                           
return