def change(money):
    # write your code here
    ten = money // 10
    money = money % 10
    five = money // 5
    money = money % 5
    one = money
    return ten + five + one   


if __name__ == '__main__':
    m = int(input())
    print(change(m))
