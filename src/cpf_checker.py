from .str_utils import keep_only_numbers

class CPF_Checker():
    CPF_NUM_DIGITS = 11

    def __init__(self, cpf=""):
        self.cpf = cpf

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, value):
        value = keep_only_numbers(value)
        self._cpf = value

    @property
    def pretty(self):
        if self.check():
            return "%s.%s.%s-%s" % (self.cpf[:3], self.cpf[3:6], self.cpf[6:9], self.cpf[9:])
        else:
            return None

    def _check_repeatition(self) -> bool:
        return len(set(self.cpf)) > 1

    def _check_number_of_digits(self) -> bool:
        return len(self.cpf) == self.CPF_NUM_DIGITS

    def _check_validation_digits(self) -> bool:
        # J
        j = 0
        for (coeff, alg) in zip(range(10,2-1,-1), map(int, self.cpf[:9])):
            j += alg*coeff
        
        r = j%11
        if r in (0,1):
            j = 0
        else:
            j = 11 - r
        
        # K
        k = 0
        for (coeff, alg) in zip(range(11, 2-1, -1), map(int, self.cpf[:10])):
            k += coeff*alg
        
        r = k%11
        if r in (0, 1):
            k = 0
        else:
            k = 11 - r

        for a,b in zip([j, k], list(map(int, self.cpf[-2:]))):
            if a != b:
                return False
        return True



    def _checkers(self):
        return (
            self._check_repeatition,
            self._check_number_of_digits,
            self._check_validation_digits
        )

    def check(self):
        # TODO: one-line this
        for v in self._checkers():
            if v() is False:
                return False
        return True

