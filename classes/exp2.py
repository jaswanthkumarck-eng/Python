class laptop:
    price=0
    processor=""
    ram=""

hp=laptop()
dell=laptop()
lenovo=laptop()

hp.price=50000
hp.processor="i5"
hp.ram="12gb"

dell.price=60000
dell.processor="ryzen5"
dell.ram="16gb"

lenovo.price=70000
lenovo.processor="ryzen7"
lenovo.ram="24gb"

print(lenovo.ram)
print(dell.processor)
print(hp.price)
