# def serve_chai():
#     yield "cup1 : Masala Chai"
#     yield "cup2 : Ginger Chai"
#     yield "cup3 : Elaichi Chai"

# stall = serve_chai()

# for cup in stall:
#     print(cup)

# def get_chai_list():
#     return ["cup1","cup2","cup3"]    

# def gen_chai_list():
#     yield "cup1"
#     yield "cup1"
#     yield "cup1"

# func = gen_chai_list();
# print(next(func))


# # infinite generators

# def infinte_chai():
#     count = 1
#     while True:
#         yield f"Refil #{count}"
#         count += 1

# refill = infinte_chai();

# for _ in range(5) :
#     print(next(refill))

# def chai_cus():
#     print("welcome ! whai chai you want")
#     order = yield 
#     while True:
#         print(f"Preparing:{order}")
#         order = yield

# stall = chai_cus();
# next(stall)
# stall.send("masala")
# stall.send("masala")

def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"

def imported_chai():
    yield "macha"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)

def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order"
            print(order)
    except:
        print("Store closed")

stall = chai_stall()
#print(next(stall))
next(stall)
stall.send("macha")
stall.close()