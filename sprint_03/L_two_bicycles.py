# L Два велосипеда.


def binary_search(arr, target, left, right):
    # Если диапазон поиска пуст, значит цена не найдена
    if right < left:
        return -1
    
    mid = (left + right) // 2
    
    # Если в текущий день (mid) денег хватает
    if arr[mid] >= target:
        # Проверяем: это САМЫЙ первый такой день? 
        # (Либо это первый день в списке, либо вчера денег еще не хватало)
        if mid == 0 or arr[mid - 1] < target:
            return mid + 1  # Возвращаем номер дня (индекс + 1)
        else:
            # Ищем левее, так как нам нужен самый первый день
            return binary_search(arr, target, left, mid - 1)
    else:
        # Денег мало, ищем только в правой половине
        return binary_search(arr, target, mid + 1, right)


def main():
    count = int(input())
    money = [int(i) for i in input().split()]
    price = int(input())
    first_day = binary_search(money, price, 0, count - 1)
    second_day = binary_search(money, price * 2, 0, count - 1)
    print(first_day, second_day)
    

if __name__ == '__main__':
    main()