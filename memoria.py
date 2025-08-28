class Memoria:
    def __init__(self, tamanho_total=128, tamanho_endereco=2):
        self.tamanho_total = tamanho_total
        self.tamanho_endereco = tamanho_endereco
        self.blocos = [
            {'status': 'livre', 'tamanho': tamanho_total, 'processo_id': None}
        ]

    def __str__(self):
        # Representação visual da memória
        representacao = ""
        for bloco in self.blocos:
            if bloco['status'] == 'ocupado':
                representacao += f"[P{bloco['processo_id']}:{bloco['tamanho']}KB]"
            else:
                representacao += f"[Livre:{bloco['tamanho']}KB]"
        return representacao

    def arredondar(self, tamanho_processo):
        # Arredonda para múltiplos do tamanho_endereco
        if tamanho_processo % self.tamanho_endereco == 0:
            return tamanho_processo
        return ((tamanho_processo // self.tamanho_endereco) + 1) * self.tamanho_endereco

    def alocar_processo(self, processo_id, tamanho_processo, algoritmo):
        # Ajusta o tamanho do processo e chama o algoritmo
        tamanho_processo = self.arredondar(tamanho_processo)
        return algoritmo(self.blocos, processo_id, tamanho_processo)

    def liberar_processo(self, processo_id):
        # Libera e realiza fusão de blocos
        for bloco in self.blocos:
            if bloco['processo_id'] == processo_id:
                bloco['status'] = 'livre'
                bloco['processo_id'] = None
        self.fundir_blocos()

    def fundir_blocos(self):
        # Junta blocos consecutivos livres
        i = 0
        while i < len(self.blocos) - 1:
            if self.blocos[i]['status'] == 'livre' and self.blocos[i+1]['status'] == 'livre':
                self.blocos[i]['tamanho'] += self.blocos[i+1]['tamanho']
                del self.blocos[i+1]
            else:
                i += 1
