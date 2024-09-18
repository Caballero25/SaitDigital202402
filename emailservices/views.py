from django.http import JsonResponse
import smtplib
from rest_framework.decorators import api_view

@api_view(['POST'])
def sendEmailContact(request):
    domainCommon = (
                        ".com", ".net", ".org", ".edu", ".gov", ".mil", ".info", ".biz", ".name", ".co", ".io", 
                        ".dev", ".ai", ".app", ".xyz", ".online", ".site", ".shop", ".blog", ".tv", ".ws", ".me", 
                        ".us", ".uk", ".de", ".fr", ".es", ".it", ".ca", ".au", ".br", ".tech", ".ec"
);
    if request.method == "POST":
        print("post")
        status = False 
        message = ""
        correo_cliente: str = request.data.get('email')
        mensaje_cliente: str = request.data.get('message')
        print(correo_cliente)
        print(mensaje_cliente)
        if correo_cliente == None or correo_cliente == "" or mensaje_cliente == None or mensaje_cliente == "":
            status = False
            message = "Los campos no pueden estar vacíos"
        elif "@" not in correo_cliente or correo_cliente.endswith(domainCommon) == False:
            status = False
            message = "Correo electrónico no contiene formato válido"
        else:
            try:
                mensaje = f"""
                    El usuario {correo_cliente} quiere comunicarse contigo. \n
                    \n
                    Mensaje: {mensaje_cliente}
                """
                correo_recibe = "saittdocuments@gmail.com"
                asunto = f"Mensaje de {correo_cliente}"

                body = 'Subject: {}\n\n{}'.format(asunto, mensaje)
                server = smtplib.SMTP('smtp.gmail.com','587')
                server.starttls()
                server.login('frankpereira1258@gmail.com','hzny zpim xjlr yfjj')
                server.sendmail(correo_cliente, correo_recibe, body.encode('utf-8'))
                server.quit()
                status = True 
                message = "Su correo fue enviado exitosamente"
            except:
                status = False
                message = "Los servicios de Google no pudieron enviar el correo, por favor utilice otro medio para comunicarse con SaitDigital"
        return JsonResponse({'status': status, "message": message}, status=200)