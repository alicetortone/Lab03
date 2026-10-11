class Strumento:
    def __init__(self, id_strumento, tipo, marca, anno, valore):
        self.id_strumento = id_strumento
        self.tipo = tipo
        self.marca = marca
        self.anno = int(anno)
        self.valore = float(valore)

    def __str__(self):
        return f"{self.id_strumento} {self.tipo} {self.marca} {self.anno} {self.valore}"