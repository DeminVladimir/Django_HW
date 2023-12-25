from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def main(request):
    body = '''
    <title>Главная страница</title>
 <body>
     <div>
         <h1>Главная страница</h1>
         <p>Содержимое главной страницы</p>
         <p>Перейдите на страницу: /about</p>
     </div>
     <footer>
         <div>
             <p>
             </p>
         </div>
     </footer>
 </body>
    '''
    return HttpResponse(body)


def about(request):
    httpbody = '''
        <title>О Себе</title>
     <body>
         <div>
             <h1>Демин Владимир Станиславович</h1>
             <p>24 года</p>
             <p>Перейдите на страницу: /main</p>
         </div>
         <footer>
             <div>
                 <p>
                 </p>
             </div>
         </footer>
     </body>
        '''
    return HttpResponse(httpbody)
