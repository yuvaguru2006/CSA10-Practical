def signup(username, password):
    if not username:
        return "Username is required"
    elif len(password) < 6:
        return "Password must be at least 6 characters"
    else:
        return "Signup successful"


print(signup("student", "hello123"))