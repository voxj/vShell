import json

try:
    with open('settings.json', 'r') as stgs:
        data = json.load(stgs)
        echo = data['echo']
        devMode = data['devMode']
        Notes = data['Notes']
        bExts = data['betaExts']
        state = data['verstate']
    def ev():
        return echo
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
    def retrieve():
        echoValue = ev()
        devMode = dm()
        log = lv()
        note = nt()
        betaExts = be()
        verState = st()
except Exception as e:
    print(f'Setting Retriever tool had an error: {e}')
