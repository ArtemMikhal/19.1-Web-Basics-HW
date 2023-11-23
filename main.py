from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

hostName = "localhost"
serverPort = 8080


class MyHandler(BaseHTTPRequestHandler):
    """
            Специальный класс, который отвечает за
            обработку входящих запросов от клиентов
    """
    def __get_index(self):
        '''Читает страницу HTML из файла'''
        file_path = Path(__file__).parent.joinpath('index.html')
        with open(file_path, encoding='utf-8') as file:
            data_html = file.read()
        return data_html

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        page_content = self.__get_index()
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
     # Инициализация веб-сервера, который будет по заданным параметрам в сети
     # принимать запросы и отправлять их на обработку специальному классу, который был описан выше
     webServer = HTTPServer((hostName, serverPort), MyHandler)
     print("Server started http://%s:%s" % (hostName, serverPort))

     try:
         # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
         webServer.serve_forever()
     except KeyboardInterrupt:
             # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
         pass

     # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
     webServer.server_close()
     print("Server stopped.")