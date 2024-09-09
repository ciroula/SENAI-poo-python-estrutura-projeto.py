from models.enums.sexo import Sexo
from models.endereco import Endereco


class Pessoa:
    def __init__(self, nome: str, idade: int, sexo: Sexo, endereco: Endereco) -> None:
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.endereco = endereco

       
    def __str__(self) -> str:
        return(
            "===DADOS DO USUARIO==="
            f"\nNome: {self.nome}"
            f"\nIdade: {self.idade}"
            f"\nSexo: {self.sexo.value}"
            f"\nEndereco: {self.endereco.logradouro}"
            f"\nEndereco: {self.endereco.numero}"
            "\n===FIM DOS DADOS==="
        )