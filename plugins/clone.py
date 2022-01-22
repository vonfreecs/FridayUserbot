#~ Ported from Friday[Telethon]
#~ ©FridayUB

import os

from main_startup.core.decorators import friday_on_cmd
from main_startup.helper_func.basic_helpers import edit_or_reply, get_text, get_user


OWNER = os.environ.get("OWNER", None)
BIO = os.environ.get("BIO", None)

@friday_on_cmd(['clone'],
    cmd_help={
    "help": "Clone a user",
    "example": "{ch}clone",
    })
async def clone(client, message):
  text = get_text(message)
  op = await edit_or_reply(message, "`Cloning`")
  userk = get_user(message, text)[0]
  user_ = await client.get_users(userk)
  if not user_:
    await op.edit("`Whom i should clone:(`")
    return
    
  get_bio = await client.get_chat(user_.id)
  f_name = user_.first_name
  c_bio = get_bio.bio
  pic = user_.photo.big_file_id
  poto = await client.download_media(pic)

  await client.set_profile_photo(photo=poto)
  await client.update_profile(
       first_name=f_name,
       bio=c_bio,
  )
  await message.edit(f"**From now I'm** __{f_name}__")
    
#Now lets revert:
@friday_on_cmd(['revert'],
    cmd_help={
    "help": "Get ur identity back",
    "example": "{ch}revert",
    })
async def revert(client, message):
 await message.edit("`Reverting`")
 r_bio = BIO
	
	#Get ur Name back
 await client.update_profile(
	  first_name=OWNER,
	  bio=r_bio,
	)
	#Delte first photo to get ur identify
 photos = await client.get_profile_photos("me")
 await client.delete_profile_photos(photos[0].file_id)
 await message.edit("`I am back!`")