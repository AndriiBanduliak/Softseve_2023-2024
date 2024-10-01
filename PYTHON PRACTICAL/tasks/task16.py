class Testpaper:
    def __init__(self, subject, markscheme, pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark


class Student:
    def __init__(self):
        self.tests_taken = "No tests taken"

    def take_test(self, testpaper, answers):
        if self.tests_taken == "No tests taken":
            self.tests_taken = {}

        correct_answers = sum(1 for i in range(
            len(answers)) if answers[i] == testpaper.markscheme[i])
        total_questions = len(testpaper.markscheme)
        percentage = (correct_answers / total_questions) * 100
        pass_mark = int(testpaper.pass_mark.strip('%'))

        if percentage >= pass_mark:
            result = f"Passed! ({percentage:.0f}%)"
        else:
            result = f"Failed! ({percentage:.0f}%)"

        self.tests_taken[testpaper.subject] = result
