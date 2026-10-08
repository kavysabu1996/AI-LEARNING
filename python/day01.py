
try:
    with open("python/sample.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print('File not found')

class AIProject:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def show_info(self):
        print("Project : ", self.name)
        print("Model : ", self.model)


aiproject = AIProject("ai agent", "gemini")
aiproject.show_info()

from utils import clean_text, add_numbers

print(clean_text("   Hello baby!.....    "))
print(add_numbers(1.2, 0.8))