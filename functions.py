def say_hello(name: str ):
    print(f"Hello {name}")

def get_sum(a: int ,b: int):
    result= a+b
    return result

def get_cube(number:int):
    result= number **3
    return result

def get_steps(length,len_of_step=0.75):
    result= int(length / len_of_step)
    return result

def absolute_distance(a,b):
    if a > b:
        result= a-b
    else:
        result= b-a
    return result

def list_average(seznam: list):
    sum = 0
    count=0
    for item in seznam:
        sum+= item
        count+= 1
    return sum/ count


def calc_square(height: int, width: int):
    area= height*width
    circumstance= 2*height + 2* width

    return {"area": area, "circumstance":circumstance}

#ali samo za touple

def calc_square(height: int, width: int):
    area= height*width
    circumstance= 2*height + 2* width

    return area, circumstance