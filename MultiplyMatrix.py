print("MultiplyMatrix---> Colum Matrix A = Row of Matrix B")
r1 = int(input("Number of row for Matrix A :"))
c1 = int(input("Number of column for Matrix A :"))
r2 = int(input("Number of row for Matrix B :"))
c2 = int(input("Number of column for Matrix B :"))
if c1 != r2:
   print("\nERROR--> Column of Matrix A = Row of Matrix B") #ถ้าคอลัม A ไม่เท่ากับแถว B จะ Error
else:
   print("Enter element in matrix A :")
   A = []
   for i in range(r1):
       arrA = []
       for j in range(c1):
           arrA.append(int(input())) 
       A.append(arrA) #ใช้คำสั่ง append สำหรับเก็บใน list A
   print("Enter element in matrix B :")
   B = []
   for i in range(r2):
       arrB = []
       for j in range(c2):
           arrB.append(int(input()))
       B.append(arrB)  # ใช้คำสั่ง append สำหรับเก็บใน list B
   print("Matrix A =")
   for x in A:
       print(x)
   print("Matrix B =")
   for y in B:
       print(y)
   result = []
   for i in range(r1): 
       arrR = []
       for j in range(c2):
           arrR.append(0) 
       result.append(arrR)
   for i in range(len(A)):
       for j in range(len(B[0])):
           for k in range(len(B)):
               result[i][j] = A[i][k] * B[k][j] + result[i][j]
   print("Matrix_A X Matrix_B =")
   for res in result:
       print(res)


#63050095 กัญธิชา ไตรศรี