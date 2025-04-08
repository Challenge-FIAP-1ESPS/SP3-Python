# Receita Médica Automatizada - Hospital Sabará

**Integrantes**
- Davi Daparé RM: 560721
- Erick Cardoso RM: 560440
- Gabrielly Candido RM: 560916
- João Victor Ferreira RM: 560439
- Luiza Ribeiro RM: 560200

## Descrição do Projeto

Este projeto visa automatizar o processo de emissão e envio de receitas médicas no Hospital Sabará. Por meio da tecnologia de reconhecimento de voz e automação de documentos, o sistema permite que o médico dite a receita, que é transcrita automaticamente, preenchida em um modelo padrão e enviada por e-mail ao paciente.

## Objetivo

- Reduzir o tempo de emissão de receitas médicas;
- Minimizar erros manuais na prescrição;
- Facilitar a comunicação entre médicos e pacientes;
- Melhorar a experiência dos pacientes e a eficiência do atendimento.

## Funcionalidades

- Coleta de dados do paciente (nome e e-mail);
- Reconhecimento de voz para transcrição da receita;
- Preenchimento automático de um modelo de receita médica;
- Envio da receita ao paciente por e-mail com anexo em `.docx`.

## Tecnologias e Ferramentas Utilizadas

- **Python 3.x**
- Bibliotecas:
  - `os`
  - `docx`
  - `datetime`
  - `speech_recognition`
  - `smtplib`
  - `email`

## Estrutura do Código

- **Função `coletar_dados_pacientes()`**: Solicita o nome e e-mail do paciente.
- **Função `ouvir_medico()`**: Utiliza o microfone para capturar a receita ditada pelo médico.
- **Função `preencher_receita()`**: Gera o arquivo `.docx` com os dados coletados.
- **Função `enviar_email()`**: Envia a receita por e-mail automaticamente.

## Fluxograma do Projeto

