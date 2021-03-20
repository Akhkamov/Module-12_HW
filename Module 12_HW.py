per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
TKB = per_cent['ТКБ']
SKB = per_cent['СКБ']
VTB = per_cent['ВТБ']
SBER = per_cent['СБЕР']
print('Введите сумму')
money = float(input())
TKB = money * TKB
SKB = money * SKB
VTB = money * VTB
SBER = money * SBER
deposit = [TKB, SKB, VTB, SBER]
deposit.sort()
print('Максимальная сумма, которую вы можете заработать — ', deposit[-1])