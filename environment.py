from browser import Browser

#executar antes de todos os testes iniciarem
def before_all(context):
    context.browser = Browser()

#executar depois de todos os testes finalizarem
def after_all(context):
    context.browser.browser_quit()

#executar antes de cada teste
def after_scenario(context, scenario):
    context.browser.browser_clear()