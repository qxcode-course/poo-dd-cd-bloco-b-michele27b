class Pessoa:
    def __init__(self, nome: str, dinheiro: int):
        self._nome = nome
        self._dinheiro = dinheiro

    def get_nome(self):
        return self._nome

    def get_dinheiro(self):
        return self._dinheiro

    def pagar(self, valor: int):
        if valor > self._dinheiro:
            pago = self._dinheiro
            self._dinheiro = 0
            return pago
        else:
            self._dinheiro -= valor
            return valor

    def receber(self, valor: int):
        self._dinheiro += valor

    def __str__(self):
        return f"{self._nome}:{self._dinheiro}"


class Moto:
    def __init__(self):
        self._custo = 0
        self._motorista = None
        self._passageiro = None

    def set_driver(self, nome: str, dinheiro: int):
        self._motorista = Pessoa(nome, dinheiro)

    def set_pass(self, nome: str, dinheiro: int):
        self._passageiro = Pessoa(nome, dinheiro)

    def drive(self, distancia: int):
        if self._motorista is None or self._passageiro is None:
            print("fail: missing driver or passenger")
            return
        self._custo += distancia

    def leave_pass(self):
        if self._passageiro is None:
            print("fail: no passenger")
            return

        valor_pago = self._passageiro.pagar(self._custo)

        if valor_pago < self._custo:
            print("fail: Passenger does not have enough money")

        print(f"{self._passageiro.get_nome()}:{self._passageiro.get_dinheiro()} left")

        if self._motorista:
            self._motorista.receber(self._custo)

        self._passageiro = None
        self._custo = 0

    def show(self):
        driver_str = str(self._motorista) if self._motorista else "None"
        pass_str = str(self._passageiro) if self._passageiro else "None"
        print(f"Cost: {self._custo}, Driver: {driver_str}, Passenger: {pass_str}")


def main():
    moto = Moto()
    while True:
        try:
            line = input()
            parts = line.strip().split()
            if len(parts) == 0:
                continue
            cmd = parts[0]

            print(f"${line}")

            if cmd == "end":
                break
            elif cmd == "show":
                moto.show()
            elif cmd == "setDriver":
                moto.set_driver(parts[1], int(parts[2]))
            elif cmd == "setPass":
                moto.set_pass(parts[1], int(parts[2]))
            elif cmd == "drive":
                moto.drive(int(parts[1]))
            elif cmd == "leavePass":
                moto.leave_pass()
        except EOFError:
            break


if __name__ == "__main__":
    main()