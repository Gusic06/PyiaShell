"""Some failed experiment idk"""
import random

class PyiaObfuscator:

    def __init__(self, file):
        self.regex = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789(){}[]-_+=*&^%$£!,.<>~#@";:`¬|\\'
        with open(file, "r") as file:
            self.contents = file.read()

    def __index__(self, step):
        self.step = step
        self.step = random.randint(1, len(self.junk_data))

    def random_string_generator(self, str_size, allowed_chars):
        self._junk = ''.join(random.SystemRandom().choice(allowed_chars) for i in range(str_size))
        return self._junk

    def obfuscate(self, file):
        self.items = file
        self.junk_data = self.random_string_generator(80, self.regex)
        print(self.junk_data)
        self.step = random.randint(1, len(self.junk_data))
        self.__index__(self.step)
        if self.step < 10:
            self.step = str(self.step)
            self.step = f"0{self.step}"
            self.step = int(self.step)
        self.new_contents = f"{self.junk_data}[{self.step}:]{self.contents}[{self.step}]"
        with open(self.items, "w") as file:
            file.write(f"{self.new_contents}")

    def get_obfuscation_step(self, file):
        self.items = file
        with open(self.items, "r") as file:
            self.key: int = file.read()
        self.step: str = f"{self.key}[:4]"
        return f"{self.key}[:4]"
        
    def deobfuscate(self, file):
        self.items = file
        with open(self.items, "r") as file:
            self.contents: str = file.read()
        self.get_obfuscation_step(self.items)
        self.deobfuscated_text: str = f"{self.contents}[{self.step}:4]"
        print(self.deobfuscated_text)
        return self.deobfuscated_text


if __name__ == "__main__":
    main = PyiaObfuscator("test.txt")
    main.obfuscate("test.txt")
    main.deobfuscate("test.txt")