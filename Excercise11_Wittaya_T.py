"""          *       1 = (0 * 2) + 1    เปรียบเทียบบรรทัด 1 กับ 5
            ***      3 = (1 * 2) + 1    ; บรรทัดทัดแรกมี 1 บรรทัดสุดท้าย มี 9 ห่างกัน 8
           *****     5 = (2 * 2) + 1      ถ้า input=5 บรรทัดแรกต้องต้องมีช่องว่างห่างกันข้างละ 4 รวมกันจะได้ 8
          *******    7 = (3 * 2) + 1      จะได้ space = (input-1)*2 แล้วต้องลดลงใน loop ที่ละ 1
         *********   9 = (4 * 2) + 1      จะได้ space -= 1 ใน loop
"""
userInput = int(input("number pyramid generator : "))
space = userInput
for i in range(userInput):
    print(space * 2 * " "," *" * (i*2+1))
    space -= 1
