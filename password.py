import re

def check_password_strength(password):
    feedback = []
    strength_score = 0

    # Length check
    if len(password) >= 8:
        strength_score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Uppercase check
    if re.search(r'[A-Z]', password):
        strength_score += 1
    else:
        feedback.append("❌ Add at least one uppercase letter.")

    # Lowercase check
    if re.search(r'[a-z]', password):
        strength_score += 1
    else:
        feedback.append("❌ Add at least one lowercase letter.")

    # Digit check
    if re.search(r'\d', password):
        strength_score += 1
    else:
        feedback.append("❌ Add at least one number.")

    # Special character check
    if re.search(r'[^A-Za-z0-9]', password):
        strength_score += 1
    else:
        feedback.append("❌ Add at least one special character (e.g., @, #, $, etc.).")

    # Strength rating
    if strength_score == 5:
        strength = "🔒 Strong"
    elif strength_score >= 3:
        strength = "🔐 Moderate"
    else:
        strength = "🔓 Weak"

    return strength, feedback

def main():
    print("🔍 Password Strength Checker 🔍")
    password = input("Enter your password: ")
    
    strength, feedback = check_password_strength(password)
    
    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("\nSuggestions to improve:")
        for suggestion in feedback:
            print(f" - {suggestion}")
    else:
        print("✅ Great job! Your password is strong.")

if __name__ == "__main__":
    main()
