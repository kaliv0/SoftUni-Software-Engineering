class Programmer:
    def __init__(self, name: str, language: str, skills: int):
        self._name = name
        self._language = language
        self._skills = skills

    @property
    def name(self):
        return self._name

    @property
    def language(self):
        return self._language

    @property
    def skills(self):
        return self._skills

    def watch_course(self, course_name: str, language: str, skills_earned: int) -> str:
        if language == self._language:
            self._skills += skills_earned
            return f"{self._name} watched {course_name}"
        return f"{self.name} does not know {language}"

    def change_language(self, new_language: str, skills_needed: int) -> str:
        if self._skills >= skills_needed:
            if self._language != new_language:
                previous_language = self._language
                self._language = new_language
                return f"{self._name} switched from {previous_language} to {new_language}"
            return f"{self._name} already knows {self._language}"
        return f"{self._name} needs {skills_needed - self._skills} more skills"


if __name__ == "__main__":
    programmer = Programmer("John", "Java", 50)
    print(programmer.watch_course("Python Masterclass", "Python", 84))
    print(programmer.change_language("Java", 30))
    print(programmer.change_language("Python", 100))
    print(programmer.watch_course("Java: zero to hero", "Java", 50))
    print(programmer.change_language("Python", 100))
    print(programmer.watch_course("Python Masterclass", "Python", 84))
