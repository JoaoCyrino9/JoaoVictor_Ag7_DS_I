TIPOS_IMOVEL = {"comercial", "casa", "apartamento"}


def classificar_consumo():
    # Solicita o tipo de imóvel
    tipo_imovel = input('Digite o tipo de imóvel ("comercial", "casa" ou "apartamento"): ').strip().lower()

    # Validação simples do tipo de imóvel
    if tipo_imovel not in ["comercial", "casa", "apartamento"]:
        print("Tipo de imóvel inválido.")
        return

    # Solicita o consumo mensal de água (número decimal)
    try:
        consumo = float(input("Digite o consumo mensal de água em m³: "))
    except ValueError:
        print("Erro: digite um número decimal válido (exemplo: 15.5).")
        return

    # Regras de negócio exatamente como solicitadas
    if tipo_imovel == "comercial":
        print("Tarifa comercial aplicada – consulte o plano corporativo.")
        
    elif tipo_imovel == "apartamento" and consumo < 10:
        print("Consumo econômico – excelente controle de água!")
        
    elif (tipo_imovel == "apartamento" or tipo_imovel == "casa") and consumo <= 25:
        print("Consumo moderado – dentro do padrão residencial.")
        
    else:
        print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")

if __name__ == "__main__":
    classificar_consumo()