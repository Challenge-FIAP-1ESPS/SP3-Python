import os
from docx import Document
from datetime import datetime
import speech_recognition as sr
import smtplib
from email.message import EmailMessage


def coletar_dados_pacientes():
    nome = input("Digite o nome do paciente: ")
    email = input("Digite o e-mail do paciente: ")
    print(f"\n[INFO] Nome: {nome}")
    print(f"[INFO] E-mail: {email}")
    return nome, email


def ouvir_medico():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("\n[INFO] Ajustando ruído de fundo... Aguarde um pouco.")
        recognizer.adjust_for_ambient_noise(source)
        print("[INFO] Pode falar a prescrição agora:")
        audio = recognizer.listen(source)

    try:
        texto = recognizer.recognize_google(audio, language="pt-BR")
        print(f"\n[TRANSCRIÇÃO] Você disse: {texto}")
        return texto
    except sr.UnknownValueError:
        print("[ERRO] Não entendi o que você falou.")
        return ""
    except sr.RequestError as e:
        print(f"[ERRO] Problema com o serviço de reconhecimento: {e}")
        return ""


def preencher_receita(nome_paciente, receita_formatada, caminho_modelo):
    doc = Document(caminho_modelo)
    data_hoje = datetime.now().strftime("%d/%m/%Y")

    for paragrafo in doc.paragraphs:
        paragrafo.text = paragrafo.text.replace("{{nome_paciente}}", nome_paciente)
        paragrafo.text = paragrafo.text.replace("{{receita_formatada}}", receita_formatada)
        paragrafo.text = paragrafo.text.replace("{{data}}", data_hoje)

    nome_arquivo = f"receita_{nome_paciente.replace(' ', '_')}.docx"
    caminho_saida = os.path.join(os.getcwd(), nome_arquivo)
    doc.save(caminho_saida)
    print(f"\n✅ Receita salva como: {caminho_saida}")
    return caminho_saida


def enviar_email(destinatario, caminho_anexo, nome_paciente):
    msg = EmailMessage()
    msg["Subject"] = "Receita médica digital"
    msg["From"] = "gabriellycasilva@gmail.com"
    msg["To"] = destinatario
    msg.set_content(f"Olá {nome_paciente},\n\nSegue em anexo sua receita médica.\n\nAtenciosamente,\nHospital Sabará")

    with open(caminho_anexo, "rb") as file:
        conteudo = file.read()
        nome_arquivo = os.path.basename(caminho_anexo)
        msg.add_attachment(conteudo, maintype="application", subtype="vnd.openxmlformats-officedocument.wordprocessingml.document", filename=nome_arquivo)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("gabriellycasilva@gmail.com", "xcup fldl dclb hbzo")  # <- senha de app
        smtp.send_message(msg)

    print("✅ E-mail enviado com sucesso!")



nome_paciente, email_paciente = coletar_dados_pacientes()
transcricao = ouvir_medico()

if transcricao != "":
    caminho_modelo = "receita_medica.docx"
    caminho_receita = preencher_receita(nome_paciente, transcricao, caminho_modelo)
    enviar_email(email_paciente, caminho_receita, nome_paciente)
else:
    print("[ERRO] Nenhuma prescrição foi detectada, receita não gerada.")
