
from collections import deque

clientes = [
    {
    "id_cliente" : 1,
    "nome" : "Alanzoka Silva Batista",
    "cpf" : "11122233344",
    "endereco": "Londrina",
    "telefone": "7488889999",
    "historico": []
},
{
    "id_cliente" : 1,
    "nome" : "TazerCraft Junior",
    "cpf" : "22233344455",
    "endereco": "Amsterdan",
    "telefone": "7488889999",
    "historico": []
}
]

equipamentos = [
    {
    'id' : 1,
    'tipo' : "Notebook",
    'marca' : "Dell",
    'modelo' : "Inspiron 15",
    'estado' : "Funcionando normalmente; Algumas marcas de uso"
},
    {
    'id' : 2,
    'tipo' : "Celular",
    'marca' : "Samsung",
    'modelo' : "A14",
    'estado' : "Touch danificado"
}
]

ordensDeServicos = [
        {
    'numero_os' : 1,
    'cliente_cpf' : "11122233344",
    'aparelho' : "Notebook Dell, Inspiron 15",
    'descricao' : "Notebook com defeito no teclado",
    'entrada' : 27092026,
    'prazo_maximo' : "30 dias úteis",
    'valor_estimulado': 250.00
    },
 {
    'numero_os' : 2,
    'cliente_cpf' : "22233344455",
    'aparelho' : "Celular Samsung A14",
    'descricao' : "Celular não liga",
    'entrada' : 28092026,
    'prazo_maximo' : "30 dias úteis",
    'valor_estimulado': 250.00
    }    
]

tecnicos = [{
    'nome' : "Orretadinha",
    'cpf'  : "77788899911",
    'telefone' : '4002-8922'
}]

fila_orcamento = deque()
fila_aprovacao = deque()
fila_execucao = deque()
finalizados = []

