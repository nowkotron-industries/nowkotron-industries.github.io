"""Builds the privacy policy pages from one template, one per language.

Run from the repository root: python tools/build.py
The contact address lives in CONTACT, so it only has to change here.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTACT = "CORREO_DE_CONTACTO"
PUBLISHER = "Nowkotron Industries"

LANGS = [
    ("es", "privacidad", "Español"),
    ("en", "privacy", "English"),
    ("pt-BR", "privacidade", "Português"),
    ("ca", "privadesa", "Català"),
]

STYLE = """
  :root { --bg: #fbf5ec; --ink: #3a2a22; --muted: #6f5c52; --accent: #b8553d; --line: #e6d8c9; }
  @media (prefers-color-scheme: dark) {
    :root { --bg: #1f1a17; --ink: #f1e7de; --muted: #c2b3a8; --accent: #e58a70; --line: #40362f; }
  }
  body { margin: 0; background: var(--bg); color: var(--ink); font: 17px/1.6 system-ui, -apple-system, "Segoe UI", Roboto, sans-serif; }
  main { max-width: 720px; margin: 0 auto; padding: 24px 16px 64px; }
  nav { display: flex; flex-wrap: wrap; gap: 4px 16px; font-size: 15px; margin-bottom: 24px; }
  nav a[aria-current] { color: var(--ink); font-weight: 600; text-decoration: none; }
  h1 { font-family: Georgia, "Noto Serif", serif; color: var(--accent); font-size: 32px; line-height: 1.2; margin: 0 0 4px; }
  h2 { font-size: 20px; margin: 32px 0 8px; }
  p, li { margin: 6px 0; }
  .date { color: var(--muted); margin-bottom: 24px; }
  .box { border: 1px solid var(--line); border-radius: 12px; padding: 12px 16px; }
  footer { color: var(--muted); font-size: 15px; margin-top: 48px; border-top: 1px solid var(--line); padding-top: 16px; }
  a { color: var(--accent); }
"""

MAIL = f'<a href="mailto:{CONTACT}">{CONTACT}</a>'

TEXT = {
    "es": dict(
        title="Política de privacidad de Ciclo",
        date="Última actualización: 9 de noviembre de 2026",
        summary="<strong>En resumen:</strong> Ciclo no recoge ningún dato. Todo lo que anotas se guarda en tu móvil y, si tienes activada la copia de seguridad de Google, en esa copia, cifrada con el bloqueo de tu pantalla. Nadie más, tampoco quien ha creado la app, tiene acceso a ello.",
        sections=[
            ("Quién publica Ciclo", f"<p>Ciclo es una app de {PUBLISHER}. Para cualquier pregunta sobre esta política o sobre tus datos, escribe a {MAIL}.</p>"),
            ("Qué guarda la app", """<p>Para funcionar, Ciclo guarda en tu móvil:</p>
<ul>
  <li>Las fechas de inicio y fin de las reglas que anotas.</li>
  <li>Tus ajustes: la duración habitual del ciclo y de la regla, el aspecto del asistente y qué notificaciones quieres recibir.</li>
  <li>El dibujo del asistente, si haces uno.</li>
  <li>Tu respuesta a «¿Qué tal vas?» de hoy. Se sustituye al día siguiente y no se guarda ningún historial.</li>
  <li>El último mensaje que escribiste para «Emitir aviso», si escribes uno.</li>
</ul>"""),
            ("Dónde se guarda", "<p>En tu móvil. Ciclo no tiene cuentas ni servidores propios, no muestra anuncios y no incluye servicios de terceros ni herramientas de analítica. La app no tiene permiso para conectarse a internet, así que no puede enviar nada a ningún sitio.</p>"),
            ("Copia de seguridad de Google", """<p>Si tienes activada la copia de seguridad de Android en tu cuenta de Google, Android incluye en ella los datos de Ciclo, para que vuelvan solos si cambias a otro móvil con la misma cuenta de Google o reinstalas la app. Ciclo solo permite esta copia si va cifrada de extremo a extremo con el PIN, patrón o contraseña de tu pantalla de bloqueo: ni Google ni quien ha creado la app puede leerla. Si tu móvil no tiene bloqueo de pantalla, o tiene Android 8, los datos de Ciclo no se copian.</p>
<p>Esta copia es un servicio de Android entre tú y Google: la app no envía nada por su cuenta ni recibe nada de ella. Puedes desactivarla en los ajustes de Android, en el apartado de copia de seguridad. Al pasar los datos a un móvil nuevo por cable o de forma inalámbrica, también se trasladan los de Ciclo.</p>"""),
            ("Lo que sale de la app porque tú lo decides", """<p>Solo sale de Ciclo lo que tú eliges compartir o guardar:</p>
<ul>
  <li><strong>Emitir aviso:</strong> una imagen con una frase que envías con la app que elijas. Llega solo a quien tú decidas.</li>
  <li><strong>Informe:</strong> un PDF con las fechas de tus reglas que puedes compartir, guardar o imprimir.</li>
  <li><strong>Copias:</strong> un archivo con el estado de la app que guardas donde tú elijas. Este archivo no tiene contraseña: guárdalo en un lugar de confianza.</li>
</ul>
<p>Desde ese momento, esos archivos quedan bajo tu control y bajo las condiciones de la app o el servicio que uses para enviarlos o guardarlos.</p>"""),
            ("Permisos", """<p>El único permiso que Ciclo te pide es el de mostrar notificaciones, que sirven para avisarte cuando falta poco para la regla o para preguntarte si ya ha llegado o se ha ido. Es opcional: puedes rechazarlo o desactivar cada aviso en Ajustes.</p>
<p>Además, Android concede a la app algunos permisos técnicos para programar esos avisos, por ejemplo para volver a programarlos cuando reinicias el móvil. Ninguno da acceso a internet ni a tus datos.</p>"""),
            ("Cómo borrar tus datos", "<p>En Ajustes › Tus datos › «Borrar todos mis datos». También se borra todo del móvil al desinstalar la app. La copia de seguridad de Google se vacía la próxima vez que se actualiza tras borrar los datos; si desinstalas la app, se conserva por si la vuelves a instalar, y puedes eliminarla desde la copia de seguridad de tu cuenta de Google. Las copias que hayas guardado tú en archivos no se borran: puedes eliminarlas tú.</p>"),
            ("Menores", "<p>Ciclo no recoge datos de nadie, tampoco de menores de edad.</p>"),
            ("Salud", "<p>Las fechas de Ciclo son estimaciones a partir de lo que anotas. La app no es un método anticonceptivo, no sirve para buscar un embarazo y no sustituye el consejo médico.</p>"),
            ("Cambios en esta política", "<p>Si la política cambia, se publicará aquí con su nueva fecha.</p>"),
            ("Contacto", f"<p>Si tienes cualquier pregunta sobre esta política, escribe a {MAIL}.</p>"),
        ],
    ),
    "en": dict(
        title="Ciclo privacy policy",
        date="Last updated: November 9, 2026",
        summary="<strong>In short:</strong> Ciclo doesn’t collect any data. Everything you log is stored on your phone and, if Google backup is on, in that backup, encrypted with your screen lock. Nobody else, including whoever made the app, has access to it.",
        sections=[
            ("Who publishes Ciclo", f"<p>Ciclo is an app by {PUBLISHER}. For any question about this policy or your data, write to {MAIL}.</p>"),
            ("What the app stores", """<p>To work, Ciclo stores on your phone:</p>
<ul>
  <li>The start and end dates of the periods you log.</li>
  <li>Your settings: usual cycle and period length, your sidekick’s look and which notifications you want.</li>
  <li>Your sidekick drawing, if you make one.</li>
  <li>Today’s answer to “How are you?”. It’s replaced the next day and no history is kept.</li>
  <li>The last message you wrote for “Make an announcement”, if you write one.</li>
</ul>"""),
            ("Where it’s stored", "<p>On your phone. Ciclo has no accounts or servers of its own, shows no ads and includes no third-party services or analytics tools. The app has no permission to connect to the internet, so it can’t send anything anywhere.</p>"),
            ("Google backup", """<p>If Android backup is on for your Google account, Android includes Ciclo’s data in it, so it comes back by itself if you switch to another phone with the same Google account or reinstall the app. Ciclo only allows this backup when it’s end-to-end encrypted with your screen lock PIN, pattern or password: neither Google nor whoever made the app can read it. If your phone has no screen lock, or runs Android 8, Ciclo’s data isn’t backed up.</p>
<p>This backup is an Android service between you and Google: the app sends nothing on its own and receives nothing from it. You can turn it off in Android’s settings, under backup. When you move your data to a new phone by cable or wirelessly, Ciclo’s data moves too.</p>"""),
            ("What leaves the app because you decide so", """<p>Only what you choose to share or save leaves Ciclo:</p>
<ul>
  <li><strong>Make an announcement:</strong> a picture with a phrase that you send with the app you choose. It only reaches whoever you decide.</li>
  <li><strong>Report:</strong> a PDF with your period dates that you can share, save or print.</li>
  <li><strong>Backups:</strong> a file with the app’s data that you save wherever you choose. This file has no password: keep it somewhere you trust.</li>
</ul>
<p>From then on, those files are under your control and under the terms of the app or service you use to send or store them.</p>"""),
            ("Permissions", """<p>The only permission Ciclo asks for is to show notifications, which let you know when your period is coming soon or ask whether it has started or ended. It’s optional: you can decline it or turn each reminder off in Settings.</p>
<p>Android also grants the app a few technical permissions to schedule those reminders, for example to schedule them again after you restart your phone. None of them gives access to the internet or to your data.</p>"""),
            ("How to delete your data", "<p>Go to Settings › Your data › “Delete all my data”. Uninstalling the app also deletes everything from the phone. The Google backup is emptied the next time it updates after you delete your data; if you uninstall the app, it’s kept in case you install it again, and you can delete it from your Google account’s backup. Backup files you saved yourself aren’t deleted: you can delete them yourself.</p>"),
            ("Children", "<p>Ciclo doesn’t collect data from anyone, children included.</p>"),
            ("Health", "<p>Ciclo’s dates are estimates based on what you log. The app is not a contraceptive method, can’t be used to plan a pregnancy and doesn’t replace medical advice.</p>"),
            ("Changes to this policy", "<p>If the policy changes, it will be published here with its new date.</p>"),
            ("Contact", f"<p>If you have any question about this policy, write to {MAIL}.</p>"),
        ],
    ),
    "pt-BR": dict(
        title="Política de privacidade do Ciclo",
        date="Última atualização: 9 de novembro de 2026",
        summary="<strong>Em resumo:</strong> o Ciclo não coleta nenhum dado. Tudo o que você anota fica salvo no seu celular e, se o backup do Google estiver ativado, nesse backup, criptografado com o bloqueio de tela. Mais ninguém, nem quem fez o app, tem acesso a isso.",
        sections=[
            ("Quem publica o Ciclo", f"<p>O Ciclo é um app da {PUBLISHER}. Para qualquer dúvida sobre esta política ou sobre seus dados, escreva para {MAIL}.</p>"),
            ("O que o app salva", """<p>Para funcionar, o Ciclo salva no seu celular:</p>
<ul>
  <li>As datas de início e fim das menstruações que você anota.</li>
  <li>Seus ajustes: a duração habitual do ciclo e da menstruação, o visual do assistente e quais notificações você quer receber.</li>
  <li>O desenho do assistente, se você fizer um.</li>
  <li>Sua resposta de hoje a “Como você tá?”. Ela é substituída no dia seguinte e nenhum histórico é guardado.</li>
  <li>A última mensagem que você escreveu em “Emitir aviso”, se escrever uma.</li>
</ul>"""),
            ("Onde fica salvo", "<p>No seu celular. O Ciclo não tem contas nem servidores próprios, não mostra anúncios e não inclui serviços de terceiros nem ferramentas de análise. O app não tem permissão para se conectar à internet, então não consegue enviar nada para lugar nenhum.</p>"),
            ("Backup do Google", """<p>Se o backup do Android estiver ativado na sua conta do Google, o Android inclui nele os dados do Ciclo, para que voltem sozinhos se você trocar para outro celular com a mesma conta do Google ou reinstalar o app. O Ciclo só permite esse backup se ele for criptografado de ponta a ponta com o PIN, padrão ou senha do seu bloqueio de tela: nem o Google nem quem fez o app consegue lê-lo. Se o seu celular não tiver bloqueio de tela, ou tiver Android 8, os dados do Ciclo não são copiados.</p>
<p>Esse backup é um serviço do Android entre você e o Google: o app não envia nada por conta própria nem recebe nada dele. Você pode desativá-lo nas configurações do Android, na parte de backup. Ao passar os dados para um celular novo por cabo ou sem fio, os do Ciclo também vão junto.</p>"""),
            ("O que sai do app porque você decide", """<p>Só sai do Ciclo o que você escolhe compartilhar ou salvar:</p>
<ul>
  <li><strong>Emitir aviso:</strong> uma imagem com uma frase que você envia pelo app que escolher. Só chega a quem você decidir.</li>
  <li><strong>Relatório:</strong> um PDF com as datas das suas menstruações que você pode compartilhar, salvar ou imprimir.</li>
  <li><strong>Cópias:</strong> um arquivo com os dados do app que você salva onde quiser. Esse arquivo não tem senha: guarde-o num lugar de confiança.</li>
</ul>
<p>A partir daí, esses arquivos ficam sob o seu controle e sob as condições do app ou serviço que você usar para enviá-los ou guardá-los.</p>"""),
            ("Permissões", """<p>A única permissão que o Ciclo pede é a de mostrar notificações, que servem para avisar quando falta pouco para a menstruação ou para perguntar se ela já desceu ou já foi embora. É opcional: você pode recusá-la ou desativar cada aviso em Ajustes.</p>
<p>Além disso, o Android concede ao app algumas permissões técnicas para programar esses avisos, por exemplo para reprogramá-los quando você reinicia o celular. Nenhuma dá acesso à internet nem aos seus dados.</p>"""),
            ("Como apagar seus dados", "<p>Em Ajustes › Seus dados › “Apagar todos os meus dados”. Ao desinstalar o app, tudo também é apagado do celular. O backup do Google é esvaziado na próxima atualização depois que você apaga os dados; se você desinstalar o app, ele fica guardado caso você instale de novo, e você pode excluí-lo no backup da sua conta do Google. As cópias que você salvou em arquivos não são apagadas: você pode excluí-las quando quiser.</p>"),
            ("Menores de idade", "<p>O Ciclo não coleta dados de ninguém, nem de menores de idade.</p>"),
            ("Saúde", "<p>As datas do Ciclo são estimativas a partir do que você anota. O app não é um método anticoncepcional, não serve para planejar uma gravidez e não substitui a orientação médica.</p>"),
            ("Mudanças nesta política", "<p>Se a política mudar, ela será publicada aqui com a nova data.</p>"),
            ("Contato", f"<p>Se tiver qualquer dúvida sobre esta política, escreva para {MAIL}.</p>"),
        ],
    ),
    "ca": dict(
        title="Política de privadesa de Ciclo",
        date="Última actualització: 9 de novembre de 2026",
        summary="<strong>En resum:</strong> Ciclo no recull cap dada. Tot el que anotes es desa al teu mòbil i, si tens activada la còpia de seguretat de Google, en aquesta còpia, xifrada amb el bloqueig de pantalla. Ningú més, tampoc qui ha creat l’app, hi té accés.",
        sections=[
            ("Qui publica Ciclo", f"<p>Ciclo és una app de {PUBLISHER}. Per a qualsevol pregunta sobre aquesta política o sobre les teves dades, escriu a {MAIL}.</p>"),
            ("Què desa l’app", """<p>Per funcionar, Ciclo desa al teu mòbil:</p>
<ul>
  <li>Les dates d’inici i final de les regles que anotes.</li>
  <li>Els teus ajustos: la durada habitual del cicle i de la regla, l’aspecte de l’assistent i quines notificacions vols rebre.</li>
  <li>El dibuix de l’assistent, si en fas un.</li>
  <li>La teva resposta d’avui a «Com estàs?». Se substitueix l’endemà i no es desa cap historial.</li>
  <li>L’últim missatge que vas escriure per a «Emetre avís», si n’escrius un.</li>
</ul>"""),
            ("On es desa", "<p>Al teu mòbil. Ciclo no té comptes ni servidors propis, no mostra anuncis i no inclou serveis de tercers ni eines d’analítica. L’app no té permís per connectar-se a internet, així que no pot enviar res enlloc.</p>"),
            ("Còpia de seguretat de Google", """<p>Si tens activada la còpia de seguretat d’Android al teu compte de Google, Android hi inclou les dades de Ciclo, perquè tornin soles si canvies a un altre mòbil amb el mateix compte de Google o reinstal·les l’app. Ciclo només permet aquesta còpia si va xifrada d’extrem a extrem amb el PIN, el patró o la contrasenya del bloqueig de pantalla: ni Google ni qui ha creat l’app la pot llegir. Si el teu mòbil no té bloqueig de pantalla, o té Android 8, les dades de Ciclo no es copien.</p>
<p>Aquesta còpia és un servei d’Android entre tu i Google: l’app no envia res pel seu compte ni en rep res. La pots desactivar als ajustos d’Android, a l’apartat de còpia de seguretat. Quan passes les dades a un mòbil nou per cable o sense fil, les de Ciclo també s’hi traslladen.</p>"""),
            ("El que surt de l’app perquè tu ho decideixes", """<p>Només surt de Ciclo el que tries compartir o desar:</p>
<ul>
  <li><strong>Emetre avís:</strong> una imatge amb una frase que envies amb l’app que triïs. Només arriba a qui tu decideixis.</li>
  <li><strong>Informe:</strong> un PDF amb les dates de les teves regles que pots compartir, desar o imprimir.</li>
  <li><strong>Còpies:</strong> un fitxer amb l’estat de l’app que deses on vulguis. Aquest fitxer no té contrasenya: desa’l en un lloc de confiança.</li>
</ul>
<p>A partir d’aquell moment, aquests fitxers queden sota el teu control i sota les condicions de l’app o el servei que facis servir per enviar-los o desar-los.</p>"""),
            ("Permisos", """<p>L’únic permís que et demana Ciclo és el de mostrar notificacions, que serveixen per avisar-te quan falta poc per a la regla o per preguntar-te si ja ha arribat o ja se n’ha anat. És opcional: el pots rebutjar o desactivar cada avís a Ajustos.</p>
<p>A més, Android concedeix a l’app alguns permisos tècnics per programar aquests avisos, per exemple per tornar-los a programar quan reinicies el mòbil. Cap d’ells dona accés a internet ni a les teves dades.</p>"""),
            ("Com esborrar les teves dades", "<p>A Ajustos › Les teves dades › «Esborrar totes les meves dades». També s’esborra tot del mòbil en desinstal·lar l’app. La còpia de seguretat de Google es buida la propera vegada que s’actualitza després d’esborrar les dades; si desinstal·les l’app, es conserva per si la tornes a instal·lar, i la pots eliminar des de la còpia de seguretat del teu compte de Google. Les còpies que hagis desat tu en fitxers no s’esborren: les pots eliminar tu.</p>"),
            ("Menors", "<p>Ciclo no recull dades de ningú, tampoc de menors d’edat.</p>"),
            ("Salut", "<p>Les dates de Ciclo són estimacions a partir del que anotes. L’app no és un mètode anticonceptiu, no serveix per buscar un embaràs i no substitueix el consell mèdic.</p>"),
            ("Canvis en aquesta política", "<p>Si la política canvia, es publicarà aquí amb la nova data.</p>"),
            ("Contacte", f"<p>Si tens qualsevol pregunta sobre aquesta política, escriu a {MAIL}.</p>"),
        ],
    ),
}


def page(lang: str, folder: str) -> str:
    t = TEXT[lang]
    nav = " ".join(
        f'<a href="../{f}/" hreflang="{l}" lang="{l}"' + (' aria-current="page"' if l == lang else "") + f">{name}</a>"
        for l, f, name in LANGS
    )
    alternates = "\n".join(
        f'<link rel="alternate" hreflang="{l}" href="https://nowkotron-industries.github.io/ciclo/{f}/">' for l, f, _ in LANGS
    )
    body = "\n\n".join(f"<h2>{h}</h2>\n{html}" for h, html in t["sections"])
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t["title"]}</title>
{alternates}
<style>{STYLE}</style>
</head>
<body>
<main>
<nav aria-label="Idioma / Language">{nav}</nav>
<h1>{t["title"]}</h1>
<p class="date">{t["date"]}</p>

<p class="box">{t["summary"]}</p>

{body}

<footer>{PUBLISHER}</footer>
</main>
</body>
</html>
"""


INDEX = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{PUBLISHER}</title>
<style>{STYLE}
  ul {{ padding-left: 20px; }}
</style>
</head>
<body>
<main>
<h1>{PUBLISHER}</h1>
<p class="date">Apps pequeñas, hechas con cariño. · Small apps, made with care.</p>

<h2>Ciclo</h2>
<p>Calendario de la regla con un asistente que te anima. · A period calendar with a sidekick that cheers you on.</p>
<ul>
  <li>Política de privacidad: <a href="ciclo/privacidad/">Español</a> · <a href="ciclo/privacy/">English</a> · <a href="ciclo/privacidade/">Português</a> · <a href="ciclo/privadesa/">Català</a></li>
</ul>

<h2>Contacto · Contact</h2>
<p>{MAIL}</p>
</main>
</body>
</html>
"""

if __name__ == "__main__":
    for lang, folder, _ in LANGS:
        out = ROOT / "ciclo" / folder / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page(lang, folder), encoding="utf-8")
    (ROOT / "index.html").write_text(INDEX, encoding="utf-8")
    print("ok")
