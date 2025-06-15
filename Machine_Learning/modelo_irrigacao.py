import pandas as pd
import sqlite3
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


# Carregar dados do banco
def carregar_dados():
    conexao = sqlite3.connect('../Banco de dados/farmtech.db')
    df = pd.read_sql_query("SELECT * FROM sensores", conexao)
    conexao.close()
    return df


# Treinar o modelo de ML
def treinar_modelo(df):
    X = df[['umidade', 'nutriente']]
    y = df['irrigar']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo.fit(X_train, y_train)

    y_pred = modelo.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    matriz = confusion_matrix(y_test, y_pred)

    print(f"Acurácia do modelo: {acc:.2f}")
    print("Matriz de Confusão:")
    print(matriz)

    return modelo


# Simular algumas predições
def nova_predicao(modelo, umidade, nutriente):
    pred = modelo.predict([[umidade, nutriente]])
    if pred[0] == 1:
        print(f"Para umidade={umidade}% e nutriente={nutriente}%: IRRIGAR ✅")
    else:
        print(f"Para umidade={umidade}% e nutriente={nutriente}%: NÃO IRRIGAR 🚫")


if __name__ == '__main__':
    df = carregar_dados()
    modelo = treinar_modelo(df)

    # Testes manuais de exemplo
    nova_predicao(modelo, umidade=40, nutriente=20)
    nova_predicao(modelo, umidade=75, nutriente=60)