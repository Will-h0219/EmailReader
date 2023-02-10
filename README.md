# EmailReader

### [ENG]
Simple message reader developed with Python and the Gmail API, it uses a static filter that can be a word contained in the mail or a [gmail filter](https://developers.google.com/gmail/api/guides/filtering), addicionally it uses the third-party package win10toast to add push notifications in Windows 10, a simple and ellegant solution that can be executed as a .bat file and even can be set to be run at windows startup. The reader notifies the most recent email that matches the specified query within the last 2 days since the script execution (be free to modify this parameter).

### [SPA]
Simple lector de mensajes con Python y el API de Gmail, utiliza un filtro estatico que puede ser una palabra dentro de un correo o un [filtro](https://developers.google.com/gmail/api/guides/filtering) usado en gmail, adicionalmente se incluye el paquete de terceros win10toast para agregar una notificación push en Windows 10, una solución elegante y sencilla que puede ejecutarse con un archivo .bat e incluso configurarlo para que se ejecute al iniciar Windows. El lector notifica del correo más reciente que haga match con el query especificado dentro de los ultimos 2 días desde la ejecución del script (el parametro puede modificarse a necesidad).

## Requisitos

- API de Google para Python. Para más información se recomienda ir a la [documentación oficial.](https://developers.google.com/gmail/api/quickstart/python)
- Win10toast. Para más información click [aquí.](https://pypi.org/project/win10toast/)
- Las credenciales generadas en [Gogle Cloud Console](https://developers.google.com/workspace/guides/create-credentials). **IMPORTANTE!** Las credenciales deben estar en el mismo fichero que el archivo .py y debe llamarse "credenciales.json".
