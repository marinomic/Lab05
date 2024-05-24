from model.corso import Corso
from model.studente import Studente
from database.DB_connect import get_connection


def cerca_studente(matricola) -> Studente | None:
    """ Funzione che data una matricola ricerca nel database lo studente corrispondente (se presente)
       :param matricola: la matricola dello studente da ricercare
       :return: uno studente, se presente
   """
    cnx = get_connection()
    if cnx is not None:
        query = """SELECT *
                   FROM studente
                   WHERE studente.matricola=%s
           """
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(query, (matricola,))
        row = cursor.fetchone()
        if row is not None:
            result = Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"])
        else:
            result = None
        cursor.close()
        cnx.close()
        return result
    else:
        print("Could not connect")
        return None
