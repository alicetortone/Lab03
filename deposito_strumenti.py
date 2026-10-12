import csv
from strumento import Strumento
from prestito import Prestito
from operator import attrgetter

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome
        self.__responsabile = responsabile

        self.lista_strum = []
        self.prestiti = []
        self.contatore_prestiti = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def responsabile(self):
        return self.__responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self.__responsabile = responsabile


    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        with open(file_path, "r", encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file)
            for riga in csv_reader:
                if not riga:
                    continue
                strum = Strumento(riga[0], riga[1], riga[2], riga[3], riga[4])
                self.lista_strum.append(strum)

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        if self.lista_strum :
            ultimo_id = self.lista_strum[-1].id_strumento
            nuovo_id = "S" + str(int(ultimo_id[1:]) + 1)
        else:
            nuovo_id = "S1"
        strum = Strumento(nuovo_id, tipo, marca, anno_acquisto, valore)
        self.lista_strum.append(strum)
        return strum

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        ordinati = sorted(self.lista_strum, key=attrgetter("marca"))
        return ordinati

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        trovato=False
        for s in self.lista_strum:
            if s.id_strumento == id_strumento:
                trovato = True
                break
        if not trovato:
            raise Exception("Strumento non trovato")

        for p in self.prestiti:
            if p.id_strumento == id_strumento:
                raise Exception("Strumento gia in prestito")

        self.contatore_prestiti += 1
        id_prestito = "P" + str(self.contatore_prestiti)
        prest = Prestito(id_prestito, data, id_strumento, cognome_allievo)
        self.prestiti.append(prest)
        return prest

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        for i, prestito in enumerate(self.prestiti):
            if prestito.id_prestito == id_prestito:
                self.prestiti.pop(i)
                return
        raise Exception("Codice prestito non trovato")

    def __str__(self):
        return f"{self.__nome} {self.__responsabile} {self.lista_strum}"