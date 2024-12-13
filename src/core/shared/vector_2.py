class Vector2:
    """
    Representa um vetor em duas dimensões.

    Atributos:
        x (float): A coordenada x do vetor.
        y (float): A coordenada y do vetor.
    """

    def __init__(self, x, y):
        """
        Inicializa um novo objeto Vector2 com as coordenadas x e y.

        Parâmetros:
            x (float): A coordenada x inicial do vetor.
            y (float): A coordenada y inicial do vetor.
        """
        self._x = x
        self._y = y

    @property
    def x(self):
        """
        Obtém a coordenada x do vetor.

        Retorna:
            float: A coordenada x do vetor.
        """
        return self._x

    @x.setter
    def x(self, value):
        """
        Define a coordenada x do vetor.

        Parâmetros:
            value (float): O valor a ser atribuído à coordenada x.
        """
        self._x = value

    @property
    def y(self):
        """
        Obtém a coordenada y do vetor.

        Retorna:
            float: A coordenada y do vetor.
        """
        return self._y

    @y.setter
    def y(self, value):
        """
        Define a coordenada y do vetor.

        Parâmetros:
            value (float): O valor a ser atribuído à coordenada y.
        """
        self._y = value

    def __repr__(self):
        """
        Retorna uma representação em string do vetor no formato de tupla.

        Retorna:
            str: A representação em string do vetor.
        """
        return f"({self._x}, {self._y})"

    def __iter__(self):
        """
        Permite que o objeto Vector2 seja iterado como (x, y).

        Retorna:
            iterator: Um iterador que percorre as coordenadas x e y do vetor.
        """
        yield self._x
        yield self._y
