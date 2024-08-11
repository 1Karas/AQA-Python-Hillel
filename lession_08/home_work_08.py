'''Створіть масив зі строками, які будуть складатися з чисел, які розділені комою. Наприклад:

[”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]

Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).

Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі), вам потрібно зловити вийняток і вивести “Не можу це зробити!”'''


lst = ['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3']
lst2 = ['1,2,3,4', '1,2,3,4,50', '1,2,3']
result: list[int] = list()
def sum_all_chards_is_string_if_int(lst) -> None:
    try:
        for item in lst:
            chars_list: list =  item.split(",")
            result.append(sum(int(integer) for integer in chars_list))
    except ValueError as exeption:
        print(f"I can not sum your item from list due to: {exeption} ")
    else:
        print(result)
sum_all_chards_is_string_if_int(lst)
sum_all_chards_is_string_if_int(lst2)