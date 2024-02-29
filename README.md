# Repositório criado para armazenar o desenvolvimento da tarefa "Crie um Web Proxy", da disciplina de "Sistemas para a internet 2".
# Este projeto é um proxy web simples implementado usando o Flask, um microframework web para Python. O servidor proxy intercepta solicitações HTTP, busca o conteúdo solicitado na web e o serve ao cliente. Além disso, ele fornece funcionalidade para filtrar conteúdo sensível com base na idade do usuário.

## Recursos
### Servidor Proxy: Age como intermediário entre o cliente e o servidor web, permitindo que os usuários acessem conteúdo da web por meio do proxy.
### Filtro de Conteúdo: Filtra conteúdo sensível das páginas da web com base em uma lista predefinida de palavras-chave sensíveis.
### Modificação de Links: Modifica os links no conteúdo HTML recuperado para passar pelo servidor proxy, garantindo que todas as solicitações subsequentes sejam roteadas pelo proxy.
### Gerenciamento de Sessão: Mantém uma sessão para cada usuário com base em sua idade, armazenando sua URL atual para permitir navegação contínua.

## Como Funciona
### O usuário envia uma solicitação ao servidor proxy com a URL desejada e a idade.
### O servidor proxy intercepta a solicitação e busca o conteúdo da URL solicitada.
### Se o usuário tiver menos de 18 anos, o conteúdo é filtrado para substituir palavras-chave sensíveis por "SENSÍVEL".
### Os links dentro do conteúdo HTML recuperado são modificados para passar pelo servidor proxy.
### O conteúdo modificado é enviado de volta ao usuário.
