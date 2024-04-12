from database.DB_connect import get_connection
from model.corso import Corso
from model.studente import Studente


def fill_mappa_corsi(mappa_corsi):
    """
    Funzione che legge tutti i corsi nel database
    """
    cnx = get_connection()
    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM corso")
        for row in cursor:
            corso = Corso(row["codins"], row["crediti"], row["nome"], row["pd"])
            mappa_corsi[corso.codins] = corso
        cursor.close()
        cnx.close()
    else:
        print("Could not connect")


def get_iscritti_corso(codins) -> list[Studente] | None:
    """
    Funzione che recupera una lista con tutti gl istudenti iscritti al corso selezionato
    :param corso: il corso di cui recuperare gli iscritti
    :return: una lista con tutti gli studenti iscritti
    """
    cnx = get_connection()
    result = []
    query = """SELECT studente.* 
                FROM iscrizione, studente 
                WHERE iscrizione.matricola=studente.matricola AND iscrizione.codins=%s"""

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


def get_corsi_studente(matricola, studente):
    """
            Funzione che data una matricola ricerca nel database i corsi frequentati
            :param matricola: la matricola dello studente da ricercare
            :param studente: lo studente di cui si cercano i corsi frequentati
            :return: una lista di corsi
            """
    cnx = get_connection()
    query = """ SELECT corso.* 
    FROM corso, iscrizione 
    WHERE iscrizione.codins=corso.codins AND iscrizione.matricola = %s
    """
    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(query, (matricola,))
        for row in cursor:
            studente.corsi.add(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))
        cursor.close()
        cnx.close()
    else:
        print("Could not connect")


def iscrivi_corso(matricola, codins) -> bool:
    """
    Funzione che aggiunge uno studente agli iscritti di un corso
    :param matricola: la matricola dello studente
    :param codins: il codice del corso
    :return: True se l-operazione va a buon fine, False altrimenti
    """
    cnx = get_connection()
    result = []
    query = """INSERT IGNORE INTO `iscritticorsi`.`iscrizione` 
    (`matricola`, `codins`) 
    VALUES(%s,%s)
    """
    if cnx is not None:
        cursor = cnx.cursor()
        cursor.execute(query, (matricola, codins,))
        cnx.commit()
        cursor.close()
        cnx.close()
        return True
    else:
        print("Could not connect")
        return False
