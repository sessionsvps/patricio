from dotenv import load_dotenv
from telethon.sync import TelegramClient, events
import os
import json
import asyncio

async def getListOfGroups(client):
    try:
        dialogs = await client.get_dialogs()
        groups_info = []
        for dialog in dialogs:
            if dialog.is_group or dialog.is_channel:
                entity = await client.get_entity(dialog.id)
                can_send_messages = entity.default_banned_rights is None or not entity.default_banned_rights.send_messages
                if can_send_messages:
                    group_info = {'group_id': dialog.id, 'group_name': dialog.title}
                    groups_info.append(group_info)

        return groups_info
    except Exception as e:
        print(e)
        return []
async def getMessagesFromGroup(client, group_id):
    try:
        all_messages = []
        async for message in client.iter_messages(group_id):
            try:
                all_messages.append(message)
            except:
                pass
        return all_messages
    except Exception as e:
        print(e)
        return []
async def logUserBot():
    load_dotenv()
    api_id = int(21903330)
    api_hash = "ce2f386b58bb45d359c88c80c3da47b7"
    phone_number = "51973890722"
    session_name = "bot_spammer"
    client = TelegramClient(session_name, api_id, api_hash)
    await client.connect()
    if not await client.is_user_authorized():
        await client.send_code_request(phone_number)
        await client.sign_in(phone_number, input('Ingrese el código de verificación: '))
    await client.send_message("@spmpatricio2025", f'<b>Bot encendido</b>', parse_mode="HTML")
    spammer_group = int("-4629759706")

    @client.on(events.NewMessage)
    async def my_event_handler(event):
        # Verificar si el mensaje proviene de un chat privado
        if event.is_private:
            sender = await event.get_sender()
            sender_id = sender.id
            message = event.message.message
            # Responder solo en chats privados
            await client.send_message(sender_id, "Hola ,Si deceas comprar un NÚMERO SMS :\nHABLAME @Bobpatricio888 🧨\nHABLAME @Lucky66x 🧨")

    while True:
        groups_info = await getListOfGroups(client)
        messages_list = await getMessagesFromGroup(client, spammer_group)
            
        try:
            await client.send_message("@spmpatricio2025", f"<b>CANTIDAD DE MENSAJES CONSEGUIDOS PARA PUBLICAR</b> <code>{len(messages_list)-1}</code>",parse_mode="HTML")
        except:
            pass
            
        try:
            for i in groups_info:
                if i['group_name'] not in ["Spam"] and i['group_id'] not in[-1002351366917,-1002331326186,-1002425258747,-1002432211914,-1002216176545,-1001926519077,-1001580673964,-1001907073788,-1001737351681,-1001733869168,-1001829996546,-1002018025154,-1001859082953,-4553972318,-4553791708,-4559750226,-4586567990,-1001724620371,-1001760634472,-1002125807620,-1001617010310,-1001867739320,-1002074331354,-1001789640951,-1001899823705,-1001890531963,-1002296434091]:
                    j=0
                    for message_spam in messages_list:
                        j+=1
                        resultado = True
                        try:
                            await client.forward_messages(i["group_id"], message_spam)
                        except Exception as error:
                            await client.send_message("@spmpatricio2025", f'<b>Error enviando mensajes a {i["group_id"]}</b> - <code>{i["group_name"]}<code>\nCausa:{error}',parse_mode="HTML")
                            resultado = False
                        if resultado:
                            await client.send_message("@spmpatricio2025", f'<b>Mensaje enviado a {i["group_id"]}</b> - <code>{i["group_name"]}</code>',parse_mode="HTML")  
                        else: break
                        await asyncio.sleep(10)
                        if j==1: break
            await client.send_message("@spmpatricio2025", f'<b>RONDA ACABADA</b>', parse_mode="HTML")
            await asyncio.sleep(300) 
        except:
            pass
    
            
if __name__ == "__main__":
    asyncio.run(logUserBot())