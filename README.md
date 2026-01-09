# 📶 Campaner WiFi — Teste de Velocidade de Internet

Aplicativo desktop desenvolvido em **Python com Tkinter** para medir a **velocidade de download e upload da conexão com a internet** de forma simples, rápida e visual.

O sistema utiliza a biblioteca **speedtest-cli**, exibindo os resultados em **Mbps**, com uma interface gráfica limpa e intuitiva.

---

## 🚀 Funcionalidades

-  Teste de velocidade de **Download**
-  Teste de velocidade de **Upload**
-  Resultados exibidos em **Mbps**
-  Botão para repetir o teste quantas vezes quiser
-  Interface gráfica com ícones personalizados
-  Layout compacto e fácil de usar

---

## 🖥 Interface Gráfica

- Desenvolvida com **Tkinter**
- Layout dividido em:
    - Cabeçalho com ícone e título
    - Área principal com resultados
- Ícones visuais para download e upload
- Interface fixa (tamanho não redimensionável)

---

## 🧠 Organização do Código

- **main.py**
  - Criação da interface gráfica
  - Configuração dos frames
  - Integração com a biblioteca `speedtest`
  - Função principal para execução do teste
  - Atualização dinâmica dos valores na tela

---

## 🛠 Tecnologias Utilizadas

- **Python 3**
- **Tkinter**
- **Pillow (PIL)**
- **speedtest-cli**

---

## 📦 Instalação das Dependências

```bash
pip install speedtest-cli pillow
