"""Builds the privacy policy pages from one template, one per language.

Run from the repository root: python tools/build.py
The contact address lives in CONTACT, so it only has to change here.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTACT = "nowkotron.industries@gmail.com"
PUBLISHER = "Nowkotron Industries"

LANGS = [
    ("es", "privacidad", "Español"),
    ("en", "privacy", "English"),
    ("pt-BR", "privacidade", "Português"),
    ("ca", "privadesa", "Català"),
    ("fr", "confidentialite", "Français"),
    ("de", "datenschutz", "Deutsch"),
    ("it", "informativa-privacy", "Italiano"),
    ("pl", "prywatnosc", "Polski"),
    ("nl", "privacybeleid", "Nederlands"),
    ("id", "privasi", "Bahasa Indonesia"),
    ("tr", "gizlilik", "Türkçe"),
    ("ja", "privacy-ja", "日本語"),
    ("ko", "privacy-ko", "한국어"),
    ("zh-Hant", "privacy-zh", "繁體中文"),
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
EN = '<a href="../privacy/" hreflang="en">'

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
  <li>La teva configuració: la durada habitual del cicle i de la regla, l’aspecte de l’assistent i quines notificacions vols rebre.</li>
  <li>El dibuix de l’assistent, si en fas un.</li>
  <li>La teva resposta d’avui a «Com estàs?». Se substitueix l’endemà i no es desa cap historial.</li>
  <li>L’últim missatge que vas escriure per a «Emet un avís», si n’escrius un.</li>
</ul>"""),
            ("On es desa", "<p>Al teu mòbil. Ciclo no té comptes ni servidors propis, no mostra anuncis i no inclou serveis de tercers ni eines d’analítica. L’app no té permís per connectar-se a internet, així que no pot enviar res enlloc.</p>"),
            ("Còpia de seguretat de Google", """<p>Si tens activada la còpia de seguretat d’Android al teu compte de Google, Android hi inclou les dades de Ciclo, perquè tornin soles si canvies a un altre mòbil amb el mateix compte de Google o reinstal·les l’app. Ciclo només permet aquesta còpia si va xifrada d’extrem a extrem amb el PIN, el patró o la contrasenya del bloqueig de pantalla: ni Google ni qui ha creat l’app la pot llegir. Si el teu mòbil no té bloqueig de pantalla, o té Android 8, les dades de Ciclo no es copien.</p>
<p>Aquesta còpia és un servei d’Android entre tu i Google: l’app no envia res pel seu compte ni en rep res. La pots desactivar a la configuració d’Android, a l’apartat de còpia de seguretat. Quan passes les dades a un mòbil nou per cable o sense fil, les de Ciclo també s’hi traslladen.</p>"""),
            ("El que surt de l’app perquè tu ho decideixes", """<p>Només surt de Ciclo el que tries compartir o desar:</p>
<ul>
  <li><strong>Emet un avís:</strong> una imatge amb una frase que envies amb l’app que triïs. Només arriba a qui tu decideixis.</li>
  <li><strong>Informe:</strong> un PDF amb les dates de les teves regles que pots compartir, desar o imprimir.</li>
  <li><strong>Còpies:</strong> un fitxer amb l’estat de l’app que deses on vulguis. Aquest fitxer no té contrasenya: desa’l en un lloc de confiança.</li>
</ul>
<p>A partir d’aquell moment, aquests fitxers queden sota el teu control i sota les condicions de l’app o el servei que facis servir per enviar-los o desar-los.</p>"""),
            ("Permisos", """<p>L’únic permís que et demana Ciclo és el de mostrar notificacions, que serveixen per avisar-te quan falta poc per a la regla o per preguntar-te si ja ha arribat o ja se n’ha anat. És opcional: el pots rebutjar o desactivar cada avís a Configuració.</p>
<p>A més, Android concedeix a l’app alguns permisos tècnics per programar aquests avisos, per exemple per tornar-los a programar quan reinicies el mòbil. Cap d’ells dona accés a internet ni a les teves dades.</p>"""),
            ("Com esborrar les teves dades", "<p>A Configuració › Les teves dades › «Esborra totes les meves dades». També s’esborra tot del mòbil en desinstal·lar l’app. La còpia de seguretat de Google es buida la propera vegada que s’actualitza després d’esborrar les dades; si desinstal·les l’app, es conserva per si la tornes a instal·lar, i la pots eliminar des de la còpia de seguretat del teu compte de Google. Les còpies que hagis desat tu en fitxers no s’esborren: les pots eliminar tu.</p>"),
            ("Menors", "<p>Ciclo no recull dades de ningú, tampoc de menors d’edat.</p>"),
            ("Salut", "<p>Les dates de Ciclo són estimacions a partir del que anotes. L’app no és un mètode anticonceptiu, no serveix per buscar un embaràs i no substitueix el consell mèdic.</p>"),
            ("Canvis en aquesta política", "<p>Si la política canvia, es publicarà aquí amb la nova data.</p>"),
            ("Contacte", f"<p>Si tens qualsevol pregunta sobre aquesta política, escriu a {MAIL}.</p>"),
        ],
    ),
    "fr": dict(
        title="Politique de confidentialité de Ciclo",
        date="Dernière mise à jour : 9 novembre 2026",
        summary="<strong>En bref :</strong> Ciclo ne collecte aucune donnée. Tout ce que tu notes est enregistré sur ton téléphone et, si la sauvegarde Google est activée, dans cette sauvegarde, chiffrée avec le verrouillage de ton écran. Personne d’autre, pas même la personne qui a créé l’appli, n’y a accès.",
        sections=[
            ("Qui publie Ciclo", f"<p>Ciclo est une appli de {PUBLISHER}. Pour toute question sur cette politique ou sur tes données, écris à {MAIL}.</p>"),
            ("Ce que l’appli enregistre", """<p>Pour fonctionner, Ciclo enregistre sur ton téléphone :</p>
<ul>
  <li>Les dates de début et de fin des règles que tu notes.</li>
  <li>Tes réglages : la durée habituelle du cycle et des règles, l’apparence de ton acolyte et les notifications que tu veux recevoir.</li>
  <li>Le dessin de ton acolyte, si tu en fais un.</li>
  <li>Ta réponse du jour à « Ça va ? ». Elle est remplacée le lendemain et aucun historique n’est conservé.</li>
  <li>Le dernier message que tu as écrit pour « Faire une annonce », si tu en écris un.</li>
</ul>"""),
            ("Où c’est enregistré", "<p>Sur ton téléphone. Ciclo n’a ni comptes ni serveurs à lui, n’affiche pas de publicité et n’intègre aucun service tiers ni outil d’analyse. L’appli n’a pas l’autorisation de se connecter à Internet : elle ne peut donc rien envoyer nulle part.</p>"),
            ("Sauvegarde Google", """<p>Si la sauvegarde Android est activée sur ton compte Google, Android y inclut les données de Ciclo, pour qu’elles reviennent toutes seules si tu passes à un autre téléphone avec le même compte Google ou si tu réinstalles l’appli. Ciclo n’autorise cette sauvegarde que si elle est chiffrée de bout en bout avec le code, le schéma ou le mot de passe de ton écran de verrouillage : ni Google ni la personne qui a créé l’appli ne peut la lire. Si ton téléphone n’a pas de verrouillage d’écran, ou s’il est sous Android 8, les données de Ciclo ne sont pas sauvegardées.</p>
<p>Cette sauvegarde est un service d’Android entre toi et Google : l’appli n’envoie rien d’elle-même et n’en reçoit rien. Tu peux la désactiver dans les paramètres d’Android, dans la rubrique sauvegarde. Quand tu transfères tes données vers un nouveau téléphone, par câble ou sans fil, celles de Ciclo sont transférées aussi.</p>"""),
            ("Ce qui sort de l’appli parce que tu le décides", """<p>Seul ce que tu choisis de partager ou d’enregistrer sort de Ciclo :</p>
<ul>
  <li><strong>Faire une annonce :</strong> une image avec une phrase que tu envoies avec l’appli de ton choix. Elle n’arrive qu’aux personnes que tu choisis.</li>
  <li><strong>Rapport :</strong> un PDF avec les dates de tes règles, que tu peux partager, enregistrer ou imprimer.</li>
  <li><strong>Sauvegardes :</strong> un fichier avec les données de l’appli, que tu enregistres où tu veux. Ce fichier n’a pas de mot de passe : garde-le dans un endroit de confiance.</li>
</ul>
<p>À partir de là, ces fichiers sont sous ton contrôle et soumis aux conditions de l’appli ou du service que tu utilises pour les envoyer ou les stocker.</p>"""),
            ("Autorisations", """<p>La seule autorisation que Ciclo te demande est celle d’afficher des notifications, qui servent à te prévenir quand tes règles approchent ou à te demander si elles ont commencé ou si elles sont finies. Elle est facultative : tu peux la refuser ou désactiver chaque rappel dans Paramètres.</p>
<p>Android accorde aussi à l’appli quelques autorisations techniques pour programmer ces rappels, par exemple pour les reprogrammer quand tu redémarres ton téléphone. Aucune ne donne accès à Internet ni à tes données.</p>"""),
            ("Comment supprimer tes données", "<p>Dans Paramètres › Tes données › « Supprimer toutes mes données ». Tout est aussi supprimé du téléphone quand tu désinstalles l’appli. La sauvegarde Google est vidée lors de sa prochaine mise à jour après la suppression de tes données ; si tu désinstalles l’appli, elle est conservée au cas où tu la réinstallerais, et tu peux la supprimer depuis la sauvegarde de ton compte Google. Les sauvegardes que tu as enregistrées toi-même dans des fichiers ne sont pas supprimées : tu peux les effacer toi-même.</p>"),
            ("Mineurs", "<p>Ciclo ne collecte de données sur personne, mineurs compris.</p>"),
            ("Santé", "<p>Les dates de Ciclo sont des estimations à partir de ce que tu notes. L’appli n’est pas une méthode de contraception, ne permet pas de planifier une grossesse et ne remplace pas un avis médical.</p>"),
            ("Modifications de cette politique", "<p>Si la politique change, la nouvelle version sera publiée ici avec sa date.</p>"),
            ("Contact", f"<p>Pour toute question sur cette politique, écris à {MAIL}.</p>"),
        ],
    ),
    "de": dict(
        title="Datenschutzerklärung von Ciclo",
        date="Zuletzt aktualisiert: 9. November 2026",
        summary="<strong>Kurz gesagt:</strong> Ciclo erhebt keine Daten. Alles, was du einträgst, wird auf deinem Handy gespeichert und, wenn die Google-Sicherung aktiviert ist, in dieser Sicherung, verschlüsselt mit deiner Displaysperre. Niemand sonst hat Zugriff darauf, auch nicht, wer die App entwickelt hat.",
        sections=[
            ("Wer Ciclo veröffentlicht", f"<p>Ciclo ist eine App von {PUBLISHER}. Bei Fragen zu dieser Datenschutzerklärung oder zu deinen Daten schreib an {MAIL}.</p>"),
            ("Was die App speichert", """<p>Damit sie funktioniert, speichert Ciclo auf deinem Handy:</p>
<ul>
  <li>Beginn und Ende der Perioden, die du einträgst.</li>
  <li>Deine Einstellungen: die übliche Länge von Zyklus und Periode, das Aussehen deines Assistenten und welche Benachrichtigungen du bekommen möchtest.</li>
  <li>Die Zeichnung deines Assistenten, falls du eine machst.</li>
  <li>Deine heutige Antwort auf „Wie geht’s?“. Sie wird am nächsten Tag ersetzt, ein Verlauf wird nicht gespeichert.</li>
  <li>Die letzte Nachricht, die du für „Durchsage machen“ geschrieben hast, falls du eine schreibst.</li>
</ul>"""),
            ("Wo die Daten gespeichert werden", "<p>Auf deinem Handy. Ciclo hat keine eigenen Konten oder Server, zeigt keine Werbung und enthält keine Dienste von Drittanbietern oder Analysetools. Die App hat keine Berechtigung, sich mit dem Internet zu verbinden, und kann deshalb nichts irgendwohin senden.</p>"),
            ("Google-Sicherung", """<p>Wenn die Android-Sicherung für dein Google-Konto aktiviert ist, nimmt Android die Daten von Ciclo darin auf, damit sie von selbst zurückkommen, wenn du auf ein anderes Handy mit demselben Google-Konto wechselst oder die App neu installierst. Ciclo lässt diese Sicherung nur zu, wenn sie mit der PIN, dem Muster oder dem Passwort deiner Displaysperre Ende-zu-Ende-verschlüsselt ist: Weder Google noch wer die App entwickelt hat, kann sie lesen. Wenn dein Handy keine Displaysperre hat oder mit Android 8 läuft, werden die Daten von Ciclo nicht gesichert.</p>
<p>Diese Sicherung ist ein Android-Dienst zwischen dir und Google: Die App sendet nichts von sich aus und empfängt nichts daraus. Du kannst sie in den Android-Einstellungen im Bereich Sicherung deaktivieren. Wenn du deine Daten per Kabel oder drahtlos auf ein neues Handy überträgst, werden auch die von Ciclo übertragen.</p>"""),
            ("Was die App verlässt, weil du es so entscheidest", """<p>Nur was du teilen oder speichern möchtest, verlässt Ciclo:</p>
<ul>
  <li><strong>Durchsage machen:</strong> ein Bild mit einem Spruch, das du mit einer App deiner Wahl verschickst. Es erreicht nur, wen du auswählst.</li>
  <li><strong>Bericht:</strong> ein PDF mit den Daten deiner Perioden, das du teilen, speichern oder drucken kannst.</li>
  <li><strong>Kopien:</strong> eine Datei mit den Daten der App, die du speicherst, wo du möchtest. Diese Datei hat kein Passwort: Bewahre sie an einem vertrauenswürdigen Ort auf.</li>
</ul>
<p>Ab dann unterliegen diese Dateien deiner Kontrolle und den Bedingungen der App oder des Dienstes, mit dem du sie verschickst oder speicherst.</p>"""),
            ("Berechtigungen", """<p>Die einzige Berechtigung, um die Ciclo dich bittet, ist die für Benachrichtigungen. Sie erinnern dich, wenn deine Periode bald kommt, oder fragen, ob sie angefangen hat oder vorbei ist. Die Berechtigung ist freiwillig: Du kannst sie ablehnen oder jede Erinnerung in den Einstellungen ausschalten.</p>
<p>Außerdem gewährt Android der App einige technische Berechtigungen, um diese Erinnerungen zu planen, zum Beispiel, um sie nach einem Neustart des Handys neu zu planen. Keine davon gibt Zugriff auf das Internet oder auf deine Daten.</p>"""),
            ("So löschst du deine Daten", "<p>Unter Einstellungen › Deine Daten › „Alle meine Daten löschen“. Wenn du die App deinstallierst, wird ebenfalls alles vom Handy gelöscht. Die Google-Sicherung wird bei ihrer nächsten Aktualisierung nach dem Löschen geleert; wenn du die App deinstallierst, bleibt sie erhalten, falls du die App wieder installierst, und du kannst sie in der Sicherung deines Google-Kontos löschen. Kopien, die du selbst in Dateien gespeichert hast, werden nicht gelöscht: Die kannst du selbst löschen.</p>"),
            ("Minderjährige", "<p>Ciclo erhebt von niemandem Daten, auch nicht von Minderjährigen.</p>"),
            ("Gesundheit", "<p>Die Termine in Ciclo sind Schätzungen anhand deiner Einträge. Die App ist kein Verhütungsmittel, eignet sich nicht zur Planung einer Schwangerschaft und ersetzt keinen ärztlichen Rat.</p>"),
            ("Änderungen dieser Datenschutzerklärung", "<p>Wenn sich die Datenschutzerklärung ändert, wird sie hier mit dem neuen Datum veröffentlicht.</p>"),
            ("Kontakt", f"<p>Bei Fragen zu dieser Datenschutzerklärung schreib an {MAIL}.</p>"),
        ],
    ),
    "it": dict(
        title="Informativa sulla privacy di Ciclo",
        date="Ultimo aggiornamento: 9 novembre 2026",
        summary="<strong>In breve:</strong> Ciclo non raccoglie alcun dato. Tutto ciò che segni viene salvato sul tuo telefono e, se il backup di Google è attivo, in quel backup, crittografato con il tuo blocco schermo. Nessun’altra persona, nemmeno chi ha creato l’app, può accedervi.",
        sections=[
            ("Chi pubblica Ciclo", f"<p>Ciclo è un’app di {PUBLISHER}. Per qualsiasi domanda su questa informativa o sui tuoi dati, scrivi a {MAIL}.</p>"),
            ("Cosa salva l’app", """<p>Per funzionare, Ciclo salva sul tuo telefono:</p>
<ul>
  <li>Le date di inizio e di fine delle mestruazioni che segni.</li>
  <li>Le tue impostazioni: la durata abituale del ciclo e delle mestruazioni, l’aspetto dell’assistente e quali notifiche vuoi ricevere.</li>
  <li>Il disegno dell’assistente, se ne fai uno.</li>
  <li>La tua risposta di oggi a «Come va?». Viene sostituita il giorno dopo e non viene conservato alcuno storico.</li>
  <li>L’ultimo messaggio che hai scritto per «Dirama un avviso», se ne scrivi uno.</li>
</ul>"""),
            ("Dove vengono salvati", "<p>Sul tuo telefono. Ciclo non ha account né server propri, non mostra pubblicità e non include servizi di terze parti né strumenti di analisi. L’app non ha l’autorizzazione a connettersi a internet, quindi non può inviare nulla da nessuna parte.</p>"),
            ("Backup di Google", """<p>Se il backup di Android è attivo sul tuo account Google, Android vi include i dati di Ciclo, così tornano da soli se passi a un altro telefono con lo stesso account Google o se reinstalli l’app. Ciclo consente questo backup solo se è protetto con crittografia end-to-end tramite il PIN, la sequenza o la password del blocco schermo: né Google né chi ha creato l’app possono leggerlo. Se il tuo telefono non ha un blocco schermo, o ha Android 8, i dati di Ciclo non vengono inclusi nel backup.</p>
<p>Questo backup è un servizio di Android tra te e Google: l’app non invia nulla di sua iniziativa e non ne riceve nulla. Puoi disattivarlo nelle impostazioni di Android, nella sezione dedicata al backup. Quando trasferisci i dati su un nuovo telefono via cavo o in modalità wireless, vengono trasferiti anche quelli di Ciclo.</p>"""),
            ("Cosa esce dall’app per tua scelta", """<p>Da Ciclo esce solo ciò che scegli di condividere o salvare:</p>
<ul>
  <li><strong>Dirama un avviso:</strong> un’immagine con una frase che invii con l’app che scegli. Arriva solo a chi decidi tu.</li>
  <li><strong>Report:</strong> un PDF con le date delle tue mestruazioni che puoi condividere, salvare o stampare.</li>
  <li><strong>Copie:</strong> un file con i dati dell’app che salvi dove preferisci. Questo file non ha password: conservalo in un posto di cui ti fidi.</li>
</ul>
<p>Da quel momento, questi file sono sotto il tuo controllo e soggetti alle condizioni dell’app o del servizio che usi per inviarli o conservarli.</p>"""),
            ("Autorizzazioni", """<p>L’unica autorizzazione che Ciclo ti chiede è quella di mostrare notifiche, che servono ad avvisarti quando manca poco alle mestruazioni o a chiederti se sono iniziate o finite. È facoltativa: puoi rifiutarla o disattivare i singoli promemoria nelle Impostazioni.</p>
<p>Inoltre, Android concede all’app alcune autorizzazioni tecniche per programmare questi promemoria, per esempio per programmarli di nuovo quando riavvii il telefono. Nessuna di queste dà accesso a internet o ai tuoi dati.</p>"""),
            ("Come eliminare i tuoi dati", "<p>Vai in Impostazioni › I tuoi dati › «Elimina tutti i miei dati». Anche disinstallando l’app si elimina tutto dal telefono. Il backup di Google viene svuotato al primo aggiornamento successivo all’eliminazione dei dati; se disinstalli l’app, viene conservato nel caso tu la reinstalli, e puoi eliminarlo dal backup del tuo account Google. Le copie che hai salvato tu in un file non vengono eliminate: puoi eliminarle tu.</p>"),
            ("Minori", "<p>Ciclo non raccoglie dati di nessuno, minori compresi.</p>"),
            ("Salute", "<p>Le date di Ciclo sono stime basate su ciò che segni. L’app non è un metodo contraccettivo, non serve per pianificare una gravidanza e non sostituisce il parere medico.</p>"),
            ("Modifiche a questa informativa", "<p>Se l’informativa cambia, sarà pubblicata qui con la nuova data.</p>"),
            ("Contatti", f"<p>Per qualsiasi domanda su questa informativa, scrivi a {MAIL}.</p>"),
        ],
    ),
    "pl": dict(
        title="Polityka prywatności aplikacji Ciclo",
        date="Ostatnia aktualizacja: 9 listopada 2026 r.",
        summary="<strong>W skrócie:</strong> Ciclo nie zbiera żadnych danych. Wszystko, co zapisujesz, jest przechowywane na twoim telefonie oraz – jeśli masz włączoną kopię zapasową Google – w tej kopii, zaszyfrowanej przy użyciu blokady ekranu. Nikt inny, nawet osoba, która stworzyła aplikację, nie ma do tego dostępu.",
        sections=[
            ("Kto wydaje Ciclo", f"<p>Ciclo to aplikacja wydawana przez {PUBLISHER}. Jeśli masz pytania dotyczące tej polityki lub swoich danych, napisz na adres {MAIL}.</p>"),
            ("Co przechowuje aplikacja", """<p>Aby działać, Ciclo przechowuje na twoim telefonie:</p>
<ul>
  <li>Daty początku i końca okresów, które zapisujesz.</li>
  <li>Twoje ustawienia: zwykłą długość cyklu i okresu, wygląd asystenta oraz to, jakie powiadomienia chcesz otrzymywać.</li>
  <li>Rysunek asystenta, jeśli go stworzysz.</li>
  <li>Dzisiejszą odpowiedź na „Jak tam?”. Następnego dnia zostaje zastąpiona, a historia nie jest przechowywana.</li>
  <li>Ostatnią wiadomość napisaną przez ciebie w „Wydaj komunikat”, jeśli taką napiszesz.</li>
</ul>"""),
            ("Gdzie są przechowywane dane", "<p>Na twoim telefonie. Ciclo nie ma własnych kont ani serwerów, nie wyświetla reklam i nie zawiera usług podmiotów trzecich ani narzędzi analitycznych. Aplikacja nie ma uprawnienia do łączenia się z internetem, więc nie może nigdzie niczego wysłać.</p>"),
            ("Kopia zapasowa Google", """<p>Jeśli na twoim koncie Google jest włączona kopia zapasowa Androida, Android umieszcza w niej dane Ciclo, aby same wróciły, gdy przeniesiesz się na inny telefon z tym samym kontem Google lub ponownie zainstalujesz aplikację. Ciclo pozwala na tę kopię tylko wtedy, gdy jest ona objęta szyfrowaniem end-to-end przy użyciu kodu PIN, wzoru lub hasła blokady ekranu: ani Google, ani osoba, która stworzyła aplikację, nie mogą jej odczytać. Jeśli twój telefon nie ma blokady ekranu albo działa na Androidzie 8, dane Ciclo nie są uwzględniane w kopii zapasowej.</p>
<p>Ta kopia zapasowa to usługa Androida między tobą a Google: aplikacja sama niczego nie wysyła i niczego z niej nie otrzymuje. Możesz ją wyłączyć w ustawieniach Androida, w części dotyczącej kopii zapasowej. Gdy przenosisz dane na nowy telefon za pomocą kabla lub bezprzewodowo, dane Ciclo również zostają przeniesione.</p>"""),
            ("Co opuszcza aplikację, gdy tak zdecydujesz", """<p>Z Ciclo wychodzi tylko to, co zdecydujesz się udostępnić lub zapisać:</p>
<ul>
  <li><strong>Wydaj komunikat:</strong> obraz z napisem, który wysyłasz za pomocą wybranej przez siebie aplikacji. Trafia tylko do osób, które wybierzesz.</li>
  <li><strong>Raport:</strong> plik PDF z datami twoich okresów, który możesz udostępnić, zapisać lub wydrukować.</li>
  <li><strong>Kopie:</strong> plik z danymi aplikacji, który zapisujesz w wybranym przez siebie miejscu. Ten plik nie jest chroniony hasłem: przechowuj go w zaufanym miejscu.</li>
</ul>
<p>Od tej chwili pliki te pozostają pod twoją kontrolą i podlegają warunkom aplikacji lub usługi, za pomocą której je wysyłasz lub przechowujesz.</p>"""),
            ("Uprawnienia", """<p>Jedyne uprawnienie, o które prosi Ciclo, to wyświetlanie powiadomień. Powiadomienia informują, że okres się zbliża, lub pytają, czy już się zaczął albo skończył. To uprawnienie jest opcjonalne: możesz odmówić jego przyznania albo wyłączyć poszczególne przypomnienia w Ustawieniach.</p>
<p>Android przyznaje też aplikacji kilka uprawnień technicznych potrzebnych do planowania tych przypomnień, na przykład aby zaplanować je na nowo po ponownym uruchomieniu telefonu. Żadne z nich nie daje dostępu do internetu ani do twoich danych.</p>"""),
            ("Jak usunąć swoje dane", "<p>Wybierz Ustawienia › Twoje dane › „Usuń wszystkie moje dane”. Odinstalowanie aplikacji również usuwa wszystko z telefonu. Kopia zapasowa Google zostaje opróżniona przy jej najbliższej aktualizacji po usunięciu danych; jeśli odinstalujesz aplikację, kopia zostaje zachowana na wypadek ponownej instalacji i możesz ją usunąć z kopii zapasowej swojego konta Google. Kopie zapisane przez ciebie w plikach nie są usuwane: możesz je usunąć samodzielnie.</p>"),
            ("Osoby niepełnoletnie", "<p>Ciclo nie zbiera danych od nikogo, także od osób niepełnoletnich.</p>"),
            ("Zdrowie", "<p>Daty w Ciclo to szacunki oparte na tym, co zapisujesz. Aplikacja nie jest metodą antykoncepcji, nie służy do planowania ciąży i nie zastępuje porady lekarskiej.</p>"),
            ("Zmiany w tej polityce", "<p>Jeśli polityka się zmieni, zostanie opublikowana tutaj z nową datą.</p>"),
            ("Kontakt", f"<p>Jeśli masz jakiekolwiek pytania dotyczące tej polityki, napisz na adres {MAIL}.</p>"),
        ],
    ),
    "nl": dict(
        title="Privacybeleid van Ciclo",
        date="Laatst bijgewerkt: 9 november 2026",
        summary="<strong>In het kort:</strong> Ciclo verzamelt geen gegevens. Alles wat je noteert, wordt bewaard op je telefoon en, als de back-up van Google aanstaat, in die back-up, versleuteld met je schermvergrendeling. Niemand anders heeft er toegang toe, ook de maker van de app niet.",
        sections=[
            ("Wie Ciclo uitbrengt", f"<p>Ciclo is een app van {PUBLISHER}. Heb je een vraag over dit privacybeleid of over je gegevens? Stuur dan een e-mail naar {MAIL}.</p>"),
            ("Wat de app bewaart", """<p>Om te kunnen werken, bewaart Ciclo op je telefoon:</p>
<ul>
  <li>De begin- en einddatums van de menstruaties die je noteert.</li>
  <li>Je instellingen: de gebruikelijke lengte van je cyclus en je menstruatie, het uiterlijk van je assistent en welke meldingen je wilt krijgen.</li>
  <li>De tekening van je assistent, als je er een maakt.</li>
  <li>Je antwoord van vandaag op ‘Hoe gaat het?’. Dat wordt de volgende dag vervangen en er wordt geen geschiedenis bijgehouden.</li>
  <li>Het laatste bericht dat je voor ‘Mededeling doen’ hebt geschreven, als je er een schrijft.</li>
</ul>"""),
            ("Waar het wordt bewaard", "<p>Op je telefoon. Ciclo heeft geen eigen accounts of servers, toont geen advertenties en bevat geen diensten van derden of analysetools. De app heeft geen toestemming om verbinding te maken met internet, en kan dus nergens iets naartoe sturen.</p>"),
            ("Back-up van Google", """<p>Staat de Android-back-up aan voor je Google-account, dan neemt Android de gegevens van Ciclo daarin op, zodat ze vanzelf terugkomen als je overstapt op een andere telefoon met hetzelfde Google-account of de app opnieuw installeert. Ciclo staat deze back-up alleen toe als die end-to-end versleuteld is met de pincode, het patroon of het wachtwoord van je schermvergrendeling: Google kan de back-up niet lezen, en de maker van de app ook niet. Heeft je telefoon geen schermvergrendeling, of draait hij op Android 8, dan wordt er geen back-up gemaakt van de gegevens van Ciclo.</p>
<p>Deze back-up is een dienst van Android tussen jou en Google: de app verstuurt zelf niets en ontvangt er ook niets van. Je kunt de back-up uitzetten in de instellingen van Android, bij het onderdeel voor back-ups. Zet je je gegevens via een kabel of draadloos over naar een nieuwe telefoon, dan gaan de gegevens van Ciclo ook mee.</p>"""),
            ("Wat de app verlaat omdat jij daarvoor kiest", """<p>Alleen wat jij besluit te delen of op te slaan, verlaat Ciclo:</p>
<ul>
  <li><strong>Mededeling doen:</strong> een afbeelding met een zin, die je verstuurt met de app die je kiest. Die komt alleen terecht bij wie jij kiest.</li>
  <li><strong>Rapport:</strong> een pdf met de datums van je menstruaties, die je kunt delen, opslaan of afdrukken.</li>
  <li><strong>Back-ups:</strong> een bestand met de gegevens van de app, dat je opslaat waar je maar wilt. Dit bestand heeft geen wachtwoord: bewaar het op een plek die je vertrouwt.</li>
</ul>
<p>Vanaf dat moment vallen die bestanden onder jouw beheer en onder de voorwaarden van de app of dienst waarmee je ze verstuurt of opslaat.</p>"""),
            ("App-rechten", """<p>Het enige recht waar Ciclo je om vraagt, is het recht om meldingen te tonen. Die laten je weten wanneer je menstruatie bijna begint, of vragen of je menstruatie al begonnen of voorbij is. Dit recht is optioneel: je kunt het weigeren of elke herinnering afzonderlijk uitzetten in Instellingen.</p>
<p>Daarnaast geeft Android de app een paar technische rechten om die herinneringen in te plannen, bijvoorbeeld om ze opnieuw in te plannen nadat je telefoon opnieuw is opgestart. Geen van deze rechten geeft toegang tot internet of tot je gegevens.</p>"""),
            ("Je gegevens verwijderen", "<p>Ga naar Instellingen › Je gegevens › ‘Al mijn gegevens verwijderen’. Als je de app verwijdert, wordt ook alles van de telefoon gewist. De back-up van Google wordt geleegd zodra die na het verwijderen van je gegevens opnieuw wordt bijgewerkt; als je de app verwijdert, blijft de back-up bewaard voor het geval je de app opnieuw installeert, en kun je die verwijderen uit de back-up van je Google-account. Back-upbestanden die je zelf hebt opgeslagen, worden niet verwijderd: die kun je zelf verwijderen.</p>"),
            ("Minderjarigen", "<p>Ciclo verzamelt van niemand gegevens, ook niet van minderjarigen.</p>"),
            ("Gezondheid", "<p>De datums in Ciclo zijn schattingen op basis van wat je noteert. De app is geen anticonceptiemethode, is niet geschikt om een zwangerschap te plannen en vervangt geen medisch advies.</p>"),
            ("Wijzigingen in dit privacybeleid", "<p>Als het privacybeleid verandert, wordt het hier gepubliceerd met de nieuwe datum.</p>"),
            ("Contact", f"<p>Heb je een vraag over dit privacybeleid? Stuur dan een e-mail naar {MAIL}.</p>"),
        ],
    ),
    "id": dict(
        title="Kebijakan Privasi Ciclo",
        date="Terakhir diperbarui: 9 November 2026",
        summary="<strong>Ringkasnya:</strong> Ciclo tidak mengumpulkan data apa pun. Semua yang Anda catat disimpan di ponsel Anda dan, jika cadangan Google aktif, di cadangan tersebut, terenkripsi dengan kunci layar Anda. Tidak ada orang lain, termasuk pembuat aplikasi ini, yang dapat mengaksesnya.",
        sections=[
            ("Siapa yang menerbitkan Ciclo", f"<p>Ciclo adalah aplikasi dari {PUBLISHER}. Untuk pertanyaan apa pun tentang kebijakan ini atau tentang data Anda, kirimkan email ke {MAIL}.</p>"),
            ("Apa yang disimpan aplikasi", """<p>Agar dapat berfungsi, Ciclo menyimpan hal-hal berikut di ponsel Anda:</p>
<ul>
  <li>Tanggal mulai dan selesai haid yang Anda catat.</li>
  <li>Setelan Anda: panjang siklus dan lama haid biasanya, tampilan asisten, dan notifikasi yang ingin Anda terima.</li>
  <li>Gambar asisten, jika Anda membuatnya.</li>
  <li>Jawaban Anda hari ini untuk “Apa kabar?”. Jawaban ini diganti keesokan harinya dan tidak ada riwayat yang disimpan.</li>
  <li>Pesan terakhir yang Anda tulis untuk “Buat pengumuman”, jika Anda menulisnya.</li>
</ul>"""),
            ("Di mana data disimpan", "<p>Di ponsel Anda. Ciclo tidak memiliki akun maupun server sendiri, tidak menampilkan iklan, dan tidak menyertakan layanan pihak ketiga ataupun alat analitik. Aplikasi ini tidak memiliki izin untuk terhubung ke internet, sehingga tidak dapat mengirim apa pun ke mana pun.</p>"),
            ("Cadangan Google", """<p>Jika cadangan Android aktif di akun Google Anda, Android menyertakan data Ciclo di dalamnya, sehingga data tersebut kembali dengan sendirinya jika Anda pindah ke ponsel lain dengan akun Google yang sama atau menginstal ulang aplikasi. Ciclo hanya mengizinkan pencadangan ini jika cadangan tersebut dienkripsi secara end-to-end dengan PIN, pola, atau kata sandi kunci layar Anda: baik Google maupun pembuat aplikasi ini tidak dapat membacanya. Jika ponsel Anda tidak memiliki kunci layar, atau menggunakan Android 8, data Ciclo tidak dicadangkan.</p>
<p>Cadangan ini adalah layanan Android antara Anda dan Google: aplikasi ini tidak mengirim apa pun atas inisiatifnya sendiri dan tidak menerima apa pun dari cadangan tersebut. Anda dapat menonaktifkannya di setelan Android, di bagian pencadangan. Saat Anda memindahkan data ke ponsel baru melalui kabel atau secara nirkabel, data Ciclo juga ikut dipindahkan.</p>"""),
            ("Yang meninggalkan aplikasi atas keputusan Anda", """<p>Hanya yang Anda pilih untuk dibagikan atau disimpan yang meninggalkan Ciclo:</p>
<ul>
  <li><strong>Buat pengumuman:</strong> gambar berisi sebuah kalimat yang Anda kirim melalui aplikasi pilihan Anda. Gambar ini hanya sampai kepada orang yang Anda tentukan.</li>
  <li><strong>Laporan:</strong> PDF berisi tanggal-tanggal haid Anda yang dapat Anda bagikan, simpan, atau cetak.</li>
  <li><strong>Salinan:</strong> file berisi data aplikasi yang Anda simpan di tempat pilihan Anda. File ini tidak memiliki kata sandi: simpanlah di tempat yang Anda percayai.</li>
</ul>
<p>Sejak saat itu, file tersebut berada di bawah kendali Anda dan tunduk pada ketentuan aplikasi atau layanan yang Anda gunakan untuk mengirim atau menyimpannya.</p>"""),
            ("Izin", """<p>Satu-satunya izin yang diminta Ciclo adalah izin untuk menampilkan notifikasi, yang berfungsi untuk memberi tahu Anda saat haid sudah dekat atau untuk menanyakan apakah haid sudah datang atau sudah selesai. Izin ini opsional: Anda dapat menolaknya atau menonaktifkan setiap pengingat di Setelan.</p>
<p>Selain itu, Android memberikan beberapa izin teknis kepada aplikasi untuk menjadwalkan pengingat tersebut, misalnya untuk menjadwalkannya kembali setelah Anda memulai ulang ponsel. Tidak satu pun dari izin tersebut memberikan akses ke internet atau ke data Anda.</p>"""),
            ("Cara menghapus data Anda", "<p>Buka Setelan › Datamu › “Hapus semua dataku”. Jika aplikasi di-uninstal, semua data di ponsel juga akan terhapus. Cadangan Google dikosongkan saat diperbarui berikutnya setelah Anda menghapus data; jika Anda meng-uninstal aplikasi, cadangan tersebut tetap disimpan untuk berjaga-jaga jika Anda menginstalnya lagi, dan Anda dapat menghapusnya dari cadangan akun Google Anda. Salinan yang Anda simpan sendiri dalam bentuk file tidak ikut terhapus: Anda dapat menghapusnya sendiri.</p>"),
            ("Anak-anak", "<p>Ciclo tidak mengumpulkan data siapa pun, termasuk anak-anak.</p>"),
            ("Kesehatan", "<p>Tanggal-tanggal di Ciclo adalah perkiraan berdasarkan apa yang Anda catat. Aplikasi ini bukan metode kontrasepsi, tidak dapat dipakai untuk program hamil, dan tidak menggantikan saran medis.</p>"),
            ("Perubahan kebijakan ini", "<p>Jika kebijakan ini berubah, versi barunya akan dipublikasikan di sini beserta tanggal barunya.</p>"),
            ("Kontak", f"<p>Jika Anda memiliki pertanyaan apa pun tentang kebijakan ini, kirimkan email ke {MAIL}.</p>"),
        ],
    ),
    "tr": dict(
        title="Ciclo Gizlilik Politikası",
        date="Son güncelleme: 9 Kasım 2026",
        summary="<strong>Kısaca:</strong> Ciclo hiçbir veri toplamaz. Kaydettiğin her şey telefonunda saklanır; Google yedeklemesi açıksa ekran kilidinle şifrelenmiş olarak o yedekte de saklanır. Uygulamayı geliştiren kişi de dâhil olmak üzere başka hiç kimse bu verilere erişemez.",
        sections=[
            ("Ciclo’yu kim yayımlıyor", f"<p>Ciclo, {PUBLISHER} tarafından yayımlanan bir uygulamadır. Bu politika veya verilerin hakkında her türlü soru için {MAIL} adresine yaz.</p>"),
            ("Uygulamanın sakladığı bilgiler", """<p>Ciclo, çalışabilmek için telefonunda şunları saklar:</p>
<ul>
  <li>Kaydettiğin reglerin başlangıç ve bitiş tarihleri.</li>
  <li>Ayarların: olağan döngü ve regl süresi, asistanının görünüşü ve hangi bildirimleri almak istediğin.</li>
  <li>Asistanını çizdiysen bu çizim.</li>
  <li>“Nasılsın?” sorusuna bugün verdiğin yanıt. Bu yanıt ertesi gün yenisiyle değiştirilir ve geçmiş tutulmaz.</li>
  <li>“Duyuru yap” için bir mesaj yazdıysan, yazdığın son mesaj.</li>
</ul>"""),
            ("Bilgilerin saklandığı yer", "<p>Telefonun. Ciclo’nun kendine ait hesapları veya sunucuları yoktur; Ciclo reklam göstermez, üçüncü taraf hizmetleri veya analiz araçları içermez. Uygulamanın internete bağlanma izni yoktur; bu nedenle hiçbir yere hiçbir şey gönderemez.</p>"),
            ("Google yedeklemesi", """<p>Google hesabında Android yedeklemesi açıksa Android, Ciclo’nun verilerini bu yedeğe dâhil eder; böylece aynı Google hesabıyla başka bir telefona geçtiğinde veya uygulamayı yeniden yüklediğinde veriler kendiliğinden geri gelir. Ciclo bu yedeklemeye yalnızca yedek, ekran kilidinin PIN’i, deseni veya şifresi kullanılarak uçtan uca şifrelenmişse izin verir: ne Google ne de uygulamayı geliştiren kişi bu yedeği okuyabilir. Telefonunda ekran kilidi yoksa veya telefonun Android 8 kullanıyorsa Ciclo’nun verileri yedeklenmez.</p>
<p>Bu yedekleme, seninle Google arasındaki bir Android hizmetidir: uygulama kendi başına hiçbir şey göndermez ve bu yedeklemeden hiçbir şey almaz. Yedeklemeyi Android ayarlarındaki yedekleme bölümünden kapatabilirsin. Verilerini kabloyla veya kablosuz olarak yeni bir telefona aktardığında Ciclo’nun verileri de aktarılır.</p>"""),
            ("Senin kararınla uygulamadan çıkanlar", """<p>Ciclo’dan yalnızca paylaşmayı veya kaydetmeyi seçtiğin şeyler çıkar:</p>
<ul>
  <li><strong>Duyuru yap:</strong> bir cümle içeren ve seçtiğin uygulamayla gönderdiğin bir görsel. Yalnızca senin belirlediğin kişilere ulaşır.</li>
  <li><strong>Rapor:</strong> regl tarihlerini içeren ve paylaşabileceğin, kaydedebileceğin veya yazdırabileceğin bir PDF.</li>
  <li><strong>Yedekler:</strong> uygulamanın verilerini içeren ve istediğin yere kaydettiğin bir dosya. Bu dosyanın parolası yoktur: güvendiğin bir yerde sakla.</li>
</ul>
<p>O andan itibaren bu dosyalar senin kontrolündedir ve onları göndermek veya saklamak için kullandığın uygulamanın ya da hizmetin koşullarına tabidir.</p>"""),
            ("İzinler", """<p>Ciclo’nun senden istediği tek izin bildirim gösterme iznidir. Bildirimler, reglin yaklaştığında seni uyarmak veya reglinin gelip gelmediğini ya da bitip bitmediğini sormak için kullanılır. Bu izin isteğe bağlıdır: izni reddedebilir veya her hatırlatıcıyı Ayarlar’dan ayrı ayrı kapatabilirsin.</p>
<p>Android ayrıca bu hatırlatıcıları planlamak için uygulamaya bazı teknik izinler verir; örneğin telefonunu yeniden başlattığında hatırlatıcıları yeniden planlamak için. Bu izinlerin hiçbiri internete veya verilerine erişim sağlamaz.</p>"""),
            ("Verilerini silme", "<p>Ayarlar › Verilerin › “Tüm verilerimi sil” adımlarını izle. Uygulamayı sildiğinde de telefondaki her şey silinir. Google yedeği, verilerini sildikten sonraki ilk güncellenişinde temizlenir; uygulamayı silersen Google yedeği, uygulamayı yeniden yükleme ihtimaline karşı saklanır ve onu Google hesabının yedeğinden silebilirsin. Kendi kaydettiğin yedek dosyaları silinmez: bunları kendin silebilirsin.</p>"),
            ("Çocuklar", "<p>Ciclo, çocuklar da dâhil olmak üzere hiç kimseden veri toplamaz.</p>"),
            ("Sağlık", "<p>Ciclo’daki tarihler, kaydettiklerine dayanan tahminlerdir. Uygulama bir doğum kontrol yöntemi değildir, gebe kalmayı planlamak için kullanılamaz ve tıbbi tavsiyenin yerini tutmaz.</p>"),
            ("Bu politikadaki değişiklikler", "<p>Politika değişirse yeni hâli, yeni tarihiyle birlikte burada yayımlanır.</p>"),
            ("İletişim", f"<p>Bu politikayla ilgili herhangi bir soru için {MAIL} adresine yaz.</p>"),
        ],
    ),
    "ja": dict(
        title="Cicloプライバシーポリシー",
        date="最終更新日：2026年11月9日",
        summary="<strong>概要：</strong>Cicloはデータを一切収集しません。記録した内容はすべてお使いのスマートフォンに保存されます。Googleバックアップをオンにしている場合は、画面ロックで暗号化されたうえで、そのバックアップにも保存されます。アプリの開発者を含め、ほかの誰もそのデータにアクセスすることはできません。",
        sections=[
            ("Cicloの提供者", f"<p>Cicloは{PUBLISHER}が提供するアプリです。本ポリシーやご自身のデータについてご質問がある場合は、{MAIL}までご連絡ください。</p>"),
            ("アプリが保存する情報", """<p>Cicloは、動作するために次の情報をお使いのスマートフォンに保存します。</p>
<ul>
  <li>記録した生理の開始日と終了日。</li>
  <li>設定：いつもの周期と生理期間の日数、アシスタントの見た目、受け取りたい通知の種類。</li>
  <li>アシスタントの絵（描いた場合）。</li>
  <li>その日の「調子はどう？」への回答。翌日には置き換えられ、履歴は残りません。</li>
  <li>「お知らせを出す」用に最後に書いたメッセージ（書いた場合）。</li>
</ul>"""),
            ("保存場所", "<p>お使いのスマートフォンの中です。Cicloには独自のアカウントやサーバーはなく、広告も表示せず、第三者のサービスや分析ツールも組み込んでいません。アプリにはインターネットに接続する権限がないため、どこにも何も送信することはできません。</p>"),
            ("Googleバックアップ", """<p>GoogleアカウントでAndroidのバックアップをオンにしている場合、AndroidはCicloのデータもバックアップに含めます。そのため、同じGoogleアカウントで別のスマートフォンに切り替えたときや、アプリを再インストールしたときに、データが自動で戻ります。Cicloがこのバックアップを許可するのは、画面ロックのPIN、パターン、またはパスワードを使ってエンドツーエンドで暗号化される場合に限られます。そのため、Googleもアプリの開発者も、このバックアップを読むことはできません。お使いのスマートフォンに画面ロックが設定されていない場合や、Android 8で動作している場合は、Cicloのデータはバックアップされません。</p>
<p>このバックアップは、あなたとGoogleとの間のAndroidのサービスです。アプリが独自に何かを送信したり、バックアップから何かを受け取ったりすることはありません。バックアップは、Androidの設定にあるバックアップの項目でオフにできます。ケーブルまたはワイヤレスで新しいスマートフォンにデータを移行すると、Cicloのデータも移行されます。</p>"""),
            ("ご自身の判断でアプリの外に出るもの", """<p>Cicloの外に出るのは、ご自身で共有または保存することを選んだものだけです。</p>
<ul>
  <li><strong>お知らせを出す：</strong>ひとことを添えた画像で、選んだアプリを使って送信します。届くのは、ご自身が決めた相手だけです。</li>
  <li><strong>レポート：</strong>生理の日付をまとめたPDFで、共有、保存、印刷ができます。</li>
  <li><strong>バックアップファイル：</strong>アプリのデータを収めたファイルで、好きな場所に保存できます。このファイルにはパスワードがかかっていないため、信頼できる場所に保管してください。</li>
</ul>
<p>その時点から、これらのファイルはご自身の管理下に置かれ、送信や保存に使うアプリやサービスの規約に従うことになります。</p>"""),
            ("権限", """<p>Cicloが求める権限は、通知を表示する権限だけです。通知は、生理が近づいたことをお知らせしたり、生理が来たかどうか、終わったかどうかを確認したりするために使います。この権限は任意です。許可しないことも、設定でリマインダーを個別にオフにすることもできます。</p>
<p>また、Androidはこれらのリマインダーを設定するために、いくつかの技術的な権限をアプリに付与します。たとえば、スマートフォンを再起動したときにリマインダーを設定し直すための権限です。いずれの権限も、インターネットやあなたのデータへのアクセスを可能にするものではありません。</p>"""),
            ("データの削除方法", "<p>設定 › あなたのデータ › 「すべてのデータを削除」から削除できます。アプリをアンインストールした場合も、スマートフォンからすべて削除されます。Googleバックアップは、データを削除したあとの次回の更新時に空になります。アプリをアンインストールした場合、Googleバックアップは再インストールに備えて保持されます。このバックアップは、Googleアカウントのバックアップから削除できます。ご自身で保存したバックアップファイルは削除されません。これらはご自身で削除できます。</p>"),
            ("未成年者", "<p>Cicloは誰のデータも収集しません。未成年者のデータも同様です。</p>"),
            ("健康について", "<p>Cicloの日付は、記録した内容をもとにした推定です。このアプリは避妊法ではなく、妊娠を望む場合にも使えません。また、医療上の助言に代わるものではありません。</p>"),
            ("本ポリシーの変更", "<p>本ポリシーが変更された場合は、新しい日付とともにこのページで公開されます。</p>"),
            ("お問い合わせ", f"<p>本ポリシーについてご質問がある場合は、{MAIL}までご連絡ください。</p>"),
        ],
    ),
    "ko": dict(
        title="Ciclo 개인정보 처리방침",
        date="최종 수정일: 2026년 11월 9일",
        summary="<strong>요약:</strong> Ciclo는 어떤 데이터도 수집하지 않습니다. 기록한 내용은 모두 휴대전화에 저장되며, Google 백업을 켜 두었다면 화면 잠금으로 암호화되어 백업에도 저장됩니다. 앱을 만든 사람을 포함해 다른 누구도 이 데이터에 접근할 수 없습니다.",
        sections=[
            ("Ciclo 제공자", f"<p>Ciclo는 {PUBLISHER}에서 제공하는 앱입니다. 이 개인정보 처리방침이나 데이터에 관해 궁금한 점이 있으면 이메일({MAIL})로 문의해 주시기 바랍니다.</p>"),
            ("앱에 저장되는 정보", """<p>Ciclo는 작동하는 데 필요한 다음 정보를 휴대전화에 저장합니다.</p>
<ul>
  <li>기록한 생리의 시작일과 종료일</li>
  <li>설정: 평소 주기 길이와 생리 기간, 짝꿍의 모습, 받고 싶은 알림</li>
  <li>짝꿍 그림(직접 그린 경우)</li>
  <li>그날 ‘오늘 어때요?’에 한 답변. 다음 날이 되면 새 답변으로 바뀌며, 이력은 저장되지 않습니다.</li>
  <li>‘안내 방송하기’에 마지막으로 쓴 메시지(쓴 경우)</li>
</ul>"""),
            ("저장 위치", "<p>데이터는 휴대전화에 저장됩니다. Ciclo에는 자체 계정이나 서버가 없고, 광고를 표시하지 않으며, 제3자 서비스나 분석 도구도 포함되어 있지 않습니다. 앱에는 인터넷 연결 권한이 없으므로 어디로도 아무것도 보낼 수 없습니다.</p>"),
            ("Google 백업", """<p>Google 계정에서 Android 백업을 켜 두었다면 Android가 Ciclo의 데이터를 백업에 포함하므로, 같은 Google 계정으로 다른 휴대전화로 바꾸거나 앱을 다시 설치하면 데이터가 자동으로 돌아옵니다. Ciclo는 이 백업이 화면 잠금 PIN, 패턴 또는 비밀번호로 엔드 투 엔드 암호화되는 경우에만 백업을 허용합니다. 따라서 Google도 앱을 만든 사람도 백업을 읽을 수 없습니다. 휴대전화에 화면 잠금이 설정되어 있지 않거나 Android 8을 사용하는 경우에는 Ciclo의 데이터가 백업되지 않습니다.</p>
<p>이 백업은 이용자와 Google 사이의 Android 서비스로, 앱이 자체적으로 무언가를 보내거나 백업에서 무언가를 받는 일은 없습니다. 백업은 Android 설정의 백업 항목에서 끌 수 있습니다. 케이블이나 무선으로 데이터를 새 휴대전화로 옮기면 Ciclo의 데이터도 함께 옮겨집니다.</p>"""),
            ("직접 결정해 앱 밖으로 내보내는 정보", """<p>Ciclo 밖으로 나가는 것은 직접 공유하거나 저장하기로 선택한 것뿐입니다.</p>
<ul>
  <li><strong>안내 방송하기:</strong> 문구가 담긴 이미지로, 직접 고른 앱으로 보냅니다. 직접 정한 상대에게만 전달됩니다.</li>
  <li><strong>보고서:</strong> 생리 날짜가 담긴 PDF로, 공유하거나 저장하거나 인쇄할 수 있습니다.</li>
  <li><strong>백업 파일:</strong> 앱의 데이터가 담긴 파일로, 원하는 곳에 저장합니다. 이 파일에는 비밀번호가 없으므로 신뢰할 수 있는 곳에 보관하시기 바랍니다.</li>
</ul>
<p>그 이후로 이 파일은 직접 관리하게 되며, 파일을 보내거나 보관하는 데 사용하는 앱이나 서비스의 약관이 적용됩니다.</p>"""),
            ("권한", """<p>Ciclo가 요청하는 권한은 알림 표시 권한 하나뿐입니다. 알림은 생리가 얼마 남지 않았을 때 알려 주거나, 생리가 시작되었는지 또는 끝났는지 물어보는 데 사용됩니다. 이 권한은 선택 사항으로, 허용하지 않을 수도 있고 설정에서 각 리마인더를 끌 수도 있습니다.</p>
<p>또한 Android는 이러한 리마인더를 예약하기 위해 앱에 몇 가지 기술적 권한을 부여합니다. 예를 들어 휴대전화를 다시 시작한 후 리마인더를 다시 예약하기 위한 권한입니다. 이 중 어떤 권한도 인터넷이나 데이터에 접근할 수 있게 하지 않습니다.</p>"""),
            ("데이터 삭제 방법", "<p>설정 › 내 데이터 › ‘내 데이터 모두 삭제’에서 삭제할 수 있습니다. 앱을 삭제해도 휴대전화에 있는 데이터가 모두 지워집니다. Google 백업은 데이터를 삭제한 후 다음에 업데이트될 때 비워집니다. 앱을 삭제한 경우에는 앱을 다시 설치할 때에 대비해 Google 백업이 보관되며, 이 백업은 Google 계정의 백업에서 삭제할 수 있습니다. 직접 저장한 백업 파일은 삭제되지 않습니다. 이 파일은 직접 삭제할 수 있습니다.</p>"),
            ("미성년자", "<p>Ciclo는 미성년자를 포함해 누구의 데이터도 수집하지 않습니다.</p>"),
            ("건강", "<p>Ciclo의 날짜는 기록한 내용을 바탕으로 한 추정치입니다. 이 앱은 피임법이 아니며, 임신을 시도하는 용도로 쓸 수 없고, 의학적 조언을 대신하지 않습니다.</p>"),
            ("개인정보 처리방침의 변경", "<p>이 개인정보 처리방침이 변경되면 새 날짜와 함께 이곳에 게시됩니다.</p>"),
            ("문의", f"<p>이 개인정보 처리방침에 관해 궁금한 점이 있으면 이메일({MAIL})로 문의해 주시기 바랍니다.</p>"),
        ],
    ),
    "zh-Hant": dict(
        title="Ciclo隱私權政策",
        date="最後更新日期：2026年11月9日",
        summary="<strong>重點摘要：</strong>Ciclo不會蒐集任何資料。你記錄的所有內容都儲存在你的手機上；如果你開啟了Google備份，也會儲存在備份中，並以你的螢幕鎖定加密。其他任何人，包括應用程式的開發者，都無法存取這些資料。",
        sections=[
            ("Ciclo的發布者", f"<p>Ciclo是由{PUBLISHER}發布的應用程式。如果對本政策或你的資料有任何疑問，請寄信至{MAIL}。</p>"),
            ("應用程式儲存的內容", """<p>為了正常運作，Ciclo會在你的手機上儲存：</p>
<ul>
  <li>你記錄的生理期開始日期和結束日期。</li>
  <li>你的設定：平常的週期長度和生理期長度、小幫手的造型，以及你想收到哪些通知。</li>
  <li>小幫手的畫作（如果你有畫）。</li>
  <li>你今天對「今天還好嗎？」的回答。這個回答隔天就會被取代，不會保留任何歷史記錄。</li>
  <li>你最後一次為「發布公告」寫的訊息（如果你有寫）。</li>
</ul>"""),
            ("儲存位置", "<p>儲存在你的手機上。Ciclo沒有自己的帳戶或伺服器，不會顯示廣告，也不含任何第三方服務或分析工具。本應用程式沒有連上網路的權限，因此無法將任何內容傳送到任何地方。</p>"),
            ("Google備份", """<p>如果你的Google帳戶開啟了Android備份，Android會將Ciclo的資料納入備份，讓你在換到登入同一個Google帳戶的另一支手機，或重新安裝應用程式時，資料能自動還原。只有在備份以你螢幕鎖定的PIN碼、解鎖圖案或密碼進行端對端加密時，Ciclo才允許這項備份：Google和應用程式的開發者都無法讀取。如果你的手機沒有設定螢幕鎖定，或是執行Android 8，Ciclo的資料就不會備份。</p>
<p>這項備份是你與Google之間的Android服務：本應用程式不會自行傳送任何內容，也不會從備份接收任何內容。你可以在Android設定的備份項目中關閉這項備份。當你透過傳輸線或無線方式將資料轉移到新手機時，Ciclo的資料也會一併轉移。</p>"""),
            ("由你決定而離開應用程式的內容", """<p>只有你選擇分享或儲存的內容，才會離開Ciclo：</p>
<ul>
  <li><strong>發布公告：</strong>一張附上一句話的圖片，由你透過自己選擇的應用程式傳送。只有你決定的對象會收到。</li>
  <li><strong>報告：</strong>一份含有你生理期日期的PDF，你可以分享、儲存或列印。</li>
  <li><strong>備份檔案：</strong>一個含有應用程式資料的檔案，由你儲存在自己選擇的位置。這個檔案沒有密碼保護，請存放在你信任的地方。</li>
</ul>
<p>從那一刻起，這些檔案就由你掌控，並受你用來傳送或存放檔案的應用程式或服務的條款規範。</p>"""),
            ("權限", """<p>Ciclo唯一會向你要求的權限是顯示通知。通知的用途是在生理期快到時提醒你，或是問你生理期是否已經來了或結束了。這項權限是選用的：你可以拒絕，也可以在設定中逐一關閉每項提醒。</p>
<p>此外，Android會授予應用程式一些技術性權限，用來排定這些提醒，例如在你重新啟動手機後重新排定提醒。這些權限都不會讓應用程式存取網路或你的資料。</p>"""),
            ("如何刪除你的資料", "<p>前往設定 › 你的資料 › 「刪除我的所有資料」。解除安裝應用程式也會刪除手機上的所有資料。刪除資料後，Google備份會在下次更新時清空；如果你解除安裝應用程式，Google備份會保留下來，以便你日後重新安裝，你也可以從Google帳戶的備份中刪除它。你自行儲存的備份檔案不會被刪除：你可以自行刪除。</p>"),
            ("未成年人", "<p>Ciclo不會蒐集任何人的資料，未成年人也不例外。</p>"),
            ("健康", "<p>Ciclo的日期是根據你記錄的內容推估而來。本應用程式不是避孕方法，不能用來備孕，也不能取代醫療建議。</p>"),
            ("本政策的變更", "<p>如果本政策有所變更，新版本將連同新的日期公布於此。</p>"),
            ("聯絡方式", f"<p>如果對本政策有任何疑問，請寄信至{MAIL}。</p>"),
        ],
    ),
}


# Which text is binding: the English one. Every other language points to it.
VERSION_NOTE = {
    "es": f"La versión de referencia de esta política es la {EN}versión en inglés</a>. Si hay alguna diferencia entre ambas, prevalece la versión en inglés.",
    "en": "This English version is the reference version of this policy. If another language version differs from it, this version prevails.",
    "pt-BR": f"A versão de referência desta política é a {EN}versão em inglês</a>. Em caso de divergência, prevalece a versão em inglês.",
    "ca": f"La versió de referència d’aquesta política és la {EN}versió en anglès</a>. Si hi ha alguna diferència entre totes dues, preval la versió en anglès.",
    "fr": f"La version de référence de cette politique est la {EN}version anglaise</a>. En cas de divergence, la version anglaise prévaut.",
    "de": f"Maßgeblich ist die {EN}englische Fassung</a> dieser Datenschutzerklärung. Bei Abweichungen gilt die englische Fassung.",
    "it": f"La versione di riferimento di questa informativa è la {EN}versione inglese</a>. In caso di discrepanze, prevale la versione inglese.",
    "pl": f"Wersją referencyjną tej polityki jest {EN}wersja angielska</a>. W razie rozbieżności rozstrzygająca jest wersja angielska.",
    "nl": f"De referentieversie van dit privacybeleid is de {EN}Engelse versie</a>. Bij verschillen tussen beide gaat de Engelse versie voor.",
    "id": f"Versi acuan kebijakan ini adalah {EN}versi bahasa Inggris</a>. Jika terdapat perbedaan di antara keduanya, yang berlaku adalah versi bahasa Inggris.",
    "tr": f"Bu politikanın esas metni {EN}İngilizce metindir</a>. Metinler arasında herhangi bir farklılık olması hâlinde İngilizce metin geçerlidir.",
    "ja": f"本ポリシーは{EN}英語版</a>を正本とします。日本語版と英語版の内容に相違がある場合は、英語版が優先されます。",
    "ko": f"이 개인정보 처리방침은 {EN}영어 버전</a>을 기준으로 합니다. 한국어 버전과 영어 버전의 내용이 다를 경우 영어 버전이 우선합니다.",
    "zh-Hant": f"本隱私權政策的正式版本為{EN}英文版</a>。中文版與英文版如有任何歧異，以英文版為準。",
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

<p class="date">{VERSION_NOTE[lang]}</p>

<footer>{PUBLISHER}</footer>
</main>
</body>
</html>
"""


POLICY_LINKS = " · ".join(f'<a href="ciclo/{f}/" hreflang="{l}" lang="{l}">{n}</a>' for l, f, n in LANGS)

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
  <li>Política de privacidad · Privacy policy: {POLICY_LINKS}</li>
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
