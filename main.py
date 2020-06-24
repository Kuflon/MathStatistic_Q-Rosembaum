smpl1 = [8.8, 15, 0.9, 0.5, 4.3, 1.8, 2.9, 3.2, 5.6, 11.2, 3.4]
smpl2 = [5.4, 5, 0.8, 0.9, 2.7, 1.7, 1.6, 5.3, 0.9, 2.7, 3.1, 0.3] # Your samples/ Ваши выборки

'''
Hypotheses:
H0: the trait Level in sample 1 does not exceed the trait level in sample 2
H1: the trait Level in sample 1 exceeds the trait level in sample 2
--------------------------------------------------------------------------
Гипотезы:
H0: Уровень признака в выборке 1 не превышает уровня признака в выборке 2
H1: Уровень признака в выборке 1 превышает уровня признака в выборке 2
'''

def check_n(s1, s2):
    '''
    Checks for the number of items in each selection.
    return + if 11 or more(it's good)
    return - if less than 11(it's bad)
    -------------------------------------------------
    Проверяет количество элементов в каждой выборке.
    возврат + если 11 или больше(это хорошо)
    возврат - если меньше 11(это плохо)
    '''

    if(len(s1) >= 11 and len(s2) >= 11):
        return '+'
    else:
        print('Insufficient data, the minimum number of items in each sample is 11')
        return '-'


def q_tbl(n1, n2):
    '''
    Returns the q-Rosenbaum table value
    ------------------------------------
    Возвращает табличное значение Q-Розенбаума
    '''
    tbl005 = [[6],
              [6, 6],
              [6, 6, 6],
              [7, 7, 6, 6],
              [7, 7, 6, 6, 6],
              [8, 7, 7, 7, 6, 6],
              [7, 7, 7, 7, 7, 7, 7],
              [7, 7, 7, 7, 7, 7, 7, 7],
              [7, 7, 7, 7, 7, 7, 7, 7, 7],
              [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
              [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
              [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
              [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
              [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7],
              [8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7],
              [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7],
              ]#Table values for significance level a = 0.05% / Табличные значения для уровня значимости a = 0,05%
    tbl001 = [[9],
              [9, 9],
              [9, 9, 9],
              [9, 9, 9, 9],
              [9, 9, 9, 9, 9],
              [9, 9, 9, 9, 9, 9],
              [10, 9, 9, 9, 9, 9, 9],
              [10, 10, 9, 9, 9, 9, 9, 9],
              [10, 10, 10, 9, 9, 9, 9, 9, 9],
              [10, 10, 10, 10, 9, 9, 9, 9, 9, 9],
              [11, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9],
              [11, 11, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9],
              [11, 11, 10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9],
              [12, 11, 11, 10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9],
              [12, 11, 11, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9],
              [12, 12, 11, 11, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9],
              ]#Table values for significance level a = 0.01% / Табличные значения для уровня значимости a = 0,01%

    if n1 > n2:
        q_005 = tbl005[n1 - 11][n2 - 11]
        q_001 = tbl001[n1 - 11][n2 - 11]
    else:
        q_005 = tbl005[n2 - 11][n1 - 11]
        q_001 = tbl001[n2 - 11][n1 - 11]

    if n1 > 26 or n2 > 26:
        q_005 = 8
        q_001 = 10

    return q_005, q_001


def q_rosenbaum(s1, s2):
    answr = check_n(s1, s2)# Step 1. Checking for sample size

    if(answr == '+'):
        s1 = sorted(s1)# Step 2. Sorting values in ascending order
        s2 = sorted(s2)

        if(max(s2) > max(s1)):# Defining the leading sample
            s_temp = []
            s_temp = s1
            s1 = s2
            s2 = s_temp

        sum1 = sum2 = 0
        for i in range(len(s1)):
            if s1[i] > max(s2):# Step 3. Determine the max value in sample 2 and calculate the number of items in the first sample larger than the selected one.
                sum1 += 1

        for i in range(len(s2)):# Step 4. Determine the minimum value in sample 1 and calculate the number of elements in the second sample that are smaller than the selected one.
            if s2[i] < min(s1):
                sum2 += 1

        q = sum1 + sum2
        q_005, q_001 = q_tbl(len(s1), len(s2))

        print(f'\nq = {q}, q_005 = {q_005}, q_001 = {q_001}\n')
        if(q > q_005):
            print('q > q_005 Ho rejects is rejected with a confidence level of 95%\n')
            if(q > q_001):
                print('q > q_001 Ho rejects is rejected with a confidence level of 99%\n')
        else:
            print('q < q_table there is no reason to reject Ho\n')


q_rosenbaum(smpl1, smpl2)
