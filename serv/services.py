class Services:
    def __init__(self, table_width):
        self.table_width = table_width

    def sp(self, space_holder):
        return "\n" + space_holder + " " * (self.table_width - len(space_holder) - 1) + "|\n" + '=' * self.table_width

