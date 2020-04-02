import math #подключаем библиотеку, чтобы использовать метод округления вверх

def game_core_v3(number, A, B):  # в функцию передаем загаданное число из диапазона от A до B
    # Определяем серидину интервала - это первое предсказание.  
    count = 1  
    predict = A + round((B-A)/2)
    predict_step = round((B-A)/2) # Задаем шаг предсказания, который в цикле предсказания на каждом шаге делим пополам, 
                                  # обеспечивая сходимость
    
    while number != predict:
        count+=1
        predict_step = math.ceil(predict_step/2) # используем округление вверх, чтобы исключить нулевой шаг
        if number > predict:          #в цикле поочередно изменяем переменную предсказания на величину шага в сторону
            predict += predict_step   # увеличения или уменьшения
        elif number < predict: 
            predict -= predict_step
        
    
    return(count) # выход из цикла, если угадали
        
        
def score_game(game_core,As,Bs):
    '''Запускаем игру 1000 раз, чтоб узнать как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(As, Bs+1, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number,As,Bs))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return


# тест

score_game(game_core_v3,1,100)