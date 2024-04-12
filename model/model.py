from database import corso_DAO
from database import studente_DAO


class Model:
    def get_corsi(self):
        return corso_DAO.get_corsi()

    def get_iscritti(self, codins):
        return corso_DAO.get_iscritti_corso(codins)

    def count_iscritti(self, codins):
        return corso_DAO.count_iscritti_corso(codins)
