#@property - um getter no modo pythonico
#getter - um metodo para obter atributo
#cor -> get_cor()
#@property e uma propriedade do objeto,ela e um metodo que se comporta como um atributo
#geralmente e usada nas seguintes situações
# -- como getter
#--p/evitar quebrar codigo cliente
# -- p/ habilitr setter
#--- p/ executar ações ao obter um atributo


class Caneta:
    def __init__(self,cor): #METODO DE INICIALIZAÇÃO
        self.cor_tinta = cor

    @property #property e um metodo que pode ser utilizado como getter e setter com python para podermos criar,
    #outras instancias do nosso atributo com nomes difrentes onde possibilitara que gerenciamos somente 1 atributo sem alterar os demais,
    #ou causar falaha em alguns deles 
    def cor(self):
        print('Nunca nem vi')
        return self.cor_tinta

    @property
    def cor_tampa(self):
        return 12345

caneta = Caneta('azul')
print(caneta.cor)
print(caneta.cor_tampa)
