# Funcionamento da lógica de negócios para os dashboards e modelos:
# No front-end, haverá cards dos dashboards e modelos,
# eles deverão ter uma propriedade com um id específico do dash ou model.
# Ao clicar no card, será disparada uma requisição com o parâmetro id.
# Esse id deverá ser checado quanto ao status do dash/model da requisição.
# Caso o produto esteja pronto, o serviço encontrar o diretório com mesmo nome de id do produto
# e deve retornar os dados do dash ou fazar a previsão com o modelo e devolver o resultado.