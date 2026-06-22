# Client API Timenet

## Introducció
Client API per a [Timenet](https://www.registrejornadalaboral.cat/), una eina de
gestió de temps i projectes.  Aquesta biblioteca permet interactuar amb l'API de
Timenet per gestionar marcatges, grups, treballadors, projectes i configuració
d'empresa.

## Instal·lació

```bash
pip install timenet
```

## Funcionalitats
### Funcions principals
- Marcatges
- Grups
- Treballadors
- Projectes
- Configuració d'empresa

## Exemple d'ús
A continuació es mostra un exemple bàsic d'ús de l'API:

```python
from timenet import TimenetClient

# Crear una instància del client
tc = TimenetClient(token="XXXX")

# Obtenir la llista de treballadors
tc.workers.list()
```

## Tests

```bash
python -m unittest discover -v
```

GitHub Actions executes the test suite on pull requests with Python 3.11 using
the pinned dependencies in `requirements-ci.txt`.

Python 2.7 compatibility is kept as a local validation path only because GitHub
hosted runners no longer provide a maintained Python 2.7 runtime:

```bash
python2.7 -m pip install -r requirements-py27.txt
python2.7 -m unittest discover -v
```

## Contribució
Les contribucions són benvingudes! Si vols col·laborar, si us plau,
fes un fork del repositori i envia un pull request.

## Llicència
Aquest projecte està llicenciat sota la [MIT License](LICENSE).
