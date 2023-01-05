import pyperclip


def input_result(browser):
    result = browser.switch_to.alert.text.split()[-1:]
    print(*result)
    pyperclip.copy(*result)
