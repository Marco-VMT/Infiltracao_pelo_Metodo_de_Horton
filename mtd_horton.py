# Bibliotecas

import math
from scipy.optimize import minimize


# Funções

def calc_corr(tempo, a, fc, f0):
    return fc + (f0 - fc) * math.exp(-a * tempo)

def calc_dif2(interm, corr):
    return (interm - corr) ** 2

def calc_f(tempo, a, fc, f0):
    return (fc * tempo) + (1 / a) * (f0 - fc) * (1 - math.exp(-a * tempo))

def error_function(params, tempos, interms):
    a, fc, f0 = params
    error = 0
    for i, tempo in enumerate(tempos):
        corr = calc_corr(tempo, a, fc, f0)
        error += calc_dif2(interms[i], corr)
    return error


# Chutes iniciais

a_chute = float(input('Valor chute de a: '))
fc_chute = float(input('Valor chute de fc: '))
f0_chute = float(input('Valor chute de f0: '))


# Vetores

tempos = []
infils = []
interms = []
corris = []
difs = []
fs = []


# Cálculos

contador = 1
while True:
    tempo = input(f"T{contador} (min): ")
    if not tempo:
        break
    tempos.append(float(tempo))
    contador += 1

# Total Infiltrado
for contador, _ in enumerate(tempos):
    infil = input(f"Total Infiltrado {contador + 1} (mm): ")
    infils.append(float(infil))

# Cálculos intermitentes
for i in range(len(tempos)):
    if i == 0:
        interm = infils[0]
    else:
        interm = infils[i] - infils[i - 1]
    interms.append(interm)


# Função para gerar tabela

def gerar_tabela(a, fc, f0, tempos, interms, title):
    corris.clear()
    difs.clear()
    fs.clear()
    
    for i, tempo in enumerate(tempos):
        corr = calc_corr(tempo, a, fc, f0)
        corris.append(corr)
        dif = calc_dif2(interms[i], corr)
        difs.append(dif)
        fs.append(calc_f(tempo, a, fc, f0))

    sum_difs = round(sum(difs), 4)
    sum_interms = round(sum(interms), 4)
    sum_corris = round(sum(corris), 4)

    # Valores arredondados

    tempos_f = ['%.0f' % elem for elem in tempos]
    infils_f = ['%.4f' % elem for elem in infils]
    interms_f = ['%.4f' % elem for elem in interms]
    corris_f = ['%.4f' % elem for elem in corris]
    difs_f = ['%.4f' % elem for elem in difs]
    fs_f = ['%.4f' % elem for elem in fs]

    # Função print da tabela

    def formatar(tempos, tempos_f, infils_f, interms_f, corris_f, difs_f, fs_f, cols_sizes):
        forma_col = '{:^{col1_size}} {:^{col2_size}} {:^{col3_size}} {:^{col4_size}} {:^{col5_size}} {:^{col6_size}}'
        
        print(' - ' * 42)
        print(f'{title:^120}')
        print(' - ' * 42)
        print(forma_col.format('Tempo', 'Total Infiltrado', 'Intermitente', 'Corrigido', 'Diferença^2', 'F', **cols_sizes))
        print(' - ' * 42)
        
        for i in range(len(tempos)):
            print(forma_col.format(tempos_f[i], infils_f[i], interms_f[i], corris_f[i], difs_f[i], fs_f[i], **cols_sizes))     

        print(' - ' * 42)
        print(forma_col.format('Σ', '', sum_interms, sum_corris, sum_difs, '', **cols_sizes))
        print(' - ' * 42)
        print('\n \n \n')


    cols_sizes = {'col1_size': 15, 'col2_size': 20, 'col3_size': 20, 'col4_size': 20, 'col5_size': 20, 'col6_size': 15}
    formatar(tempos, tempos_f, infils_f, interms_f, corris_f, difs_f, fs_f, cols_sizes)


print('\n \n \n')
print(f"Valores de chute: a = {a_chute:.4f} | fc = {fc_chute:.4f} | f0 = {f0_chute:.4f}")
gerar_tabela(a_chute, fc_chute, f0_chute, tempos, interms, "Método de Horton - Valores Iniciais")


# Otimização

chute_inicial = [a_chute, fc_chute, f0_chute]
result = minimize(error_function, chute_inicial, args=(tempos, interms))
a_otim, fc_otim, f0_otim = result.x


# Tabela Valores Otimizados

print(f"Valores otimizados: a = {a_otim:.4f} | fc = {fc_otim:.4f} | f0 = {f0_otim:.4f}")
gerar_tabela(a_otim, fc_otim, f0_otim, tempos, interms, "Método de Horton - Valores Otimizados")


quit()