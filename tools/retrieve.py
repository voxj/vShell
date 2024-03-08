# Retriever Tool v1.1 * added FirstRun

import json

try:
    with open('settings.json', 'r') as stgs:
        data = json.load(stgs)
        echo = data['echo']
        devMode = data['devMode']
        Notes = data['Notes']
        bExts = data['betaExts']
        state = data['verstate']
        firstrun = data['firstRun']
        startalert = data['NonStopAlertRadio']
    def ev():
        return echo
    def sa():
        return startalert
    def dm():
        return devMode
    def lv():
        dm()
    def nt():
        return Notes
    def be():
        return bExts
    def st():
        return state
    def fr():
        return firstrun
    def retrieve():
        echoValue = ev()
        devMode = dm()
        log = lv()
        note = nt()
        betaExts = be()
        verState = st()
        firstr = fr()
        stalert = sa()
except Exception as e:
    print(f'Retriever tool had an error: {e}')
