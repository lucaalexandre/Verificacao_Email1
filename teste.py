import re
import dns.resolver
import smtplib

fromAddress = 'corn@bt.com'
regex = '^[_az0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'

inputAddress = input('Escreva o e mail para a verificação: ')
addressToVerify = str(inputAddress)

match = re.match(regex, addressToVerify)
if match == None:
    print('Bad Syntax')
    raise ValueError('Bad Syntax')


spitAddress = addressToVerify.split('@')
domain = str(spitAddress[1])
print('Domain:', domain)

records = dns.resolver.query(domain, 'MX')
mxRecord = records[0].exchange
mxRecord = str(mxRecord)

server = smtplib.SMTP()
server.set_debuglevel(0)


server.connect(mxRecord)
server.helo(server.local_hostname)
server.mail(fromAddress)
code, message = server.rcpt(str(addressToVerify))
server.quit()

if code == 250:
    print('Esse endereço de e mail e valido')
else:
    print('esse endereço nao existe')
