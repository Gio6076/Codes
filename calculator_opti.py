choice, fn, sn = float(input("[1] Addition\n[2] Subtraction\n[3] Multiplication\n[4] Division\nPlease choose an Operator: ")), float(input("Please Enter the First Number: ")), float(input("Please Enter the Second Number: "))
if choice == 1: print("The Sum is ",fn + sn)
elif choice == 2: print ("The Difference is ",fn - sn)
elif choice == 3: print ("The Product is ",fn * sn)
elif choice == 4: print ("The Quotient is ", fn/sn)
else: print("INVALID.")
