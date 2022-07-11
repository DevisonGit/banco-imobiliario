Desafio técnico em Python

Aplicação representa um desafio técnico em Python onde é 
simulado com algumas regras diferentes o jogo do banco imobiliário

Instalação

git clone https://github.com/DevisonGit/banco-imobiliario.git

cd banco-imobiliario/

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

Executar Aplicação

python ./banco_imobiliario/main.py

Observações
Como não tem a especificação dos valores para gerar as propriedades, quando gero um objeto Propriedades 
associo um valor aleatório para o custo de venda e pego uma porcentagem sobre este valor para gerar o aluguel.

Tive um problema para testar a classe Tabuleiro, como ela instancia outras classes não sei se o unittest não consegue
gerar os imports ou deu algum conflito como o poetry ou mesmo meu ambiente, caso for executar os testes e apresentar erro, 
entrar na classe Tabuleiro comentar o import com caminho relativo e deixar o caminho completo.

Sobre a execução da simulação em si percebi alguns comportamentos.
Quanto mais alto a porcentagem do aluguel, menos partidas terminam com time out e as chances dos perfis: impulsivo ou exigente ganharem
Quanto menor a porcentagem do aluguel, mais partidas terminam com time out e as chances dos perfis: impulsivo ou cauteloso ganharem

