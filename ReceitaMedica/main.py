#Importa bibliotecas necessárias
import os  #Trabalha com caminhos e operações do sistema de arquivos
from datetime import datetime  #Trabalha com datas e horários
import speech_recognition as sr  #Reconhecimento de voz
import smtplib  #Envia e-mails usando protocolo SMTP
from email.message import EmailMessage  #Cria e gerencia mensagens de e-mail
import uuid
from fpdf import FPDF  # Biblioteca para gerar arquivos PDF

#Coleta dados do paciente
def coletar_dados_pacientes():
    #Solicita ao usuário o nome do paciente
    nome = input("Digite o nome do paciente: ")
    #Solicita ao usuário o e-mail do paciente
    email = input("Digite o e-mail do paciente: ")
    #Exibe informações coletadas
    print(f"\n[INFO] Nome: {nome}")
    print(f"[INFO] E-mail: {email}")
    #Retorna o nome e e-mail para uso posterior
    return nome, email

#Escuta a voz do médico
def ouvir_medico():
    #Cria um reconhecedor de fala
    recognizer = sr.Recognizer()
    #Configura o microfone como fonte de áudio
    mic = sr.Microphone()

    #Usa o microfone para capturar o áudio
    with mic as source:
        print("\n[INFO] Ajustando ruído de fundo... Aguarde um pouco.")
        #Ajusta o reconhecimento para o ruído ambiente
        recognizer.adjust_for_ambient_noise(source)
        print("[INFO] Pode falar a prescrição agora:")
        #Escuta o que for falado
        audio = recognizer.listen(source)

    try:
        #Tenta reconhecer o áudio usando o Google Speech Recognition
        texto = recognizer.recognize_google(audio, language="pt-BR")
        #Exibe o texto reconhecido
        print(f"\n[TRANSCRIÇÃO] Você disse: {texto}")
        return texto
    except sr.UnknownValueError:
        #Caso não entenda o áudio
        print("[ERRO] Não entendi o que você falou.")
        return ""
    except sr.RequestError as e:
        #Caso tenha problema com o serviço de reconhecimento
        print(f"[ERRO] Problema com o serviço de reconhecimento: {e}")
        return ""

#Preenche a receita no modelo
from fpdf import FPDF  # Biblioteca para gerar arquivos PDF

def preencher_receita_pdf(nome_paciente, receita_formatada):
    pdf = FPDF()  # Cria um novo objeto PDF
    pdf.add_page()  # Adiciona uma nova página em branco no PDF
    pdf.set_font("Arial", size=12)  # Define a fonte inicial como Arial, tamanho 12

    # Obtém a data atual no formato brasileiro (ex: 15/04/2025)
    data_hoje = datetime.now().strftime("%d/%m/%Y")

    # === Cabeçalho ===
    pdf.set_font("Arial", style='B', size=14)  # Define fonte em negrito e maior para o título
    pdf.cell(200, 10, txt="Hospital Sabará - Receita Médica", ln=True, align='C')  # Escreve o título centralizado
    pdf.ln(10)  # Adiciona uma linha em branco (espaçamento)

    # === Informações do paciente ===
    pdf.set_font("Arial", size=12)  # Volta a fonte normal, tamanho 12
    pdf.cell(200, 10, txt=f"Paciente: {nome_paciente}", ln=True)  # Escreve o nome do paciente
    pdf.cell(200, 10, txt=f"Data: {data_hoje}", ln=True)  # Escreve a data da receita
    pdf.ln(10)  # Linha em branco

    # === Prescrição médica ===
    pdf.multi_cell(0, 10, txt=f"Prescrição:\n{receita_formatada}")  # Escreve a prescrição recebida do médico
    pdf.ln(20)  # Espaço antes da assinatura

    # === Assinatura digital e rodapé ===
    pdf.set_font("Arial", size=11)  # Define fonte um pouco menor
    pdf.cell(200, 10, txt=f"Assinado digitalmente em: {data_hoje}", ln=True)  # Mostra a data da assinatura
    pdf.ln(10)  # Espaço em branco
    pdf.cell(200, 10, txt="________________________", ln=True)  # Linha para simular a assinatura
    pdf.cell(200, 10, txt="Dr. Marcos L. Ferreira", ln=True)  # Nome do médico
    pdf.cell(200, 10, txt="CRM-SP 123456", ln=True)  # Registro CRM
    pdf.cell(200, 10, txt="Clínico Geral", ln=True)  # Especialidade médica

    # === Geração e salvamento do PDF ===
    nome_arquivo = f"receita_{uuid.uuid4().hex[:8]}.pdf"  # Cria um nome de arquivo com ID único
    caminho_saida = os.path.join(os.getcwd(), nome_arquivo)  # Define o caminho para salvar o arquivo na pasta atual

    pdf.output(caminho_saida)  # Salva o arquivo PDF no caminho definido

    # Mensagem final confirmando onde o PDF foi salvo
    print(f"\n✅ Receita PDF salva como: {caminho_saida}")

    return caminho_saida  # Retorna o caminho do arquivo gerado para uso posterior (ex: envio por e-mail)




#Envia e-mail com a receita
def enviar_email(destinatario, caminho_anexo, nome_paciente):
    # Cria um objeto de mensagem de e-mail
    msg = EmailMessage()

    # Define o assunto do e-mail que o paciente vai ver na caixa de entrada
    msg["Subject"] = "Receita mágica digital"

    # Define o remetente (quem está enviando o e-mail)
    msg["From"] = "gabriellycasilva@gmail.com"

    # Define o destinatário (o paciente que vai receber a receita)
    msg["To"] = destinatario

    # Define o corpo do e-mail com uma mensagem personalizada
    msg.set_content(f"""Olá, {nome_paciente}

Segue em anexo sua receita mágica.

Atenciosamente,
Hospital Sabará""")

    # Abre o arquivo do PDF gerado com a receita
    with open(caminho_anexo, "rb") as file:
        conteudo = file.read()  # Lê o conteúdo binário do PDF
        nome_arquivo = os.path.basename(caminho_anexo)  # Pega só o nome do arquivo (sem o caminho)

        # Adiciona o PDF como anexo na mensagem
        msg.add_attachment(
            conteudo,  # conteúdo binário do arquivo
            maintype="application",  # tipo principal do arquivo (arquivo genérico)
            subtype="pdf",  # tipo específico (arquivo PDF)
            filename=nome_arquivo  # nome do arquivo que aparecerá no anexo
        )

    # Cria uma conexão segura com o servidor do Gmail pela porta 465
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        # Faz login na conta do Gmail usando uma senha de aplicativo
        smtp.login("gabriellycasilva@gmail.com", "xcup fldl dclb hbzo")

        # Envia a mensagem com o anexo para o destinatário
        smtp.send_message(msg)

    # Mensagem de confirmação no terminal
    print("✅ E-mail enviado com sucesso!")


#Execução principal

# Coleta os dados do paciente
nome_paciente, email_paciente = coletar_dados_pacientes()
#Escuta a prescrição médica através do microfone
transcricao = ouvir_medico()

#Se conseguiu transcrever a prescrição
if transcricao != "":
    #Caminho do modelo de receita que será usado
    caminho_modelo = "receita_medica.docx"
    #Preenche a receita com os dados coletados
    caminho_receita = preencher_receita_pdf(nome_paciente, transcricao)
    #Envia o e-mail com a receita em anexo
    enviar_email(email_paciente, caminho_receita, nome_paciente)
else:
    #Caso não tenha conseguido captar a prescrição, exibe mensagem de erro
    print("[ERRO] Nenhuma prescrição foi detectada, receita não gerada.")

