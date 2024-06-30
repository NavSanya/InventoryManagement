import yagmail
yag = yagmail.SMTP('anandnavsanya', 'opfd qrpr vrgl vybu')
contents = ['This is the body, and here is just text http://somedomain/image.png',
            'You can find an audio file attached.']
yag.send('navsanyanand@gmail.com', 'Hello Test Python', contents)