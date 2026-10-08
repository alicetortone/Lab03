import csv
from operator import attrgetter

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.responsabile = responsabile

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        with open(file_path, "r", encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file)
            first=True
            for riga in csv_reader:
                if first:
                    first=False
                strumento = Strumenti(riga[0], riga[1], riga[2], riga[3], riga[4])



    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO