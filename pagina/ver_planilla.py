#!/usr/bin/env python
# -*- coding: utf-8 -*-
class AddNotas():
    def __init__(self,RutaDocumentoExel,numPag=0):
        import xlrd
        self.libro=xlrd.open_workbook(RutaDocumentoExel)
        self.hoja=self.libro.sheet_by_index(numPag)

    def get_codigo_materia(self):
        return self.hoja.cell_value(7,6)

    def get_seccion(self):
        return self.hoja.cell_value(6,15)

    def get_notas(self,lista,cedula):
        for n in range(self.hoja.ncols):
            if n > 11 and n<30:
                self.i=self.hoja.cell_value(n,1)
                try:
                    if int(self.i) == cedula:
                        for a in range(self.hoja.nrows):
                            if a>3 and a<31:
                                if a%2 != 1 and a!=28:
                                    lista.append(self.hoja.cell_value(n,a))
                except ValueError:
                    pass
        return lista

    def get_leyenda_notas(self,lista):
        aux=""
        try:
            for a in range(self.hoja.nrows):
                if a>3 and a<31:
					if a != 29 and a != 28:
						if a%2 != 1:
							aux=str(self.hoja.cell_value(11,a))
							if a == 30:
								lista.append(self.hoja.cell_value(11,a))
						else:
							aux="<"+aux+">["+str(int(float(self.hoja.cell_value(11,a))*100))+"%"+"]"
							lista.append(aux)
							aux=""

        except ValueError:
            pass
        return lista

    def get_full_name(self,cedula):
        for n in range(self.hoja.ncols):
            if n > 11 and n<30:
                self.i=self.hoja.cell_value(n,1)
                try:
                    if int(self.i) == cedula:
                        self.nombre=self.hoja.cell_value(n,2)
                        self.nombre+=" "+self.hoja.cell_value(n,3)
                except ValueError:
                    pass
        return self.nombre

"""
nota=[]
ruta='C:/Documents and Settings/Admin/Escritorio/agarrando notas/planilla.xls'
notas=AddNotas(ruta)
notas.get_notas(nota,25009456)
print nota
print notas.get_full_name(25009456)
print notas.get_codigo_materia()
"""
