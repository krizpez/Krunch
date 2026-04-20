def verify_age(birth_date):
    from datetime import datetime
    today = datetime.utcnow()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age >= 18

# Example usage
if __name__ == '__main__':
    import datetime
    birth_date = datetime.datetime(2005, 4, 20)  # Replace with actual birth date
    if verify_age(birth_date):
        print("Access granted.")
    else:
        print("Access denied.")