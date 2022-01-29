# IMPORTS

from pypresence import Presence
from json import load
from colorama import Fore, init
import os
import time
import colorama

# IMPORTS

# Preparar comando para limpiar la consola

def limpiarConsola():
    os.system('cls')

# Preparar comando para limpiar la consola

# JSON CONFIG

with open('kaydyCFG.json') as f:
    d = load(f)
    primeralinea = d["primeralinea"]
    segundalinea = d["segundalinea"]
    imagenGrande = d["imagenGrande"]
    imagenChica = d["imagenChica"]
    client_id = d["clientID"]

# JSON CONFIG

# COLORES

# COLORES

red = Fore.RED
lred = Fore.LIGHTRED_EX
black = Fore.BLACK
lblack = Fore.LIGHTBLACK_EX
white = Fore.WHITE
lwhite = Fore.LIGHTWHITE_EX
green = Fore.GREEN
lgreen = Fore.LIGHTGREEN_EX
cyan = Fore.CYAN
lcyan = Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
lmagenta = Fore.LIGHTMAGENTA_EX
yellow = Fore.YELLOW
lyellow = Fore.LIGHTYELLOW_EX
blue = Fore.BLUE
lblue = Fore.LIGHTBLUE_EX
reset = Fore.RESET

colorama.init()

# COLORES

# PRINTS

banner = rf"""{reset}
{lred}   ▄█   ▄█▄  {lwhite}  ▄████████ {lred}▄██   ▄   {lwhite}████████▄ {lred} ▄██   ▄   {lwhite}   ▄████████  {lred}  ▄███████▄ {lwhite} ▄████████ 
{lred}  ███ ▄███▀  {lwhite} ███    ███{lred} ███   ██▄ {lwhite}███   ▀███{lred} ███   ██▄ {lwhite}  ███    ███ {lred}  ███    ███ {lwhite}███    ███ 
{lred}  ███▐██▀    {lwhite} ███    ███{lred} ███▄▄▄███{lwhite} ███    ███{lred} ███▄▄▄███ {lwhite}  ███    ███ {lred}  ███    ███ {lwhite}███    █▀  
{lred} ▄█████▀     {lwhite} ███    ███{lred} ▀▀▀▀▀▀███{lwhite} ███    ███ {lred}▀▀▀▀▀▀███ {lwhite} ▄███▄▄▄▄██▀ {lred}  ███    ███ {lwhite}███         {lred}e{lwhite}a{lred}s{lwhite}y {lred}c{lwhite}o{lred}o{lwhite}l{lred} a{lwhite}n{lred}d        
{lred}▀▀█████▄   {lwhite} ▀███████████{lred} ▄██   ███{lwhite} ███    ███ {lred}▄██   ███{lwhite} ▀▀███▀▀▀▀▀  {lred} ▀█████████▀  {lwhite}███         f{lred}u{lwhite}n{lred}n{lwhite}y{lred} {red}RPC {lred}f{lwhite}o{lred}r {lblue}Discord
{lred}  ███▐██▄   {lwhite}  ███    ███{lred} ███   ███{lwhite} ███    ███{lred} ███   ███ {lwhite}▀███████████ {lred}  ███        {lwhite}███    █▄  
{lred}  ███ ▀███▄  {lwhite} ███    ███{lred} ███   ███{lwhite} ███   ▄███{lred} ███   ███ {lwhite}  ███    ███  {lred} ███        {lwhite}███    ███ 
{lred}  ███   ▀█▀  {lwhite} ███    █▀  {lred} ▀█████▀  {lwhite}████████▀  {lred} ▀█████▀  {lwhite}  ███    ███ {lred} ▄████▀      {lwhite}████████▀  
{lred}  ▀                                         {lwhite}              ███    ███                         
"""

status1sv = rf"""
{lmagenta}Status of {yellow}KaydyRPC {lyellow}({yellow}Discord RPC{lyellow}) {lgreen}| Setting.
"""

status2sv = rf"""
{lmagenta}Status of {yellow}KaydyRPC {lyellow}({yellow}Discord RPC{lyellow}) {lgreen}/ Setting..
"""

status3sv = rf"""
{lmagenta}Status of {yellow}KaydyRPC {lyellow}({yellow}Discord RPC{lyellow}) {lgreen}- Setting...
"""

status4sv = rf"""
{lmagenta}Status of {yellow}KaydyRPC {lyellow}({yellow}Discord RPC{lyellow}) {lgreen}\ Setting.
"""

completed = rf"""
 {reset}╔═════ {lred}root@KaydyRPC {reset}════════════════════════════════════════════════════════════════════════╗
 {reset}║
 {reset}║      {lred}Application Client ID: {reset}{client_id}                                             
 {reset}║      {lred}Texto de la Primera Linea: {reset}{primeralinea}                                        
 {reset}║      {lred}Texto de la Segunda Linea: {reset}{segundalinea}                                         
 {reset}║      
 {reset}║
 {reset}║      {lred}This script has been developed by {red}Kaydy Cain#0001
 {reset}║      {lred}Can follow in github as {red}github.com/apolo1337
 {reset}║      {lred}And can join in our community {red}discord.gg/comunidad{lred}!
 {reset}║
 {reset}╚════════════════════════════════════════════════════════════════════════════════════════════╝
"""

# PRINTS
RPC = Presence(client_id) 
RPC.connect() 

limpiarConsola()
print(banner)
time.sleep(2.5)
print(status1sv)
time.sleep(0.5)
limpiarConsola()
print(banner)
print(status2sv)
time.sleep(0.5)
limpiarConsola()
print(banner)
print(status3sv)
time.sleep(0.5)
limpiarConsola()
print(banner)
print(status4sv)
time.sleep(0.5)
limpiarConsola()
print(banner)
print(status2sv)
time.sleep(0.5)
limpiarConsola()
print(banner)
print(status3sv)
time.sleep(0.5)
print(RPC.update(details=primeralinea, state=segundalinea, large_image=imagenGrande, small_image=imagenChica, large_text="github.com/apolo1337/KaydyRPC", small_text="discord.gg/comunidad", start=time.time()))  # Set the presence
limpiarConsola()
print(banner)
print(completed)


while True: 
    time.sleep(15) 