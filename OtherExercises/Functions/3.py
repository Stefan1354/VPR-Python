#3.Напишете програма с функция с произволен брой числови аргументи, която връща като 
#резултат списък от три елемента: средноаритметичната, максималната и минималната стойност
#на аргументите.

def n_arg_func(*args):
    list = args
    return [sum(list)/len(list), max(list), min(list)]
print(n_arg_func(1,2,3)) #[2.0, 3, 1]
