# Automação com Selenium

Este repositório contém scripts em Python que utilizam a biblioteca Selenium para automatizar tarefas na web. A automação é realizada através do navegador Chrome, gerenciado pelo `webdriver_manager`.

## Pré-requisitos

Para executar os scripts, você precisará ter o Python instalado em sua máquina. Além disso, as seguintes bibliotecas devem ser instaladas:

- selenium
- webdriver_manager

Você pode instalar essas bibliotecas usando o pip:

```bash
pip install selenium webdriver_manager
```

## Descrição dos Scripts

### Script 1: Automação de Preenchimento de Formulário

Este script automatiza o processo de abrir uma página web, preencher um formulário com um e-mail aleatório e enviar o formulário. O processo é repetido até 3000 vezes, com atrasos aleatórios entre as iterações. O script pode ser interrompido se atingir uma hora específica do dia.

#### Estrutura do Código

- **Classe `automatizaWeb`**: Contém os métodos para abrir a página, preencher o formulário, enviar o formulário e fechar o navegador.
- **Método `abrirPagina(url)`**: Abre a página web fornecida.
- **Método `preencherFormulario()`**: Preenche o formulário com um e-mail aleatório e seleciona uma opção aleatória.
- **Método `enviarFormulario()`**: Envia o formulário preenchido.
- **Método `fecharNavegador()`**: Fecha o navegador.

### Script 2: Automação de Login no Google

Este script automatiza o processo de login em uma conta do Google. Ele utiliza uma instância de navegador Chrome já em execução para completar o login.

#### Estrutura do Código

- **Configuração do Chrome**: Conecta-se a uma instância de navegador Chrome já em execução.
- **Variáveis `username` e `password`**: Armazena as credenciais de login do Google.
- **URL de login**: URL para a página de login do Google.
- **Processo de Login**: Preenche o campo de e-mail, navega para a próxima página, preenche o campo de senha e conclui o login.

### Observações

- Certifique-se de substituir os seletores `xpath` no primeiro script com os valores corretos para o formulário que você deseja automatizar.
- No segundo script, certifique-se de que o Chrome esteja configurado para permitir conexões remotas e que o endereço e a porta estejam corretos.
- Você pode alternar para o navegador Firefox descomentando as linhas apropriadas e comentando as linhas correspondentes ao Chrome no primeiro script.
