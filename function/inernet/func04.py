import main


def get_list(food):
    if food == 'korean':
        data = ['냉면','오미자차','팥빙수']
    elif food == 'japan':
        data = ['우동','생면']
    else:
        data = ['라면','커피']
        return data

    if __name__ == '__main__':
        result = get_list('japan')
        print(result)