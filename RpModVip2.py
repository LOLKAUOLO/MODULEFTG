from .. import loader

class RPMod(loader.Module):
    """Рп модуль, Вип версия. by @CREATIVE_tg1"""
    strings = {"name": "RPModVip2"}

    async def client_ready(self, client, db):
        self.db = db
        self.db.set("RPModVip2", "status", True)
        
    async def rpmodcmd(self, message):
        """Вкл/выкл модуль."""
        status = self.db.get("RPModVip2", "status")
        if status is not False:
            self.db.set("RPModVip2", "status", False)
            await message.edit("<b>Рп модуль выключен!</b>")
        else:
            self.db.set("RPModVip2", "status", True)
            await message.edit("<b>Рп модуль включен!</b>")

    async def creatorcmd(self, message):
        """Инфа о создателе."""
        return await message.edit("Привет! Создатель этого модуля - @CREATIVE_tg1. Данный модуль существует уже достаточно долго, и теперь, после долгожданного обновления, появились некоторые плюшки, о которых вы можете узнать на официальном канале этого модуля. Спасибо за внимание!\n\n<b>Если появились баги, пиши @CREATIVE_tg1!</b>")
    
    async def rpcommandcmd(self, message):
        """Инфа о командах."""
        return await message.edit("Я ленивый человек, поэтому мне лень было делать команду, в которой будут все рп команды))))\nТак что, ищи их сам)\n\n<b>С любовью, @CREATIVE_tg1. Удачи!</b>")
    
    async def watcher(self, message):
        status = self.db.get("RPModVip2", "status")
        if status == False:
            return
        user1 = await message.client.get_me()
        if user1.id != message.sender_id:
            return
        msg1 = message.text.split("\n")
        msg = msg1[0].lower().split(" ")
        replika = ""
        if len(msg1) == 2:
            replika = '💭 Со словами: «' + str(msg1[1]) + '»'
        if await message.get_reply_message(): #если реплей
            user2 = await message.client.get_entity((await message.get_reply_message()).sender_id)
            text = " ".join(msg)
        else:
            text = " ".join(msg[:-1])
            user2 = await message.client.get_entity(msg[-1])
        #12-16+    
        if text == "кусь" or text == "куснуть":
            return await message.edit(f"😬 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> кусьнул(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "чмок":
            return await message.edit(f"😙 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> чмокнул(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "обнять":
            return await message.edit(f"🤗 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> обнял(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "укусить":
            return await message.edit(f"😬 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> укусил(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "съесть":
            return await message.edit(f"🥩 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> съел(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "выплюнуть":
            return await message.edit(f"🤮 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> выплюнул(-а) в <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "плюнуть":
            return await message.edit(f"😗💦 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> плюнул(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "шлеп" or text == "шлёп" or text == "шлёпнуть" or text == "шлепнуть": #8
            return await message.edit(f"🍑 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> шлёпнуть(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "связать":
            return await message.edit(f"😁⛓️ | <a href=tg://user?id={user1.id}>{user1.first_name}</a> связал(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "ударить": 
            return await message.edit(f"😡👊 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> ударил(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "убить": 
            return await message.edit(f"🔪🩸 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> убил(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "задушить": 
            return await message.edit(f"😫⛓️ | <a href=tg://user?id={user1.id}>{user1.first_name}</a> задушил(-а) подушкой <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "украсть": 
            return await message.edit(f"🤭💵 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> украл(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "погладить": 
            return await message.edit(f"🥰 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> погладил(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "притянуть": 
            return await message.edit(f"✊ | <a href=tg://user?id={user1.id}>{user1.first_name}</a> притянул(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "поцеловать": 
            return await message.edit(f"😘 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> поцеловал(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "дать пять": 
            return await message.edit(f"👏 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> дал(-а) пять <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "лизнуть" or text == "лизь": #18
            return await message.edit(f"👅 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> лизнул(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "кастрировать": 
            return await message.edit(f"😳✂🥚 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> кастрировал(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "пнуть": 
            return await message.edit(f"👊🦵 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> пнул(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "ущипнуть": 
            return await message.edit(f"🤏 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> ущипнул(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "толкнуть": 
            return await message.edit(f"👊 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> толкнул(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "выпороть": 
            return await message.edit(f"🖐️🍑 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> выпорол(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "увернуться": 
            return await message.edit(f"👀 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> уверну(-лся/-лась) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "отдаться": 
            return await message.edit(f"🏳🥵 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> отда(-лся/-лась) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "прижать": 
            return await message.edit(f"😏✌️ | <a href=tg://user?id={user1.id}>{user1.first_name}</a> прижал(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "записать на ноготочки": #27
            return await message.edit(f"💅 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> записал(-а) на ноготочки <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "отравить": 
            return await message.edit(f"☠ | <a href=tg://user?id={user1.id}>{user1.first_name}</a> отравил(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "поздравить": 
            return await message.edit(f"🥳🎂 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> поздравил(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "понюхать": 
            return await message.edit(f"👃 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> понюхал(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "покормить": 
            return await message.edit(f"🥡🍕🍦 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> покормил(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "пицца": 
            return await message.edit(f"🍕 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> кинул(-а) кусок пиццы в <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "расстрелять": 
            return await message.edit(f"🔫 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> расстрелял(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "сжечь": 
            return await message.edit(f"🔥 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> сжег <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "облизнуть" or text == "облизать": #35
            return await message.edit(f"👅 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> облизнул(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "угостить": 
            return await message.edit(f"🍦 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> угостил(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "похвалить": 
            return await message.edit(f"😉🖐️ | <a href=tg://user?id={user1.id}>{user1.first_name}</a> похвалил(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "выкинуть": 
            return await message.edit(f"<a href=tg://user?id={user1.id}>{user1.first_name}</a> выкинул(-а) <a href=tg://user?id={user2.id}>мусор</a>\n{replika}")
        if text == "рассмешить": 
            return await message.edit(f"🤡 | <a href=tg://user?id={user1.id}>Клоун</a> рассмешил <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "позвонить": 
            return await message.edit(f"📱 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> позвонил(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "утопить": 
            return await message.edit(f"💧😵 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> утопил(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "вырубить": 
            return await message.edit(f"🏏 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> вырубил(-а) дубинкой<a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "обозвать": 
            return await message.edit(f"🤬 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> некультурно обозвал(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "чапалах": 
            return await message.edit(f"👊😠 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> дал(-а) чапалах со скоростью света <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "подзатыльник": 
            return await message.edit(f"😶✋ | <a href=tg://user?id={user1.id}>{user1.first_name}</a> дал(-а) подзатыльник <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "выпить": 
            return await message.edit(f"🍷 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> культурно выпил(-а) с <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "тюрьма": 
            return await message.edit(f"👮🏻‍♂️ | <a href=tg://user?id={user1.id}>{user1.first_name}</a> посадил(-а) в обезьянник на 15 суток <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "спи" or text == "ложись спать" or text == "засыпай": 
            return await message.edit(f"😴🛏 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> уложил(-а) в кроватку и спел колыбельную <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "порвать": 
            return await message.edit(f"😼 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> порвал(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "превратить": 
            return await message.edit(f"🐸 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> превратил(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a> в жабку\n{replika}")
        if text == "замурчать": 
            return await message.edit(f"😻 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> замурчал(-а) до полусмерти <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "треснуть": 
            return await message.edit(f"🛠 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> треснул(-а) молотком <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "наорать": 
            return await message.edit(f"😠💨 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> наорал(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "согреть": 
            return await message.edit(f"🤗🔥 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> согрел(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "натравить": 
            return await message.edit(f"🐶 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> натравил(-а) собак на <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "стерилизовать" or text == "контрапцетовать": #56
            return await message.edit(f"✂😿 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> стерилизовал(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "разделить": 
            return await message.edit(f"➗ | <a href=tg://user?id={user1.id}>{user1.first_name}</a> разделил(-а) пополам <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "побить": 
            return await message.edit(f"🤕👊 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> побил(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "сильный кусь":
            return await message.edit(f"😬😡 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> сделал(-а) очень синый кусь <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "ррр": 
            return await message.edit(f"🤬🐶 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> порычал(-а) на <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "гена на": 
            return await message.edit(f"🛁 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> дал(-а) полотенце <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "пожать руку":
            return await message.edit(f"🤝 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> пожал(-а) руку <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "поговорить":
            return await message.edit(f"😄 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> поговорил(-а) с <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "сделать сюрприз":
            return await message.edit(f"🎁 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> сделал(-а) сюрприз <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "приготовить завтрак":
            return await message.edit(f"🍳🥓 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> приготовил(-а) завтрак <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "покатать":
            return await message.edit(f"🏎 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> покатал(-а) на своей ламбе <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "сделать комплимент":
            return await message.edit(f"😻 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> сделал(-а) комплимент <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "поднять":
            return await message.edit(f"💪 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> поднял(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "кинуть":
            return await message.edit(f"🥲 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> кинул(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "бросить снежок":
            return await message.edit(f"❄️ | <a href=tg://user?id={user1.id}>{user1.first_name}</a> бросил(-а) снежок в голову <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "звездочка" or text == "звёздочка":
            return await message.edit(f"⭐️ | <a href=tg://user?id={user1.id}>{user1.first_name}</a> достал(-а) звездочку с неба для <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "пилить":
            return await message.edit(f"🪚🧠 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> выпилил(-а) мозги <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "охладить":
            return await message.edit(f"🥶 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> охладил(-а) пыл <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "придушить":
            return await message.edit(f"😱 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> придушил(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "расчленить":
            return await message.edit(f"⚔️ | <a href=tg://user?id={user1.id}>{user1.first_name}</a> расчленил(-а) пополам <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "застрелить":
            return await message.edit(f"🔫 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> застрел(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "кляп":
            return await message.edit(f"🤭 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> засунул(-а) кляп в рот <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "коронавирус":
            return await message.edit(f"🦠 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> заразил(-а) коронавирусом <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "извиниться" or text == "прости" or text == "извини":
            return await message.edit(f"🥺 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> извинился(-лась) перед <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "поклониться":
            return await message.edit(f"👀🧎‍♂️ | <a href=tg://user?id={user1.id}>{user1.first_name}</a> поклонился(-лась) перед <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "заскамить":
            return await message.edit(f"🦣 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> заскамил(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "съесть шаурму":
            return await message.edit(f"🌯| <a href=tg://user?id={user1.id}>{user1.first_name}</a> съел(-а) шаурму с <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "предложить по пиву":
            return await message.edit(f"🍻 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> предложил(-а) по пиву <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "угостил пивом":
            return await message.edit(f"🍻 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> угостил(-а) пивом <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "наказать": 
            return await message.edit(f"😡 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> наказал(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")

        #18+
        if text == "чпокнуть": 
            return await message.edit(f"😏 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> чпокнул(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "выебать": 
            return await message.edit(f"👉👌 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> выебал(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "уебать": 
            return await message.edit(f"💪🤬 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> уебал(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "отсосать": 
            return await message.edit(f"👄💦 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> отсосал(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "отлизать": 
            return await message.edit(f"👅💦 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> отлизал(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "изнасиловать": 
            return await message.edit(f"👉👌😬 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> изнасиловал(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "трахнуть": 
            return await message.edit(f"😜💦 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> трахнул(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "послать": 
            return await message.edit(f"🤬🖕 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> послал(-а) на хер <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "спиздить":
            return await message.edit(f"🧔👶🏻 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> спиздил(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "засосать": 
            return await message.edit(f"💋💞 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> засосал(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "делать секс": 
            return await message.edit(f"👉👌💦 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> сделал(-а) секс с <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "камингаут": 
            return await message.edit(f"🤫 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> сделал(-а) камингаут <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "отпиздить": 
            return await message.edit(f"😤👊 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> отпиздил(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "обматерить": 
            return await message.edit(f"🖕🤬🖕 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> жестко обматерил(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "отрезать": 
            return await message.edit(f"🔪🌭 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> отрезал(-а) хуй <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "бухнуть": 
            return await message.edit(f"🥴🍻🥃 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> бухнул(-а) ёршика с <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "покурить": 
            return await message.edit(f"🚬 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> покурил(-а) с <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "посадить": 
            return await message.edit(f"📥 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> посадил(-а) на свой хуй <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "гейпорн": 
            return await message.edit(f"👯‍♂️ | <a href=tg://user?id={user1.id}>{user1.first_name}</a> отдал(-а) в студию гей-продакшн <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "отодрать": 
            return await message.edit(f"😏🔥8⃣ | <a href=tg://user?id={user1.id}>{user1.first_name}</a> отодрал(-а) во все дыры <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "фаталити": 
            return await message.edit(f"🩸⛓ | <a href=tg://user?id={user1.id}>{user1.first_name}</a> вырвал(-а) кишки и проломил(-а) бошку <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "отыметь": 
            return await message.edit(f"👉👌👀 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> отымел(-а) <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "дать хуем по лбу" or text == "дать хуём по лбу":
            return await message.edit(f"☺️👀 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> дал(-а) хуем по лбу <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "уебать с ноги": 
            return await message.edit(f"🦵👶 | <a href=tg://user?id={user1.id}>{user1.first_name}</a> уебал(-а) с ноги по ебалу <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
        if text == "наказать плеткой" or text == "наказать плёткой": 
            return await message.edit(f"😡⛓ | <a href=tg://user?id={user1.id}>{user1.first_name}</a> наказал(-а) плеткой <a href=tg://user?id={user2.id}>{user2.first_name}</a>\n{replika}")
