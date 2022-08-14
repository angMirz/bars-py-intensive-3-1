"""
Что будет выведено после выполнения кода? Почему?
Обращаемся к функции, передав ей значение агрумента Test message, после вызывется вложенная функция,
которая выведет сообщение.
далее вывод None потому что функция transmit_to_space ничего не возвращает.
"""


def transmit_to_space(message):
   
    def data_transmitter():        
        print(message)

    data_transmitter()


print(transmit_to_space("Test message"))
