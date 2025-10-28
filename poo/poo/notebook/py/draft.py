class Bateria:
    def __init__(self, capacidade: int) -> None:
        self.__capacidade: int = capacidade
        self.__carga: int = capacidade

    def getCarga(self) -> int:
        return self.__carga

    def getCapacidade(self) -> int:
        return self.__capacidade

    def descarregar(self, valor: int) -> None:
        self.__carga -= valor
        if self.__carga < 0:
            self.__carga = 0

    def carregar(self, valor: int) -> None:
        self.__carga += valor
        if self.__carga > self.__capacidade:
            self.__carga = self.__capacidade

    def mostrar(self) -> None:
        print(f"({self.__carga}/{self.__capacidade})")


class Carregador:
    def __init__(self, potencia: int) -> None:
        self.__potencia: int = potencia

    def getPotencia(self) -> int:
        return self.__potencia

    def mostrar(self) -> None:
        print(f"(Potência {self.__potencia})")


from typing import Optional

class Notebook:
    def __init__(self) -> None:
        self.__ligado: bool = False
        self.__bateria: Optional[Bateria] = None
        self.__carregador: Optional[Carregador] = None

    def setBateria(self, bateria: Bateria) -> None:
        self.__bateria = bateria

    def rmBateria(self) -> Optional[Bateria]:
        if self.__bateria is not None:
            b: Bateria = self.__bateria
            self.__bateria = None
            print("bateria removida")
            return b
        return None

    def setCarregador(self, carregador: Carregador) -> None:
        self.__carregador = carregador

    def ligar(self) -> None:
        if (self.__bateria is not None and self.__bateria.getCarga() > 0) or self.__carregador is not None:
            self.__ligado = True
            print("notebook ligado")
        else:
            print("erro: sem energia")

    def desligar(self) -> None:
        if self.__ligado:
            self.__ligado = False

    def usar(self, tempo: int) -> None:
        if not self.__ligado:
            print("notebook desligado")
            return
        if self.__bateria is None and self.__carregador is None:
            print("erro: sem energia")
            self.desligar()
            return
        if self.__bateria is not None:
            if self.__carregador is not None:
                self.__bateria.carregar(self.__carregador.getPotencia() * tempo)
            else:
                if tempo >= self.__bateria.getCarga():
                    tempo = self.__bateria.getCarga()
                    self.__bateria.descarregar(tempo)
                    print(f"Usando por {tempo} minutos, notebook descarregou")
                    self.desligar()
                    return
                self.__bateria.descarregar(tempo)
                print(f"Usando por {tempo} minutos")
        else:
            print("Notebook utilizado com sucesso")

    def mostrar(self) -> None:
        status = "Ligado" if self.__ligado else "Desligado"
        if self.__bateria is not None:
            bat = f"({self.__bateria.getCarga()}/{self.__bateria.getCapacidade()})"
        else:
            bat = "Nenhuma"
        if self.__carregador is not None:
            car = f"(Potência {self.__carregador.getPotencia()})"
        else:
            car = "Desconectado"
        print(f"Status: {status}, Bateria: {bat}, Carregador: {car}")


notebook = Notebook()
while True:
    try:
        line = input()
    except EOFError:
        break
    if line == "$end":
        break
    cmd = line.split()
    if cmd[0] == "$mostrar":
        notebook.mostrar()
    elif cmd[0] == "$ligar":
        notebook.ligar()
    elif cmd[0] == "$desligar":
        notebook.desligar()
    elif cmd[0] == "$usar":
        notebook.usar(int(cmd[1]))
    elif cmd[0] == "$bateria":
        notebook.setBateria(Bateria(int(cmd[1])))
    elif cmd[0] == "$carregador":
        notebook.setCarregador(Carregador(int(cmd[1])))
    elif cmd[0] == "$rmbateria":
        b = notebook.rmBateria()
        if b:
            b.mostrar()