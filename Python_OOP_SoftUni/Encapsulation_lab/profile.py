import re


class Profile:
    def __init__(self, username_input: str, password_input: str):
        self._username = None
        self.username = username_input

        self._password = None
        self.password = password_input

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not 5 < len(value) < 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        else:
            self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        valid = True
        if len(value) < 8:
            valid = False
        elif not re.search("\d", value):
            valid = False
        elif not re.search("[A-Z]", value):
            valid = False

        if not valid:
            raise TypeError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        else:
            self._password = value

    def __str__(self):
        return f"You have a profile with username: \"{self._username}\" and password: {'*' * len(self._password)}"


if __name__ == "__main__":
    profile_with_invalid_password = Profile('My_username', 'My-password')
    profile_with_invalid_username = Profile('Too_long_username', 'Any')
    correct_profile = Profile("Username", "Passw0rd")
    print(correct_profile)
