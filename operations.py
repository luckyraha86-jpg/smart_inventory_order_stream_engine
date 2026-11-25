from database import Database
from collections import Counter

class CustomerOperations(Database):
    def add_orders(self, order_id, customer, category, amount):
        old_data = self.load_file()
        new_data = {
            "id" : order_id,
            "customer" : customer,
            "category" : category,
            "amount" : amount
        }
        old_data.append(new_data)
        self.save_data(old_data)
        return f"The customer with order id: {order_id} and amount: {amount} has been successfully added in the database."

    def stream_orders(self, min_amount=0):
        orders = self.load_file()
        for order in orders:
            if order['amount'] >= min_amount:
                yield order

    def unique_categories(self):
        orders = self.load_file()
        categories = [
            order["category"]
            for order in orders
        ]

        unique_category = [
            category
            for category in categories
            if categories.count(category) == 1
        ]

        return unique_category

    def active_customers(self, n):
        orders = self.load_file()
        id = [
            order["id"]
            for order in orders
        ]

        count_id = list(Counter(id))
        active_id = []

        for i in range(n):
            if count_id:
                active_id.append(max(count_id))
                count_id.remove(max(count_id))
            else:
                break
        return active_id

    def category_total_revenue(self):
        orders = self.load_file()
        total_revenue = {}
        
        for order in orders:
            if order["category"] not in total_revenue:
                total_revenue[order["category"]] = []
            total_revenue[order["category"]].append(order["amount"])

        for category, prices in total_revenue.items():
            total_revenue[category] = sum(prices)

        return total_revenue

    def high_value_orders(self):
        orders = self.load_file()
        price_id = {
            order["amount"] : order["id"]
            for order in orders
        }

        max_amt = []
        if len(orders) >= 3:
            for i in range(3):
                f = max(price_id)
                max_amt.append((f, price_id[f]))
                price_id.pop(f)

        high_orders = [
            order
            for order in orders
            for amt, id in max_amt
            if order["amount"] == amt and order["id"] == id
        ]

        return high_orders

