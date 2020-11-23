import discord
from discord.ext import commands

#Définisser le déclencheur pour la commande ici
robot = commands.Bot(command_prefix = "!")


#Message de lancement pour la console
@robot.event
async def on_ready():
    print("[ServerCall] Prêt !")

@robot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        for channel in member.guild.channels:
            #Nom du salon textuel où votre bot va afficher automatiquement le panel d'appel
            if str(channel) == "bots":
                message = await channel.send(f"**{member.name}** vient de se connecter dans **{member.voice.channel.name}**\n>>> Utilise :white_medium_small_square: pour notifier tout le monde ici !\nOu clique sur la couleur des personnes que tu souhaites notifier en MP :\n*Attend que les réactions apparaissent et supprime ce message avec :x: si tu ne veux appeler personne ou que tu as fini !*")
                #Ici, vous pouvez choisir le smiley qui vous convient pour envoyer à tout le monde une notification
                await message.add_reaction("◻")
                #Puis ici, vous pouvez choisir les smileys qui correspond à vos amis
                await message.add_reaction("🔵")
                await message.add_reaction("🔴")
                await message.add_reaction("🟠")
                await message.add_reaction("🟢")
                await message.add_reaction("🟣")
                #Enfin ici, vous pouvez choisir le smiley pour supprimer le message
                await message.add_reaction("❌")

                def GoodUser(reaction, user):
                    #Ne pas oublier de changer aussi ici les smileys
                    return member == user and message.id == reaction.message.id and (str(reaction.emoji) == "◻" or str(reaction.emoji) == "🔵" or str(reaction.emoji) == "🔴" or str(reaction.emoji) == "🟠" or str(reaction.emoji) == "🟢" or  str(reaction.emoji) == "🟣" or  str(reaction.emoji) == "❌")  

                for channel in member.guild.channels:
                    #Nom du salon textuel où votre bot va afficher la notification @everyone
                    if str(channel) == "général":
                        loop = 1
                        while loop == 1:
                            reaction, user = await robot.wait_for("reaction_add", check = GoodUser)
                            #Ne pas oublier de changer aussi ici les smileys

                            if reaction.emoji == "◻":
                                await channel.send(f"@everyone | **{member.name}** vous attend dans **{member.voice.channel.name}** pour parler.")
                                
                            if reaction.emoji == "🔵":
                                #Modifier "1ID" par l'ID de votre ami (obtenable en faisant clic droit sur lui en étant en mode développeur sur Discord)
                                target = await robot.fetch_user(1ID)
                                await target.send(f"Coucou ! **{member.name}** t'invite à le rejoindre maintenant dans le salon **{member.voice.channel.name}** de **{member.guild.name}**.")
                                
                            if reaction.emoji == "🔴":
                                #Modifier "2ID" par l'ID de votre ami (obtenable en faisant clic droit sur lui en étant en mode développeur sur Discord)
                                target = await robot.fetch_user(2ID)
                                await target.send(f"Coucou ! **{member.name}** t'invite à le rejoindre maintenant dans le salon **{member.voice.channel.name}** de **{member.guild.name}**.")
                                
                            if reaction.emoji == "🟠":
                                #Modifier "3ID" par l'ID de votre ami (obtenable en faisant clic droit sur lui en étant en mode développeur sur Discord)
                                target = await robot.fetch_user(3ID)
                                await target.send(f"Coucou ! **{member.name}** t'invite à le rejoindre maintenant dans le salon **{member.voice.channel.name}** de **{member.guild.name}**.")
                                
                            if reaction.emoji == "🟢":
                                #Modifier "4ID" par l'ID de votre ami (obtenable en faisant clic droit sur lui en étant en mode développeur sur Discord)
                                target = await robot.fetch_user(4ID)
                                await target.send(f"Coucou ! **{member.name}** t'invite à le rejoindre maintenant dans le salon **{member.voice.channel.name}** de **{member.guild.name}**.")
                                
                            if reaction.emoji == "🟣":
                                #Modifier "5ID" par l'ID de votre ami (obtenable en faisant clic droit sur lui en étant en mode développeur sur Discord)
                                target = await robot.fetch_user(5ID)
                                await target.send(f"Coucou ! **{member.name}** t'invite à le rejoindre maintenant dans le salon **{member.voice.channel.name}** de **{member.guild.name}**.")
                            
                            if reaction.emoji == "❌":
                                loop = 0
                                await message.delete()

#Refaire toute les étapes ci-dessus ici pour personnaliser les paramètres de la commande !call.
@robot.command()
async def call(ctx):
    if ctx.author.voice.channel != "None":
        message = await ctx.send(f"**{ctx.author.name}** se trouve dans **{ctx.author.voice.channel}**\n>>> Utilise :white_medium_small_square: pour notifier tout le monde ici !\nOu clique sur la couleur des personnes que tu souhaites notifier en MP :\n*Attend que les réactions apparaissent et supprime ce message avec :x: si tu ne veux appeler personne ou que tu as fini !*")
        #Ne pas oublier de changer aussi ici les smileys
        await message.add_reaction("◻")
        await message.add_reaction("🔵")
        await message.add_reaction("🔴")
        await message.add_reaction("🟠")
        await message.add_reaction("🟢")
        await message.add_reaction("🟣")
        await message.add_reaction("❌")

        def GoodUser(reaction, user):
            return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "◻" or str(reaction.emoji) == "🔵" or str(reaction.emoji) == "🔴" or str(reaction.emoji) == "🟠" or str(reaction.emoji) == "🟢" or  str(reaction.emoji) == "🟣" or  str(reaction.emoji) == "❌")  

        for channel in ctx.guild.channels:
            if str(channel) == "général":
                loop = 1
                while loop == 1:
                    reaction, user = await robot.wait_for("reaction_add", check = GoodUser)
                    if reaction.emoji == "◻":
                        await channel.send(f"@everyone | **{ctx.author.name}** vous attend dans **{ctx.author.voice.channel}** pour parler.")
                        
                    elif reaction.emoji == "🔵":
                        target = await robot.fetch_user(1ID)
                        await target.send(f"Coucou ! **{ctx.author.name}** t'invite à le rejoindre maintenant dans le salon **{ctx.author.voice.channel}** de **{ctx.guild.name}**.")
                        
                    elif reaction.emoji == "🔴":
                        target = await robot.fetch_user(2ID)
                        await target.send(f"Coucou ! **{ctx.author.name}** t'invite à le rejoindre maintenant dans le salon **{ctx.author.voice.channel}** de **{ctx.guild.name}**.")
                        
                    elif reaction.emoji == "🟠":
                        target = await robot.fetch_user(3ID)
                        await target.send(f"Coucou ! **{ctx.author.name}** t'invite à le rejoindre maintenant dans le salon **{ctx.author.voice.channel}** de **{ctx.guild.name}**.")
                        
                    elif reaction.emoji == "🟢":
                        target = await robot.fetch_user(4ID)
                        await target.send(f"Coucou ! **{ctx.author.name}** t'invite à le rejoindre maintenant dans le salon **{ctx.author.voice.channel}** de **{ctx.guild.name}**.")
                        
                    elif reaction.emoji == "🟣":
                        target = await robot.fetch_user(5ID)
                        await target.send(f"Coucou ! **{ctx.author.name}** t'invite à le rejoindre maintenant dans le salon **{ctx.author.voice.channel}** de **{ctx.guild.name}**.")
                    
                    elif reaction.emoji == "❌":
                        loop = 0
                        await message.delete()

#Changer ici le token de votre bot.
robot.run("SERV_ID")