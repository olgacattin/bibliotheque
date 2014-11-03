LANGUE_TYPE = [
        {'code':'FR', 'desc':'Français'},
        {'code':'ALL', 'desc':'Allemand'},
        {'code':'ANG', 'desc':'Anglais'},
        {'code':'ITA', 'desc':'Italiano'},
    ]
 
    LIVRE_TYPE = [
        {'code':'BUS', 'desc':'Business'},
        {'code':'ARC', 'desc':'Architecture'},
        {'code':'INF', 'desc':'Informatique'},
        {'code':'CTF', 'desc':'Cientifique'},
    ]
	
    LIVRE_SUBTYPE = [
        {'code':'MATH', 'desc':'Mathematiques', 'code_type':'CTF'},
        {'code':'PROG', 'desc':'Programmation', 'code_type':'INF'},
        {'code':'BDON', 'desc':'Base de données', 'code_type':'ARC'},
        {'code':'ALGO', 'desc':'Algorithmique', 'code_type':'INF'},
        {'code':'MARK', 'desc':'Marketing', 'code_type':'BUS'},
        {'code':'FINA', 'desc':'Finances', 'code_type':'BUS'},
    ]

    LIVRE_MONNAIE = [
        {'code':'CHF', 'desc':'Francs Suisses'},
        {'code':'EURO', 'desc':'Euros'},
        {'code':'USD', 'desc':'Dolars'},
    ]

    LIVRE_CATEGORIE= [
        {'code': 'TXTBK', 'desc':'Text book'},
        {'code': 'JOURN', 'desc': 'Journal'},
        {'code': 'PROCE', 'desc': 'Processing note'},
        {'code': 'MAGAZ', 'desc': 'Magazine'},
    ]

    PROP_TYPE = [
        {'code':'PERS', 'desc': 'Personne'},
        {'code':'ENTR', 'desc': 'Entreprise'},
    ]


(http://www.dajaxproject.com/forms/)
ajax.py
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

@dajaxice_register
def updatecombo(request, option):
    dajax = Dajax()
    options = [['Madrid', 'Barcelona', 'Vitoria', 'Burgos'],
               ['Paris', 'Evreux', 'Le Havre', 'Reims'],
               ['London', 'Birmingham', 'Bristol', 'Cardiff']]
    out = []
    for option in options[int(option)]:
        out.append("<option value='#'>%s</option>" % option)

    dajax.assign('#combo2', 'innerHTML', ''.join(out))
    return dajax.json()


html
<select onchange="Dajaxice.examples.updatecombo(Dajax.process, {'option':this.value})" size="1">
    <option value="0">Select...</option>
    <option value="0">Spain</option>
    <option value="1">France</option>
    <option value="2">United Kingdom</option>
</select>
<select id="combo2" onchange="" size="1"></select>



