import datetime
import math
from typing import List

class Pessoa:
    def __init__(self, nome: str, sobrenome: str, data_de_nascimento: datetime.date):
        self.data_de_nascimento = data_de_nascimento
        self.sobrenome = sobrenome
        self.nome = nome
        
    @property    
    def idade(self) -> int:
        return math.floor((datetime.date.today() - self.data_de_nascimento).days / 365.2425)
    
    
    def __str__(self) -> str:
        return f"{self.nome} {self.sobrenome} tem {self.idade} anos"
        


andre = Pessoa(nome='Andre', sobrenome='Sionek', data_de_nascimento=datetime.date(1991,5,12))



class Curriculo:
    def __init__(self, pessoa: Pessoa, experiencias: List[str]):
        self.experiencias = experiencias
        self.pessoa = pessoa
        
        
    @property
    def quantidade_de_experiencias(self) -> int:
        return len(self.experiencias)
    
    @property
    def empresa_atual(self) -> str:
        return self.experiencias[-1]
    
    
    def adiciona_experiencia(self, experiencia: str) -> None:
        self.experiencias.append(experiencia)
        
        
    def __str__(self):
        return f"{self.pessoa.nome} {self.pessoa.sobrenome} tem {self.pessoa.idade} anos e já " \
        f"trabalho em {self.quantidade_de_experiencias} empresas e atualmente trabalha na empresa {self.empresa_atual} " 
        
        
curriculo_andre = Curriculo(
    pessoa=andre, 
    experiencias=['HSBC','Polytack','Grupo Boticario','Olist','Emcasa','Gousto']
    )



#print(andre)
#print(andre.nome)
#print(andre.sobrenome)
#print(andre.idade)

print(curriculo_andre)
curriculo_andre.adiciona_experiencia("How Education")
#print(curriculo_andre.pessoa.idade)
print(curriculo_andre)
        
        
        
        
class Vivente:
    def __init__(self, nome: str, data_de_nascimento: datetime.date) -> None:
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento
        
        
    @property
    def idade(self) -> int:
        return math.floor((datetime.date.today() - self.data_de_nascimento).days / 365.2425)
    
    def emite_ruido(self, ruido: str):
        print(f"{self.nome} fez ruido: {ruido}")
    



class PessoaHerenca(Vivente):
    def __str__(self) -> str:
        return f"{self.nome} tem {self.idade} anos"
    
    def fala(self, frase):
        return self.emite_ruido(frase)
    
    
    
    
class Cachorro(Vivente):
    def __init__(self, nome: str, data_de_nascimento: datetime.date, raca: str) -> None:
        super().__init__(nome, data_de_nascimento)
        self.raca = raca
   
    def __str__(self) -> str:
        return f"{self.nome} é da raça {self.raca} e tem {self.idade} anos"
    
    def late(self):
        return self.emite_ruido("Au! Au!")
    

belisco = Cachorro(nome='Belisco', data_de_nascimento=datetime.date(2019,4,15), raca='Lhasa Apso')
     
andre4 = PessoaHerenca(nome='Andre', data_de_nascimento=datetime.date(1991,5,12))
        

print(belisco)


belisco.late()
belisco.late()
belisco.late()
belisco.late()
andre4.fala("Cala a boca, Belisco!")
belisco.late()
belisco.late()
belisco.late()
belisco.late()