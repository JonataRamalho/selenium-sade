import sqlite3
import pandas as pd

conn = sqlite3.connect("anuncios.db")

conn.execute("""
    CREATE TABLE IF NOT EXISTS dimtempo (
        idTempo INTEGER PRIMARY KEY AUTOINCREMENT,
        AnoTempo int(4) UNIQUE DEFAULT NULL
    )
""")


conn.execute("""
    CREATE TABLE IF NOT EXISTS dimlocal (
        idLocal INTEGER PRIMARY KEY AUTOINCREMENT,
        nomMunicipio varchar(45) DEFAULT NULL,
        nomBairro varchar(45) UNIQUE DEFAULT NULL
    )
""")


conn.execute("""
    CREATE TABLE IF NOT EXISTS dimveiculo (
        idVeiculo INTEGER PRIMARY KEY AUTOINCREMENT,
        NomVeiculo varchar(30) DEFAULT NULL,
        NomMarca varchar(30) DEFAULT NULL,
        AnoVeiculo int(4) DEFAULT NULL,
        QtdKm bigint(6) DEFAULT NULL,
        TipCambio varchar(12) DEFAULT NULL,
        TipCombustivel varchar(20) DEFAULT NULL,
        ValPreco bigint(15) DEFAULT NULL,
        dscAnuncio varchar(100) DEFAULT NULL
    )
""")

conn.execute("""
    CREATE TABLE IF NOT EXISTS tblfato (
        idTempo int(11) NOT NULL,
        idLocal bigint(5) NOT NULL,
        idVeiculo bigint(5) NOT NULL,
        valPreco int(11) DEFAULT NULL,
        FOREIGN KEY (idTempo) REFERENCES dimtempo(idTempo),
        FOREIGN KEY (idLocal) REFERENCES dimlocal(idLocal),
        FOREIGN KEY (idVeiculo) REFERENCES dimveiculo(idVeiculo)
    )
""")

conn.execute("""
    CREATE TABLE IF NOT EXISTS tbl_temp_veiculo (
        codAnuncio INTEGER PRIMARY KEY AUTOINCREMENT,
        dscAnuncio varchar(100) DEFAULT NULL,
        qtdKm varchar(20) DEFAULT NULL,
        tipCambio varchar(45) DEFAULT NULL,
        tipCombustivel varchar(45) DEFAULT NULL,
        valPreco varchar(15) DEFAULT NULL,
        diaAnuncio varchar(25) DEFAULT NULL,
        horAnuncio varchar(8) DEFAULT NULL,
        dscLocal varchar(45) DEFAULT NULL,
        dscMarca varchar(45) DEFAULT NULL,
        dscModelo varchar(45) DEFAULT NULL
    )
""")

conn.close()


def insert_data_into_temp_veiculo(data):
    conn = sqlite3.connect("anuncios.db")
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO tbl_temp_veiculo (
        dscAnuncio, qtdKm, tipCambio, tipCombustivel, valPreco, diaAnuncio, horAnuncio, dscLocal, dscMarca, dscModelo
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    cursor.executemany(insert_query, data)
    conn.commit()
    conn.close()
