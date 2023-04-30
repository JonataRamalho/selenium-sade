import sqlite3
import pandas as pd

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
df['dscMarca'] = df['dscMarca'].str.replace('2020/2020', 'Mercedes Benz', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('4porta', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('ACTIVE', 'Peugeot', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('AGILE', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('ALLURE', 'Peugeot', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('ASX', 'Mitsubishi', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Activ', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Agile', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Alfa', 'Alfa Romeo', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Allure', 'Peugeot', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('ALUGO', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('ALUGUEL', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('ANO', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('AT', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('ATACAMA', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('AUT', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('AUTOMÁTICA', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('AWD', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Aaa', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Aceita', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Altomovel', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Aluga', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Alugo', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Aluguel', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Ambulância', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Ap', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Arapiraca-Al', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Asia', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Automóvel', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Autonino', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Baixei', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Baixou', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Botão', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('CARRO', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('CLIQUE', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('2017', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('2018', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('2021/2022', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('4P', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('ACEITO', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('AP', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('CERNão informadoO', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Carro', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Carrocinha', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Comf', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Carros', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('CERO', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Cabine', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Caminhão', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Camionete', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('DRIVE', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Completa', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Completo', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Corda', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('zap', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(r'\bv\b', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('troco', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('DIESEL', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('sport', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('sedan', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Deus', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Diesel', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(r'\bECO\b', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('EVOL', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('new', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('kms', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Não informado/', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Não informadoACAMA', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Não informadoOMÁTICA', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Não informadoUTION', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Não informadoage', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Não informadocinha', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Não informadoort', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Não informados', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('flex', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('CNão informadoTUR', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(r'\bEco\b', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('EcoNão informado', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('EcoNão informadoe', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('EcoeNão informado', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Edifício', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(r'\bel\b', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Engate', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Extra', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('FINão informado', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('FLEX', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Flat', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Flex', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('EXCLUSIVO', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('EXTRA', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Fapinha', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('GNV', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('GRAN', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('GRAND', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('GRIFFE', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Geração', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Gnv', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Gran', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Grand', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Grande', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('HNão informadoCH', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Hatch', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Hoje', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('IMPECÁVEL', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('IMPERDÍVEL', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('IPVA', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Impecável', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Imponente', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Junior', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(r'\bL\b', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace(r'\bKM\b', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('LEIA', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('LIKE', 'Não informado', regex=True)
# df['dscMarca'] = df['dscMarca'].str.replace('', 'Não informado', regex=True)
# df['dscMarca'] = df['dscMarca'].str.replace('', 'Não informado', regex=True)
# df['dscMarca'] = df['dscMarca'].str.replace('', 'Não informado', regex=True)
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

df['dscMarca'] = df['dscMarca'].str.replace('EVOLUTION', 'Mitsubishi', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Evolution', 'Mitsubishi', regex=True)

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
df['dscMarca'] = df['dscMarca'].str.replace('FinancioVolkswagen9', 'Volkswagen', regex=True)
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
df['dscMarca'] = df['dscMarca'].str.replace('GLX', 'Citroën', regex=True)
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
df['dscMarca'] = df['dscMarca'].str.replace('Chevrolet/', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Creta', 'Hyundai', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Gol', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Gol', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Golf', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Komby', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Kombi', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('KOMBI', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('HIGHLINE', 'Volkswagen', regex=True)
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
df['dscMarca'] = df['dscMarca'].str.replace('HyundaiLINE', 'Hyundai', regex=True)
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
df['dscMarca'] = df['dscMarca'].str.replace('Hyundai20S', 'Hyundai', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Hyundai20s', 'Hyundai', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Hyundai20x', 'Hyundai', regex=True)
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
df['dscMarca'] = df['dscMarca'].str.replace('', '', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('', '', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('', '', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Não informadoortChevrolet', 'Chevrolet', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Não informadoortline', 'Volkswagen', regex=True)








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

df['dscMarca'] = df['dscMarca'].str.replace('special', 'Volkswagen', regex=True)

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




grouped = df.groupby('dscMarca')
result = grouped.size()
result.to_csv('output.csv', header=['count'])
