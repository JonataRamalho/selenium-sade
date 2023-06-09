import sqlite3
import pandas as pd

from createSqliteDatabase import insert_data_into_temp_veiculo

conn = sqlite3.connect("anuncios.db")

df = pd.read_sql_query('SELECT * FROM tbl_temp_veiculo', conn)

df['qtdKm'] = df['qtdKm'].str.replace(' km', '', regex=True)
df['qtdKm'] = df['qtdKm'].str.replace('.', '', regex=True)

df['valPreco'] = df['valPreco'].str.replace('R\$ ', '', regex=True)
df['valPreco'] = df['valPreco'].str.replace('.', '', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace(
    '//', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('16V', 'Jeep', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('2.0', 'Jeep', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('2.3', 'Nissan', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('2004', 'Mitsubishi', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('2009', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('2009/2010', 'Fiat', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('2016/2017', 'Renault', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    '2020/2020', 'Mercedes Benz', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('4porta', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('ACTIVE', 'Peugeot', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('AGILE', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('ALLURE', 'Peugeot', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('ASX', 'Mitsubishi', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Activ', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Agile', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Alfa', 'Alfa Romeo', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Allure', 'Peugeot', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace(
    'ALUGO', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'ALUGUEL', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('ANO', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    r'\bAT\b', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'ATACAMA', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('AUT', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'AUTOMÁTICA', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('AWD', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Aaa', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Aceita', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Altomovel', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Aluga', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Alugo', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Aluguel', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Ambulância', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    r'\bAp\b', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Arapiraca-Al', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Asia', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Automóvel', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Autonino', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Baixei', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Baixou', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Botão', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'CARRO', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'CLIQUE', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    '2017', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    '2018', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    '2021/2022', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    r'\b4P\b', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'ACEITO', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    r'\bAP\b', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'CERNão informadoO', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Carro', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Carrocinha', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Comf', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Carros', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'CERO', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Cabine', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Caminhão', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Camionete', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'DRIVE', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Completa', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Completo', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Corda', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    r'\bzap\b', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    r'\bv\b', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'troco', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'DIESEL', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'sport', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'sedan', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Deus', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Diesel', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    r'\bECO\b', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'EVOL', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('new', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('kms', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Não informado/', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Não informadoACAMA', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Não informadoOMÁTICA', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Não informadoUTION', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Não informadoage', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Não informadocinha', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Não informadoort', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Não informados', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'flex', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'CNão informadoTUR', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    r'\bEco\b', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'EcoNão informado', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'EcoNão informadoe', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'EcoeNão informado', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Edifício', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    r'\bel\b', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Engate', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Extra', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'FINão informado', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'FLEX', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Flat', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Flex', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'EXCLUSIVO', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'EXTRA', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Fapinha', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('GNV', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'GRAN', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'GRAND', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'GRIFFE', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Geração', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Gnv', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Gran', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Grand', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Grande', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'HNão informadoCH', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Hatch', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Hoje', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'IMPECÁVEL', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'IMPERDÍVEL', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'IPVA', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Impecável', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Imponente', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Junior', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    r'\bL\b', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    r'\bKM\b', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'LEIA', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'LIKE', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'ICON', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Kit', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'LONGITUDE', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    r'\bLT\b', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    r'\bLTZ\b', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    r'\bLtz\b', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Locação', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'MAIS', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'MANUAL', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'LIVE', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Land', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Life', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Linda', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'MINI', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('NEW', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('New', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Nossa', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Nova', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Novo', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Não informado/', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Não informadoD', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Não informadod', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Não informadoe', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Não informado/', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Oportunidade', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'OPORTUNIDADE', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Obs', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'PLUS', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'PORTAS', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'PREMIER', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'PROMOÇÃO', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Particular', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Power', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    r'\bPra\b', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    r'\bPra\b', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Premier', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Preço', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Quitação', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Repasse', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'MPFI', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    r'\bNOV\b', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'NOVA', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'SEDAN', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'SEDÃ', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    r'\bSEL\b', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'SPORT', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    r'\bSR\b', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    r'\bSUV\b', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'não informado', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'diesel', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    '"completa,9-"', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    r'\baro\b', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'ambulância', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'ahuyomsrf', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    r'\bactiv\b', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Troco', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'VENDE-SE', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'VENDO', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Vende', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Vendo', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Veículo', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'TURBO', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'VISION', 'Não informado', regex=True)
# df['dscMarca'] = df['dscMarca'].str.replace('', 'Não informado', regex=True)
# df['dscMarca'] = df['dscMarca'].str.replace('', 'Não informado', regex=True)
# df['dscMarca'] = df['dscMarca'].str.replace('', 'Não informado', regex=True)
# df['dscMarca'] = df['dscMarca'].str.replace('', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'COMPLETA', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'COMPLETO', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'CONCESSIONÁRIA', 'Não informado', regex=True)


df['dscMarca'] = df['dscMarca'].str.replace('palio', 'Fiat', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('PALIO', 'Fiat', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Palio', 'Fiat', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Pálio', 'Fiat', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('ARGO', 'Fiat', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Argo', 'Fiat', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('AMAROK', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Amarok', 'Volkswagen', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('COMMANDE', 'Jeep', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('CR-V', 'Jeep', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('Arrizo', 'Chery', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Arrizzo', 'Chery', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('Astra', 'Chevrolet', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('A3', 'Audi', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('a3', 'Audi', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('AUDI', 'Audi', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('audi', 'Audi', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('AMG', 'Mercedes-Benz', regex=True)


df['dscMarca'] = df['dscMarca'].str.replace(
    'ADVANTAGE', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'advantage', 'Chevrolet', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace(
    'Azera', 'Hyundai ', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'AZERA', 'Hyundai ', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'azera', 'Hyundai ', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('BMW', 'Bmw', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('BMW', 'Bmw', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('Bongo', 'Kia', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace(
    'Brasilia', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Brasília', 'Volkswagen', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace(
    'Blazer', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'blazer', 'Chevrolet', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace(
    'Buggy', 'Bugre', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('CRV', 'Honda', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('C10', 'Chevrolet', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('C3', 'Citroën', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('C4', 'Citroën', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('CAPTUR', 'Renault', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Captur', 'Renault', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace(
    'CELTA', 'Chevrolet', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('CERATO', 'Kia', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Cerato', 'Kia', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Cerrato', 'Kia', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('CHERY', 'Chery', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('chery', 'Chery', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Cherry', 'Chery', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Caoa', 'Chery', regex=True)


df['dscMarca'] = df['dscMarca'].str.replace('CGI', 'Mercedes-Benz', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('CHEV', 'Chevrolet', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace(
    'CHEVROLET', 'Chevrolet', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('CITROEN', 'Citroën', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('CITROËN', 'Citroën', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Citroem', 'Citroën', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Cintroen', 'Citroën', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Citröen', 'Citroën', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Citroen', 'Citroën', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('CITY', 'Honda', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('City', 'Honda', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('CIVIC', 'Honda', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Civic', 'Honda', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace(
    'Chevette', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'ChevroletROLET', 'Chevrolet', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('Celta', 'Chevrolet', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('Classic', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Clássic', 'Chevrolet', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('Cobalt', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Colbat', 'Chevrolet', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('Cronos', 'Fiat', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('Cross', 'Volkswagen', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('Colina', 'Chevrolet', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('Cruze', 'Chevrolet', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('Clio', 'Renault', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('COMFORT', 'Hyundai', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('CONFORT', 'Hyundai', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Comfort', 'Hyundai', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('CRETA', 'Hyundai', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('COROLLA', 'Toyota', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Corola', 'Toyota', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Corola', 'Toyota', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Corrola', 'Toyota', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace(
    'COMFORTLINE', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'CROSSFOX', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Crossfox', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Combes', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Comfortline', 'Volkswagen', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace(
    'COMPASS', 'Jeep', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Compass', 'Jeep', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Commander', 'Jeep', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace(
    'CRUZE', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'CRUZE', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Capitiva', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Captiva', 'Chevrolet', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('D5', 'Volvo', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('DOBLÒ', 'FIAT', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Doblo', 'FIAT', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Doblò', 'FIAT', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Doblô', 'FIAT', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('DUSTER', 'Renault', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Duster', 'Renault', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('DYNAMIQUE', 'Renault', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('Dodge', 'Stellantis', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('ESSENCE', 'Fiat', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('ETIOS', 'Toyota', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Etios', 'Toyota', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace(
    'EVOLUTION', 'Mitsubishi', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Evolution', 'Mitsubishi', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('EX2', 'Kia', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('Elantra', 'Hyunday', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('Endurance', 'Fiat', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Escort', 'Ford', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('FIAT', 'Fiat', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('FIESTA', 'Ford', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('FIORINO', 'Fiat', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Fiorino', 'Fiat', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Fiornio', 'Fiat', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('FIT', 'Honda', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Fit', 'Honda', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('FLUENCE', 'Renault', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Fluence', 'Renault', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('KWID', 'Renault', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Kwid', 'Renault', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Focus', 'Ford', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Ford/', 'Ford', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Fox', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Freedom', 'Fiat', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Freestyle', 'Ford', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Frontier', 'Nissan', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Fusca', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Fusion', 'Ford', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Entrada', 'Fiat', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('FOCUS', 'Ford', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('FORD', 'Ford', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('FOX', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('FREEDON', 'Fiat', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('FREESTYLE', 'Ford', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('FRONTIER', 'Nissan', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('FUSION', 'Ford', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Festa', 'Ford', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Fiesta', 'Ford', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('FiestaJeep1', 'Ford', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('FordJeep1', 'Ford', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'FinancioVolkswagen9', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('GLI', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('GII', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('GOL', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('GOLF', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('GLA', 'Mercedes Benz', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('GLB', 'Mercedes Benz', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('GLC', 'Mercedes Benz', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('GLS', 'Mercedes Benz', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Gla', 'Mercedes Benz', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Glb', 'Mercedes Benz', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('MB', 'Mercedes Benz', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'MERCEDES-BENZ', 'Mercedes Benz', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Mercedes Benz', 'Mercedes Benz', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Mercedes-Benz', 'Mercedes Benz', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Mercedes', 'Mercedes Benz', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Mercedez', 'Mercedes Benz', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Mercedes Benz Benz', 'Mercedes Benz', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('GLX', 'Citroën', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('MCitroën', 'Citroën', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('GM', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('HILUX', 'Toyota', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('HLX', 'Toyota', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Hillux', 'Toyota', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Hilux', 'Toyota', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Corolla', 'Toyota', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Corsa', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Gm', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Joy', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('GM/', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Chevrolet/', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Creta', 'Hyundai', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Gol', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Gol', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Golf', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Komby', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Kombi', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('KOMBI', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Não informadoline', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'HIGHLINE', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Jeta', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Jetta', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('HB', 'Hyundai', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Hb', 'Hyundai', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Hb20', 'Hyundai', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Hb20s', 'Hyundai', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Hb20x', 'Hyundai', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('HB20', 'Hyundai', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('HB20S', 'Hyundai', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('HB20s', 'Hyundai', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Hyundai', 'Hyundai', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'HyundaiLINE', 'Hyundai', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Hyunday', 'Hyundai', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('HONDA', 'Honda', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('HR', 'Honda', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Hr', 'Honda', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Hrv', 'Honda', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('HR-V', 'Honda', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('HRV', 'Honda', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('HYNDAI', 'Hyundai', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('HYUNDAI', 'Hyundai', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Hyundai ', 'Hyundai', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Hyundai20', 'Hyundai', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Hyundai20S', 'Hyundai', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Hyundai20s', 'Hyundai', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Hyundai20x', 'Hyundai', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('HyundaiS', 'Hyundai', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Hyundais', 'Hyundai', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Hyundaix', 'Hyundai', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('I30', 'Hyundai', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('IDEA', 'Fiat', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Idea', 'Fiat', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('JEEP', 'Jeep', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Jeep4', 'Jeep', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Jeep9', 'Jeep', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Jeep/2010', 'Jeep', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Jeep9/2010', 'Jeep', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('JIMNY', 'Suzuki', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Jimny', 'Suzuki', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('KA', 'Ford', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Ka', 'Ford', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Ká', 'Ford', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('FordDETT', 'Ford', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Forddett', 'Ford', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Fordngoo', 'Ford', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('KIA', 'Kia', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('KICKS', 'Nissan', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Kicks', 'Nissan', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Honda-V', 'Honda', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Honda-V', 'Honda', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Honda-V', 'Honda', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('HondaV', 'Honda', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Hondav', 'Honda', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('LINEA', 'Fiat', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Linea', 'Fiat', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('MARCH', 'Nissan', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('LJeep', 'Jeep', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'LJeepMercedes Benz', 'Jeep', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('LOGAN', 'Renault', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Logan', 'Renault', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Longan', 'Renault', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Oroch', 'Renault', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Lancer', 'Mitsubishi', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'MITSUBISHI', 'Mitsubishi', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Pajero', 'Mitsubishi', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Outlander', 'Mitsubishi', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Triton', 'Mitsubishi', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Mobi', 'Fiat', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('MOBI', 'Fiat', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('MONTANA', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Montana', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('MONZA', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Monza', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Move', 'Nissan', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('ONIX', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Omega', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Onix', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('PEUGEOT', 'Peugeot', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Pegeeot', 'Peugeot', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Pegeout', 'Peugeot', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Pegout', 'Peugeot', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'PegPeugeot/208out', 'Peugeot', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Peugeot/208', 'Peugeot', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('POLO', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Polo', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'QUADRADO', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Parati', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Passat', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('OVERLAND', 'Overland', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('PICANTO', 'Kia', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('PORSCHE', 'Porsche', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('PRISMA', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Prisma', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(r'\bS\b', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    r'\bS-1\b', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    r'\bS10\b', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Pampa', 'Ford', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Punto', 'Fiat', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Q3', 'Audi', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('RENAULT', 'Renault', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Renalt', 'Renault', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Renaul', 'Renault', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Renaut', 'Renault', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Renaultt', 'Renault', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Renout', 'Renault', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Reno', 'Renault', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('SANDERO', 'Renault', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Sandero', 'Renault', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Sandeo', 'Renault', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('RENEGADE', 'Jeep', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Renegade', 'Jeep', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('RANGER', 'Ford', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Range', 'Ford', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Ranger', 'Ford', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Rocam', 'Ford', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('S60', 'Volvo', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'SANTANA', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'SAVEIRO', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Saveiro', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Savero', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('MPI', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('MSI', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Nivus', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('SENSE', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Santa', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Santana', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'SPACEVolkswagen', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'JeepMercedes Benz', 'Jeep', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'KOMercedes BenzI', 'Mercedes Benz', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('SL', 'Mercedes Benz', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Fordl', 'Ford', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Fordr', 'Ford', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('March', 'Nissan', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('SENTRA', 'Nissan', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('NISSAN', 'Nissan', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    r'\bNISSAN/ \b', 'Nissan', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Meriva', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('SPIN', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('SIENA', 'Fiat', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'SPRINTER', 'Mercedes Benz', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('STRADA', 'Fiat', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('SW4', 'Toyota', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('SW4', 'Toyota', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('corola', 'Toyota', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('classic', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('city', 'Honda', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'chevrolet', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('buggy', 'Bugre', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('bmw', 'Bmw', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('atractive', 'Fiat', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('attractiv', 'Fiat', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Volksvagen', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'VolkswagenF', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Volkswagenf', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Volkswagenfox', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Volkswagenna', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Voyagem', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Voyage', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Vw', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('VW', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('VOYAGE', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'VOLKSWAGEN', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Virtus', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('VIRTUS', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(r'\bT\b', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    r'\bUP\b', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Chevrolet-10', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Spin', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Sentra', 'Nissan', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Siena', 'Fiat', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Strada', 'Fiat', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('TIGGO', 'Chery', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Tiggo', 'Chery', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('TORO', 'Fiat', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Tracker', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Tucson', 'Hyundai', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('UNO', 'Fiat', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Uno', 'Fiat', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Volcano', 'Fiat', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Vulcano', 'Fiat', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('YARIS', 'Toyota', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Yaris', 'Toyota', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Toro', 'Fiat', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('TOYOTA', 'Toyota', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Versa', 'Nissan', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('', '', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('', '', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('', '', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Não informadoChevrolet', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Não informadoortChevrolet', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Não informadoortline', 'Volkswagen', regex=True)


df['dscMarca'] = df['dscMarca'].str.replace('fire', 'Fiat', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('focus', 'Ford', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('freedom', 'Fiat', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('G2', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('G3', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('G4', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('G5', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('G6', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('G7', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('g7', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('g5', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('g6', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('g3', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('gol', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    r'\bTSI\b', 'Volkswagen', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('gransiena', 'Fiat', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('hilux', 'Toyota', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('honda', 'Honda', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('hb20', 'Hyundai', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('iveco', 'Iveco', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('jeep', 'Jeep', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('kombi', 'Volkswagen', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('last', 'Volkswagen', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('longitude', 'Jeep', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('ls', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('ltz', 'Chevrolet', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('nissan', 'Nissan', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('parati', 'Volkswagen', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('plus', 'Chevrolet', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('robust', 'Volkswagen', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('rodeio', 'Chevrolet', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace(
    'special', 'Volkswagen', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('sportage', 'Kia', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('sw4', 'Toyota', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace(
    'tracker', 'Chevrolet', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace(
    'trend', 'Volkswagen', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace(
    'uno', 'Fiat', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace(
    'voyage', 'Volkswagen', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace(
    'Ônix', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'ÔNIX', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(
    'Ômega', 'Chevrolet', regex=True)


# grouped = df.groupby('dscMarca')
# df['dscMarca'] = grouped['dscMarca'].transform(
#     lambda x: x if len(x) > 3 else 'Não informado')
# grouped_novo = df.groupby('dscMarca')
# result = grouped_novo.size().to_frame('count')
# result.to_csv('output.csv', header=['count'])

df['dscModelo'] = df['dscModelo'].str.replace(
    '320I', '320i', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'^8$', 'Tiggo', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    '2021/2022', 'Voyage', regex=True)


df['dscModelo'] = df['dscModelo'].str.replace(
    'AGILE', 'Agile', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'ARGO', 'Argo', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'ARGO', 'Argo', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'Altis', 'Corolla', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'CACTUS', 'C4', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'Cactus', 'C4', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'CIVIC', 'Civic', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'COMFORTLINE', 'Comfortline', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'COMPASS', 'Compass', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'COROLLA', 'Corolla', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'Comfort', 'HB20', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'Confort', 'HB20', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'Connect', 'UP', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'DRIVE', 'Argo', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'Drive', 'Argo', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'Dakar', 'Pajero', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'Dynamique', 'Duster', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'Expression', 'Logan', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'EXTRA', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'Extra', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'EXL', 'Civic', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'FIESTA', 'Fiesta', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'Fire', 'Palio', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'FIRE', 'Palio', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'FIT', 'Fit', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'FOX', 'Fox', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'G4', 'Gol', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'G4', 'Gol', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'GOL', 'Gol', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'GLI', 'jetta', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'GRAND', 'Siena', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'Grand', 'Siena', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'HB20S', 'HB20', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'HB20line', 'HB20', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'Hatch', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'Highline', 'Nivus', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'JOY', 'Joy', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'KA', 'ka', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'KICKS', 'Kicks', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'KWID', 'Kwid', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'KWID', 'Kwid', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'MARCH', 'March', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'MOBI', 'Mobi', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'MPI', 'UP', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'New', 'Fiesta', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'ONIX', 'Onix', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'ONIX', 'Onix', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'PREMIER', 'Spin', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'Premium', 'Corsa', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'RENEGADE', 'Renegade', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'Robust', 'Saveiro', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'Rover', 'Sport', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'SIENA', 'Siena', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'SR', 'Hilux', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'SR', 'Hilux', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'SRV', 'Hilux', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'SRX', 'Hilux', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'STRADA', 'Strada', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'SV', 'Kicks', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'SW4', 'Hilux', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'Sporting', 'Palio', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'Sporting', 'Palio', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'TORO', 'Toro', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'TOTAL', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'TR4', 'Pajero', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'TREND', 'Gol', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'Trailhawk', 'Compass', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'L200', 'Triton', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'Troco', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'UNO', 'Uno', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'V6', 'Amarok', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'Veiculos', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'Vivace', 'Uno', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'Way', 'Uno', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'XEI', 'Corolla', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'Xei', 'Corolla', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'ZEN', 'Kwid', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'baú', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'civic', 'Civic', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'classic', 'Classic', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'compass', 'Compass', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'fiesta', 'Fiesta', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'fire', 'Palio', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'fit', 'Fit', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'focus', 'Focus', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'hatch', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'jetta', 'Jetta', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'joy', 'Joy', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'ka', 'Ka', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'limited', 'Compass', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'não informado', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'plus', 'Onix', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'PLUS', 'Onix', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'Plus', 'Onix', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'trend', 'Voyage', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'uno', 'Uno', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'veiculos', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'weekend', 'Palio', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'xei', 'Corolla', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'ÔNIX', 'Onix', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\b2008\b', 'Griffe', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\bLike\b', 'Mobi', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\bHiluxV\b', 'Hilux', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\bHiluxX\b', 'Hilux', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\bFull\b', 'Pajero', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'^Cross$', 'Saveiro', regex=True)

df['dscModelo'] = df['dscModelo'].str.replace(
    'CARRO', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'Carro', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'CHEVROLET', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'Chevrolet', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'Benz', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'Benz', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'Automática', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'Automático', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    'AUT', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\bAT\b', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    '4x4', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    '2018/2019', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\b2018\b', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\b2017\b', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\b2014\b', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\b2012/2013\b', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\b2010/2011\b', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\b2010\b', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\b2009\b', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\b1.0\b', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\b1.4\b', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\b1.6\b', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\b1.8\b', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\b2.0\b', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\bltz\b', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\bLTZ\b', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\bdiesel\b', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\bflex\b', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\bVOLKSWAGEN\b', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\bTSI\b', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\bTURBO\b', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\bSPORT\b', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\bSEDAN\b', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\bSedan\b', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\bS\b', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\bNão informado/Não informado\b', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\bMSI\b', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\bMANUAL\b', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\bLT\b', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\bLS\b', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\bHonda\b', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\bFlex\b', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\bEX\b', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\bDIESEL\b', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\bDiesel\b', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\bCompleto\b', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\bFLEX\b', 'Não informado', regex=True)
df['dscModelo'] = df['dscModelo'].str.replace(
    r'\bGNV\b', 'Não informado', regex=True)


groupedMarca = df.groupby('dscMarca')
df['dscMarca'] = groupedMarca['dscMarca'].transform(
    lambda x: x if len(x) > 3 else 'Não informado')

groupedModelo = df.groupby('dscModelo')
df['dscModelo'] = groupedModelo['dscModelo'].transform(
    lambda x: x if len(x) > 3 else 'Não informado')

grouped_novo = df.groupby('dscModelo')
result = grouped_novo.size().to_frame('count')
result.to_csv('output.csv', header=['count'])

df = df.drop('codAnuncio', axis=1)
ads = df.to_numpy()
# print(ads)
# print(df.head(30))
insert_data_into_temp_veiculo(ads)