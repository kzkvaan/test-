class Table:

    def __init__(self, material: str,width: int,height: int):

        if  width<= 0 or height <= 0:
            raise ValueError("Высота и ширина стола должны быть положительными числами.")
        self.material = material
        self.width = width
        self.height = height

    def fold(self) -> None:

        table = Table("металл", 50, 60)
        table.fold()  # Заглушка для метода


    def paint(self, color: str) -> None:

        table = Table("дерево", 50, 60)
        table.paint("красный")  # Заглушка для метода


class Tree:

    def __init__(self, species: str, age: int, height: int):

        if age < 0 or height <= 0:
            raise ValueError("Возраст должен быть неотрицательным, а высота положительной.")
        self.species = species
        self.height = height
        self.age = age

    def grow(self, years: int) -> None:
        tree = Tree("береза", 3, 7)
        tree.grow(3)

    def shed_leaves(self) -> None:

        tree = Tree("береза", 5, 3)
        tree.shed_leaves()  # Заглушка для метода


class Stack:

    def __init__(self):

        self.stack: list[int] = []

    def push(self, value: int) -> None:

        s = Stack()
        s.push(10)  # Заглушка для метода

    def pop(self) -> int:
        s = Stack()
        s.pop()  # Заглушка для метода


    def peek(self) -> int:

        s = Stack()
        s.peek()  # Заглушка для метода

if __name__ == "__main__":
    import doctest

    doctest.testmod()