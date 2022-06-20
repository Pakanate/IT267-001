from measure import Measure 

if __name__ == "__main__":
    m1 = Measure (12.5)
    m2 = Measure (100)
    m3 = Measure(56)
    m4 = Measure(78)
    m5 = Measure(14)
    m6 = Measure(250)
    print(m1.inch_cm())
    print(m2.cm_inch())
    print(m3.inch_cm())
    print(m3.inch_cm())
    print(m4.cm_inch())
    print(m5.cm_inch())
    print(m6.cm_inch())


    inch_list = [52,18,20,40]
    for item in inch_list:
        m = Measure(item)
        print(m.inch_cm())

    num = float(input("Enter number:"))
    ch = input("Choose I(ingch->cm), C(cm->inch):").upper()
    if ch == 'I':
        m = Measure(num)
        print(m.inch_cm())
    elif ch == "C":
        m = Measure(num)
        print("Wrong Character")
