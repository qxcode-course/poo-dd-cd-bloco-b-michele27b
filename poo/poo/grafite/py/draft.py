class Lead:
    def __init__(self, thickness: float, hardness: str, size: int):
        self.thickness = thickness
        self.hardness = hardness
        self.size = size

    def usagePerSheet(self):
        if self.hardness == "HB":
            return 1
        elif self.hardness == "2B":
            return 2
        elif self.hardness == "4B":
            return 4
        elif self.hardness == "6B":
            return 6
        return 0

    def __str__(self):
        return f"[{self.thickness}:{self.hardness}:{self.size}]"


class Pencil:
    def __init__(self, thickness: float):
        self.thickness = thickness
        self.lead = None

    def insert(self, lead: Lead):
        if self.lead is not None:
            print("fail: ja existe grafite")
            return
        if lead.thickness != self.thickness:
            print("fail: calibre incompativel")
            return
        self.lead = lead

    def remove(self):
        if self.lead is None:
            print("fail: nao existe grafite")
            return
        self.lead = None

    def writePage(self):
        if self.lead is None:
            print("fail: nao existe grafite")
            return
        if self.lead.size <= 10:
            print("fail: tamanho insuficiente")
            return

        gasto = self.lead.usagePerSheet()
        if self.lead.size - gasto < 10:
            print("fail: folha incompleta")
            self.lead.size = 10
        else:
            self.lead.size -= gasto

    def __str__(self):
        grafite_str = "null" if self.lead is None else str(self.lead)
        return f"calibre: {self.thickness}, grafite: {grafite_str}"


def main():
    pencil = None
    while True:
        try:
            line = input().strip()
            if not line:
                continue
            print(f"${line}")
            parts = line.split()
            cmd = parts[0]

            if cmd == "end":
                break
            elif cmd == "init":
                pencil = Pencil(float(parts[1]))
            elif cmd == "show":
                if pencil is None:
                    print("fail: nenhum lapis")
                else:
                    print(pencil)
            elif cmd == "insert":
                if pencil is None:
                    print("fail: nenhum lapis")
                else:
                    lead = Lead(float(parts[1]), parts[2], int(parts[3]))
                    pencil.insert(lead)
            elif cmd == "remove":
                if pencil is None:
                    print("fail: nenhum lapis")
                else:
                    pencil.remove()
            elif cmd == "write":
                if pencil is None:
                    print("fail: nenhum lapis")
                else:
                    pencil.writePage()
        except EOFError:
            break


if __name__ == "__main__":
    main()