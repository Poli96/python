a=int(input("Введите первое число: "))
b=int(input("Введите второе число: "))
c=int(input("Введите третье число: "))
def main(a,b,c):
   if a>b and a>c:
      if b>c:
         print(b)
      else:
         print(c)
   if b>a and b>c:
      if a>c:
         print(a)
      else:
         print(c)
   if c>a and c>b:
      if a>b:
         print(a)
      else:
         print(b)
main(a,b,c)
