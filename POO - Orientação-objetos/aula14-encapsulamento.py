#Encapsulamento(modificadres de acesso public,protected,private)
#Python não tem modificadores de acesso
#Mas podemos seguir as seguintes convenções
#--------------------------------------------------------
#(sem underline) = public
#pode ser usado em qualquer lugar
#--------------------------------------------------------
#(um underline) = protected
#nao deve ser usado fota da classe
#ou suas subclasses
#--------------------------------------------------------
#dois underlines = private
#'name mangling' (desfiguração de nomes) em python
#so deve ser usado na classe que foi declarada

canal_muda = input("Digite se você quer mudar para o canal de cima ou de baixo Digite [A]Para cima e [B]Para baixo: ")


class Televisao:
    def __init__(self,min,max):
        self.ligada = False
        self.canal = 2
        self.cmin = min
        self.cmax = max

    def muda_baixo(self):
        if canal_muda == 'B' or canal_muda == 'b':
            if self.canal -1 >= self.cmin:
                self.canal -=1
            else:
                self.canal = self.cmax
    def muda_cima(self):
        if canal_muda == 'A' or canal_muda == 'a':
            if self.canal +1 <= self.cmax:
                self.canal += 1
            else:
                self.canal = self.cmin

tv = Televisao(2,10)
tv.muda_cima()
print('Canal de cima',tv.canal)
tv.muda_baixo()
print('canal de baixo',tv.canal)