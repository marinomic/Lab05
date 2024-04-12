import database.corso_DAO
from database import corso_DAO
from database import studente_DAO
from model.corso import Corso


class Model:

    def __init__(self):
        self._mappa_corsi = None
        self._mappa_studenti = dict()

    def get_corsi(self) -> dict[Corso]:
        if self._mappa_corsi is None:
            self._mappa_corsi = dict()
            corso_DAO.fill_mappa_corsi(self._mappa_corsi)
        return self._mappa_corsi

    def get_iscritti_corso(self, codins):
        if self._mappa_corsi[codins].studenti is None:
            self._mappa_corsi[codins].studenti = corso_DAO.get_iscritti_corso(codins)
        return self._mappa_corsi[codins].studenti


    def cerca_studente(self, matricola):
        if self._mappa_studenti.get(matricola) is None:
            studente_DAO.cerca_studente(matricola, self._mappa_studenti)
        return self._mappa_studenti.get(matricola)

    def get_corsi_studente(self, matricola):
        studente = self.cerca_studente(matricola)
        if studente is None:
            return None
        else:
            if studente.corsi is None:
                studente.corsi = set()
                corso_DAO.get_corsi_studente(matricola, studente)
            return studente.corsi

    def iscrivi_corso(self, matricola, codin):
        self._mappa_studenti[matricola].add(self._mappa_corsi[codin])
        return corso_DAO.iscrivi_corso(matricola, codin)