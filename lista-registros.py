import click as click

from modelo import obtiene_registros, obtiene_tablas
from stdout import imprime_registros


@click.command()
@click.argument("tabla", required=False)
def lista_registros(tabla):
    if tabla:
        # Se obtiene la lista de registros de tabla
        registros = obtiene_registros(tabla)
        # Se imprimen los registros en formato texto en la salida estándar
        imprime_registros(registros, "Tabla: {}".format(tabla))
    else:
        tablas = obtiene_tablas()
        imprime_registros(tablas, "Tablas disponibles")


if __name__ == '__main__':
    lista_registros()
