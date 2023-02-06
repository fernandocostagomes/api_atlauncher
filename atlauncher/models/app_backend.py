# Objeto que representa o uma App generico do device cadastrado no backend.
class AppBackend:
    def __init__(self, appNumId, appTxtLabel, appTxtPackage ):
   #long
        self.appNumId = appNumId
        self.appTxtLabel = appTxtLabel
        self.appTxtPackage = appTxtPackage