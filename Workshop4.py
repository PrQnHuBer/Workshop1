def data():
    x = (int(input("ใส่ตัวเลข : ")))
    return x

def cal(x):
    y =2*(x^2)+2*(x)+1
    return y

def show(x,y):
    print(f"x มีค่าเท่ากับ {x}")
    print(f"y มีค่าเท่ากับ {y}")

x=data()
y=cal(x)
show(x,y)