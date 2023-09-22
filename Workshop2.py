def data():
    name =input("กรุณาใส่ชื่อ : ")
    id =input("กรุณาใส่รหัสนักศึกษา : ")
    n1= int(input("ใส่คะแนนสอบครั้งที่ 1 :"))
    n2= int(input("ใส่คะแนนสอบครั้งที่ 2 :"))
    n3= int(input("ใส่คะแนนสอบครั้งที่ 3 :"))
    return name,id,n1,n2,n3

def average(n1,n2,n3):
    average = ((n1+n2+n3)/3)
    return average

def show(name,id,n1,n2,n3,average):
    print(f'คุณ {name} รหัสนักศึกษา {id} ')
    print(f'คะแนนสอบครั้งที่ 1 = {n1}')
    print(f'คะแนนสอบครั้งที่ 2 = {n2}')
    print(f'คะแนนสอบครั้งที่ 3 = {n3}')
    print(f'คะแนนสอบเฉลี่ย = {average}')

name,id,n1,n2,n3 =data()
average = average(n1,n2,n3)
show(name,id,n1,n2,n3,average)