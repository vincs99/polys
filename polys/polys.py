class Polynomial:
    def __init__(self, coefs):
        self.coefficients = coefs
    
    def degree(self):

        return len(self.coefficients)-1

    def __str__(self):

        terms=[]
        coefs=self.coefficients

        if coefs[0]:
            terms.append(str(coefs[0]))
        
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1]==1 else coefs[1]}x")

        terms+=[f"{'' if c==1 else c}x^{d}" for d, c in enumerate(coefs[2:], start=2) if c]
        
        return " + ".join(reversed(terms)) or "0"