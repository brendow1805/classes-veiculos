class veiculos(object):
    def __init__(self,marca,modelo,cor,velocidade):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.velocidade = velocidade

    def __setMarca(self,marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

    def __setModelo(self, modelo):
        self.modelo = modelo
        return self.modelo

    def getModelo(self):
        return self.modelo

    def __setCor(self, cor):
        self.cor = cor
        return self.cor

    def getCor(self):
        return self.cor

    def __setVelocidade(self, velocidade):
        self.velocidade = velocidade
        return self.velocidade

    def getVelocidade(self):
        return self.velocidade

    def __str__(self):
        return "\nMarca: "+self.marca+"\nModelo: "+self.modelo+"\nCor: "+self.cor+"\nVelocidade: "+str(self.velocidade)+"Km/h\n"

    def acelerar(self):
        if self.velocidade < 151:
            self.velocidade = self.getVelocidade() +1

    def frear(self):
        if self.velocidade ==0:
            self.velocidade = self.getVelocidade()

