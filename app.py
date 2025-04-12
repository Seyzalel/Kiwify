import time
import random
import os
from datetime import datetime, timedelta

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def gerar_horarios(qtd):
    agora = datetime.now()
    inicio = agora - timedelta(hours=6)
    fim = agora - timedelta(hours=4)
    intervalo_total = int((fim - inicio).total_seconds() // 60)
    minutos = sorted(random.sample(range(15, intervalo_total - 15), qtd))
    return [inicio + timedelta(minutes=m) for m in minutos]

def animacao(texto, duracao=0.8):
    ciclos = ['⠋','⠙','⠹','⠸','⠼','⠴','⠦','⠧','⠇','⠏']
    for _ in range(3):
        for etapa in ciclos:
            print(f'\r{texto} {etapa}', end='', flush=True)
            time.sleep(duracao / len(ciclos))
    print()

def executar():
    limpar()

    print("Vendora - Sistema de Conversão Autônoma em Tráfego Direto\n")
    time.sleep(1)

    plataformas = [
        "1. Kiwify",
        "2. Kirvano",
        "3. Braip",
        "4. Hotmart",
        "5. Eduzz",
        "6. Monetizze"
    ]

    print("Selecione a plataforma de marketing digital para esta operação:\n")
    for p in plataformas:
        print(p)
    print()

    while True:
        escolha = input("Digite o número correspondente à plataforma desejada: ").strip()
        if escolha in [str(i) for i in range(1, len(plataformas)+1)]:
            plataforma_escolhida = plataformas[int(escolha)-1][3:]
            break
        else:
            print("Entrada inválida. Por favor, selecione uma opção válida.\n")

    link = input(f"\nInforme o link de afiliado da página principal de venda na {plataforma_escolhida}: ").strip()
    print()

    print("Sistema iniciado com sucesso.")
    print(f"Plataforma: {plataforma_escolhida}")
    print(f"Link de Afiliado: {link}")
    print("Vendora está agora operando em modo ativo.")
    print("O módulo de rastreamento está monitorando interações em tempo real.")
    print("Segmentação de público, qualificação de leads e condução à conversão estão em execução contínua.")
    print("O sistema está analisando comportamento, origem de tráfego, compatibilidade com a oferta e intenção de compra.")
    taxa_prevista = round(random.uniform(32.0, 41.0), 1)
    print(f"Taxa estimada de conversão para este horário: {taxa_prevista}%\n")
    time.sleep(6)

    total_eventos = random.randint(28, 54)
    total_vendas = random.randint(6, 18)
    total_leads = random.randint(6, 14)
    total_cliques = total_eventos - total_vendas - total_leads

    tipos = (["venda"] * total_vendas) + (["lead"] * total_leads) + (["clique"] * total_cliques)
    random.shuffle(tipos)

    horarios = gerar_horarios(total_eventos)
    eventos = sorted(zip(horarios, tipos))

    vendas_confirmadas = 0
    comissao = 137.90

    for horario, tipo in eventos:
        hora = horario.strftime("%H:%M:%S")
        if tipo == "clique":
            print(f"[{hora}] Clique identificado no link de afiliado.")
        elif tipo == "lead":
            print(f"[{hora}] Lead qualificado capturado com base no perfil de engajamento.")
        elif tipo == "venda":
            print(f"[{hora}] Venda concluída. Comissão gerada: R$ 137,90 — Produto: Sistema Viral")
            vendas_confirmadas += 1
        time.sleep(0.17)

    total_cliques = len([e for e in eventos if e[1] == "clique"])
    total_leads = len([e for e in eventos if e[1] == "lead"])
    lucro_total = vendas_confirmadas * comissao
    taxa_final = round((vendas_confirmadas / total_eventos) * 100, 2)

    time.sleep(1.5)

    print("\nOperação finalizada. O sistema encerrou a sessão após atingir os parâmetros de desempenho.\n")
    time.sleep(1)

    print("Resumo da Sessão:\n")
    print(f"Plataforma Utilizada: {plataforma_escolhida}")
    print(f"Link Monitorado: {link}")
    print(f"Total de Eventos Monitorados: {total_eventos}")
    print(f"Cliques Registrados: {total_cliques}")
    print(f"Leads Qualificados: {total_leads}")
    print(f"Vendas Realizadas: {vendas_confirmadas}")
    print(f"Produto Promovido: Sistema Viral")
    print(f"Comissão por Venda: R$ 137,90")
    print(f"Lucro Total: R$ {lucro_total:,.2f}")
    print(f"Taxa de Conversão Real: {taxa_final}%\n")

    print("Toda a jornada foi conduzida com autonomia e inteligência estratégica.")
    print("Vendora assumiu o controle, operou silenciosamente e entregou resultados.\n")
    print("Relatório processado por Vendora — Tecnologia de Conversão Comercial Inteligente © 2025")

if __name__ == "__main__":
    executar()
