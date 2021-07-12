from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView

class IndexView(TemplateView):
    template_name = 'index.html'

class DadosJASONView(BaseLineChartView):
    
    def get_labels(self):
        """Retorna 12 labels para a representação do x"""
        labels = [
            "Janeiro",
            "Fevereiro",
            "Abril",
            "Maio",
            "Junho",
            "Julho",
            "Agosto",
            "Setembro",
            "Outubro",
            "Novembro",
            "Dezembro"
        ]
        
        return labels

    def get_providers(self):
        """Retorna os nomes dos datasets."""
        datasets = [
            "Programação para Leigos",
            "Algoritmos e lógica de programação",
            "Programação em C",
            "Porgramação em Java",
            "Programação em Python",
            "Banco de dados"
        ]
        return datasets
    
    def get_data(self):
        """
        Retorna 6 datasets para plotar o grafico

        Cada linha representa um dataset
        Cada coluna representa um label
        
        A quantidade de dados precisa ser igual aos datasets/Labels
        
        12 labels, então 12 colunas,
        6 datasets, então 6 linhas.

        """

        dados = []
        for linhas in range(6):
            for colunas in range(12):
                dado = [
                    randint(1,200), # jan
                    randint(1,200), # fev
                    randint(1,200), # mar
                    randint(1,200), # abr
                    randint(1,200), # mai
                    randint(1,200), # jun
                    randint(1,200), # jul
                    randint(1,200), # ago
                    randint(1,200), # set
                    randint(1,200), # out
                    randint(1,200), # nov
                    randint(1,200), # dez
                ]
            dados.append(dado)
        return dados