from model.corso import Corso
from model.studente import Studente
from database.DB_connect import get_connection


def get_corsi() -> list[Corso] | None:
    """
    Funzione che legge tutti i corsi presenti nel Database
    :return: una lista con tutti i corsi presenti oppure None
    """
    cnx = get_connection()
    result = []
    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT *"
                       " FROM corso")
        for row in cursor:
            result.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))
        cursor.close()
        cnx.close()
        return result
    else:
        print("Couldn't retrieve connection")
        return None


def get_iscritti_corso(codins) -> list[Studente] | None:
    """
    Una funzione che recupera una lista di tutti gli studenti iscritti al corso selezionato
    :param codins: il corso di cui recuperare gli iscritti
    :return: una lista di tutti gli studenti iscritti
    """
    cnx = get_connection()
    result = []
    query = """SELECT studente.*
                FROM iscrizione AS i, studente AS s
                WHERE i.matricola=s.matricola AND i.codins=%s"""
    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(query, (codins,))
        for row in cursor:
            result.append(Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"]))
        cursor.close()
        cnx.close()
        return result
    else:
        print("Could not connect")
        return None


def count_iscritti_corso(codins) -> int | None:
    """
    Una funzione che recupera una lista di tutti gli studenti iscritti al corso selezionato
    :param codins: il corso di cui recuperare gli iscritti
    :return: una lista di tutti gli studenti iscritti
    """
    cnx = get_connection()
    counter = 0
    query = """SELECT COUNT(studente.*)
                FROM iscrizione AS i, studente AS s
                WHERE i.matricola=s.matricola AND i.codins=%s"""
    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        counter = cursor.execute(query, (codins,))
        cursor.close()
        cnx.close()
        return counter
    else:
        print("Could not connect")
        return None
