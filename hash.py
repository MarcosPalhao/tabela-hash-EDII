class Tabela_Hash:
    def _init_(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho

    def _hash(self, key):
        return hash(key) % self.tamanho

    def inserir(self, key, value):
        index = self._hash(key)
        if self.tabela[index] is None:
            self.tabela[index] = [(key, value)]
        else:
            for i, (existing_key, existing_value) in enumerate(self.tabela[index]):
                if existing_key == key:
                    self.tabela[index][i] = (key, value)
                    return
            self.tabela[index].append((key, value))

    def buscar(self, key):
        index = self._hash(key)
        if self.tabela[index] is not None:
            for existing_key, existing_value in self.tabela[index]:
                if existing_key == key:
                    return existing_value
        return None

    def remover(self, key):
        index = self._hash(key)
        if self.tabela[index] is not None:
            for i, (existing_key, existing_value) in enumerate(self.tabela[index]):
                if existing_key == key:
                    del self.tabela[index][i]
                    return

hash_table = Tabela_Hash(10)

# Inserir
hash_table.inserir("Baltazar Gustavo", "Membro do grupo")
hash_table.inserir("Guilherme Santos", "Membro do grupo")
hash_table.inserir("Marcos Palhao", "Membro do grupo")

# Buscar
print(hash_table.buscar("Baltazar Gustavo"))
print(hash_table.buscar("Marcos Palhao"))

# Remover
hash_table.remover("Guilherme Santos")
print(hash_table.buscar("Guilherme Santos"))