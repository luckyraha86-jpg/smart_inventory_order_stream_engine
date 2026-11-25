from database import Database

class Algorithms(Database):
    def sorting_orders(self, check):
        orders = self.load_file()
        if check == 1:
            for i in range(len(orders)):
                for j in range(0, len(orders)-i-1):
                    if orders[j]["amount"] < orders[j+1]["amount"]:
                        orders[j], orders[j+1] = orders[j+1], orders[j]

        elif check == 2:
            for i in range(1, len(orders)):
                key = orders[i]
                j = i - 1
                while j >= 0 and orders[j]["amount"] > key["amount"]:
                    orders[j + 1] = orders[j]
                    j -= 1

                orders[j + 1] = key
                
        return orders

    def searching_id(self, id):
        orders = self.load_file()
        for i in range(len(orders)):
            min_index = i
            for j in range(i + 1, len(orders)):
                if orders[min_index]["id"] > orders[j]["id"]:
                    min_index = j

            if min_index != i:
                orders[i], orders[min_index] = orders[min_index], orders[i]

        left = 0
        right = len(orders) - 1
        
        while left <= right:
            middle = (right + left) // 2
            if orders[middle]["id"] == id:
                return orders[middle]
            elif orders[middle]["id"] < id:
                left = middle + 1
            else:
                right = middle - 1
       
        return "Id not Found!"

