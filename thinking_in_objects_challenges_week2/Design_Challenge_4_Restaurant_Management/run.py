"""
Design Challenge 4: Restaurant Management
There is a restaurant which has many of its branch at various location. The restaurant offers a wide
range of menu and there is also a special menu where a discount of 30% is given. Every menu is
composed of minimum 3 course category have its own items.
Design the OO model for the above problem statement and implement the code to
• List the total number of menu items
• List all the menu items for a particular course category
• List all the special discount menu
"""
from restaurant import (
    RestaurantBranch,
    Menu,
    SpecialMenu,
    CourseCategory,
    MenuItem,
    RestaurantManager,
)

branch = RestaurantBranch(1, "Rameshwaram Cafe")

regular_menu = Menu(1, "South Indian Menu", branch)
special_menu = SpecialMenu(2, "Festival Special Menu", branch, discount_percent=30.0)

appetizer = CourseCategory(1, "Appetizer")
main_course = CourseCategory(2, "Main")

dessert = CourseCategory(3, "Dessert")

appetizer.add_item(MenuItem(1, "Medu Vada", 60.0))

main_course.add_item(MenuItem(2, "Masala Dosa", 120.0))
main_course.add_item(MenuItem(3, "Idli Sambar", 80.0))


dessert.add_item(MenuItem(4, "Kesari Bath", 70.0))

regular_menu.add_course_category(appetizer)
regular_menu.add_course_category(main_course)


regular_menu.add_course_category(dessert)

s_appetizer = CourseCategory(4, "Appetizer")
s_main = CourseCategory(5, "Main")

s_dessert = CourseCategory(6, "Dessert")

s_appetizer.add_item(MenuItem(5, "Ghee Pongal", 100.0))
s_main.add_item(MenuItem(6, "Paper Roast Dosa", 150.0))


s_dessert.add_item(MenuItem(7, "Mysore Pak", 90.0))

special_menu.add_course_category(s_appetizer)

special_menu.add_course_category(s_main)

special_menu.add_course_category(s_dessert)

manager = RestaurantManager()

manager.add_menu(regular_menu)

manager.add_menu(special_menu)

print("Total menu items:", manager.total_menu_items())

print("\nItems for course 'Appetizer':")
for it in manager.get_items_by_course("Appetizer"):
    print("-", it.item_name, "₹" + str(it.price))



print("\nSpecial menus:")
for sm in manager.get_special_menus():
    print("-", sm.menu_name, f"({sm.discount_percent}%)")
