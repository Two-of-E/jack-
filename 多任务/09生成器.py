def create_num(all_num):
    a,b = 0,1
    current_num = 0
    while current_num < all_num:
        ret = yield a
        print(">>>>ret>>>",ret)
        a,b = b,a+b
        current_num += 1

obj = create_num(10)


# next方式不穿回参数，默认为none
ret = next(obj)
print(ret)


ret = next(obj)
print(ret)

# 向内部传递参数
ret = obj.send("hhhh")
print(ret)

