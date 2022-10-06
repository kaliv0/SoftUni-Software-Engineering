from typing import List


class EmailValidator:
    def __init__(self, min_length: int, mails_list: List[str], domains_list: List[str]):
        self._min_length = min_length
        self._mails = mails_list
        self._domains = domains_list

    def __is_name_valid(self, name):
        return len(name) >= self._min_length

    def __is_mail_valid(self, mail):
        return mail in self._mails

    def __is_domain_valid(self, domain):
        return domain in self._domains

    def validate(self, email):
        name, tail = email.split("@")
        email, domain = tail.split(".")
        return self.__is_name_valid(name) and self.__is_mail_valid(email) and self.__is_domain_valid(domain)


if __name__ == "__main__":
    mails = ["gmail", "softuni"]
    domains = ["com", "bg"]
    email_validator = EmailValidator(6, mails, domains)
    print(email_validator.validate("pe77er@gmail.com"))
    print(email_validator.validate("georgios@gmail.net"))
    print(email_validator.validate("stamatito@abv.net"))
    print(email_validator.validate("abv@softuni.bg"))
