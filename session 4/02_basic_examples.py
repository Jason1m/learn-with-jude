# Session 4: Basic Examples - If/Else Decision Making

print("=" * 50)
print("BASIC IF/ELSE EXAMPLES")
print("=" * 50)

# Example 1: Simple Age Check
print("\n1. SIMPLE AGE CHECK")
print("-" * 25)

def age_check_demo():
    age = 20
    print(f"Person's age: {age}")
    
    if age >= 18:
        print("✅ This person is an adult")
    else:
        print("❌ This person is a minor")

age_check_demo()

# Example 2: Number Comparison
print("\n2. NUMBER COMPARISON")
print("-" * 25)

def number_comparison():
    num1 = 15
    num2 = 10
    print(f"Comparing {num1} and {num2}")
    
    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    elif num1 < num2:
        print(f"{num1} is less than {num2}")
    else:
        print(f"{num1} is equal to {num2}")

number_comparison()

# Example 3: Grade Calculator
print("\n3. GRADE CALCULATOR")
print("-" * 25)

def grade_calculator(score):
    print(f"Score: {score}")
    
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Test different scores
scores = [95, 87, 72, 65, 45]
for score in scores:
    grade = grade_calculator(score)
    print(f"Score {score} = Grade {grade}")

# Example 4: Weather Advisor
print("\n4. WEATHER ADVISOR")
print("-" * 25)

def weather_advisor(weather, temperature):
    print(f"Weather: {weather}, Temperature: {temperature}°F")
    
    if weather == "sunny":
        if temperature > 80:
            advice = "Perfect day! Go to the beach! 🏖️"
        elif temperature > 65:
            advice = "Great day for outdoor activities! 🌞"
        else:
            advice = "Sunny but cool. Bring a light jacket! 🧥"
    elif weather == "rainy":
        advice = "Stay inside or bring an umbrella! ☔"
    elif weather == "snowy":
        advice = "Bundle up and be careful driving! ❄️"
    else:
        advice = "Check the weather forecast! 🌤️"
    
    print(f"Advice: {advice}")
    return advice

# Test different weather conditions
weather_advisor("sunny", 85)
weather_advisor("sunny", 60)
weather_advisor("rainy", 70)
weather_advisor("snowy", 25)

# Example 5: Password Validator
print("\n5. PASSWORD VALIDATOR")
print("-" * 25)

def validate_password(password):
    print(f"Checking password: {'*' * len(password)}")
    
    # Check length
    if len(password) < 8:
        print("❌ Password too short (minimum 8 characters)")
        return False
    
    # Check for numbers
    has_number = any(char.isdigit() for char in password)
    if not has_number:
        print("❌ Password must contain at least one number")
        return False
    
    # Check for uppercase
    has_upper = any(char.isupper() for char in password)
    if not has_upper:
        print("❌ Password must contain at least one uppercase letter")
        return False
    
    print("✅ Password is strong!")
    return True

# Test different passwords
passwords = ["weak", "password123", "Password123", "Pass1"]
for pwd in passwords:
    print(f"\nTesting: {pwd}")
    validate_password(pwd)

# Example 6: Simple Login System
print("\n6. SIMPLE LOGIN SYSTEM")
print("-" * 25)

def simple_login(username, password):
    # Stored credentials (in real life, these would be in a database)
    correct_username = "admin"
    correct_password = "secret123"
    
    print(f"Login attempt - Username: {username}")
    
    if username == correct_username and password == correct_password:
        print("✅ Login successful! Welcome!")
        return True
    elif username != correct_username:
        print("❌ Invalid username")
        return False
    else:
        print("❌ Invalid password")
        return False

# Test login attempts
print("Valid login:")
simple_login("admin", "secret123")

print("\nInvalid username:")
simple_login("user", "secret123")

print("\nInvalid password:")
simple_login("admin", "wrongpass")

# Example 7: Even or Odd Checker
print("\n7. EVEN OR ODD CHECKER")
print("-" * 25)

def check_even_odd(number):
    print(f"Checking if {number} is even or odd...")
    
    if number % 2 == 0:
        print(f"{number} is EVEN")
    else:
        print(f"{number} is ODD")

# Test various numbers
numbers = [2, 7, 10, 15, 0]
for num in numbers:
    check_even_odd(num)

# Example 8: Shopping Cart Total
print("\n8. SHOPPING CART TOTAL")
print("-" * 25)

def calculate_total(cart_amount, member_status):
    print(f"Cart total: ${cart_amount}")
    print(f"Member status: {member_status}")
    
    # Apply discounts based on conditions
    if member_status == "premium" and cart_amount > 100:
        discount = 0.20  # 20% discount
        final_total = cart_amount * (1 - discount)
        print(f"Premium member + $100+ purchase: 20% discount applied")
    elif member_status == "premium":
        discount = 0.10  # 10% discount
        final_total = cart_amount * (1 - discount)
        print(f"Premium member: 10% discount applied")
    elif cart_amount > 50:
        discount = 0.05  # 5% discount
        final_total = cart_amount * (1 - discount)
        print(f"Large purchase: 5% discount applied")
    else:
        discount = 0
        final_total = cart_amount
        print("No discount applied")
    
    print(f"Final total: ${final_total:.2f}")
    return final_total

# Test different scenarios
calculate_total(150, "premium")
calculate_total(75, "premium")
calculate_total(80, "regular")
calculate_total(30, "regular")

print("\n" + "=" * 50)
print("🎯 These examples show common if/else patterns!")
print("Practice these to build your decision-making skills!")
print("=" * 50)