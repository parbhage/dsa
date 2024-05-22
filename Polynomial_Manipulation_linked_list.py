#Polynomial Manipulation representation using linked list
class Node:
    def __init__(self, coeff, exp):
        self.coefficient = coeff
        self.exponent = exp
        self.next = None

class Polynomial:
    def __init__(self):
        self.head = None

    def insert_term(self, coeff, exp):
        if self.head is None:
            self.head = Node(coeff, exp)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(coeff, exp)

    def display(self):
        current = self.head
        while current:
            print(f"{current.coefficient}x^{current.exponent}", end=" ")
            if current.next:
                print("+", end=" ")
            current = current.next
        print()

    def add_polynomials(self, p2):
        result = Polynomial()
        current1 = self.head
        current2 = p2.head

        while current1 and current2:
            if current1.exponent > current2.exponent:
                result.insert_term(current1.coefficient, current1.exponent)
                current1 = current1.next
            elif current1.exponent < current2.exponent:
                result.insert_term(current2.coefficient, current2.exponent)
                current2 = current2.next
            else:
                coeff_sum = current1.coefficient + current2.coefficient
                result.insert_term(coeff_sum, current1.exponent)
                current1 = current1.next
                current2 = current2.next

        # Add remaining terms of the first polynomial
        while current1:
            result.insert_term(current1.coefficient, current1.exponent)
            current1 = current1.next

        # Add remaining terms of the second polynomial
        while current2:
            result.insert_term(current2.coefficient, current2.exponent)
            current2 = current2.next

        return result

# Example usage:
poly1 = Polynomial()
poly1.insert_term(4, 3)
poly1.insert_term(3, 2)
poly1.insert_term(2, 1)
print("Polynomial 1:")
poly1.display()

poly2 = Polynomial()
poly2.insert_term(2, 3)
poly2.insert_term(1, 2)
poly2.insert_term(2, 0)
print("Polynomial 2:")
poly2.display()

result = poly1.add_polynomials(poly2)
print("Resultant Polynomial (Polynomial 1 + Polynomial 2):")
result.display()
