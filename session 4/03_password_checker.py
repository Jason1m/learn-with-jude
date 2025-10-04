# Session 4: Password Checker - Step by Step Build

print("=" * 60)
print("BUILDING A PASSWORD CHECKER")
print("=" * 60)

print("Let's build a comprehensive password checker!")
print("We'll start simple and add features step by step.")

# STEP 1: Basic Password Check
print("\n" + "="*50)
print("STEP 1: BASIC PASSWORD CHECK")
print("="*50)

def basic_password_check():
    """Simple password check - just compare to a stored password"""
    stored_password = "mypassword123"
    
    user_password = input("Enter your password: ")
    
    if user_password == stored_password:
        print("✅ Password correct! Access granted.")
    else:
        print("❌ Password incorrect! Access denied.")

print("Testing basic password checker:")
# Uncomment the line below to test interactively
# basic_password_check()

# Let's test with code instead for demo purposes
def test_basic_check(password, correct_password="mypassword123"):
    """
    Test a password against the correct password and print the result.

    Args:
        password (str): The password to test.
        correct_password (str, optional): The correct password to compare against. Defaults to "mypassword123".
    """
    print(f"Testing password: {password}")
    if password == correct_password:
        print("✅ Password correct! Access granted.")
    else:
        print("❌ Password incorrect! Access denied.")
    print()

test_basic_check("mypassword123")  # Should pass
test_basic_check("wrongpassword")  # Should fail

# STEP 2: Password Length Checker
print("\n" + "="*50)
print("STEP 2: PASSWORD LENGTH REQUIREMENTS")
print("="*50)

def check_password_length(password, min_length=8):
    """Check if password meets minimum length requirement"""
    print(f"Checking password length...")
    print(f"Password length: {len(password)}")
    print(f"Required minimum: {min_length}")
    
    if len(password) >= min_length:
        print("✅ Password length is acceptable")
        return True
    else:
        print(f"❌ Password too short! Need at least {min_length} characters")
        return False

# Test password lengths
test_passwords = ["short", "medium123", "verylongpassword"]
for pwd in test_passwords:
    print(f"\nTesting: {pwd}")
    check_password_length(pwd)

# STEP 3: Password Complexity Checker
print("\n" + "="*50)
print("STEP 3: PASSWORD COMPLEXITY REQUIREMENTS")
print("="*50)

def check_password_complexity(password):
    """Check password for various complexity requirements"""
    print(f"Analyzing password complexity...")
    
    # Check for different character types
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
    
    print(f"Has lowercase letters: {has_lower}")
    print(f"Has uppercase letters: {has_upper}")
    print(f"Has numbers: {has_digit}")
    print(f"Has special characters: {has_special}")
    
    # Calculate complexity score
    complexity_score = sum([has_lower, has_upper, has_digit, has_special])
    
    if complexity_score >= 3:
        print("✅ Password has good complexity")
        return True
    else:
        print("❌ Password needs more complexity (mix of letters, numbers, symbols)")
        return False

# Test password complexity
test_passwords = ["password", "Password", "Password123", "Password123!"]
for pwd in test_passwords:
    print(f"\nTesting: {pwd}")
    check_password_complexity(pwd)

# STEP 4: Complete Password Validator
print("\n" + "="*50)
print("STEP 4: COMPLETE PASSWORD VALIDATOR")
print("="*50)

def validate_password_complete(password):
    """Complete password validation with all requirements"""
    print(f"Validating password: {'*' * len(password)}")
    print("-" * 40)
    
    is_valid = True
    
    # Check length
    if len(password) < 8:
        print("❌ Password must be at least 8 characters long")
        is_valid = False
    else:
        print("✅ Length requirement met")
    
    # Check for lowercase
    if not any(c.islower() for c in password):
        print("❌ Password must contain lowercase letters")
        is_valid = False
    else:
        print("✅ Contains lowercase letters")
    
    # Check for uppercase
    if not any(c.isupper() for c in password):
        print("❌ Password must contain uppercase letters")
        is_valid = False
    else:
        print("✅ Contains uppercase letters")
    
    # Check for numbers
    if not any(c.isdigit() for c in password):
        print("❌ Password must contain numbers")
        is_valid = False
    else:
        print("✅ Contains numbers")
    
    # Check for special characters
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if not any(c in special_chars for c in password):
        print("❌ Password must contain special characters")
        is_valid = False
    else:
        print("✅ Contains special characters")
    
    # Final result
    print("-" * 40)
    if is_valid:
        print("🎉 PASSWORD IS STRONG! ✅")
    else:
        print("💡 PASSWORD NEEDS IMPROVEMENT ❌")
    
    return is_valid

# Test the complete validator
test_passwords = [
    "weak",
    "password123",
    "Password123",
    "Password123!",
    "MySecureP@ss1"
]

for pwd in test_passwords:
    print(f"\n{'='*50}")
    validate_password_complete(pwd)

# STEP 5: Interactive Password Checker with Multiple Attempts
print("\n" + "="*50)
print("STEP 5: INTERACTIVE PASSWORD CHECKER")
print("="*50)

def interactive_password_checker():
    """Interactive password checker with multiple attempts"""
    max_attempts = 3
    attempts = 0
    
    print("Welcome to the Secure Password Checker!")
    print("Create a password that meets all requirements:")
    print("• At least 8 characters long")
    print("• Contains uppercase and lowercase letters")
    print("• Contains numbers")
    print("• Contains special characters (!@#$%^&*)")
    
    while attempts < max_attempts:
        attempts += 1
        print(f"\nAttempt {attempts}/{max_attempts}")
        
        password = input("Enter your new password: ")
        
        if validate_password_complete(password):
            print("\n🎉 Congratulations! Your password has been accepted!")
            return True
        else:
            if attempts < max_attempts:
                print(f"\n💡 Please try again. {max_attempts - attempts} attempts remaining.")
            else:
                print("\n❌ Maximum attempts reached. Please try again later.")
                return False
    
    return False

# Uncomment to test interactively:
# interactive_password_checker()

# STEP 6: Password Strength Meter
print("\n" + "="*50)
print("STEP 6: PASSWORD STRENGTH METER")
print("="*50)

def password_strength_meter(password):
    """Rate password strength from 1-5"""
    print(f"Analyzing password strength...")
    
    score = 0
    feedback = []
    
    # Length scoring
    if len(password) >= 12:
        score += 2
        feedback.append("✅ Excellent length")
    elif len(password) >= 8:
        score += 1
        feedback.append("✅ Good length")
    else:
        feedback.append("❌ Too short (minimum 8 characters)")
    
    # Character variety scoring
    if any(c.islower() for c in password):
        score += 1
        feedback.append("✅ Has lowercase letters")
    else:
        feedback.append("❌ Missing lowercase letters")
    
    if any(c.isupper() for c in password):
        score += 1
        feedback.append("✅ Has uppercase letters")
    else:
        feedback.append("❌ Missing uppercase letters")
    
    if any(c.isdigit() for c in password):
        score += 1
        feedback.append("✅ Has numbers")
    else:
        feedback.append("❌ Missing numbers")
    
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        score += 1
        feedback.append("✅ Has special characters")
    else:
        feedback.append("❌ Missing special characters")
    
    # Determine strength level
    if score >= 6:
        strength = "VERY STRONG 💪"
        stars = "⭐⭐⭐⭐⭐"
    elif score >= 5:
        strength = "STRONG 💪"
        stars = "⭐⭐⭐⭐"
    elif score >= 4:
        strength = "MODERATE 🔶"
        stars = "⭐⭐⭐"
    elif score >= 3:
        strength = "WEAK 🔸"
        stars = "⭐⭐"
    else:
        strength = "VERY WEAK 🔻"
        stars = "⭐"
    
    print(f"\nPassword Strength: {strength}")
    print(f"Rating: {stars} ({score}/6)")
    print("\nFeedback:")
    for item in feedback:
        print(f"  {item}")
    
    return score

# Test password strength meter
test_passwords = [
    "123",
    "password",
    "Password123",
    "MySecureP@ss1",
    "VeryLongAndSecurePassword123!"
]

for pwd in test_passwords:
    print(f"\n{'='*60}")
    print(f"Testing: {pwd}")
    password_strength_meter(pwd)

print("\n" + "="*60)
print("🎯 PASSWORD CHECKER COMPLETE!")
print("You've learned how to build a comprehensive password validation system!")
print("Key concepts covered:")
print("• Basic string comparison")
print("• Length validation")
print("• Character type checking")
print("• Complex conditional logic")
print("• User interaction and loops")
print("• Scoring and feedback systems")
print("="*60)