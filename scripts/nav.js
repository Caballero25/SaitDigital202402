function scrollToSection(event, sectionId) {
    var section = document.getElementById(sectionId);

    if (section) {

        section.scrollIntoView({
            behavior: 'smooth', 
            block: 'start'       // Esto alinea el inicio del elemento con la parte superior del contenedor de desplazamiento
        });
        event.preventDefault();
    }
}

var whatsAppUrl = "https://wa.me/593962636961?text=Estoy%20interesado%20en%20recibir%20una%20cotización%20personalizada%20para%20encargar%20mi%20proyecto%20web.";
document.getElementsByClassName("whatsaap")[0].href=whatsAppUrl


var gmailUrl = "mailto:saittdocuments@gmail.com?subject=Cotización%20personalizada-%20SaitDigital&body=Estoy%20interesado%20en%20recibir%20una%20cotización%20personalizada%20para%20encargar%20mi%20proyecto%20web."
document.getElementsByClassName("gmail")[0].href=gmailUrl

document.getElementsByClassName("facebook")[0].href = "https://www.facebook.com/saitdigital"