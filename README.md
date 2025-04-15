Receita Médica Automatizada - Hospital Sabará
Integrantes
Davi Daparé – RM: 560721

Erick Cardoso – RM: 560440

Gabrielly Candido – RM: 560916

João Victor Ferreira – RM: 560439

Luiza Ribeiro – RM: 560200

Descrição do Projeto
Este projeto tem como objetivo automatizar o processo de emissão e envio de receitas médicas no Hospital Sabará. Utilizando tecnologias de reconhecimento de voz, manipulação de arquivos e envio automático por e-mail, o sistema permite que o médico dite a prescrição, que é transcrita automaticamente, preenchida em um modelo .docx padrão e enviada diretamente ao paciente por e-mail.

Objetivos
Reduzir o tempo de emissão de receitas médicas

Minimizar erros manuais na prescrição

Facilitar a comunicação entre médicos e pacientes

Garantir maior organização e segurança no envio das receitas

Funcionalidades
Coleta de dados do paciente (nome e e-mail)

Transcrição automática da receita por comando de voz

Geração de arquivos .docx com base em um modelo personalizado

Nome do arquivo com ID aleatório para preservar o anonimato

Envio automático da receita para o e-mail do paciente com anexo

Tecnologias e Ferramentas Utilizadas
Python 3.x

Bibliotecas:

os

docx

datetime

uuid

speech_recognition

smtplib

email.message

Estrutura do Código
coletar_dados_pacientes(): solicita ao médico o nome e o e-mail do paciente

ouvir_medico(): utiliza o microfone para capturar a receita ditada e transcrevê-la com a API do Google

preencher_receita(): preenche automaticamente um modelo .docx com os dados coletados (nome, receita e data)

enviar_email(): envia a receita para o e-mail do paciente com o arquivo .docx em anexo

Como Executar
Verifique se o Python está instalado e instale as bibliotecas necessárias:

nginx
Copiar
Editar
pip install python-docx speechrecognition
Certifique-se de que o arquivo receita_medica.docx contém os marcadores {{nome_paciente}}, {{receita_formatada}} e {{data}} no conteúdo

Execute o arquivo principal:

nginx
Copiar
Editar
python nome_do_arquivo.py
Digite o nome e o e-mail do paciente quando solicitado

Dite a receita no microfone

O sistema irá gerar automaticamente a receita preenchida e enviá-la por e-mail ao paciente

Contribuição
Este projeto foi desenvolvido como atividade prática da disciplina Computational Thinking With Python, com foco em aplicar habilidades de automação e processamento de dados para solucionar desafios reais.
