def data():
    name = input(" ใส่ฃื่อสินค้า :")
    price = float(input("ใส่ราคาสินค้า :"))
    return name, price

def pricetax(price):
    pc=7
    tax = (price*pc)/100
    return tax


def show(name, price,tax):
    print(f'ชื่อสินค้า{name}')
    print(f'ราคาสินค้า{price:.2f}')
    print(f'ภาษีของสินค้าชิ้นนี้{tax:.2f}')

name,price=data()
tax = pricetax(price)
show(name,price,tax)