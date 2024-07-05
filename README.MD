# Automação com Selenium

Este repositório contém um script em Python que utiliza a biblioteca Selenium para automatizar o preenchimento e envio de formulários na web. A automação é realizada através do navegador Chrome, gerenciado pelo `webdriver_manager`.

## Pré-requisitos

Para executar o script, você precisará ter o Python instalado em sua máquina. Além disso, as seguintes bibliotecas devem ser instaladas:

- selenium
- webdriver_manager

Você pode instalar essas bibliotecas usando o pip:

```bash
pip install selenium webdriver_manager
```

## Descrição do Script

O script automatiza o processo de abrir uma página web, preencher um formulário com um e-mail aleatório e enviar o formulário. O processo é repetido até 3000 vezes, com atrasos aleatórios entre as iterações. O script pode ser interrompido se atingir uma hora específica do dia.

### Estrutura do Código

- **Classe `automatizaWeb`**: Contém os métodos para abrir a página, preencher o formulário, enviar o formulário e fechar o navegador.
- **Método `abrirPagina(url)`**: Abre a página web fornecida.
- **Método `preencherFormulario()`**: Preenche o formulário com um e-mail aleatório e seleciona uma opção aleatória.
- **Método `enviarFormulario()`**: Envia o formulário preenchido.
- **Método `fecharNavegador()`**: Fecha o navegador.

### Observações

- Certifique-se de substituir os seletores `xpath` no método `preencherFormulario` com os valores corretos para o formulário que você deseja automatizar.
- Você pode alternar para o navegador Firefox descomentando as linhas apropriadas e comentando as linhas correspondentes ao Chrome.
