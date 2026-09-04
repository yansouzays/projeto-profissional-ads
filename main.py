from sistema_estoque_add import gerenciar_estoque_manual
from collections import deque
from Funçoes import RegistrarClientes, RegistrarEquipamentos
from sistema_ordens_de_serviço import abrir_OSs, mostrar_os, orcamento_Os, aprovar_Os, finalizar_Os

proximo_id = 0

estoque = [
    {
        'id' : 1,
        'nome' : "BATERIA SAMSUNG",
        'categoria' : "BATERIA",
        'quantidade' : 14,
        'estado' : "novo",
        'preco' : 10.50
        },
    {
        'id' : 2,
        'nome' : "TELA SAMSUNG A32",
        'categoria' : 'TELA',
        'quantidade' : 3,
        'estado' : 'usado',
        'preco' : 280.00
        },
    {
        'id' : 3,
        'nome' : "TELA REDMI NOTE 10",
        'categoria' : "TELA",
        'quantidade' : 2,
        'estado' : 'novo',
        'preco' : 150.00
    },

    {
        'id' : 4,
        'nome' : "CONECTOR CARGA MOTO G8",
        'categoria' : "CONECTOR",
        'quantidade' : 15,
        'estado' : "novo",
        'preco' : 12.00
    },
    {
         'id' : 5,
         'nome' : "CAMERA TRASEIRA IPHONE XR",
         'categoria' : "CAMERA",
         'quantidade' : 8,
         'estado' : "novo",
         'preco' : 350.00,     
    },
    {
         'id' : 6,
         'nome' : "TAMPA TRASEIRA DE VIDRO IPHONE 11",
         'categoria' : "CARCAÇA",
         'quantidade' : 5,
         'estado' : "novo",
         'preco' : 90.00,     
     },
    {
         'id' : 7,
         'nome' : "FLEX BOTAO POWER E VOLUME A20",
         'categoria' : "FLEX",
         'quantidade' : 20,
         'estado' : "usado",
         'preco' : 15.00,     
     },
    {
         'id' : 8,
         'nome' : "BATERIA IPHONE 11",
         'categoria' : "BATERIA",
         'quantidade' : 9,
         'estado' : "novo",
         'preco' : 135.00,     
     },    
]

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

'''abrir_OSs(fila_orcamento, clientes, proximo_id)
orcamento_Os(fila_orcamento, fila_aprovacao, estoque)
aprovar_Os(fila_aprovacao, fila_execucao, finalizados)'''

while True:
    print("\n1 - Registrar Cliente.")
    print("2 - Registrar Equipamentos.")
    print("3 - Gerenciar estoque.")
    print("4 - Abrir Ordem de serviços.")
    print("5 - Orçamento.")
    print("6 - Aprovar ordem de serviços.")
    print("7 - Sair")
    opcao = int(input("Digite o número conforme as opções acima: "))

    match opcao:
        case 1:
            RegistrarClientes(clientes)
        case 2:
            RegistrarEquipamentos(equipamentos)
        case 3:
            gerenciar_estoque_manual(estoque)
        case 4:
            abrir_OSs(fila_orcamento, clientes, proximo_id)
        case 5:
            orcamento_Os(fila_orcamento, fila_aprovacao, estoque)
        case 6:
            aprovar_Os(fila_aprovacao, fila_execucao, finalizados)
        case 7:
            print("SAINDO...")
            exit()
        case _:
            print("Opção inválida!")