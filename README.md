# Monitoreo de recursos esenciales usando psutil.

##### Toma de información
* Memoria RAM disponible
* Porcentaje de Memoria RAM en uso
* Memoria SWAP disponible
* Porcentaje de Memoria SWAP en uso
* Disco libre
* Porcentaje de disco en uso
* CPU en uso


### Prerequsitos

Tener una version de python 3.x

```
psutil
```

### Installing

Si deseas instalar un entorno virtual.

```
 pip install virtualenvwrapper
```
Agregue tres líneas a su archivo de inicio de shell (.bashrc, .profile, etc.) para establecer la ubicación donde deben vivir los entornos virtuales, la ubicación de los directorios de su proyecto de desarrollo y la ubicación del script instalado con este paquete

```
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/ruta
source /usr/local/bin/virtualenvwrapper.sh
```

Después de editarlo, vuelva a cargar el archivo de inicio (por ejemplo, ejecute source ~ / .bashrc). y cree su entorno virtual con mkvirtual

Ahora vamos a clonar el proyecto.

```
git clone git@github.com:EduardoCibernetica/moninlaw.git
cd moninlaw
pip3 install -r requeriments.txt
```

## Ejemplo de visualización

[![N|Data](https://github.com/EduardoCibernetica/moninlaw/blob/master/docs/data.png?raw=true)]()    


## Autores

* **Cruz Eduardo Muñoz Cervantes** - [EduardoCibernetica](https://github.com/EduardoCibernetica)


## License

This project is licensed under GNU GENERAL PUBLIC LICENSE V3 - see the [LICENSE.md](https://github.com/EduardoCibernetica/moninlaw/blob/master/LICENSE) file for details