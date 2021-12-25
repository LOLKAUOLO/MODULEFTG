from .. import loader, utils

class RpMod(loader.Module):
	strings = {"name": "RpBot"}

	async def watcher(self, message):
	    reply = await message.get_reply_message()
	    user = await message.client.get_entity(reply.sender_id)
	    me = (await message.client.get_me())
	    sender = await message.get_sender()
	    if message.sender_id != me.id:

	    	#-----------------12+---------------------

	        if message.text.lower() == "чмок":
	            await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> чмокнул/a <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "кусь":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> сделал/a кусь <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "обнять":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> обнял/a <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "шлеп":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> шлепнул/a <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "убить":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> убил/a <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "задушить":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> задушил/a <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "связать":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> связал/a <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "ударить":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> ударил/a <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "украсть":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> украл/a <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "погладить":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> погладил/a <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "притянуть":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> притянуть/a <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "поцеловать":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> поцеловал/a <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "дать пять":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> дал/а пять <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "лизнуть":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> лизнул/a <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "кастрировать":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> кастрировал/a <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "пнуть":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> пнул/a <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "ущипнуть":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> ущипнул/a <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "отпороть":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> отпорил/a <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "увернуться":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> увернулся/a <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "отдаться":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> отдался/ась <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "прижать":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> прижал/a <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "записать на ноготочки":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> записал/а на ноготочки <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "отравить":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> отравил/a <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "понюхать":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> понюхал/a <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "покормить":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> покормил/а <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "расстрелять":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> расстрелял/a <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "сжечь":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> сжег/сожгла <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "куснуть":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> кусьнул/a <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "облизать":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> облизал/a <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "угостить":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> угостил/a <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "похвалить":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> похвалил/а <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "выкинуть":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> выкинул/a <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "позвонить":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> позвонил/а <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "утопить":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> утопил/a <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "бан":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> забанил/a <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "вырубить":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> вырубил/а <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "обозвать":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> обозвал/a <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "чапалах":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> дал/а чапалаха <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "подзатыльник":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> дал/a подзатыльник <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "выпить":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> выпил/а кровь <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "посадить":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> посадил/a на коленки <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "тюрьма":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> посадил/a в тюрьму <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "съесть":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> съел/a <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "выплюнуть":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> выплюнул/а <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "плюнуть":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> плюнул/a на <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "рвать":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> порвал/а <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "превратить":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> превратил/a <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "Мур":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> помурлыкал/a <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "треснуть":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> треснул/а <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "наорать":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> наорал/a <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "согреть":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> согрел/а <a href=tg://user?id={user.id}>{user.first_name}</a>")


	        #-----------------18+---------------------

	        elif message.text.lower() == "чпок":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> чпокнул/а <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "выебать":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> выебал/a на <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "уебать":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> уебал/а <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "отсосать":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> отсосал/а <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "отлизать":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> отлизал/a <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "изнасиловать":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> трахнул/а <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "трахнуть":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> наорал/a <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "послать":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> послал/а нахуй <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "спиздить":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> спиздил/а <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "засосать":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> засосал/а <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "делать секс":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> делает секс с <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "камингаут":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> сделал/а камингаут <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "отпиздить":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> отпиздил/а нахуй <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "обматерить":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> обматерил/а нахуй <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "обрезать":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> обрезал/а <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "бухнуть":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> бухает с <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "покурить":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> покурил/а с <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "шлепнуть":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> шлепнул/а <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "обоссать":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> обоссал/а <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "обосрать":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> обосрал/а <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        	
	        #троль
	        elif message.text.lower() == "скам":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> заскамил/а <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "спам":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> заспамил/а <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "выкинуть":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> выкинул/а <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "рассмешеить":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> рассмешил/а <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "ю":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> похую на <a href=tg://user?id={user.id}>{user.first_name}</a>")
	        elif message.text.lower() == "ы":
	        	await message.respond(f"<a href=tg://user?id={sender.id}>{sender.first_name}</a> до пизды что сказал/а <a href=tg://user?id={user.id}>{user.first_name}</a>")