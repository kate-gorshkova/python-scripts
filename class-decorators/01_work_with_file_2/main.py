class File:
    def __init__(self, file_name, mood):
        self.file_name, self.mood = file_name, mood

    def __enter__(self):
        try:
            self.file = open(self.file_name, self.mood)
        except FileNotFoundError:
            self.file = open(self.file_name, "w")

        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if FileExistsError or FileNotFoundError:
            return True


with File("example.txt", "w") as file:
    file.write("Всем привет!")

with File("example1.txt", "r") as file1:
    file1.read()

# зачёт!
