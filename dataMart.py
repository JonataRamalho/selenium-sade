import sqlite3
import pandas as pd


def insert_into_dimensions_and_fact_table():
    conn = sqlite3.connect("anuncios.db")
    cursor = conn.cursor()

    # Busque todos os dados da tabela temporária
    cursor.execute("SELECT * FROM tbl_temp_veiculo")
    temp_data = cursor.fetchall()

    # Busque todos os dados da tabela temporária como um DataFrame
    df_temp = pd.read_sql_query("SELECT * FROM tbl_temp_veiculo", conn)

    # Remover linhas duplicadas
    df_temp = df_temp.drop_duplicates()

    # Substituir células vazias por "não informado"
    df_temp = df_temp.applymap(lambda x: "não informado" if x == "" else x)

    # Iterar sobre as linhas do DataFrame
    for index, row in df_temp.iterrows():
        dscAnuncio, qtdKm, tipCambio, tipCombustivel, valPreco, diaAnuncio, horAnuncio, dscLocal, dscMarca, dscModelo = row[
            1:]

        anoTempo = diaAnuncio.split('/')[-1]

        # Inserir dados na dimensão dimtempo
        cursor.execute(
            "INSERT OR IGNORE INTO dimtempo (AnoTempo) VALUES (?)", (anoTempo,))
        cursor.execute(
            "SELECT idTempo FROM dimtempo WHERE AnoTempo = ?", (anoTempo,))
        idTempo = cursor.fetchone()[0]

        # Inserir dados na dimensão dimlocal
        nomMunicipio, *nomBairro = dscLocal.split(', ', maxsplit=1)
        nomBairro = nomBairro[0] if nomBairro else None
        cursor.execute(
            "INSERT OR IGNORE INTO dimlocal (nomMunicipio, nomBairro) VALUES (?, ?)", (nomMunicipio, nomBairro))
        cursor.execute(
            "SELECT idLocal FROM dimlocal WHERE nomMunicipio = ? AND nomBairro = ?", (nomMunicipio, nomBairro))
        idLocal_result = cursor.fetchone()
        idLocal = idLocal_result[0] if idLocal_result else None

        # Inserir dados na dimensão dimveiculo
        cursor.execute("""
            INSERT OR IGNORE INTO dimveiculo (
                NomVeiculo, NomMarca, AnoVeiculo, QtdKm, TipCambio, TipCombustivel, ValPreco, dscAnuncio
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (dscModelo, dscMarca, diaAnuncio[:4], qtdKm, tipCambio, tipCombustivel, valPreco, dscAnuncio))
        cursor.execute("""
            SELECT idVeiculo FROM dimveiculo
            WHERE NomVeiculo = ? AND NomMarca = ? AND AnoVeiculo = ? AND QtdKm = ? AND TipCambio = ? AND TipCombustivel = ? AND ValPreco = ? AND dscAnuncio = ?
        """, (dscModelo, dscMarca, diaAnuncio[:4], qtdKm, tipCambio, tipCombustivel, valPreco, dscAnuncio))
        idVeiculo_result = cursor.fetchone()
        idVeiculo = idVeiculo_result[0] if idVeiculo_result else None

        # Inserir dados na tabela fato tblfato
        if idTempo and idLocal and idVeiculo:
            cursor.execute("INSERT INTO tblfato (idTempo, idLocal, idVeiculo, valPreco) VALUES (?, ?, ?, ?)",
                           (idTempo, idLocal, idVeiculo, valPreco))

    conn.commit()
    conn.close()


insert_into_dimensions_and_fact_table()
