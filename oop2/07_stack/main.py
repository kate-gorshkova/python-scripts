class Stack:
    def __init__(self):
        self.my_list = []

    def __str__(self):
        return "; ".join(self.my_list)

    def add(self, task):
        self.my_list.append(task)

    def pop(self):
        if len(self.my_list) != 0:
            return self.my_list.pop()
        return None


class TaskManager:
    def __init__(self):
        self.tasks = dict()

    def new_task(self, task, num):
        if num not in self.tasks:
            self.tasks[num] = Stack()
        self.tasks[num].add(task)

    def delete(self, num):
        self.tasks[num].pop()

    def __str__(self):
        info = []
        if self.tasks:
            for i_num in sorted(self.tasks.keys()):
                info.append("{} {}\n".format(str(i_num), self.tasks[i_num]))

        return "".join(info)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
manager.delete(2)
print(manager)

# зачёт!
