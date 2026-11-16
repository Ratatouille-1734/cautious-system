name= input("Please enter your name: ")
first_initial= input ("Please enter your first initial:")
last_initial= input("Please enter your last initial:")
num1=float(input("Please enter a number:"))
num2= float(input("Please enter a second number:"))

print(f"{name}\t\t{first_initial}{last_initial}")

n1_disp=int(num1) if num1. is_integer() else num1
n2_disp= int(num2) if num1. is_integer() else num2

add_res= num1+num2
sub_res= num1-num2
mul_res= num1*num2
div_res= num1/num2

print(f"{n1_disp} + {n2_disp} = {int(add_res) if add_res.is_integer() else f' {add_res: .2f}'}")
print(f"{n1_disp} - {n2_disp} = {int(sub_res) if sub_res.is_integer() else f' {sub_res: .2f}'}")
print(f"{n1_disp} * {n2_disp} = {int(mul_res) if mul_res.is_integer() else f' {mul_res: .2f}'}")
print(f"{n1_disp} / {n2_disp} = {int(div_res) if div_res.is_integer() else f' {div_res: .2f}'}")
