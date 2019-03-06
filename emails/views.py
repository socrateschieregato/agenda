from certificados.models import Certificados
from datetime import date, timedelta
import email.mime.multipart
import email.mime.text
import smtplib

def sendEmails_cmd():
    today = date.today()

    cert_30 = Certificados.objects.filter(validade__exact=today + timedelta(days=30))
    cert_10 = Certificados.objects.filter(validade__exact=today + timedelta(days=10))
    cert_off = Certificados.objects.filter(validade__lte=today)
    cert_text = ''
    if cert_off:
        cert_text = '\n Vencidos: \n'
        for c in cert_off:
            cert_text = cert_text + c.empresa.razao + ' - ' + c.name + ' - ' + str(c.validade.strftime("%d/%m/%Y")) + ' - '\
                        + c.tipo.tipo_certificado + ' - ' + c.email + '\n'
    if cert_10:
        cert_text = cert_text + '\n\n' + 'a Vencer em 10 dias: \n'
        for c in cert_10:
            cert_text = cert_text + c.empresa.razao + ' - ' + c.name + ' - ' + str(c.validade.strftime("%d/%m/%Y")) + ' - '\
                        + c.tipo.tipo_certificado + ' - ' + c.email + '\n'
    if cert_30:
        cert_text = cert_text + '\n\n' + 'a Vencer em 30 dias: \n'
        for c in cert_30:
            cert_text = cert_text + c.empresa.razao + ' - ' + c.name + ' - ' + str(c.validade.strftime("%d/%m/%Y")) + ' - '\
                        + c.tipo.tipo_certificado + ' - ' + c.email + '\n'

    if cert_text != '':
        # Cabeçalho da mensagem do email
        msg = email.mime.multipart.MIMEMultipart()
        msg['Subject'] = 'Vencimento - Certificado Digital ' + str(today.strftime("%d/%m/%Y"))
        msg['From'] = 'schieregato@gmail.com'
        msg['To'] = 'schieregato@gmail.com'

        # Corpo principal do email (tb um anexo)
        body = email.mime.text.MIMEText("""Bizanha Associados""" + '\n' + cert_text)
        msg.attach(body)

        # # Anexando o PDF
        # pdfname = 'path/meu.pdf'
        # fp = open(pdfname,'rb')
        # anexo = email.mime.application.MIMEApplication(fp.read(), _subtype="pdf")
        # fp.close()
        # anexo.add_header('Content-Disposition','attachment', filename=pdfname)
        # msg.attach(anexo)

        # Enviando via "gmail" server
        s = smtplib.SMTP('smtp.gmail.com',port=587)
        s.starttls()
        s.login('socrates@bizanha.com.br', 'S0cr4#es_ba')
        s.sendmail(msg['From'], msg['To'], msg.as_string())
        s.quit()

        return 'Email enviado com sucesso!'
    else:
        return 'Não há email a ser enviado!'