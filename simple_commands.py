# Telegram bot to play UNO in group chats
# Copyright (c) 2016 Jannes Höke <uno@jhoeke.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import CommandHandler, ContextTypes

from internationalization import _, user_locale
from shared_vars import application
from user_setting import UserSetting
from utils import send_async


@user_locale
async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for the /help command"""
    help_text = _(
        "Siga estes passos:\n\n"
        "1. Adicionar este bot a um grupo\n"
        "2. No grupo, comece um novo jogo com /new ou junte-se a um já"
        " jogo em execução com /join\n"
        "3. Depois que pelo menos dois jogadores se juntarem, comece o jogo com"
        " /start\n"
        "4. Tipo <code>@Makoto_xyz_bot</code> na sua caixa de bate-papo e clique em "
        "<b>espaço</b>, ou clique no botão <code>via @Makoto_xyz_bot</code> texto "
        "ao lado de mensagens. Você verá seus cartões (alguns acinzentados), "
        "quaisquer opções extras, como desenho, e um <b>?</b> para ver o "
        "estado atual do jogo. O <b>cartões acinzentados</b> são aqueles que você "
        "<b>não pode jogar</b> no momento. Toque em uma opção para executar "
        "a ação selecionada.\n"
        "Os jogadores podem participar do jogo a qualquer momento. Para sair de um jogo, "
        "use /leave. Se um jogador demorar mais de 90 segundos a jogar, "
        "você pode usar /skip para pular esse jogador. Usar /notify_me para "
        "receber uma mensagem privada quando um novo jogo é iniciado.\n\n"
        "<b>Idiomas</b> e outras configurações: /settings\n"
        "Outros comandos (Só utilizado quem cria a partida ou o administrador do bot):\n"
        "/close - Fechar lobby\n"
        "/open - Lobby aberto\n"
        "/kill - Encerrar o jogo\n"
        "/kick - Selecione um jogador para chutar "
        "respondendo-lhe\n"
        "/enable_translations - Traduzir textos relevantes em todos "
        "idiomas falados em um jogo\n"
        "/disable_translations - Use o inglês para esses textos\n\n"
        "<b>Experimental:</b> Jogue em vários grupos ao mesmo tempo. "
        "Pressione o botão <code>Jogo atual: ...</code> e selecione o botão "
        "grupo no qual você deseja jogar uma carta.\n"
        "Se você gosta deste bot, junte-se ao "
        '<a href="https://t.me/botssaved">canal de atualização</a>'
        " e se divertir com o bot de cartas UNO."
    )

    await send_async(
        update.message.chat,
        text=help_text,
        parse_mode=ParseMode.HTML,
        message_thread_id=update.message.message_thread_id,
        disable_web_page_preview=True,
    )


@user_locale
async def modes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for the /help command"""
    modes_explanation = _(
        "Este bot UNO tem cinco modos de jogo: Clássico, Sanic, Wild, Texto e 7-0.\n\n"
        " 🎻 O modo Classic usa o deck UNO convencional e não há salto automático.\n"
        " 🚀 O modo Sanic usa o baralho UNO convencional e o bot ignora automaticamente um jogador se ele demorar muito para jogar sua vez.\n"
        " 🐉 O modo Wild usa um baralho com mais cartas especiais, menos variedade de números e nenhum salto automático.\n"
        " ✍️ O modo Texto usa o deck UNO convencional, mas em vez de adesivos ele usa o texto.\n"
        " 🔫 O 7-0 modo usa o baralho UNO convencional, mas quando um jogador joga um 7, ele / ela pode escolher um jogador para trocar cartas com."
        " Quando um jogador joga um 0, todas as cartas serão trocadas entre os jogadores atuais.\n\n"
        "Para alterar o modo de jogo, o CRIADOR do JOGO tem que digitar o apelido do bot e um espaço, "
        "assim como ao jogar uma carta, e todas as opções de modo de jogo devem aparecer."
    )
    await send_async(
        update.message.chat,
        text=modes_explanation,
        parse_mode=ParseMode.HTML,
        message_thread_id=update.message.message_thread_id,
        disable_web_page_preview=True,
    )


@user_locale
async def source(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for the /help command"""
    source_text = _(
        "Este bot é Software Livre e licenciado sob a AGPL. "
        "É sobre isso: \n"
        "https://t.me/botssaved"
    )
    attributions = _(
        "Atribuições:\n"
        "Ícone de desenho por "
        '<a href="http://www.faithtoken.com/">Faithtoken</a>\n'
        "Ícone de passagem por "
        '<a href="http://delapouite.com/">Delapouite</a>\n'
        "Originais disponíveis em http://game-icons.net\n"
        "Ícones editados por ɳick"
    )

    await send_async(
        update.message.chat,
        text=source_text + "\n" + attributions,
        parse_mode=ParseMode.HTML,
        message_thread_id=update.message.message_thread_id,
        disable_web_page_preview=True,
    )


@user_locale
async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for the /news command"""
    await send_async(
        update.message.chat,
        text=_("Todas as notícias aqui: https://t.me/botssaved"),
        message_thread_id=update.message.message_thread_id,
        disable_web_page_preview=True,
    )


@user_locale
async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    chat = update.message.chat
    us = UserSetting.get(id=user.id)
    if not us or not us.stats:
        await send_async(
            chat,
            text=_(
                "Você não habilitou estatísticas. Use /settings em "
                "um bate-papo privado com o bot para habilitá-los."
            ),
            message_thread_id=update.message.message_thread_id,
        )
    else:
        n = us.games_played
        stats_text = [
            _("{number} jogo jogado", "{number} jogos jogados", n).format(number=n)
        ]

        n = us.first_places
        m = round((us.first_places / us.games_played) * 100) if us.games_played else 0
        stats_text.append(
            _(
                "{number} primeiro lugar ({percent}%)",
                "{number} primeiros lugares ({percent}%)",
                n,
            ).format(number=n, percent=m)
        )

        n = us.cards_played
        stats_text.append(
            _("{number} cartas jogadas", "{number} cartas jogadas", n).format(number=n)
        )

        await send_async(
            chat,
            text="\n".join(stats_text),
            message_thread_id=update.message.message_thread_id,
        )


def register():
    application.add_handler(CommandHandler("help", help_handler))
    application.add_handler(CommandHandler("source", source))
    application.add_handler(CommandHandler("news", news))
    application.add_handler(CommandHandler("stats", stats))
    application.add_handler(CommandHandler("modes", modes))
