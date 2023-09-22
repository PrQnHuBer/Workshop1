def data():
    name = input(" ใส่ฃื่อสินค้า :")
    price = float(input("ใส่ราคาสินค้า :"))
    return name, price

def tax(price):
    pc=7
    tax = (price*pc)/100
    return tax


def show(name, price,tax):
    print=(f'ชื่อสินค้า{name}')
    print=(f'ราคาสินค้า{price:.2f}')
    print=(f'ราคาสินค้าหลังบวกภาษี{tax:.2f}')

name,price=data()
tax = tax(price)
show(name,price,tax)