print("CALCULATOR")
oper=input("""
Select The Operation

1 - Add
2 - Substract
3 - Multiply
4 - Divide

Enter Your Option : """)

if oper == "1":
    num1 = int(input("Enter The First Number :"))
    num2 = int(input("Enter The Second Number :"))
    sum = num1 + num2
    print("+--------------+")
    print("  sum = "+str(sum))
    print("""+-------------+
    THANK YOU!
        """)

elif oper == "2":
    num1 = int(input("Enter The First Number :"))
    num2 = int(input("Enter The Second Number :"))
    sum = num1 - num2
    print("+-------------+")
    print("  sum = "+str(sum))
    print("""+-------------+
    THANK YOU!
    """)

elif oper == "3":
    num1 = int(input("Enter The First Number :"))
    num2 = int(input("Enter The Second Number :"))
    sum = num1 * num2
    print("+-------------+")
    print("sum = "+str(sum))
    print("""+-------------+
    THANK YOU!
        """)

elif oper == "4":
    num1 = int(input("Enter The First Number :"))
    num2 = int(input("Enter The Second Number :"))
    sum = num1 / num2
    print("+-------------+")
    print("  sum = "+str(sum))
    print("""+-------------+
    THANK YOU!
        """)

elif oper == "":
    print("ERROR...Can't Be Blank!")

else: print("""More Operations Added Soon!
          THANK YOU!
""")
