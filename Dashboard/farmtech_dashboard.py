import pandas as pd
import sqlite3
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# Conectar ao banco
def carregar_dados():
    conexao = sqlite3.connect('../Banco de dados/farmtech.db')
    df = pd.read_sql_query("SELECT * FROM sensores", conexao)
    conexao.close()
    return df


# Treinar o modelo
@st.cache_data
def treinar_modelo(df):
    X = df[['umidade', 'nutriente']]
    y = df['irrigar']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo.fit(X_train, y_train)

    y_pred = modelo.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    return modelo, acc


# Função principal
def app():
    st.title("🌿 FarmTech Solutions - Sistema de Irrigação Inteligente 🚀")

    # Carrega dados e treina modelo
    df = carregar_dados()
    modelo, acc = treinar_modelo(df)

    st.subheader("📊 Dados Coletados:")
    st.dataframe(df)

    st.subheader("🎯 Performance do Modelo:")
    st.write(f"Acurácia: {acc:.2%}")

    st.subheader("🔮 Simulador de Predição:")

    # Inputs via interface
    umidade = st.slider("Umidade do Solo (%)", 0, 100, 50)
    nutriente = st.slider("Nível de Nutrientes (%)", 0, 100, 50)

    pred = modelo.predict([[umidade, nutriente]])[0]

    if pred == 1:
        st.success("✅ Ação sugerida: IRRIGAR")
    else:
        st.warning("🚫 Ação sugerida: NÃO IRRIGAR")


if __name__ == '__main__':
    app()
