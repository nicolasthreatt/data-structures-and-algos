"""
Fires in the Amazon - Dataset Validation

This class validates the detailed monthly fire statistics against the
annual summary data for Brazil. The goal is to ensure that the sum of
fires per year in the detailed dataset matches the totals in the summary dataset.

- Detailed dataset columns: year,state,month,number
- Summary dataset columns: year,number

Usage:
    validator = FireDataValidator(detailed_csv, summary_csv)
    print(validator.validate())  # True or False
"""

class FireDataValidator:
    def __init__(self, detailed_csv: str, summary_csv: str):
        self.detailed_csv = detailed_csv
        self.summary_csv = summary_csv

    def parse_detailed(self):
        totals = {}
        lines = self.detailed_csv.strip().splitlines()[1:]  # skip header
        for line in lines:
            values = line.split(',')
            year = values[0]
            number = int(values[3])
            totals[year] = totals.get(year, 0) + number
        return totals

    def parse_summary(self):
        totals = {}
        lines = self.summary_csv.strip().splitlines()[1:]  # skip header
        for line in lines:
            values = line.split(',')
            year = values[0]
            number = int(values[1])
            totals[year] = number
        return totals

    def validate(self) -> bool:
        return self.parse_detailed() == self.parse_summary()


if __name__ == "__main__":

    # Test Case 1
    detailed_csv1 = """
        year,state,month,number
        2000,Rio,Novembro,18
        2002,Pernambuco,Fevereiro,64
        2001,Mato Grosso,Maio,112
        2003,Roraima,Janeiro,547
        2002,Maranhao,Julho,4
        2003,Rio,Março,9
        2000,Roraima,Outubro,25
        2001,Paraiba,Janeiro,11
    """
    summary_csv1 = """
        year,number
        2002,68
        2000,43
        2003,556
        2001,123
    """
    validator1 = FireDataValidator(detailed_csv1, summary_csv1)
    assert validator1.validate() == True

    # Test Case 2
    detailed_csv2 = """
        year,state,month,number
        2008,Maranhao,Agosto,713
        2009,Tocantins,Maio,91
        2008,Pernambuco,Março,32
        2007,Paraiba,Janeiro,11
        2007,Piau,Setembro,4
        2008,Santa Catarina,Dezembro,29
        2009,Distrito Federal,Fevereiro,0
        2007,Sergipe,Novembro,7
        2009,Goias,Junho,179
        2008,Rio,Fevereiro,25
    """
    summary_csv2 = """
        year,number
        2009,270
        2008,713
        2007,22
    """
    validator2 = FireDataValidator(detailed_csv2, summary_csv2)
    assert validator2.validate() == False
