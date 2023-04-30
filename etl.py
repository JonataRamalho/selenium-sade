import sqlite3
import pandas as pd

conn = sqlite3.connect("anuncios.db")

df = pd.read_sql_query('SELECT * FROM tbl_temp_veiculo', conn)

df['qtdKm'] = df['qtdKm'].str.replace(' km', '', regex=True)
df['qtdKm'] = df['qtdKm'].str.replace('.', '', regex=True)

df['valPreco'] = df['valPreco'].str.replace('R\$ ', '', regex=True)
df['valPreco'] = df['valPreco'].str.replace('.', '', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace(
    '//,1', 'Volkswagen', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('16V', 'Jeep', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('2.0', 'Jeep', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('2.3', 'Nissan', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('2004', 'Mitsubishi', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('', 'Não informado', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('', 'Não informado', regex=True)
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
df['dscMarca'] = df['dscMarca'].str.replace('bmw', 'Bmw', regex=True)

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

df['dscMarca'] = df['dscMarca'].str.replace('C10', 'Chevrolet', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('C3', 'Citroën', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('C4', 'Citroën', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('CAPTUR', 'Renault', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Captur', 'Renault', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace(
    'CELTA', 'Chevrolet', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('CERATO', 'Kia', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Cerato', 'Kia', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('CHERY', 'Chery', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('chery', 'Chery', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Cherry', 'Chery', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('CGI', 'Mercedes-Benz', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('CHEV', 'Chevrolet', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace(
    'CHEVROLET', 'Chevrolet', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('CITROEN', 'Citroën', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('CITROËN', 'Citroën', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Citroem', 'Citroën', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Cintroen', 'Citroën', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('Citröen', 'Citroën', regex=True)


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

df['dscMarca'] = df['dscMarca'].str.replace('Colina', 'Chevrolet', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('Clio', 'Renault', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('COMFORT', 'Hyundai', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('CONFORT', 'Hyundai', regex=True)
df['dscMarca'] = df['dscMarca'].str.replace('CRETA', 'Hyundai', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace('COROLLA', 'Toyota', regex=True)


df['dscMarca'] = df['dscMarca'].str.replace(
    'COMFORTLINE', 'Volkswagen', regex=True)

df['dscMarca'] = df['dscMarca'].str.replace(
    'COMPASS', 'Jeep', regex=True)


grouped = df.groupby('dscMarca')
result = grouped.size()
result.to_csv('output.csv', header=['count'])
