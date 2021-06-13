import amino, concurrent.futures
email = input("Почта: ")
password = input("Пароль: ")
message = input("Сообщение: ")
msgtype = input("Тип сообщения: ")
client = amino.Client()
client.login(email=email, password=password)
clients = client.sub_clients(start=0, size=1000)
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
communityid = clients.comId[int(input("Выберите сообщество: "))-1]
sub_client = amino.SubClient(comId=communityid, profile=client.profile)
chats = sub_client.get_chat_threads(size=150)
for z, title in enumerate(chats.title, 1):
	print(f"{z}.{title}")
chatx = chats.chatId[int(input("Выберите чат: "))-1]

sub_client.send_message(chatId=chatx, message=message, messageType=msgtype)

while True:
	with concurrent.futures.ThreadPoolExecutor(max_workers=222877777) as executor:
		_ = [executor.submit(sub_client.send_message, chatx, message, msgtype) for _ in range(5000000000000)]
		
