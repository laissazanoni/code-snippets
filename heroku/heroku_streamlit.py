
# =======================================================
# deploy streamlit app in heroku
# ========================================================

# 1. Instale o Git ( Ref: https://www.atlassian.com/br/git/tutorials/install-git )
# 2. Faça o download e instale o CLI do Heroku ( Ref: https://devcenter.heroku.com/articles/heroku-cli )
# 3. Crie uma nova pasta ( house_rocket )
# 4. Copie os arquivos kc_house_data.csv e dashboard.py para dentro da pasta criada.
# 5. Crie o arquivo Procfile ( "P" maiúsculo e não tem extensão )
# 6. Copie e cole a seguinte linha dentro do Procfile
#               web: sh setup.sh && streamlit run dashboard.py
# 7. Gerar arquivo requirements.txt (utilizar a biblioteca pipreqs para pegar apenas as bibliotecas utilizadas no seu .py: )

""" pip install pipreqs
    No terminal execute o comando [pipreqs] na mesma pasta do arquivo .py """

# 8. Crie o arquivo setup.sh:

"""            mkdir -p ~/.streamlit/

               echo "\
               [general]\n\
               email = \"meu_email@gmail.com\"\n\
               " > ~/.streamlit/credentials.toml

              echo "\
              [server]\n\
              headless = true\n\
             enableCORS=false\n\
             port = $PORT\n\
             " > ~/.streamlit/config.toml """

# 9. Inicie o git dentro da pasta ( Comando: git init )
# 10. Faço o login no Heroku pelo Terminal ( Comando: heroku login )
# 11. Crie um aplicativo que armazenará o seu dashboard ( Comando: heroku apps:create analytics-house-rocket )
# 12. Versione todo os arquivos com o Git ( Comando: git add . )
# 13. Escreve uma mensagem indicando as mudanças no Git ( Comando: git commit -m 'first commit' )
# 14. Envie os dados para o Heroku ( Comando: git push heroku master )
# 15. Inicialize o serviço no Heroku ( Comando: heroku ps:scale web=1 )
