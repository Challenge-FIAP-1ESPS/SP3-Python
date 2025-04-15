# Receita Mágica - Hospital Sabará

## Integrantes

- Davi Daparé – RM: 560721  
- Erick Cardoso – RM: 560440  
- Gabrielly Candido – RM: 560916  
- João Victor Ferreira – RM: 560439  
- Luiza Ribeiro – RM: 560200  

---

## Descrição do Projeto

Este projeto tem como objetivo automatizar o processo de emissão e envio de receitas médicas no Hospital Sabará. Utilizando tecnologias de reconhecimento de voz, manipulação de arquivos `.docx` e envio automático por e-mail, o sistema permite que o médico dite a prescrição, que é transcrita automaticamente, preenchida em um modelo padrão e enviada diretamente ao paciente.

---

## Objetivos

- Reduzir o tempo de emissão de receitas médicas  
- Minimizar erros manuais na prescrição  
- Facilitar a comunicação entre médicos e pacientes  
- Garantir maior organização e segurança no envio das receitas  

---

## Funcionalidades

- Coleta de dados do paciente (nome e e-mail)  
- Transcrição automática da receita por comando de voz  
- Geração de arquivos `.docx` com base em um modelo personalizado  
- Nome do arquivo com ID aleatório para preservar o anonimato  
- Envio automático da receita para o e-mail do paciente com anexo  

---

## Tecnologias e Ferramentas Utilizadas

- Python 3.x  
- Bibliotecas utilizadas:
  - `os`  
  - `docx`  
  - `datetime`  
  - `uuid`  
  - `speech_recognition`  
  - `smtplib`  
  - `email.message`  

---

## Estrutura do Código

- `coletar_dados_pacientes()`: Solicita ao médico o nome e o e-mail do paciente.  
- `ouvir_medico()`: Utiliza o microfone para capturar a receita ditada e transcrevê-la com a API do Google.  
- `preencher_receita()`: Preenche automaticamente um modelo `.docx` com os dados coletados (nome, receita e data).  
- `enviar_email()`: Envia a receita por e-mail ao paciente com o arquivo `.docx` em anexo.  

---

## Como Executar

1. Verifique se o Python está instalado no seu computador.

2. Instale as bibliotecas necessárias com o comando:

5. Siga as instruções no terminal:
- Informe o nome e o e-mail do paciente
- Dite a prescrição médica
- Aguarde o envio automático da receita por e-mail

---

## 📚 Contribuição

Este projeto foi desenvolvido como atividade prática da disciplina **Computational Thinking With Python**, com o objetivo de aplicar conhecimentos em automação, transcrição de voz e manipulação de arquivos, solucionando problemas reais do cotidiano médico.

