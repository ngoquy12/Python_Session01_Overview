# Cú pháp: tên_biến toán tử gán giá trị
import this
firstNumber = 10  # Khai báo biến kiểu số int
secondNumber = 10.6  # Khái báo biến kiểu số thực
userName = "Nguyễn Văn Nam"  # Khái báo biến kiểu chuỗi
isMarried = True  # Khái báo biến kiểu boolean (True / False)

print(firstNumber)

# Nối chuỗi trong python
print(f"Tôi tên là: {userName}, Năm nay tôi {firstNumber} tuổi")

# Ép kiểu dữ liệu
print(str(123))  # Ép giá trị kiểu int = 123 sang chuỗi

# Kiểm tra kiểu dữ liệu của một biến
print(f"Kiểu dữ liệu của biến firstNumber là: {type(firstNumber)}")


# Nhập xuất dữ liệu
# numberA = input("Enter number A: ")
# numberB = input("Enter number B: ")

# print(
#     f"Kiểu dữ liệu là: {type(numberA)} - {type(numberB)}")

# print(f"{numberA} + {numberB} = {int(numberA) + int(numberB)}")

# Biến trong python
a = 10
print(f"Địa chỉ của a trước: {id(a)}")
a = 20
print(f"Địa chỉ của a sau: {id(a)}")
b = a
print(f"Địa chỉ của biến a trong bộ nhớ: {id(a)}")
print(f"Địa chỉ của biến b trong bộ nhớ: {id(b)}")
print(id(a) == id(b))
