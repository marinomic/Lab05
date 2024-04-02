import database.corso_DAO
from database import corso_DAO
from database import studente_DAO


class Model:

    def get_corsi(self):
        return corso_DAO.get_corsi()

    def get_iscritti_corso(self, codice_corso):
        return corso_DAO.get_iscritti_corso(codice_corso)

    def get_corso(self, codin):
        return corso_DAO.get_corso(codin)

    def cerca_studente(self, matricola):
        return studente_DAO.cerca_studente(matricola)

    def get_corsi_studente(self, matricola):
        return corso_DAO.get_corsi_studente(matricola)

    def iscrivi_corso(self, matricola, codin):
        return corso_DAO.iscrivi_corso(matricola, codin)