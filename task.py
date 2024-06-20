def update(self, description=None, deadline=None, priority=None, category=None, status=None):
    if description is not None:
        self.description = description
    if deadline is not None:
        self.deadline = deadline
    if priority is not None:
        self.priority = deadline
    if category is not None:
        self.category = category
    if status is not None:
        self.status = status

def change_status(self, new_status):
    self.status = new_status


def __str__(self):
    return f"Task ID: {self.id}\nDescription: {self.description}\nDeadline: {self.deadline}\nCategory: {self.category}\nStatus: {self.status}\n"