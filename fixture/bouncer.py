def check_admission(age):
    
    if age < 0 :
        raise ValueError("Age cannot be negative")
    if age >=18:
        return "Welcome to the VIP Club!"
    else:
        return "Access Denied"

    