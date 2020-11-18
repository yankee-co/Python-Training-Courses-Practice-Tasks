# General classes
class ProgrammingLanguage:
    def validate(self, variable, typevar):
        return isinstance(variable, typevar)


class Interpretable(ProgrammingLanguage):
    def interprete(self):
        return('Interpretation...')


class Compiled(ProgrammingLanguage):
    def compile(self):
        return 'Compilation...'


class StronglyTyped(ProgrammingLanguage):
    pass


class Python(StronglyTyped, Interpretable):
    pass


class Java(StronglyTyped, Compiled):
    pass


class Cpp(StronglyTyped, Compiled):
    pass


class JS(Interpretable):
    def validate(self, variable, typevar):
        return True


JsInst = JS()
print(JsInst.validate(1344, str))
