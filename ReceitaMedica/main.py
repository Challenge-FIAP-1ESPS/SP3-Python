#Importa bibliotecas necessárias
import os  #Trabalha com caminhos e operações do sistema de arquivos
from docx import Document  #Manipula documentos do Word (.docx)
from datetime import datetime  #Trabalha com datas e horários
import speech_recognition as sr  #Reconhecimento de voz
import smtplib  #Envia e-mails usando protocolo SMTP
from email.message import EmailMessage  #Cria e gerencia mensagens de e-mail

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
def preencher_receita(nome_paciente, receita_formatada, caminho_modelo):
    #Abre o modelo da receita (arquivo .docx)
    doc = Document(caminho_modelo)
    #Pega a data atual formatada
    data_hoje = datetime.now().strftime("%d/%m/%Y")

    #Substitui os marcadores no modelo pelo conteúdo real
    for paragrafo in doc.paragraphs:
        paragrafo.text = paragrafo.text.replace("{{nome_paciente}}", nome_paciente)
        paragrafo.text = paragrafo.text.replace("{{receita_formatada}}", receita_formatada)
        paragrafo.text = paragrafo.text.replace("{{data}}", data_hoje)

    #Define o nome do arquivo de saída baseado no nome do paciente
    nome_arquivo = f"receita_{nome_paciente.replace(' ', '_')}.docx"
    #Cria o caminho completo para salvar o arquivo
    caminho_saida = os.path.join(os.getcwd(), nome_arquivo)
    #Salva o novo documento preenchido
    doc.save(caminho_saida)
    print(f"\n✅ Receita salva como: {caminho_saida}")
    return caminho_saida  #Retorna o caminho do arquivo gerado

#Envia e-mail com a receita
def enviar_email(destinatario, caminho_anexo, nome_paciente):
    #Cria uma nova mensagem de e-mail
    msg = EmailMessage()
    msg["Subject"] = "Receita médica digital"  # Assunto do e-mail
    msg["From"] = "gabriellycasilva@gmail.com"  # Remetente
    msg["To"] = destinatario  # Destinatário
    #Corpo do e-mail
    msg.set_content(f"Olá {nome_paciente},\n\nSegue em anexo sua receita médica.\n\nAtenciosamente,\nHospital Sabará")

    #Abre o arquivo da receita para anexar ao e-mail
    with open(caminho_anexo, "rb") as file:
        conteudo = file.read()
        nome_arquivo = os.path.basename(caminho_anexo)
        #Adiciona o anexo ao e-mail
        msg.add_attachment(
            conteudo,
            maintype="application",
            subtype="vnd.openxmlformats-officedocument.wordprocessingml.document",
            filename=nome_arquivo
        )

    #Conecta ao servidor do Gmail usando conexão segura
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        #Faz login com e-mail e senha de aplicativo
        smtp.login("gabriellycasilva@gmail.com", "xcup fldl dclb hbzo")  # <- senha de app
        #Envia a mensagem de e-mail
        smtp.send_message(msg)

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
    caminho_receita = preencher_receita(nome_paciente, transcricao, caminho_modelo)
    #Envia o e-mail com a receita em anexo
    enviar_email(email_paciente, caminho_receita, nome_paciente)
else:
    #Caso não tenha conseguido captar a prescrição, exibe mensagem de erro
    print("[ERRO] Nenhuma prescrição foi detectada, receita não gerada.")

