class VazamentoDados:
    def __init__(self):
        self.pesos = {
            'Senha': 100,
            'Email': 15,
            'Telefone': 70,
            'Nome': 25
        }
        self.vazamentos = {}

    def adicionar_site(self, site, dados_vazados):
        self.vazamentos[site] = dados_vazados

    def remover_site(self, site):
        if site in self.vazamentos:
            del self.vazamentos[site]

    def atualizar_vazamento(self, site, dados_vazados):
        self.vazamentos[site] = dados_vazados

    def visualizar_pontuacao(self, site):
        return sum(self.pesos[dado] for dado in self.vazamentos[site])

    def ranking(self):
        pontuacao = {site: self.visualizar_pontuacao(site) for site in self.vazamentos}
        return sorted(pontuacao.items(), key=lambda x: x[1], reverse=True)

# Exemplo de uso
vazamento = VazamentoDados()
vazamento.adicionar_site('Instagram', ['Senha', 'Nome'])
vazamento.adicionar_site('Twitter', ['Nome'])
vazamento.adicionar_site('Facebook', ['Email', 'Telefone'])
vazamento.adicionar_site('LinkedIn', ['Email', 'Nome', 'Telefone'])
vazamento.adicionar_site('TikTok', ['Senha', 'Email'])
vazamento.adicionar_site('Snapchat', ['Senha'])

print(vazamento.ranking())