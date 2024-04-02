# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection
from model.studente import Studente


def cerca_studente(matricola) -> Studente:
    """
        Funzione che data una matricola ricerca nel database lo studente corrispondente (se presente)
        :param matricola: la matricola dello studente da ricercare
        :return: uno studente, se presente
        """
    cnx = get_connection()
    result = None
    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM studente WHERE matricola = %s", (matricola,))
        for row in cursor:
            result = Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"])
        cursor.close()
        cnx.close()
        return result
    else:
        print("Could not connect")
        return result
