class LayoutCounter:

    def __init__(self):
        self.constraint_layout_count = 0
        self.recycler_view_count = 0

    def increment_constraint_layout_count(self):
        self.constraint_layout_count += 1

    def increment_recycler_view_count(self):
        self.recycler_view_count += 1
