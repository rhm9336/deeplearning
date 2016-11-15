! sbt "run-main org.allenai.pdffigures2.FigureExtractorBatchCli /path/to/pdf/ -s stat_file.json -m /location/of/figure/output  -d /location/for/stat/output/ -f pdf"

import tabula
from tabula import read_pdf_table
import pandas as pd

figures_and_tables = pd.read_json('/Users/HyeonminRo/Downloads/pdffigures2_git/figure/data/output/prefixzhouc14.json') 
fig_info = figures_and_tables.query('figType == "Table"').iloc[0]
%pdb

read_pdf_table("/Users/HyeonminRo/Downloads/pdffigures2_git/figure/image/pdfs/prefixzhouc14-Table1-1.pdf")
tables = read_pdf_table('zhouc14.pdf', pages=6, spreadsheet=True)
 

                    
                    
            
