print("[1] Addition")
print("[2] Subtraction")
print("[3] Multiplication")
print("[4] Division")
choice = float(input("Please Choose an Operator: "))
fn = float(input("Please Enter First Number: "))
sn = float(input("Please Enter Second Number: "))
sum = fn+sn
dif = fn-sn
prod = fn*sn
quo = fn/sn
if choice == 1:
    print("The Sum is ", sum)
elif choice == 2:
    print("The DIfference is ",dif)
elif choice == 3:
    print("The product is ",prod)
elif choice == 4:
    print("The Quotient is ",quo)
else:
    print("INVALID.")
