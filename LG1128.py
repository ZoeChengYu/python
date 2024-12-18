def world(num,vol):
    if num<vol**2:
        if vol <=1:
            vol/=10
            world(num,vol)
        else:
            return vol/10
    elif num>vol**2:
        if vol>=1:
            vol*=10
            world(num,vol)
        else:
            return vol
    else:
        return vol

def country(num,unit,base:float):
    if (base**2)==num or unit==10**-5:
        return base
    elif num<base**2:
        return country(num,unit/10,base-unit)
    else:
        return country(num,unit,base+unit)

def main():
    num=float(input())
    unit=1
    world(num,unit)
    ans=country(num,unit,unit)
    print(ans)

main()