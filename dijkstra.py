# First step -- priority queue. We want to get items with lowest distance

# The operation that queue has to have are: insert(item, priority), getHighestPriority(), deleteHighestPriority()

class PrioQueueItem:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

class PrioQueueWithArrays:
    def __init__(self):
        self.items = []

    def insert(self, value, priority):
        self.items.append(PrioQueueItem(value, priority))

    def getHighestPriority(self):
        # Iterate through array and find item with highest priority

        highestPrioItem = None

        for item in self.items:
            if highestPrioItem is None:
                highestPrioItem = item

                continue

            if item.priority > highestPrioItem.priority:
                highestPrioItem = item

        return highestPrioItem


    def deleteHighestPriority(self):
        highestPrio = 0
        highestPrioKey = None

        for key, item in enumerate(self.items):
            if item.priority > highestPrio:
                highestPrio = item.priority
                highestPrioKey = key

        del self.items[highestPrioKey]


prioQueue = PrioQueueWithArrays()

prioQueue.insert(5, 100)
prioQueue.insert(5, 10)
prioQueue.insert(15, 5)

print(prioQueue.getHighestPriority().priority)
print(prioQueue.deleteHighestPriority())
print(prioQueue.getHighestPriority().priority)