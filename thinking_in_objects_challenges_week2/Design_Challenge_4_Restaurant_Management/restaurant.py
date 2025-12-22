class RestaurantBranch:
    def __init__(self, branch_id, branch_name):
        self.branch_id = branch_id

        self.branch_name = branch_name


class Menu:
    def __init__(self, menu_id, menu_name, branch):
        self.menu_id = menu_id
        self.menu_name = menu_name

        self.branch = branch
        self.course_categories = []

    def add_course_category(self, category):
        self.course_categories.append(category)


class SpecialMenu(Menu):
    def __init__(self, menu_id, menu_name, branch, discount_percent=30.0):
        super().__init__(menu_id, menu_name, branch)


        self.discount_percent = discount_percent


class CourseCategory:
    def __init__(self, category_id, category_name):

        self.category_id = category_id

        self.category_name = category_name
        self.items = []

    def add_item(self, item):
        self.items.append(item)


class MenuItem:
    def __init__(self, item_id, item_name, price):
        self.item_id = item_id
        self.item_name = item_name
        
        self.price = price


class RestaurantManager:
    def __init__(self):
        self.menus = []

    def add_menu(self, menu):
        self.menus.append(menu)

    def total_menu_items(self):
        total = 0
        for m in self.menus:
            for c in m.course_categories:
                total += len(c.items)
        return total

    def get_items_by_course(self, course_name):
        result = []
        for m in self.menus:
            for c in m.course_categories:
                if c.category_name == course_name:
                    result.extend(c.items)
        return result

    def get_special_menus(self):
        return [m for m in self.menus if isinstance(m, SpecialMenu)]
