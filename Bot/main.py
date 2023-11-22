import interactions as ext
from interactions.api.events import Component
from os import system as cmd
from keysys import check_key
from logger import *
def clr(): cmd("cls")
tver = 3
global authrole
Logger=LoggerClass()
clr()
devs = [694716077086867556]
def is_dev(user:ext.Member):
    if user.id in devs:
        return True
    else:
        return False

print(f"Fins Interaction Template V{tver}")
bot = ext.Client(intents=ext.Intents.DEFAULT)
Logger.start()
# made by fin-github on github.com
@ext.listen()
async def on_ready():
    print("Ready")
    print(f"Current Dev IDS: {devs}")
    Logger.log("Bot start up!")
    Logger.log(f"CURRENT DEVS: {devs}")




# START OF CODE

@ext.slash_command(name="load", description="DEV ONLY!!!! Load up the key auth sys panel...")
async def load_function(ctx: ext.SlashContext):
    await ctx.defer() # DO NOT DELETE
    
    if is_dev(ctx.user):
        await ctx.send(
            embed=ext.Embed(
                title="Key Authentication System (KAS)",
                description="To get your role, you must authenticate your KEY.\nClick on the button that says Authenticate to authenticate",
                color=ext.Color.from_rgb(0,255,0)
                ),
            components=ext.Button(
                style=ext.ButtonStyle.GREEN,
                label="Authenticate",
                custom_id="auth",
                disabled=False
                )
            )
        Logger.log("Sent KAS embed.")
    else:
        await ctx.send(f"<@{ctx.user.id}> Please do not run this command again!")
        Logger.log(f"{ctx.user.id} attempted to send KAS embed, without dev role.")
        return


@ext.component_callback("auth")
async def btn_callback(ctx: ext.ComponentContext):
    Logger.log(f"{ctx.user.id} Clicked on AUTH button.")
    await ctx.send_modal(
        ext.Modal(
           ext.ShortText(
               label="Enter in your key...",
               custom_id="keyinput"
           ),
           title="Key Authentication",
           custom_id="mainmodal"
        )
    )

@ext.modal_callback("mainmodal")
async def on_modal_answer(ctx: ext.ModalContext, keyinput:str):
    Logger.log(f"{ctx.user.id} Answered Modal...")
    if check_key(keyinput):
        Logger.log(f"{ctx.user.id} Put in a correct key! Key: {keyinput}")
        await ctx.send(
            ephemeral=True,
            embed=ext.Embed(
                title="Key Authentication System (KAS)",
                description="Correct Key!",
                color=ext.Color.from_rgb(0,255,0)
            )
        )
        try:
            Logger.log(f"Attempting to add a AUTHROLE to {ctx.user.id}")
            await ctx.author.add_role(authrole)
        except Exception as e:
            Logger.log(f"ERROR: While trying to add role to {ctx.user.id}, got error:\"{e}\"")
            await ctx.send(
                content="AuthRole is not setup. Please wait for the dev team to calibrate the authrole.",
                ephemeral=True
            )
            await ctx.send(
                content=f"<@{devs[0]}> AUTHROLE IS NOT CALIBRATED!!\nerr: {e}"
            )
            
    else:
        Logger.log(f"{ctx.author.id} entered a incorrect key! key: {keyinput}")
        await ctx.send(
            ephemeral=True,
            embed=ext.Embed(
                title="Key Authentication System (KAS)",
                description="Incorrect Key!",
                color=ext.Color.from_rgb(255,0,0)
            )
        )


# DEV CMDS

@ext.slash_command(name="role_calibration", description="DEV ONLY!!!! Calibrate the ROLE used if successful key auth...")
@ext.slash_option(
    name="role",
    description="Key auth role",
    required=True,
    opt_type=ext.OptionType.ROLE
)
async def role_calibration_function(ctx: ext.SlashContext, role: ext.Role):
    Logger.log(f"{ctx.user.id} Attempted to calibrate AUTHROLE. Attempted role {role}")
    if is_dev(ctx.user):
        Logger.log(f"{ctx.user.id} Calibrating AUTHROLE. Attempted role: {role}")
        global authrole
        authrole = role
        await ctx.respond("Calibrated successfully...")
    else:
        Logger.log(f"{ctx.user.id} Attempted to run a dev cmd (role_calibrate) without dev perms.")
        await ctx.send(f"<@{ctx.user.id}> Please do not run this command again!")
        return
@ext.slash_command(name="check_role", description="DEV ONLY!!!! Check if the auth role is calibrated...")
async def check_role_function(ctx: ext.SlashContext):
    Logger.log(f"{ctx.user.id} Attempting to check AUTHROLE calibration.")
    if is_dev(ctx.user):
        try:
            await ctx.send(f"Calibration Status is: {'OK' if authrole else 'NOT CALIBRATED'}")
        except Exception as e:
            await ctx.respond(f"Not Calibrated... Err:\n{e}")
    else:
        Logger.log(f"{ctx.user.id} Attempted to run a dev cmd (check_role) without dev perms.")
        await ctx.send(f"<@{ctx.user.id}> Please do not run this command again!")
        return
    
    
    
bot.start(TOKEN)
