from .. import loader

class InvisibleMod(loader.Module):
	strings = {"name": "InvisSmile"}
	
	async def inviscmd(self, message):
		await message.edit("<b>Скопируй символ:</b>")
		await message.respond("ᅠ")