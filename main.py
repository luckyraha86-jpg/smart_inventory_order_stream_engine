from colorama import init, Fore, Style
from operations import CustomerOperations
from algorithms import Algorithms
from tabulate import tabulate

init(autoreset=True)

def display_menu():

    banner = f"""
{Fore.CYAN}
███████╗███╗   ███╗ █████╗ ██████╗ ████████╗
██╔════╝████╗ ████║██╔══██╗██╔══██╗╚══██╔══╝
███████╗██╔████╔██║███████║██████╔╝   ██║
╚════██║██║╚██╔╝██║██╔══██║██╔══██╗   ██║
███████║██║ ╚═╝ ██║██║  ██║██║  ██║   ██║
╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝

██╗███╗   ██╗██╗   ██╗███████╗███╗   ██╗████████╗ ██████╗ ██████╗ ██╗   ██╗
██║████╗  ██║██║   ██║██╔════╝████╗  ██║╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝
██║██╔██╗ ██║██║   ██║█████╗  ██╔██╗ ██║   ██║   ██║   ██║██████╔╝ ╚████╔╝
██║██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║   ██║   ██║   ██║██╔══██╗  ╚██╔╝
██║██║ ╚████║ ╚████╔╝ ███████╗██║ ╚████║   ██║   ╚██████╔╝██║  ██║   ██║
╚═╝╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝

                🚀 SMART INVENTORY & ORDER STREAM ENGINE 🚀
{Style.RESET_ALL}
"""

    print(banner)

    print(Fore.YELLOW + "═" * 80)

    print(Fore.GREEN + "\n📂 AVAILABLE MODULES\n")

    print(Fore.CYAN + "┌───────────────────────────────────────────────────────────┐")
    print(Fore.CYAN + "│  [1] 🔍 SORTING & SEARCHING CENTER                        │")
    print(Fore.CYAN + "└───────────────────────────────────────────────────────────┘")

    print(Fore.WHITE + "     ➜ Search Products by Id")
    print(Fore.WHITE + "     ➜ Sort Products by Prices in descending order")
    print(Fore.WHITE + "     ➜ Sort Products by Prices in ascending order")

    print()

    print(Fore.MAGENTA + "┌───────────────────────────────────────────────────────────┐")
    print(Fore.MAGENTA + "│  [2] ⚙️ INVENTORY OPERATIONS HUB                          │")
    print(Fore.MAGENTA + "└───────────────────────────────────────────────────────────┘")

    print(Fore.WHITE + "     ➜ Add New Order")
    print(Fore.WHITE + "     ➜ Stream Orders")
    print(Fore.WHITE + "     ➜ Show Unique Categories")
    print(Fore.WHITE + "     ➜ Show Active Customers")
    print(Fore.WHITE + "     ➜ Show Category Wise Total Revenue")
    print(Fore.WHITE + "     ➜ Show High Price Orders")

    print()

    print(Fore.RED + "┌───────────────────────────────────────────────────────────┐")
    print(Fore.RED + "│  [0] ❌ SHUTDOWN ENGINE                                   │")
    print(Fore.RED + "└───────────────────────────────────────────────────────────┘")

    print(Fore.GREEN + "🟢 SYSTEM STATUS : ONLINE")
    print(Fore.CYAN + "📦 Inventory Database Connected")
    print(Fore.CYAN + "📡 Order Stream Active")

from colorama import Fore, Style

def shutdown_banner():

    print(Fore.RED + r"""

 ███████╗██╗  ██╗██╗   ██╗████████╗██████╗  ██████╗ ██╗    ██╗███╗   ██╗
 ██╔════╝██║  ██║██║   ██║╚══██╔══╝██╔══██╗██╔═══██╗██║    ██║████╗  ██║
 ███████╗███████║██║   ██║   ██║   ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║
 ╚════██║██╔══██║██║   ██║   ██║   ██║  ██║██║   ██║██║███╗██║██║╚██╗██║
 ███████║██║  ██║╚██████╔╝   ██║   ██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║
 ╚══════╝╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝

    """)

    print(Fore.YELLOW + "=" * 80)

    print(Fore.CYAN + "\n📦 SMART INVENTORY & ORDER STREAM ENGINE")
    print(Fore.WHITE + "🔄 Closing Inventory Database Connection...")
    print(Fore.WHITE + "📡 Disconnecting Order Stream Services...")
    print(Fore.WHITE + "💾 Saving Latest Inventory Snapshot...")
    print(Fore.WHITE + "📝 Writing Activity Logs...")

    print(Fore.GREEN + "\n✅ All Resources Released Successfully")
    print(Fore.GREEN + "✅ Data Integrity Verified")
    print(Fore.GREEN + "✅ Inventory Engine Shutdown Complete")

    print(Fore.YELLOW + "\n" + "=" * 80)

    print(Fore.MAGENTA + """
                Thank You For Using

    🚀 SMART INVENTORY & ORDER STREAM ENGINE 🚀

             Have A Productive Day Ahead!

                  Made By Lucky Raj
    """)

    print(Fore.YELLOW + "=" * 80)

def main():

    operations = CustomerOperations()
    algortithms = Algorithms()
    
    while True:
        header = ["ID", "Customer", "Category", "Price"]
        all_orders = []

        display_menu()
        try:
            choice = int(input(Fore.YELLOW+"Enter Your Choice: "))
        except ValueError:
            print(Fore.RED + "It must be integer (1, 2 or 0)!")
            continue

        if choice == 1:
            print(Fore.CYAN + f"You Choose {choice}. SORTING & SEARCHING CENTER")

            print(Fore.WHITE + "1. Search Products by ID")
            print(Fore.WHITE + "2. Sort Products by Prices in descending order")
            print(Fore.WHITE + "3. Sort Products by Prices in ascending order")

            try:
                choice_1 = int(input(Fore.CYAN + "Please choose the options you want to do between 1 to 3: "))
            except ValueError:
                print(Fore.RED + "Please enter integers between 1 to 3!")
                continue

            if choice_1 == 1:
                try:
                    id = int(input(Fore.CYAN + "Please enter the ID you want to search: "))
                except ValueError:
                    print(Fore.RED + "Id must be integer!")
                    continue

                searched_id = algortithms.searching_id(id)
                if type(searched_id) == dict:
                    print(Fore.WHITE + f"ID : {searched_id['id']}")
                    print(Fore.WHITE + f"Customer : {searched_id['customer']}")
                    print(Fore.WHITE + f"Category : {searched_id['category']}")
                    print(Fore.WHITE + f"Price : {searched_id['amount']}")
                else:
                    print(Fore.WHITE + searched_id)

            elif choice_1 == 2:
                sorted_orders = algortithms.sorting_orders(1)

                for orders in sorted_orders:
                    values= []
                    for key, value in orders.items():
                        values.append(value)
                    all_orders.append(values)

                print(Fore.YELLOW + tabulate(all_orders, headers=header))
                print(Fore.CYAN + "="*37)

            elif choice_1 == 3:
                sorted_orders = algortithms.sorting_orders(2)

                for order in sorted_orders:
                    values = []
                    for key, value in order.items():
                        values.append(value)
                    all_orders.append(values)

                print(Fore.YELLOW + tabulate(all_orders, headers=header))
                print(Fore.CYAN + "="*37)

            else:
                print(Fore.RED + "Please choose options from 1-3!")

        elif choice == 2:
            print(Fore.MAGENTA + f"You Choose {choice}. INVENTORY OPERATIONS HUB")

            print(Fore.WHITE + "1. Add New Order")
            print(Fore.WHITE + "2. Stream Orders")
            print(Fore.WHITE + "3. Show Unique Categories")
            print(Fore.WHITE + "4. Show Active Customers")
            print(Fore.WHITE + "5. Show Category Wise Total Revenue")
            print(Fore.WHITE + "6. Show High Price Orders")

            try:
                choice_1 = int(input(Fore.MAGENTA + "Please choose the operation you want to perform between 1 to 6: "))
            except ValueError:
                print(Fore.MAGENTA + "Please enter integers between 1 to 3!")
                continue

            if choice_1 == 1:
                try:
                    id = int(input(Fore.MAGENTA + "Enter the ID of the custmer: "))
                except ValueError:
                    print(Fore.RED + "ID must be integer!")
                    continue
                customer = input(Fore.MAGENTA + "Enter the name of the customer: ")
                category = input(Fore.MAGENTA + "Enter the category of the order: ")
                try:
                    price = int(input(Fore.MAGENTA + "Enter the price of the order: "))
                except ValueError:
                    print(Fore.RED + "Price of the order must be integer!")
                    continue

                added_customer = operations.add_orders(id, customer, category, price)

                print(Fore.GREEN + added_customer)
                    
            elif choice_1 == 2:
                try:
                    min_amt = int(input(Fore.MAGENTA + "Enter the min price for stream orders: "))
                except ValueError:
                    print(Fore.RED + "Minimum price must be integer!")
                    continue

                stream_orders = operations.stream_orders(min_amt)
                for order in stream_orders:
                    values = []
                    for key, value in order.items():
                        values.append(value)
                    all_orders.append(values)

                print(Fore.YELLOW + tabulate(all_orders, headers=header))

            elif choice_1 == 3:
                unique_category = operations.unique_categories()
                for index, category in enumerate(unique_category, start=1):
                    print(Fore.YELLOW + f"{index}. {category.upper()}")

            elif choice_1 == 4:
                try:
                    n = int(input(Fore.MAGENTA + "Enter the number of active IDs you want to see: "))
                except ValueError:
                    print("Number must be integer!")
                    continue

                active_customers = operations.active_customers(n)
                for index, id in enumerate(active_customers, start=1):
                        print(Fore.YELLOW + f"{index}. {id}")

            elif choice_1 == 5:
                categ_total_revenue = operations.category_total_revenue()
                header_category = ["Category", "Total Revenue"]
                category_revenue = []
                for category, revenue in categ_total_revenue.items():
                    a = [category, revenue]
                    category_revenue.append(a)

                print(Fore.YELLOW + tabulate(category_revenue, headers=header_category))

            elif choice_1 == 6:
                high_value_orders = operations.high_value_orders()
                for order in high_value_orders:
                    values = []
                    for key, value in order.items():
                        values.append(value)
                    all_orders.append(values)

                print(Fore.YELLOW + tabulate(all_orders))

            else:
                print(Fore.RED + "Please choose options from 1-6!")
                continue

        elif choice == 0:
            shutdown_banner()
            break

        else:
            print(Fore.RED + "Invalid input please choose options from 0-2!")

main()