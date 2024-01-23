class ListaDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)
        print(f'Tarefa "{tarefa}" adicionada com sucesso!')

    def visualizar_tarefas(self):
        if not self.tarefas:
            print('Não há tarefas na lista.')
        else:
            print('Lista de tarefas:')
            for i, tarefa in enumerate(self.tarefas, start=1):
                print(f'{i}. {tarefa}')

    def remover_tarefa(self, indice):
        try:
            tarefa_removida = self.tarefas.pop(indice - 1)
            print(f'Tarefa "{tarefa_removida}" removida com sucesso!')
        except IndexError:
            print('Índice inválido. Verifique a lista de tarefas.')

def main():
    lista_tarefas = ListaDeTarefas()

    while True:
        print('\nMenu:')
        print('1. Adicionar Tarefa')
        print('2. Visualizar Tarefas')
        print('3. Remover Tarefa')
        print('4. Sair')

        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            tarefa = input('Digite a nova tarefa: ')
            lista_tarefas.adicionar_tarefa(tarefa)
        elif escolha == '2':
            lista_tarefas.visualizar_tarefas()
        elif escolha == '3':
            lista_tarefas.visualizar_tarefas()
            indice = int(input('Digite o número da tarefa a ser removida: '))
            lista_tarefas.remover_tarefa(indice)
        elif escolha == '4':
            print('Saindo...')
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == "__main__":
    main()
