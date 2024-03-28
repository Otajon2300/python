import re

def check_password_strength(password):
    # Parol uzunligi kamida 8 belgidan ko'proq bo'lishi kerak
    if len(password) < 8:
        return False, "Parol uzunligi 8 belgidan kam"
    
    # Parolda katta va kichik harflar bo'lishi kerak
    if not re.search("[a-z]", password):
        return False, "Kichik harf kam"
    if not re.search("[A-Z]", password):
        return False, "Katta harf kam"
    
    # Parolda sonlar bo'lishi kerak
    if not re.search("[0-9]", password):
        return False, "Sonlar kam"
    
    # Parolda ixtiyoriy belgilar bo'lishi kerak
    if not re.search("[@#$%^&+=]", password):
        return False, "Ixtiyoriy belgi kam"
    
    # Parol mukammal
    return True, "Parol mukammal"


# Foydalanuvchining parolini olish
password = input("Parolni kiriting: ")

# Parol mukammalligini tekshirish
result, message = check_password_strength(password)

# Natijani chiqarish
if result:
    print("Parol mukammal")
else:
    print("Parol mukammal emas: " + message)
