# CREATING QUEUE CLASS.
# AUTHOR: CodeWithSalman
class Queue:
    # CREATING CONSTRUCTOR.
    def __init__(self):
        self.items = []
    # CHECKING QUEUE IS EMPTY OR NOT.
    def is_Empty(self):
        return len(self.items) == 0
    # ADDING DATA INTO THE QUEUE USING ENQUEUE METHOD.
    def enqueue(self, item):
        self.items.append(item)
    # REMOVING DATA ACCORDING TO QUEUE RULE THAT IS "FIFO[FIRST-IN FIRST-OUT]".
    def dequeue(self):
        if not self.is_Empty():
            self.items.pop(0)
        else:
            print("Error! Queue is Empty")
    # PRINTING SIZE OF QUEUE.
    def size(self):
        return len(self.items)
# MAIN CODE OR DRIVER CODE.
if __name__ == '__main__':
    # CREATING OBJECT FOR QUEUE CLASS.
    # U CAN GIVE ANY NAME TO THE OBJECT.
    obj = Queue()
    while True:
        print("1 = Enqueue")
        print("2 = Dequeue")
        print("3 = Size of Queue")
        print("4 = Printing Queue")
        print("5 = Exit")
        # GOING TO TAKE INPUT FROM USER.
        selection = int(input("Make any One selection from above: "))
        if selection == 1:
            element = int(input("Enter the Element: "))
            obj.enqueue(element)
        elif selection == 2:
            obj.dequeue()
        elif selection == 3:
            obj.size()
        elif selection == 4:
            print(obj.items)
        elif selection == 5:
            exit()
        else:
            print("Invalid Input OR Selection out of Range.")
