#Wilayah (range) merupakan suatu besaran panjang yang dihitung dengan mengurangi data dengan nilai terbesar dan data dengan nilai terkecil.

import numpy as np
import pandas as pd
#definisi sebuah file
corona_Indonesia=pd.ExcelFile("D:/TeguhPermana_data/Penyebaran_data/kawalcovid-data.xlsx")
corona_Indonesia=corona_Indonesia.parse("total_positive_cases")
#filter sebuah file
corona_Indonesia=corona_Indonesia[corona_Indonesia["Total Kasus"]=="3/18/2020"]
total_kasus=corona_Indonesia.iloc[:,1:-1].values[0]
#menghitung range data
maksimum=max(total_kasus)
minimum=min(total_kasus)
range=maksimum-minimum

print("Nilai range dari data adalah {:.2f} dengan besaran maksimum adalah {:.2f} dan minimum data sebesar{:.2f}".format(range,maksimum,minimum))

